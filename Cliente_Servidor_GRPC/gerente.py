from __future__ import print_function
import logging
import grpc
import gerenciar_adm_pb2_grpc
import gerenciar_adm_pb2

def cadastro(stub):

    usuario_s = input("Nome de login do cliente: ")
    dados_cadastro[usuario_s] = input("Senha do cliente: ")
    responseCad = stub.cadastro(gerenciar_adm_pb2.CadastroRequest(usuario_s = usuario_s, senha_s = dados_cadastro[usuario_s], compra = None))

    if (responseCad.responseMessage_s != "Usuário já existente"):
        print("\nUsuário cadastrado com sucesso no sistema.\n")
    else:
        print("\nUsuário existente na base.\n")

def listarClientes(stub):
    print("Listar clientes cadastrados")

def editarCadastro(stub):
    print("Editar cadastro")

def excluirCadastro(stub):
    print("Excluir cadastro")

dados_cadastro = dict()

print("\nBem-vind@ ao portal do administrador! Faça o seu login.\n")

usuario = input("Usuário: ")
senha = input("Senha: ")


def run():
    channel = grpc.insecure_channel('localhost:50051')
    stub = gerenciar_adm_pb2_grpc.UserStub(channel)
    response = stub.login(gerenciar_adm_pb2.LoginRequest(usuario = usuario, senha = senha))

    if (response.responseMessage == "Usuário logado"):
        print(f"\nBem vind@, {usuario}.")
        print("\n === MENU DE OPÇÕES === \n\n1 - Cadastrar novo cliente"
              "\n2 - Listar clientes cadastrados \n3 - Editar cadastro \n4 - Excluir cadastro"
              "\n5 - Logout\n")

        while True:
            opcao = int(input("Opção: "))
            if opcao == 1:
                cadastro(stub)
            if opcao == 2:
                listarClientes(stub)
            if opcao == 3:
                editarCadastro(stub)
            if opcao == 4:
                excluirCadastro(stub)
            if opcao == 5:
                break

    else:
        print("\nUsuário ou senha incorretos.")

if __name__ == '__main__':
    logging.basicConfig()
    run()

