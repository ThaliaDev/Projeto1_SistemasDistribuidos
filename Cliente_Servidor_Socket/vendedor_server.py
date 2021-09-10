import socket
import json
import paho.mqtt.client as mqtt
import time
import ast

dados_usuario = dict()
'''dados_usuario['Thalia'] = ["123","null"]
dados_usuario['Thalia'][1] = dict()
print(dados_usuario)'''

s = socket.socket()
host = socket.gethostname()
port = 12347
s.bind((host, port))
s.listen(5)

def on_message(client, userdata, message):
    print("Cadastros existentes: ", str(message.payload.decode("utf-8")))
    global dados_usuario
    dados_usuario = ast.literal_eval(str(message.payload.decode("utf-8")))

mqttBroker = "mqtt.eclipseprojects.io"
client = mqtt.Client("Servidor Socket")
client.connect(mqttBroker)

client.loop_start()
client.subscribe("CADASTRO")
client.on_message = on_message
time.sleep(20)

while True:
    print(dados_usuario)
    c, addr = s.accept()
    dados_clientes = c.recv(1024)
    meuUser = dados_clientes.decode()
    meuUserJSON = json.loads(meuUser)
    print(meuUser)
    print(meuUserJSON)
    for chave, valor in meuUserJSON.items():
        print(chave, valor)
        for key, value in dados_usuario.items():
            print(key, value)
            if(key == chave and value[0] == valor):
                print(f"Usuário logado {meuUser}")
                c.sendall(f"Bem-vind@, {chave}.".encode())
                compra = c.recv(1024)
                dados_compra = compra.decode()
                dados_usuario[chave][1] = dados_compra
                dados_usuario.update(dados_usuario)
            else:
                c.sendall("Usuário ou senha incorretos.".encode())
    c.close()