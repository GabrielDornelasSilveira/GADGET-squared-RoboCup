#!/bin/bash

# echo "🔄 Recompilando ambiente Python no EV3..."
beep

# Parar motores por segurança
python3 /home/robot/src/stop.py

# Limpar cache de bytecode
rm -rf /home/robot/src/__pycache__/

# Garantir permissões
chmod +x /home/robot/src/*.py
chmod +x /home/robot/src/autostart.sh

# cd /home/robot/ev3dev2 && git pull

# echo "✅ Ambiente limpo e pronto. Iniciando novamente..."
beep

bash /home/robot/src/autostart.sh
