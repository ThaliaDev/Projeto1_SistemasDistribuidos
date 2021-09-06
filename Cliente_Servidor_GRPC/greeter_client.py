from __future__ import print_function
import logging
import grpc
import gerenciar_adm_pb2_grpc
import gerenciar_adm_pb2

dados_cadastro = dict()

print("Bem-vind@ ao portal do administrador!")

usuario = input("Usuário: ")
senha = input("Senha: ")


def run():
    channel = grpc.insecure_channel('localhost:50051')
    stub = gerenciar_adm_pb2_grpc.UserStub(channel)
    response = stub.login(gerenciar_adm_pb2.LoginRequest(usuario=usuario, senha=senha))
    if (response.responseMessage == "Usuário logado"):
        print(f"\nBem vind@, {usuario}.")
        print("Está tudo preparado para você cadastrar um novo cliente!\n")
        while True:
            usuario_s = input("Nome de login do cliente: ")
            dados_cadastro[usuario_s] = input("Senha do cliente: ")

            stub.cadastro(gerenciar_adm_pb2.CadastroRequest(usuario_s=usuario_s, senha_s=dados_cadastro[usuario_s]))
            if (gerenciar_adm_pb2.CadastroResponse(responseMessage_s='Usuário Cadastrado')):
                print("\nUsuário cadastrado com sucesso no sistema.\n")
            novoCadastro = int(input("Deseja cadastrar um novo usuário? \n 1 - Sim \n 0 - Não\n"))

            if(novoCadastro == 0):
                break
            else:
                continue
    else:
        print("\nUsuário ou senha incorretos.")


if __name__ == '__main__':
    logging.basicConfig()
    run()
