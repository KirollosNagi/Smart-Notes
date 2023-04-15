from django.shortcuts import render
from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name="home/index.html"

# def home(request):
#     return render(request, 'home/index.html', {})


