from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.utils import timezone
from django.urls import reverse_lazy
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
        chosen_year = self.request.GET.get('chosen_year')
        chosen_month = self.request.GET.get('chosen_month')
        chosen_is_outcome = self.request.GET.get('is_outcome')
        if chosen_month and chosen_month:
            return queryset.filter(date__year=chosen_year, date__month=chosen_month, is_outcome=chosen_is_outcome)

        year = timezone.now().year
        month = timezone.now().month
        return queryset.filter(date__year=year, date__month=month, is_outcome=True)


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




