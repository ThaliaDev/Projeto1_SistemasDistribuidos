from __future__ import print_function
import logging
import grpc
import gerenciar_adm_pb2_grpc
import gerenciar_adm_pb2
import ast

def removeChar(lista):
    pontuacao = ['[','{',']','}',"'"]
    for i in lista:
        if i in pontuacao:
            lista = lista.replace(i,'')
    return lista

def cadastro(stub):

    usuario_s = input("Nome de login do funcionário: ")
    dados_cadastro[usuario_s] = input("Senha do funcionário: ")
    responseCad = stub.cadastro(gerenciar_adm_pb2.CadastroRequest(usuario_s = usuario_s, senha_s = dados_cadastro[usuario_s], compra = None))

    if (responseCad.responseMessage_s != "Usuário já existente"):
        print("\nUsuário cadastrado com sucesso no sistema.\n")
    else:
        print("\nUsuário existente na base.\n")

def listarVendas(stub):
    cont = 1
    print("\n=== LISTA DE ITENS VENDIDOS ===\n")
    lista = stub.listarClientesVendas(gerenciar_adm_pb2.ListaVendas())
    lista = ast.literal_eval(lista.vendas)
    for i in lista:
        final = i.split(':')
        final = removeChar(final[1])

        if i != '':
            print(str(cont) + ". " + str(final) + "\n")
            cont += 1

def listarClientes(stub):
    cont = 1
    print("\n=== LISTA DE FUNCIONÁRIOS ===\n")
    lista = stub.listarClientes(gerenciar_adm_pb2.ListaRequest())
    lista = ast.literal_eval(lista.clientes)
    for i in lista:
        print(str(cont) + ". " + i + "\n")
        cont += 1

def editarCadastro(stub):
    usuarioEditado = input("Alteração da senha de qual usuário? ")
    senhaEditada = input("Digite a nova senha: ")
    response = stub.editarCadastro(gerenciar_adm_pb2.EditarCadastroRequest(usuario = usuarioEditado, senha = senhaEditada))
    if response.responseMessage == "Senha alterada com sucesso":
        print("A senha foi alterada com sucesso. \n")
    else:
        print("Usuário não existente.\n")

def excluirCadastro(stub):
    usuarioExcluido = input("Exclusão de qual usuário? ")
    response = stub.excluirCadastro(gerenciar_adm_pb2.ExcluirCadastroRequest(usuario = usuarioExcluido))
    if response.responseMessage == "Usuário deletado com sucesso":
        print("O usuário foi excluído com sucesso. \n")
    else:
        print("Usuário não existente.\n")

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
        print("\n === MENU DE OPÇÕES === \n\n1 - Cadastrar novo funcionário"
              "\n2 - Listar funcionários \n3 - Editar cadastro \n4 - Excluir cadastro"
              "\n5 - Listar vendas \n6 - Logout\n")

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
                listarVendas(stub)
            if opcao == 6:
                break

    else:
        print("\nUsuário ou senha incorretos.")

if __name__ == '__main__':
    logging.basicConfig()
    run()

