from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from datetime import datetime
from time import sleep

## Biblioteca para comunicar com Arduino - NAO NATIVA
import serial
import serial.tools.list_ports as lista_portas

DESATIVA_MOTOR = '0'.encode()
ATIVA_MOTOR = '1'.encode()


def home_page(request):
    hora_atual = datetime.now()
    context = {'ultima_refeicao': hora_atual.strftime("%H:%M:%S - %d/%m/%y")}
    return render(request, "home_page.html", context)

def trata_sinal_alimentacao(request):
    
    # Dicionario de dados enviados para a pagina 
    dados = {'data_sinal': ''}
    # Adquire Hora atual
    hora_atual = datetime.now()
    # Recebe sinal passado pelo Card
    sinal = request.POST.get("sinal_id", None)
    
    if sinal.encode() == ATIVA_MOTOR:
        # Ativa Motor para alimentacao
        ativar_alimentacao()
        sleep(2.5)
        desativar_alimentacao()
        
    elif sinal.encode() == DESATIVA_MOTOR:
        desativar_alimentacao()
    
    dados['data_sinal'] = hora_atual.strftime("%H:%M:%S - %d/%m/%y")
    return JsonResponse(dados)

def conecta_arduino():
    # Buscamos pela porta a qual o arduino esta
    ports = list(lista_portas.comports())
    porta = ports[0].device
    #Conectamos no arduino
    return serial.Serial(porta, 9600)
    
def ativar_alimentacao():
    serialArduino = conecta_arduino()
    serialArduino.write(ATIVA_MOTOR)
    serialArduino.close()

def desativar_alimentacao():
    serialArduino = conecta_arduino()
    serialArduino.write(DESATIVA_MOTOR)
    serialArduino.close()