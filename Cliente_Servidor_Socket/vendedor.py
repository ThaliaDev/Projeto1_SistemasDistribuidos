import socket,json

dados_entrada = dict()
horario = dict()
repetir_aceito = [1,0]

s = socket.socket()
host = socket.gethostname()
port = 12347

user = str(input("Usuário: "))
dados_entrada[user] = str(input("Senha: "))


json = json.dumps(dados_entrada).encode('utf-8')

s.connect((host, port))
s.sendall(json)
data = s.recv(1024)
logado = data.decode()

if logado == f"Bem-vind@, {user}.":
    print("\n"+ logado + " Essa é a sua área de trabalho.")
    print("Cadastre uma nova compra! \n")

    nomeCliente = input("Nome do cliente: ")
    nomeItem = input("Nome do item: ")
    valor = input("Valor: ")
    itemValor = " comprou um(a) " + nomeItem + " no valor de R$" + valor

    dados_compra = dict()
    dados_compra[nomeCliente] = [itemValor]
    dados_compra_encode = str(dados_compra)
    print("\nVenda realizada!")
    s.sendall(dados_compra_encode.encode())

else:
    print(logado)

s.close()