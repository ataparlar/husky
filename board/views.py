from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.exceptions import ObjectDoesNotExist

from .models import OldYear, Member, Danisman
from main.models import ArkaPlanFotograf, Sayfa

# Create your views here.

# This class is for OldYearPage class at bottom.
class memberTemplate(TemplateView):
    template_name = "kurul.html"
    def get_member_context(self, year):
        year_of_oldyear = OldYear.objects.get(year=year)
        if not Member.objects.filter(year=year_of_oldyear).exists():
            year = int(year) - 1,
            year_of_oldyear = OldYear.objects.get(year=year)

        member_dict = {
            'members': Member.objects.filter(year=year_of_oldyear),
            'oldyears': OldYear.objects.all().order_by("year"),
            'bg': ArkaPlanFotograf.objects.get(page=Sayfa.objects.all()[6]),
        }

        if Danisman.objects.filter(year=year_of_oldyear).exists():
            danisman = Danisman.objects.get(year=year_of_oldyear)
            member_dict["danisman"] = danisman

        return member_dict

    def get_context_data(self, **kwargs):
        last_year = OldYear.objects.all().order_by("id")[0].year
        context = super().get_context_data(**kwargs)
        year = self.kwargs.get('year', last_year)
        member_context = self.get_member_context(year)
        context.update(member_context)
        return context


class OldYearPage(TemplateView):
    template_name = 'oldyears.html'
    not_found_message = 'Year not found for old year page.'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        year = str(self.kwargs.get('year'))
        oldyear = OldYear.objects.filter(year=year).get()
        member_context = memberTemplate.get_member_context(self, year)
        context.update(oldyear=oldyear, **member_context)
        return context
