from analysis import financial_data
from django.views.generic import TemplateView

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
    aapl = financial_data.get_db_data(stmt)
    

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
