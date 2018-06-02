from django.shortcuts import render
from django.views.generic import TemplateView
from bokeh.plotting import figure
from bokeh.resources import CDN
from bokeh.embed import components


# Create your views here.
class Diagrams(TemplateView):
    template_name = 'diagrams.html'


class MSFT(TemplateView):
    template_name = 'CompaniesTemplates/microsoft.html'


class TWTR(TemplateView):
    template_name = 'CompaniesTemplates/twitter.html'


class APPL(TemplateView):
    template_name = 'CompaniesTemplates/apple.html'


class SSNLF(TemplateView):
    template_name = 'CompaniesTemplates/samsung.html'


class FB(TemplateView):
    template_name = 'CompaniesTemplates/facebook.html'


class BABA(TemplateView):
    template_name = 'CompaniesTemplates/alibaba.html'


class AMZN(TemplateView):
    template_name = 'CompaniesTemplates/amazon.html'


class BTC_USD(TemplateView):
    template_name = 'CompaniesTemplates/bitcoin.html'

def simple_chart(request):
    plot = figure()
    plot.circle([1,2], [3,4])

    script, div = components(plot, CDN)

    return render(request, "simple_chart.html", {"the_script": script, "the_div": div})
