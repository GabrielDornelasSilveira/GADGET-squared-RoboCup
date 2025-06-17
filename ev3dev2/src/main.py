#!/usr/bin/env python3

import threading
import time
import random
import sys
import signal

from ev3dev2.motor import LargeMotor, OUTPUT_B, OUTPUT_C

from ev3dev2.sensor.lego import ColorSensor
from ev3dev2.button import Button
from ev3dev2.led import Leds

# Define os estados principais
STATE_LINE = 0
STATE_RESCUE = 1

# #define DISABLE_BUTTON_START
# #define RESCUE_START

# Variáveis globais estáticas
state = None
main_thread = None
running = False

# Inicialização de hardware
btn = Button()
leds = Leds()
left_motor = LargeMotor(OUTPUT_B)
right_motor = LargeMotor(OUTPUT_C)

# ==== Funções ====
def line_start():
    print("Line mode iniciado.")

def line_stop():
    print("Parando linha.")

def line():
    # Exemplo: retorna 1 quando detecta "prata"
    return 0

def rescue():
    print("Executando resgate...")
    time.sleep(2)

def rescue_cleanup():
    print("Limpando estado do resgate...")

def robot_stop():
    left_motor.stop()
    right_motor.stop()

def robot_led(value):
    color = 'GREEN' if value else 'BLACK'
    leds.set_color('LEFT', color)
    leds.set_color('RIGHT', color)

def robot_init():
    print("Inicializando robô...")

def robot_button():
    return btn.enter

def delay(ms):
    time.sleep(ms / 1000.0)

def milliseconds():
    return int(time.time() * 1000)

# ==== Thread principal ====

def main_loop():
    global state, running
    threading.current_thread().daemon = True

    print("MAIN THREAD START\n")

    # Do all the setup here
    RESCUE_START = False
    if not RESCUE_START:
        state = STATE_LINE
        line_start()
    else:
        state = STATE_RESCUE

    random.seed(milliseconds())

    while running:
        if state == STATE_LINE:
            ret = line()
            if ret == 1:
                print("Found silver\n")
                state = STATE_RESCUE
                line_stop()
                delay(200)
        else:
            rescue()
            # Rescue finished
            state = STATE_LINE
            line_start()

# ==== Reset ====

def stop():
    global running, main_thread
    print("MAIN THREAD CANCEL\n")
    running = False
    if main_thread and main_thread.is_alive():
        main_thread.join()

    robot_stop()

    # Cleanup a bit (hopefully works)
    if state == STATE_LINE:
        line_stop()
    elif state == STATE_RESCUE:
        rescue_cleanup()

    # robot_serial_close()
    # robot_serial_init()

    print("STOP\n")

    #ifdef DISPLAY_ENABLE
    # display.set_mode(MODE_IDLE)
    #endif

def quit_program():
    stop()
    # display.destroy()
    robot_led(0)
    sys.exit(0)

def sig_int_handler(sig, frame):
    if sig == signal.SIGINT:
        print("SIGINT\n")
        quit_program()

# ==== Controle por botão ====

def button_loop(button_value, idle):
    while (1 if robot_button() else 0) == (1 if button_value else 0):
        #ifdef DISPLAY_ENABLE
        # if display.loop(): quit_program()
        if idle:
            # display.set_number(NUMBER_BAT_VOLTAGE, read_voltage())
            delay(20)
        #endif

# ==== Função principal ====

def main():
    global running, main_thread

    # if(signal(SIGINT, sig_int_handler) == SIG_ERR)
    signal.signal(signal.SIGINT, sig_int_handler)

    robot_init()

    #ifdef DISPLAY_ENABLE
    # display.create(0)
    #endif

    while True:
        DISABLE_BUTTON_START = False
        if not DISABLE_BUTTON_START:
            robot_led(1)
            button_loop(0, 1)
            robot_led(0)
            button_loop(1, 1)

        running = True
        main_thread = threading.Thread(target=main_loop)
        main_thread.start()

        button_loop(0, 0)

        sys.exit(1)

        stop()

        button_loop(1, 0)

# ==== Execução ====

if __name__ == "__main__":
    main()
