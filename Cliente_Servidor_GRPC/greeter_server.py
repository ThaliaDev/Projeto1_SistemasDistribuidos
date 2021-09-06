from concurrent import futures
import logging

import grpc
import requests

import gerenciar_adm_pb2_grpc
import gerenciar_adm_pb2

usuario = 'thalia'
senha = '123'
cadastroValido = 2

lista_clientes = []
dicionario_cliente = dict

class User(gerenciar_adm_pb2_grpc.UserServicer):

    def login(self, request, context):
        return gerenciar_adm_pb2.LoginResponse(responseMessage=(
            'Usuário logado' if (request.usuario == usuario and request.senha == senha) else f'Usuário ou senha incorretos'))

    def cadastro(self, request, context):
        global lista_clientes
        global dicionario_cliente
        lista_clientes.append((request.usuario_s,request.senha_s))
        dicionario_cliente = dict(lista_clientes)
        print(lista_clientes)
        print(dicionario_cliente)
        return gerenciar_adm_pb2.CadastroResponse(code_s = 2, responseMessage_s = 'Usuário Cadastrado')

def serve():

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    gerenciar_adm_pb2_grpc.add_UserServicer_to_server(User(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    logging.basicConfig()
    serve()