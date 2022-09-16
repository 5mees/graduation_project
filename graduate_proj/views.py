from django.shortcuts import render
from .models import GraduateProject





def main_page(request):
    graduate = GraduateProject.objects.all()
    context = {
        'graduate': graduate
    }
    return render(request, 'index.html', context)
