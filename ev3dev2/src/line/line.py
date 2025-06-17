#!/usr/bin/env python3

from time import sleep, time
from line_private import pid_follow, reset_pid
from motions import mover_tanque
# from unstuck import line_unstuck
from follow import calcula_erro
# from green import line_green
# from obstacle import line_obstacle
# from red import line_red
# from silver import line_silver

velocidade_base = 40
last_error = 0
last_time = time()

def line_start():
    # line_found_silver = 0
    reset_pid()
    # silver_init()

def line_stop():
    mover_tanque('desligado', 0, 0)
    # silver_destroy()

def line():

    global last_error, last_time

    erro = calcula_erro()
    now = time()
    dt = now - last_time if last_time > 0 else 0.01

    ajuste, last_error = pid_follow(erro, last_error, dt)

    m_esq = velocidade_base - ajuste
    m_dir = velocidade_base + ajuste
    mover_tanque('ligado', m_esq, m_dir)

    last_time = now

#camera_grab_frame(frame, LINE_FRAME_WIDTH, LINE_FRAME_HEIGHT);
#
#    // Thresholding in here as some images are required by multiple functions
#    line_black_threshold();
#
#    num_green_pixels = 0;
#    image_threshold(LINE_IMAGE_TO_PARAMS_GRAY(green), LINE_IMAGE_TO_PARAMS(frame), &num_green_pixels, is_green);
#
#    //write_image("black.png", LINE_IMAGE_TO_PARAMS_GRAY(black));
#    int ret = 0;

#ifndef LINE_CAPTURE_MODE
#    line_unstuck();
#    line_follow();
#    line_green(0);
#    line_obstacle();
#    line_red();
#
#    ret = line_silver();