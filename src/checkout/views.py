from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class checkout(TemplateView):
    template_name = 'checkout.html'

    @login_required
    def checkout(request):
        context = {}
        return render(request, template_name, context)
