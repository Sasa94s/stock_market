from django.shortcuts import render


# Create your views here.
def diagrams(request):
    context = {}
    template = 'diagrams.html'
    return render(request, template, context)


def MSFT(request):
    context = {}
    template = 'CompaniesTemplates/microsoft.html'
    return render(request, template, context)


def TWTR(request):
    context = {}
    template = 'CompaniesTemplates/twitter.html'
    return render(request, template, context)


def APPL(request):
    context = {}
    template = 'CompaniesTemplates/apple.html'
    return render(request, template, context)


def SSNLF(request):
    context = {}
    template = 'CompaniesTemplates/samsung.html'
    return render(request, template, context)


def FB(request):
    context = {}
    template = 'CompaniesTemplates/facebook.html'
    return render(request, template, context)


def BABA(request):
    context = {}
    template = 'CompaniesTemplates/alibaba.html'
    return render(request, template, context)


def AMZN(request):
    context = {}
    template = 'CompaniesTemplates/amazon.html'
    return render(request, template, context)


def BTC_USD(request):
    context = {}
    template = 'CompaniesTemplates/bitcoin.html'
    return render(request, template, context)
