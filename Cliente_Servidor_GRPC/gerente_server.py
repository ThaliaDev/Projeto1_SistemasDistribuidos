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
lista_clientes_vendas = []

mqttBroker = "mqtt.eclipseprojects.io"
client = mqtt.Client("Servidor GRPC")
client.connect(mqttBroker)

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

        if request.usuario_s in dicionario_cliente and request.senha_s == dicionario_cliente[request.usuario_s][0]:
            return gerenciar_adm_pb2.CadastroResponse(responseMessage_s = 'Usuário já existente', compra = None)
        else:
            lista_clientes.append([request.usuario_s, [request.senha_s, request.compra]])
            dicionario_cliente = dict(lista_clientes)
            client.publish("CADASTRO", str(dicionario_cliente))
            print("Castrados existentes " + str(dicionario_cliente) + " na base de dados!")

            return gerenciar_adm_pb2.CadastroResponse(responseMessage_s = 'Usuário Cadastrado', compra = None)

    def listarClientes(self, request, context):
        global dicionario_cliente
        lista_clientes = []
        lista_clientes += [x for x in dicionario_cliente.keys()]
        print(lista_clientes)
        return gerenciar_adm_pb2.ListarClientesResponse(clientes = str(lista_clientes))

    def listarClientesVendas(self, request, context):
        global dicionario_cliente
        global lista_clientes_vendas
        lista_clientes_vendas += [y[1] for x,y in dicionario_cliente.items()]
        print(lista_clientes_vendas)
        return gerenciar_adm_pb2.ListarClientesResponse(clientes = str(lista_clientes_vendas))

    def editarCadastro(self, request, context):
        global dicionario_cliente
        if request.usuario in dicionario_cliente:
            dicionario_cliente[request.usuario][0] = request.senha
            return gerenciar_adm_pb2.EditarCadastroResponse(responseMessage = "Senha alterada com sucesso")
        else:
            return gerenciar_adm_pb2.EditarCadastroResponse(responseMessage = "Usuário não existente")


    def excluirCadastro(self, request, context):
        global dicionario_cliente
        global lista_clientes_vendas
        if request.usuario in dicionario_cliente:
            dicionario_cliente.pop(request.usuario)
            return gerenciar_adm_pb2.ExcluirCadastroResponse(responseMessage = "Usuário deletado com sucesso")
        else:
            return gerenciar_adm_pb2.ExcluirCadastroResponse(responseMessage = "Usuário não existente")

print(dicionario_cliente)
print(lista_clientes)

def serve():

    server = grpc.server(futures.ThreadPoolExecutor(max_workers = 10))
    gerenciar_adm_pb2_grpc.add_UserServicer_to_server(User(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    logging.basicConfig()
    serve()
