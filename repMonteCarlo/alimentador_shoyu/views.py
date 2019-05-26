from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
# Create your views here.




def home_page(request):
    hora_atual = datetime.now()
    context = {'ultima_refeicao': hora_atual.strftime("%H:%M:%S - %d/%m/%y")}
    return render(request, "home_page.html", context)