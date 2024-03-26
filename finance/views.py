from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.utils import timezone
from .models import OneIO
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


class DetailIO(DetailView):
    model = OneIO

    def get_object(self, queryset=None):
        if not queryset:
            queryset = self.get_queryset()

        return queryset.get(pk=self.kwargs.get('pk'))





