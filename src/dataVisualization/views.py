from analysis import financial_data
from django.views.generic import TemplateView
from django.shortcuts import HttpResponse, render
from analysis import machine_models

# Create your views here.


class Diagrams(TemplateView):
    template_name = 'diagrams.html'


class AAPL(TemplateView):
    template_name = 'CompaniesTemplates/AAPL.html'
    id = 1
    stmt = '''
    SELECT date, open, high, low, close, volume,
    adj_open, adj_high, adj_low, adj_close, adj_volume
    FROM information
    WHERE company_id=%s;
    ''' % id
    amd = financial_data.get_db_data(stmt)
    # print(amd.head())
    features, label = machine_models.backtest_bollinger(amd)

    def post(self, request):

        # Select Menue form
        model = request.POST.get('model', None)

        # Rest of form
        High = request.POST.get('feature1', None)
        Low = request.POST.get('feature2', None)
        Upperband = request.POST.get('feature3', None)
        Lowerband = request.POST.get('feature4', None)

        # Sure taht selected model is in the right syntax
        if str(model).lower() == 'decesion tree c4.5':
            model = 'dts'
        elif str(model).lower() == 'gaussian nayiv bayes':
            model = 'gnb'
        else:
            model = 'knn'

        # Prepairing input feature in 2D list
        input_col = [[float(High), float(Low),
                      float(Upperband), float(Lowerband)]]

        result = machine_models.ApplyModel(
            str(model), self.features, self.label, input_col)

        if str(result).lower() == 'buy':
            message = " Since High stock price is going through bolinger band upper band we make sure that the prices will go down so we recommend that u sell your stocks befor the price get low."
            result = 'buy'
        elif str(result).lower() == 'sell':
            message = " Since low stock price is going through bolinger band upper band we make sure that the prices will go Up so we recommend that u Buy stocks as you can to sell it with profits in the future."
            result = 'sell'
        else:
            message = "you can hold down and wait or you can make to operations BUY and SELL to reduce the risk of lose."
            result = 'two operations'

        context = {
            'decesion': str(result),
            'recommendtion': str(message),
        }

        return render(request, self.template_name, context=context)


class AMD(TemplateView):
    template_name = 'CompaniesTemplates/AMD.html'
    id = 2
    stmt = '''
    SELECT date, open, high, low, close, volume,
    adj_open, adj_high, adj_low, adj_close, adj_volume
    FROM information
    WHERE company_id=%s;
    ''' % id
    amd = financial_data.get_db_data(stmt)


class FB(TemplateView):
    template_name = 'CompaniesTemplates/FB.html'
    id = 4
    stmt = '''
    SELECT date, open, high, low, close, volume,
    adj_open, adj_high, adj_low, adj_close, adj_volume
    FROM information
    WHERE company_id=%s;
    ''' % id
    fb = financial_data.get_db_data(stmt)


class GOOG(TemplateView):
    template_name = 'CompaniesTemplates/GOOG.html'
    id = 5
    stmt = '''
    SELECT date, open, high, low, close, volume,
    adj_open, adj_high, adj_low, adj_close, adj_volume
    FROM information
    WHERE company_id=%s;
    ''' % id
    goog = financial_data.get_db_data(stmt)


class INTC(TemplateView):
    template_name = 'CompaniesTemplates/INTC.html'
    id = 6
    stmt = '''
    SELECT date, open, high, low, close, volume,
    adj_open, adj_high, adj_low, adj_close, adj_volume
    FROM information
    WHERE company_id=%s;
    ''' % id
    intc = financial_data.get_db_data(stmt)


0


class MSFT(TemplateView):
    template_name = 'CompaniesTemplates/MSFT.html'
    id = 7
    stmt = '''
    SELECT date, open, high, low, close, volume,
    adj_open, adj_high, adj_low, adj_close, adj_volume
    FROM information
    WHERE company_id=%s;
    ''' % id
    msft = financial_data.get_db_data(stmt)


class EA(TemplateView):
    template_name = 'CompaniesTemplates/EA.html'
    id = 3
    stmt = '''
    SELECT date, open, high, low, close, volume,
    adj_open, adj_high, adj_low, adj_close, adj_volume
    FROM information
    WHERE company_id=%s;
    ''' % id
    ea = financial_data.get_db_data(stmt)


class NVDA(TemplateView):
    template_name = 'CompaniesTemplates/NVDA.html'
    id = 8
    stmt = '''
    SELECT date, open, high, low, close, volume,
    adj_open, adj_high, adj_low, adj_close, adj_volume
    FROM information
    WHERE company_id=%s;
    ''' % id
    nvda = financial_data.get_db_data(stmt)


class RTN(TemplateView):
    template_name = 'CompaniesTemplates/RTN.html'
    id = 9
    stmt = '''
    SELECT date, open, high, low, close, volume,
    adj_open, adj_high, adj_low, adj_close, adj_volume
    FROM information
    WHERE company_id=%s;
    ''' % id
    rtn = financial_data.get_db_data(stmt)


class TWTR(TemplateView):
    template_name = 'CompaniesTemplates/TWTR.html'
    id = 10
    stmt = '''
    SELECT date, open, high, low, close, volume,
    adj_open, adj_high, adj_low, adj_close, adj_volume
    FROM information
    WHERE company_id=%s;
    ''' % id
    twtr = financial_data.get_db_data(stmt)


class YHOO(TemplateView):
    template_name = 'CompaniesTemplates/YHOO.html'
    id = 11
    stmt = '''
    SELECT date, open, high, low, close, volume,
    adj_open, adj_high, adj_low, adj_close, adj_volume
    FROM information
    WHERE company_id=%s;
    ''' % id
    yhoo = financial_data.get_db_data(stmt)
