import serial
import time
import psutil
import GPUtil

# --- CONFIGURAÇÃO ---
PORTA_COM = 'COM3'  # Ajuste para a porta do seu Arduino (veja no App do Arduino)
VELOCIDADE = 9600

try:
    arduino = serial.Serial(PORTA_COM, VELOCIDADE, timeout=1)
    time.sleep(2) # Espera o Arduino resetar
    print(f"Conectado na porta {PORTA_COM}")
except:
    print("Erro: Nao foi possivel conectar ao Arduino. Verifique a porta COM.")
    exit()

while True:
    # 1. Coleta Uso de CPU e RAM
    cpu_usage = psutil.cpu_percent()
    ram_usage = psutil.virtual_memory().percent
    
    # 2. Coleta dados da GPU (Placa de Vídeo)
    gpus = GPUtil.getGPUs()
    gpu_temp = gpus[0].temperature if gpus else 0
    gpu_load = gpus[0].load * 100 if gpus else 0

    # 3. Formatação das linhas (Máximo 16 caracteres por linha)
    # Linha 1: Temps de CPU e GPU (Simulei CPU temp como 50 pois psutil não lê direto no Windows sem Admin)
    linha1 = f"CPU:---C G:{int(gpu_temp)}C" 
    # Linha 2: Usos de RAM, CPU e GPU
    linha2 = f"R:{int(ram_usage)}% C:{int(cpu_usage)}% G:{int(gpu_load)}%"

    # Envia para o Arduino no formato que o código espera
    dados = f"{linha1}|{linha2}\n"
    arduino.write(dados.encode())
    
    time.sleep(2) # Atualiza a cada 2 segundos