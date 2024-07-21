#!/usr/bin/env bash

# Log file location
LOG_FILE="$HOME/.config/polybar/rofi_pawer.log"

# Start logging
echo "Generating power menu..." > "$LOG_FILE" 2>&1

# Power menu options
power_menu_options="󰐥  Shutdown\n󰐦  Restart\n󰐧  Log Out\n󰑾  Lock Screen"

# Use rofi to select power option
chosen_option=$(echo -e "$power_menu_options" | rofi -dmenu -i -p "Power Menu: " -format s)
echo "Chosen option: $chosen_option" >> "$LOG_FILE"

# Process selected option
case "$chosen_option" in
    "󰐥  Shutdown")
        echo "Executing shutdown..." >> "$LOG_FILE"
        systemctl poweroff >> "$LOG_FILE" 2>&1
        ;;
    "󰐦  Restart")
        echo "Executing restart..." >> "$LOG_FILE"
        systemctl reboot >> "$LOG_FILE" 2>&1
        ;;
    "󰐧  Log Out")
        echo "Logging out..." >> "$LOG_FILE"
        i3-msg exit >> "$LOG_FILE" 2>&1 || openbox --exit >> "$LOG_FILE" 2>&1
        ;;
    "󰑾  Lock Screen")
        echo "Locking screen..." >> "$LOG_FILE"
        i3lock >> "$LOG_FILE" 2>&1
        ;;
    *)
        echo "No valid option selected" >> "$LOG_FILE"
        ;;
esac
