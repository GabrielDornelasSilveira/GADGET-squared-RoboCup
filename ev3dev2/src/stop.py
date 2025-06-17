#!/usr/bin/env python3

from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D
from time import sleep

# Lista das saídas que podem estar sendo usadas
outputs = [OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D]

# print("Parando todos os motores...")

# Tentar parar motores em todas as portas
for out in outputs:
    try:
        motor = LargeMotor(out)
        motor.stop()
        # print(f"Motor na porta {out} parado.")
    except Exception as e:
        # Porta não usada ou motor não conectado — ignorar
        pass

sleep(0.1)
