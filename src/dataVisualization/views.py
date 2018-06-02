from django.views.generic import TemplateView

# Create your views here.
class Diagrams(TemplateView):
    template_name = 'diagrams.html'

class AAPL(TemplateView):
    template_name = 'CompaniesTemplates/AAPL.html'

class AMD(TemplateView):
    template_name = 'CompaniesTemplates/AMD.html'

class FB(TemplateView):
    template_name = 'CompaniesTemplates/FB.html'

class GOOG(TemplateView):
    template_name = 'CompaniesTemplates/GOOG.html'

class INTC(TemplateView):
    template_name = 'CompaniesTemplates/INTC.html'

class MSFT(TemplateView):
    template_name = 'CompaniesTemplates/MSFT.html'

class NVDA(TemplateView):
    template_name = 'CompaniesTemplates/NVDA.html'

class RTN(TemplateView):
    template_name = 'CompaniesTemplates/RTN.html'

class TWTR(TemplateView):
    template_name = 'CompaniesTemplates/TWTR.html'

class YHOO(TemplateView):
    template_name = 'CompaniesTemplates/YHOO.html'
