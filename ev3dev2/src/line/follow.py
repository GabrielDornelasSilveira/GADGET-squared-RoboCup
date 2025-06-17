#!/usr/bin/env python3

from ev3dev2.sensor.lego import ColorSensor
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
from test.config import Configuracao

s1 = ColorSensor(INPUT_1)
s2 = ColorSensor(INPUT_2)
s3 = ColorSensor(INPUT_3)
s4 = ColorSensor(INPUT_4)

config = Configuracao("line_config")
threshold = config.obtem("line_threshold")

def calcula_erro():
    v1 = s1.reflected_light_intensity
    v2 = s2.reflected_light_intensity
    v3 = s3.reflected_light_intensity
    v4 = s4.reflected_light_intensity

    p1 = 1 if v1 < threshold else 0
    p2 = 1 if v2 < threshold else 0
    p3 = 1 if v3 < threshold else 0
    p4 = 1 if v4 < threshold else 0

    erro = (-3)*p1 + (-1)*p2 + (1)*p3 + (3)*p4
    ativos = p1 + p2 + p3 + p4

    return erro / ativos if ativos > 0 else 0
