#!/usr/bin/env python3

Kp = 1.2
Ki = 0.0
Kd = 0.6

integral = 0

def reset_pid():
    global integral
    integral = 0

def pid_follow(erro, erro_anterior, dt):
    global integral

    proporcional = erro
    integral += erro * dt
    derivada = (erro - erro_anterior) / dt

    ajuste = Kp * proporcional + Ki * integral + Kd * derivada

    return ajuste, erro
