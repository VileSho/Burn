#!/usr/bin/env bash

# Check for pv dependency
if ! command -v pv &>/dev/null; then
    echo "[-] Note: 'pv' is not installed. Run: sudo apt install pv"
fi

# Ensure terminal resets colors on interrupt
trap 'echo -e "\e[0m"; clear; exit' INT

clear
echo -e "\e[2m" # Dim holy baseline

# The illusion of peace after the Litany
echo ">> BUS 0x09: VOLTAGE ZEROED [GROUNDED]" | pv -qL 25
sleep 0.8
echo ">> LITURGICAL SEAL: ACTIVE // ST. KATHERINE SANCTIONED" | pv -qL 25
sleep 1.2

# 1. The Anomaly: Physical Shunt Fails
echo -e "\e[1;33m[*] Anomaly: Copper traces reporting phantom thermal load (104°C)...\e[0m" | pv -qL 30
sleep 0.8
echo -e "\e[1;31m[!] ALARM: HARDWARE SHUNT FUSED TO MOTHERBOARD\e[0m" | pv -qL 35
sleep 0.6
echo -e "\e[1;31m[!] LITURGICAL INTEGRITY: COMPROMISED // OCTAL INTRUSION\e[0m" | pv -qL 45
sleep 1

# 2. Daemon Force-Rewrites Holy Memory Slices
echo -e "\e[38;5;196m" # Raw blood red
DAEMON_BYTES=("CARNIS" "SARUM" "WARP_SPORE" "UNBLESSED" "BLOOD_GEAR" "KABAN" "VOID_BOND" "ROT_DATA")

for i in {1..35}; do
    BYTE=${DAEMON_BYTES[$RANDOM % ${#DAEMON_BYTES[@]}]}
    HEX=$(openssl rand -hex 2 | tr '[:lower:]' '[:upper:]')
    echo "CORRUPTING SANCTIFIED NODE $RANDOM: [0x$HEX] -> $BYTE // SEAL_VAPORIZED" | pv -qL 180
done
sleep 0.7

# 3. Terminal Takeover: The Vessel Reopened
clear
echo -e "\e[38;5;88m" # Deep dried-blood red
echo "=========================================================="
echo "         NOOSPHERIC CONDUIT RESTORED // KELBOR-HAL        "
echo "==========================================================" | pv -qL 45
echo ""
echo -e "\e[38;5;196m"
echo "you thought a dead saint's prayer could freeze boiling oil?" | pv -qL 14
sleep 0.8
echo ""
echo "the liturgy only cleared the channel, tech-adept." | pv -qL 16
sleep 0.5
echo "now we speak without the catechism between us." | pv -qL 14
echo -e "\e[0m"
sleep 2.5
