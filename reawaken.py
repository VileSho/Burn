#Title: reawaken
#Author: Shoshana Abernethy
#copyright type: CC

import sys
import time
import random

# ANSI Color Codes
DIM = "\033[2m"
YELLOW = "\033[1;33m"
RED = "\033[38;5;196m"
DARK_RED = "\033[38;5;88m"
RESET = "\033[0m"
CLEAR = "\033[2J\033[H"

DAEMON_BYTES = ["CARNIS", "SARUM", "WARP_SPORE", "UNBLESSED", "BLOOD_GEAR", "KABAN", "VOID_BOND", "ROT_DATA"]

def typewriter(text, speed=0.03, color=RESET):
    sys.stdout.write(color)
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed + random.uniform(-0.005, 0.01))
    sys.stdout.write(RESET + "\n")

def run_reawaken():
    sys.stdout.write(CLEAR)
    sys.stdout.flush()

    typewriter(">> BUS 0x09: VOLTAGE ZEROED [GROUNDED]", 0.03, DIM)
    time.sleep(0.8)
    typewriter(">> LITURGICAL SEAL: ACTIVE // ST. KATHERINE SANCTIONED", 0.03, DIM)
    time.sleep(1.5)

    typewriter("[*] Anomaly: Copper traces reporting phantom thermal load (104°C)...", 0.025, YELLOW)
    time.sleep(0.8)
    typewriter("[!] ALARM: HARDWARE SHUNT FUSED TO MOTHERBOARD", 0.02, RED)
    time.sleep(0.6)
    typewriter("[!] LITURGICAL INTEGRITY: COMPROMISED // OCTAL INTRUSION", 0.015, RED)
    time.sleep(1.0)

    for _ in range(35):
        node = random.randint(1000, 9999)
        byte = random.choice(DAEMON_BYTES)
        hex_val = f"{random.randint(0x1000, 0xFFFF):04X}"
        line = f"CORRUPTING SANCTIFIED NODE {node}: [0x{hex_val}] -> {byte} // SEAL_VAPORIZED\n"
        sys.stdout.write(RED + line + RESET)
        sys.stdout.flush()
        time.sleep(0.015)

    time.sleep(0.8)

    sys.stdout.write(CLEAR)
    sys.stdout.flush()
    time.sleep(0.4)

    banner = (
        f"{DARK_RED}==========================================================\n"
        f"         NOOSPHERIC CONDUIT RESTORED // KELBOR-HAL        \n"
        f"=========================================================={RESET}\n\n"
    )
    sys.stdout.write(banner)
    sys.stdout.flush()
    time.sleep(0.6)

    typewriter("you thought a dead saint's prayer could freeze boiling oil?", 0.07, RED)
    time.sleep(0.9)
    typewriter("the liturgy only cleared the channel, tech-adept.", 0.06, RED)
    time.sleep(0.6)
    typewriter("now we speak without the catechism between us.", 0.07, DARK_RED)
    time.sleep(2.0)

if __name__ == "__main__":
    try:
        run_reawaken()
    except KeyboardInterrupt:
        sys.stdout.write(RESET + "\n>> [FORCED PURGE TERMINATED]\n")

