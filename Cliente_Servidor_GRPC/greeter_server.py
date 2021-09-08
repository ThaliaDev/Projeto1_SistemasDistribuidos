from concurrent import futures
import logging
import paho.mqtt.client as mqtt
from random import randrange, uniform
import time
import grpc
import requests

import gerenciar_adm_pb2_grpc
import gerenciar_adm_pb2

usuario = 'thalia'
senha = '123'
dicionario_cliente = dict()
lista_clientes = []

class User(gerenciar_adm_pb2_grpc.UserServicer):
    def login(self, request, context):
        if(request.usuario == usuario and request.senha == senha):
            global adm_logado
            adm_logado = 1
            return gerenciar_adm_pb2.LoginResponse(responseMessage='Usuário logado')
        else:
            adm_logado = 0
            return gerenciar_adm_pb2.LoginResponse(responseMessage='Usuário ou senha incorretos.')

    def cadastro(self, request, context):
        global lista_clientes
        global dicionario_cliente

        print(dicionario_cliente)
        if request.usuario_s in dicionario_cliente:
            return gerenciar_adm_pb2.CadastroResponse(responseMessage_s = 'Usuário já existente', compra=None)
        else:
            lista_clientes.append([request.usuario_s, [request.senha_s, request.compra]])
            dicionario_cliente = dict(lista_clientes)

            return gerenciar_adm_pb2.CadastroResponse(responseMessage_s = 'Usuário Cadastrado', compra = None)



print(dicionario_cliente)
print(lista_clientes)

def serve():

    server = grpc.server(futures.ThreadPoolExecutor(max_workers = 10))
    gerenciar_adm_pb2_grpc.add_UserServicer_to_server(User(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

'''if(adm_logado == True and cadastrando == False):

    mqttBroker = "mqtt.eclipseprojects.io"
    client = mqtt.Client("Temperature_Inside")
    client.connect(mqttBroker)

    while True:
        informacoes = str(dicionario_cliente)
        client.publish("Infos cliente", informacoes)
        print("Just published " + str(informacoes) + " to Topic TEMPERATURE")
        time.sleep(1)'''

if __name__ == '__main__':
    logging.basicConfig()
    serve()