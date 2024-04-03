from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.utils import timezone
from django.urls import reverse_lazy
from django.db.models import Sum
import datetime
from .models import OneIO
from .forms import UpdateIOForm
"""
We need a view for to display all: 
(by default display this month)
 outcomes 1-off
 outcomes recurring
 incomes 1-off
 outcomes recurring
"""


class ListIOs(ListView):
    model = OneIO
    template_name = 'finance/one_io_list.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        year = int(self.request.COOKIES.get('ledger-year', timezone.now().year))

        js_month = self.request.COOKIES.get('ledger-month')
        month = int(js_month) + 1 if js_month else timezone.now().month

        is_outcome = self.request.COOKIES.get('is-outcome', True)
        if isinstance(is_outcome, str):
            is_outcome = True if is_outcome == 'true' else False

        # TODO: add recurring parameter
        # is_one_off = self.request.COOKIES.get('is-one-off', True)

        return queryset.filter(
            date__year=year,
            date__month=month,
            is_outcome=is_outcome,
        )

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        queryset = self.get_queryset()
        total_sum = queryset.aggregate(total=Sum('value'))['total'] or 0
        context['total_sum'] = f'{total_sum:.2f}'

        is_outcome = self.request.COOKIES.get('is-outcome', True)
        if isinstance(is_outcome, str):
            is_outcome = True if is_outcome == 'true' else False

        context['is_outcome'] = is_outcome
        return context


class DetailIO(UpdateView):
    model = OneIO
    form_class = UpdateIOForm
    template_name = 'finance/one_io_detail_update.html'

    def get_success_url(self):
        return reverse_lazy('list-io')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['one_io'] = self.object
        return context


class CreateIO(CreateView):
    model = OneIO
    form_class = UpdateIOForm
    template_name = 'finance/one_io_create.html'
    success_url = reverse_lazy('list-io')


class DeleteIO(DeleteView):
    model = OneIO
    success_url = reverse_lazy('list-io')

    def post(self, request, *args, **kwargs):
        selected_pks = request.POST.getlist('selected_pk')
        OneIO.objects.filter(pk__in=selected_pks).delete()
        return super().post(request, *args, **kwargs)




