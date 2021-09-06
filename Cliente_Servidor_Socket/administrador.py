import socket
import json


dados_usuario = dict()

dados_usuario['Thalia'] = ["123","null"]
dados_usuario['Thalia'][1] = dict()
print(dados_usuario)

s = socket.socket()
host = socket.gethostname()
port = 12346
s.bind((host, port))
s.listen(5)

while True:
    c, addr = s.accept()
    dados_clientes = c.recv(1024)
    meuUser = dados_clientes.decode()

    print(f"Usuário logado {meuUser}")
    meuUserdict = json.loads(meuUser)

    for chave, valor in meuUserdict.items():
        for key, value in dados_usuario.items():
            if(key == chave and value[0] == valor):
                c.sendall(f"Bem-vind@, {chave}.".encode())
                horario = c.recv(1024)
                dados_meu_pedido = horario.decode()
                print("dados pedido" + dados_meu_pedido)
                dados_usuario[chave][1] = dados_meu_pedido
                dados_usuario.update(dados_usuario)
                print(dados_usuario)
            else:
                c.sendall("Usuário ou senha incorretos.".encode())
        print(f"minha chave e {chave} meu valor e {valor} o horario na minha agenda é {dados_usuario[chave][1]}")
    c.close()
