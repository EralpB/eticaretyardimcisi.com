from django.shortcuts import render

from django.views.generic.base import TemplateView

from eticaret.models import Website, Category


class HomePageView(TemplateView):

    template_name = "index.html"

    def get_context_data(self, **kwargs):
        website = self.request.GET.get('websiteInfo', None)

        print(website)
        context = super().get_context_data(**kwargs)
        context['websites'] = Website.objects.all()
        return context


class SiteDetailView(TemplateView):

    template_name = "site_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        website = Website.objects.get(id=kwargs['pk'])
        context['website'] = website
        context['categories'] = Category.objects.filter(website=website)
        return context


class CategoryDetailView(TemplateView):

    template_name = "category_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        website = Website.objects.get(id=kwargs['pk'])
        category = Category.objects.get(id=kwargs['category_pk'])
        context['website'] = website
        context['category'] = category

        calculate_type = self.request.GET.get('calculatetype', None)

        context['calculate_type'] = calculate_type

        if calculate_type == 'calculateprofit':
            last_price = float(self.request.GET.get('lastprice'))
            context['last_price'] = float(last_price)
            commission = last_price * category.commission / 100
            context['commission'] = commission
            context['profit'] = last_price - commission
        elif calculate_type == 'calculatelastprice':
            profit = float(self.request.GET.get('profit'))
            context['profit'] = profit
            context['last_price'] = profit / (1 - category.commission/100)
            context['commission'] = context['last_price'] - profit

        return context
