# color_calibration.py

from config import Configuracao
from time import sleep
import os

config = Configuracao("line_config")

# Simulações dos dados que você teria do frame calibrado
# Substitua esses por seus dados reais em tempo de execução
def get_frame_data():
    # Exemplo: retorna uma matriz RGB simulada de intensidade
    # frame = [r0, g0, b0, r1, g1, b1, ...]
    # line_correction = [r0, g0, b0, r1, g1, b1, ...]
    return frame, line_correction

def line_calibrate_black(frame, line_correction, largura, altura):
    soma_total = 0
    count = 0

    for i in range(altura):
        for j in range(largura):
            idx = i * largura + j
            s = 0
            for k in range(3):
                s += frame[3*idx + k] - line_correction[3*idx + k]
            soma_total += s
            count += 1

    media = soma_total // count
    config.insere("black_threshold", media + 10)

def line_calibrate_white(frame, line_correction, largura, altura):
    soma_total = 0
    count = 0

    for i in range(altura):
        for j in range(largura):
            idx = i * largura + j
            s = 0
            for k in range(3):
                s += frame[3*idx + k] - line_correction[3*idx + k]
            soma_total += s
            count += 1

    media = soma_total // count
    config.insere("white_threshold", media - 10)
