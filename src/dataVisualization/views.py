from django.shortcuts import render

# Create your views here.
def diagrams(request):
    context = {}
    template = 'diagrams.html'
    return render(request, template, context)