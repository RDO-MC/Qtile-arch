#!/bin/bash

# Terminar todas las instancias de Polybar
killall -q polybar

# Esperar a que los procesos se detengan completamente
while pgrep -u $UID -x polybar >/dev/null; do sleep 1; done

# Iniciar Polybar
polybar -r bar &
echo "Polybar iniciada."
