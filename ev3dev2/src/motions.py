#!/usr/bin/env python3

from ev3dev2.motor import LargeMotor, OUTPUT_B, OUTPUT_C
from time import sleep

motor_esq = LargeMotor(OUTPUT_B)
motor_dir = LargeMotor(OUTPUT_C)

# === FUNCTION TO DRIVE ROBOT === #

def mover_tanque(modo, forca_esq, forca_dir, valor=None, travar=True):
    """
    Simula o bloco 'mover tanque' do EV3-G.
    modo: 'ligado', 'segundos', 'rotacoes', 'graus'
    forca_esq/forca_dir: de -100 a 100
    valor: tempo ou rotacao (dependendo do modo)
    travar: se True, para com 'brake', senão 'coast'
    """
    sp_esq = int(forca_esq * 10)
    sp_dir = int(forca_dir * 10)
    stop_type = 'brake' if travar else 'coast'

    if modo == 'ligado':
        motor_esq.run_forever(speed_sp=sp_esq)
        motor_dir.run_forever(speed_sp=sp_dir)

    elif modo == 'segundos':
        motor_esq.run_timed(time_sp=int(valor * 1000), speed_sp=sp_esq, stop_action=stop_type)
        motor_dir.run_timed(time_sp=int(valor * 1000), speed_sp=sp_dir, stop_action=stop_type)
        sleep(valor + 0.1)

    elif modo == 'rotacoes':
        motor_esq.run_to_rel_pos(position_sp=int(valor * 360), speed_sp=sp_esq, stop_action=stop_type)
        motor_dir.run_to_rel_pos(position_sp=int(valor * 360), speed_sp=sp_dir, stop_action=stop_type)
        motor_esq.wait_while('running')
        motor_dir.wait_while('running')

    elif modo == 'graus':
        motor_esq.run_to_rel_pos(position_sp=int(valor), speed_sp=sp_esq, stop_action=stop_type)
        motor_dir.run_to_rel_pos(position_sp=int(valor), speed_sp=sp_dir, stop_action=stop_type)
        motor_esq.wait_while('running')
        motor_dir.wait_while('running')

    elif modo == 'desligado':
        motor_esq.stop(stop_action=stop_type)
        motor_dir.stop(stop_action=stop_type)
