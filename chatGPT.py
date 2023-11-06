import serial
import time as sleep

while True: #Laço para conexão com o Arduino
    try: #Tenta se conectar ao Arduino
        arduino = serial.Serial('COM3', 9600) #Cria um elemento conectado a porta COM3
        arduino.flush()
        print(arduino.name)
        break
    except Exception: #Se não for possível, imprime a mensagem e dá um delay de 1 segundo
        print('Não foi possível se conectar ao Arduino')
        sleep(1)
        ~bool


pau = 'a'

arduino.write(pau.encode()) #Envia o comando
arduino.flush() #Limpa o serial