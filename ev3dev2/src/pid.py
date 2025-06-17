#!/usr/bin/env python3

from ev3dev2.motor import LargeMotor, OUTPUT_B, OUTPUT_C
from ev3dev2.sensor.lego import ColorSensor
from ev3dev2.sensor import INPUT_2, INPUT_3
from ev3dev2.button import Button
from time import sleep

# Motores individuais para controle direto
motor_esq = LargeMotor(OUTPUT_B)
motor_dir = LargeMotor(OUTPUT_C)

# Sensores
sensor_esq = ColorSensor(INPUT_2)
sensor_dir = ColorSensor(INPUT_3)

# Botão
btn = Button()

# ==== Funções ====

def calibrar_sensor(sensor, nome_sensor):
    print("Coloque o sensor {} sobre a area BRANCA e pressione ENTER.".format(nome_sensor))
    while not btn.enter:
        sleep(0.01)
    branco = sensor.reflected_light_intensity
    print("{} BRANCO: {}".format(nome_sensor, branco))
    sleep(1)

    print("Agora coloque o sensor {} sobre a area PRETA e pressione ENTER.".format(nome_sensor))
    while not btn.enter:
        sleep(0.01)
    preto = sensor.reflected_light_intensity
    print("{} PRETO: {}".format(nome_sensor, preto))
    sleep(1)

    return branco, preto


def normalizar(valor, branco, preto):
    if branco == preto:
        return 50
    return max(0, min(100, 100 * (valor - preto) / (branco - preto)))

# ==== Calibração ====
branco_e, preto_e = calibrar_sensor(sensor_esq, "ESQUERDO")
while btn.enter: pass
branco_d, preto_d = calibrar_sensor(sensor_dir, "DIREITO")
while btn.enter: pass

# ==== PID ====
kp = 1.4
ki = 0.0
kd = 0.6
integral = 0
ultimo_erro = 0


velocidade_base = 85  

# ==== Início ====
print("Seguidor turbo iniciado!")

while not btn.backspace:
    valor_e = normalizar(sensor_esq.reflected_light_intensity, branco_e, preto_e)
    valor_d = normalizar(sensor_dir.reflected_light_intensity, branco_d, preto_d)

    erro = valor_d - valor_e
    integral += erro
    derivada = erro - ultimo_erro
    correcao = kp * erro + ki * integral + kd * derivada
    ultimo_erro = erro

    esq = int(max(-100, min(100, velocidade_base - correcao)))
    dir = int(max(-100, min(100, velocidade_base + correcao)))

    motor_esq.run_direct(duty_cycle_sp=esq)
    motor_dir.run_direct(duty_cycle_sp=dir)

    sleep(0.005)  # ultra responsivo

# Parar ao sair
motor_esq.stop()
motor_dir.stop()
