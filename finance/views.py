from django.http import HttpResponse
from django.template.loader import render_to_string
from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.decorators.http import require_GET
from django.utils import timezone
from django.urls import reverse_lazy
from django.db.models import Sum
from .models import OneIO
from .forms import OneIOForm


@require_GET
def load_base(request):
    return render(request, 'base.html')


class ListIOs(ListView):
    model = OneIO

    def get_template_names(self):
        path = self.request.path
        print('GET_TEMPLATE_NAMES EXECUTED')

        if path == '/ledger/':
            return ['finance/ledger.html']
        elif path == '/ledger/update-dom/':
            return ['finance/components/ledger_table.html']

        raise ValueError(f"No template found for path: {path}")

    def get_queryset(self):
        print('GET_QUERYSET EXECUTED')
        queryset = super().get_queryset()
        year = int(self.request.COOKIES.get('ledger-year', timezone.now().year))

        js_month = self.request.COOKIES.get('ledger-month')
        month = int(js_month) + 1 if js_month else timezone.now().month

        is_outcome = self.request.COOKIES.get('is-outcome', True)
        if isinstance(is_outcome, str):
            is_outcome = True if is_outcome == 'true' else False

        is_one_off = self.request.COOKIES.get('is-one-off', 'one-off')
        if is_one_off == 'one-off':
            return queryset.filter(
                date__year=year,
                date__month=month,
                is_outcome=is_outcome,
                manager_id__isnull=True,
            )
        elif is_one_off == 'recurring':
            return queryset.filter(
                date__year=year,
                date__month=month,
                is_outcome=is_outcome,
                manager_id__isnull=False,
            )
        else:
            return queryset.filter(
                date__year=year,
                date__month=month,
                is_outcome=is_outcome,
            )

    def get_context_data(self, *, object_list=None, **kwargs):
        print('GET_CONTEXT_DATA EXECUTED')
        context = super().get_context_data(**kwargs)
        queryset = self.get_queryset()
        total_sum = queryset.aggregate(total=Sum('value'))['total'] or 0
        context['total_sum'] = f'{total_sum:.2f}'

        is_outcome = self.request.COOKIES.get('is-outcome', True)
        if isinstance(is_outcome, str):
            is_outcome = True if is_outcome == 'true' else False

        is_one_off = self.request.COOKIES.get('is-one-off', 'one-off')

        context['is_outcome'] = is_outcome
        context['is_one_off'] = is_one_off
        context['form'] = OneIOForm()
        return context

    def render_to_response(self, context, **response_kwargs):
        return HttpResponse(render_to_string(self.get_template_names(), context))

    def post(self, request, *args, **kwargs):
        print('POST EXECUTED')
        form = OneIOForm(request.POST)
        form.save()
        return redirect('ledger')


class DetailIO(UpdateView):
    model = OneIO
    # form_class = None
    template_name = 'finance/one_detail.html'

    def get_success_url(self):
        return reverse_lazy('ledger')


class CreateIO(CreateView):
    model = OneIO
    form_class = OneIOForm
    template_name = 'finance/forms/one_create.html'
    success_url = reverse_lazy('ledger')

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'form': self.form_class})

    def form_valid(self, form):
        form.save()
        form_html = render_to_string(self.template_name, {'form': self.form_class})
        return HttpResponse(form_html)


class DeleteIO(DeleteView):
    model = OneIO
    success_url = reverse_lazy('ledger')

    def post(self, request, *args, **kwargs):
        selected_pks = request.POST.getlist('selected_pk')
        OneIO.objects.filter(pk__in=selected_pks).delete()
        return super().post(request, *args, **kwargs)


def dashboard(request):
    return HttpResponse(render_to_string('finance/dashboard.html'))


def recurring(request):
    return render(request, 'finance/recurring.html')


def investments(request):
    return render(request, 'finance/investments.html')


def liabilities(request):
    return render(request, 'finance/liabilities.html')


def reminders(request):
    return render(request, 'finance/reminders.html')


def media(request):
    return render(request, 'finance/media.html')
