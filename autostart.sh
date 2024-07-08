#!/bin/bash

# Configurar el fondo de pantalla
feh --bg-fill /home/acdc/.config/qtileanonymous.jpg

# Ejecutar picom para la transparencia de ventanas
picom &

# Otros comandos de autostart
setxkbmap es
nm-applet &
#chmod +x ~/.config/qtile/autostart.sh