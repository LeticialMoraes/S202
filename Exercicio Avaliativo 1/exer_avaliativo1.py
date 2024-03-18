import threading
import random
from pymongo import MongoClient


def conectar_bd():
    client = MongoClient('localhost', 27017)
    db = client.Exercicio1
    return db.sensores

# Função para gerar temperatura aleatória
def gerar_temperatura():
    return round(random.uniform(30, 40), 2)

# Função para atualizar o documento do sensor no banco de dados
def atualizar_bd(sensor_id, valor):
    sensores_collection.update_one({"_id": sensor_id}, {"$set": {"valorSensor": valor}})
    if valor > 38:
        sensores_collection.update_one({"_id": sensor_id}, {"$set": {"sensorAlarmado": True}})
    else:
        sensores_collection.update_one({"_id": sensor_id}, {"$set": {"sensorAlarmado": False}})

# Função para simular o comportamento de um sensor
def simular_sensor(sensor_id, nome_sensor, db_collection):
    while True:
        temperatura = gerar_temperatura()
        print(f"{nome_sensor} - Temperatura: {temperatura}°C")
        atualizar_bd(sensor_id, temperatura)
        if temperatura > 38:
            print(f"Atenção! Temperatura muito alta! Verificar {nome_sensor}!")
            break

# Conectar ao banco de dados
sensores_collection = conectar_bd()

# Criar e iniciar as threads para simular os sensores
threads = []
for sensor_id, nome_sensor in [(1, "Temp1"), (2, "Temp2"), (3, "Temp3")]:
    t = threading.Thread(target=simular_sensor, args=(sensor_id, nome_sensor, sensores_collection))
    threads.append(t)
    t.start()

# Aguardar as threads terminarem
for t in threads:
    t.join()
