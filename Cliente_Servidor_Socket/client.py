import socket,json

dados_entrada = dict()
horario = dict()
repetir_aceito = [1,0]

s = socket.socket()
host = socket.gethostname()
port = 12346

user = str(input("Usuário: "))
dados_entrada[user] = str(input("Senha: "))

json = json.dumps(dados_entrada).encode('utf-8')

s.connect((host, port))
s.sendall(json)
data = s.recv(1024)
logado = data.decode()

if logado == f"Bem-vind@, {user}.":
    print("\n"+logado + " Essa é a sua agenda virtual.")
    print("Marque um horário na agenda para ser notificado! \n")

    tituloNotificacao = input("Titulo da notificação: ")
    data = input("Insira a data no formato dd/mm/aaaa: ")
    hora = input("Insira a hora no formato hh:mm: ")
    data_hora = data + ' ' + hora

    while True:
        repetir = int(input("Deseja repetir a notificação? \n 1 - Sim \n 0 - Não \n"))
        if repetir not in repetir_aceito:
            print("Opção inválida! Digite 0 ou 1.")
        else:
            break

    horario[tituloNotificacao] = [data_hora,repetir]
    horario_encode = str(horario)
    print("\nNotificação agendada!")
    s.sendall(horario_encode.encode())

else:
    print(logado)

s.close()