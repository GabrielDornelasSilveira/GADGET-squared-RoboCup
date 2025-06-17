#!/bin/bash

# Parar motores por segurança
python3 /home/robot/src/stop.py

# Entrar na pasta do projeto
cd /home/robot/src

# Executar o robô em loop (caso ele termine ou falhe, reinicia)
while true; do
    python3 main.py && break
    sleep 1
done
