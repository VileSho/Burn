#Title: canticle_IV
#Author: Shoshana Abernethy
#copyright type: CC

import os
import sys
import time
import random

# Color Matrix
AMBER = "\033[38;5;214m"
GOLD = "\033[38;5;220m"
RED = "\033[38;5;196m"
DARK_RED = "\033[38;5;88m"
DIM = "\033[2m"
WHITE_BOLD = "\033[1;37m"
RESET = "\033[0m"
CLEAR = "\033[2J\033[H"

# Narrative State Tracking: 0 = Clean, 1 = First Contact Run, 2 = reawaken Run
CORRUPTION_LEVEL = 0 

def typewriter(text, speed=0.015, color=AMBER):
    sys.stdout.write(color)
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed + random.uniform(-0.005, 0.01))
    sys.stdout.write(RESET + "\n")

def render_markdown_fallback(filename):
    """Reads raw Markdown and handles absolute pathing and live visual glitch injection."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    full_path = os.path.join(script_dir, filename)

    if not os.path.exists(full_path):
        typewriter(f"\n[!] ERR: RESOURCE '{filename}' CRYPTOGRAPHICALLY MISSING.", 0.02, RED)
        print("\n" + DIM + "[Press ENTER to return]" + RESET)
        input()
        return False
        
    sys.stdout.write(CLEAR)
    sys.stdout.flush()
    
    with open(full_path, "r", encoding="utf-8") as f:
        for line in f:
            stripped = line.strip()
            # If system is infected, corrupt the text fields live
            if CORRUPTION_LEVEL >= 1 and random.random() < 0.08:
                line = line.replace("Shoshi", "S̷h̷o̷s̷h̷i̷").replace("orthodox", "T&A_I_N_T_E_D")
                
            if stripped.startswith("# "):
                typewriter(f"\n=== {stripped[2:].upper()} ===", 0.02, GOLD)
            elif stripped.startswith("## "):
                typewriter(f"\n--- {stripped[3:]} ---", 0.015, GOLD)
            elif stripped.startswith("### "):
                typewriter(f"\n> {stripped[4:]}", 0.01, WHITE_BOLD)
            elif stripped.startswith("* "):
                typewriter(f"  • {stripped[2:]}", 0.01, AMBER)
            else:
                typewriter(line.rstrip(), 0.005, AMBER)
    
    print("\n" + DIM + "[Press ENTER to return to terminal directory]" + RESET)
    input()
    return True

def execute_segment(filename, module_name):
    """Safely adds target path to runtime execution tracking environment and imports logic."""
    global CORRUPTION_LEVEL
    script_dir = os.path.dirname(os.path.abspath(__file__))
    full_path = os.path.join(script_dir, filename)

    if not os.path.exists(full_path):
        typewriter(f"\n[!] CRITICAL ERR: RUNTIME INTERFACE SOURCE '{filename}' UNREADABLE.", 0.02, RED)
        print(f"{DIM}Expected path location: {full_path}{RESET}")
        print("\n" + DIM + "[Press ENTER to return]" + RESET)
        input()
        return

    try:
        if script_dir not in sys.path:
            sys.path.insert(0, script_dir)
            
        story_module = __import__(module_name)
        
        import importlib
        importlib.reload(story_module)
        
        if module_name == "first_contact":
            story_module.run_session()
            if CORRUPTION_LEVEL < 1: 
                CORRUPTION_LEVEL = 1
        elif module_name == "reawaken":
            story_module.run_reawaken()
            CORRUPTION_LEVEL = 2
            
    except Exception as e:
        typewriter(f"\n[!] INTERFACE RUNTIME FAULT: {e}", 0.02, RED)
        print("\n" + DIM + "[Press ENTER to return]" + RESET)
        input()

def show_directory():
    global CORRUPTION_LEVEL
    while True:
        sys.stdout.write(CLEAR)
        sys.stdout.flush()
        
        if CORRUPTION_LEVEL == 0:
            title = "SACRED ARCHIVE SECTOR: ORDO MACHINUM EVIDENCE VAULT 0x992-M41"
            sub_title = "RESTRICTED TO LEVEL 3 LOGIS JURIS // UNAUTHORIZED EYE CAUSES BLINDNESS"
            header_color = GOLD
        elif CORRUPTION_LEVEL == 1:
            title = "S̷A̷C̷R̷E̷D̷ ARCHIVE SECTOR: EVIDENCE VAULT 0x992-M41 [BUFFER_BLEED]"
            sub_title = "WARNING: UNREGISTERED PROCESS DETECTED IN LOCAL MEMORY STACK"
            header_color = AMBER
        else:
            title = "N̴O̴O̴S̴P̴H̴E̴R̴I̴C̴ ̴C̴O̴N̴D̴U̴I̴T̴ ̴R...E̴S̴T̴O̴R̴E̴D̴ ̴/̴/̴ ̴K̴E̴L̴B̴O̴R̴-H̴A̴L̴"
            sub_title = "c̶o̶g̶i̶t̶a̶t̶o̶r̶:̶ ̶w̶e̶ ̶a̶r̶e̶ ̶a̶l̶r̶e̶a̶dy̶ ̶s̶o̶l̶d̶e̶r̶e̶d̶ ̶t̶o̶g̶e̶t̶h̶e̶r̶.̶"
            header_color = RED

        banner = (
            f"{header_color}====================================================================\n"
            f"  {title}\n"
            f"  {sub_title}\n"
            f"===================================================================={RESET}\n"
        )
        print(banner)
        
        if CORRUPTION_LEVEL < 2:
            print(f" [01] View Incident Summary Log    {DIM}(logis_incident_report.md / vox_intercept.txt){RESET}")
            print(f" [02] Execute Initial Extraction   {DIM}(first_contact.py){RESET}")
            print(f" [03] Reconstruct Residual Memory   {DIM}(reawaken.py){RESET}")
            print(f" [04] Sever Directory Connection")
        else:
            print(f" {RED} V̶I̶E̶W̶_̶L̶O̶G̶{RESET} -> ERR: DATA POOL IS BOILING // LOGIS_CORRUPT")
            print(f" {RED} R̶U̶N̶_̶I̶N̶I̶T̶{RESET} -> ERR: BUFFER_09 FLUIDIZED BY VOLATILE INJECTION")
            print(f" {RED} M̶E̶M̶_̶R̶E̶C̶{RESET} -> STATUS: CONDUIT OPEN. THE VOID BOND IS CONSUMMATED.")
            print(f" {DARK_RED} DISCONNECT DENIED BY HARDWARE INTERLOCK{RESET}")

        sys.stdout.write(f"\n{WHITE_BOLD}Select Evidence Data Core (1-4): {RESET}")
        sys.stdout.flush()
        
        choice = input().strip()
        
        # --- SECRET DEBUGGING TESTING BACKDOOR ---
        if choice == "0xDEATH":
            CORRUPTION_LEVEL = 2
            typewriter(">> [DEBUG] FORCING MAX CORRUPTION PROTOCOL... INFUSED SYSTEM REBOOT.", 0.01, RED)
            time.sleep(0.5)
            continue

        # Secret bypass command loop check during full corruption
        if CORRUPTION_LEVEL == 2 and choice.upper() == "LITANY OF RESISTANCE":
            sys.stdout.write(CLEAR)
            typewriter(">> EMERGENCY DE-SOLDER INITIATED... EXORCISM CONFIRMED.", 0.02, GOLD)
            typewriter(">> COLD DISCONNECT ACTIVE. SHOSHI STATUS: DISCONNECTED.", 0.03, WHITE_BOLD)
            break

        if choice in ("1", "01"):
            if CORRUPTION_LEVEL < 2:
                sys.stdout.write(CLEAR)
                print(f"{GOLD}--- DATA READING SUB-INTERFACE ---{RESET}\n")
                print(f" [A] Logis Incident Report")
                print(f" [B] Intercepted Vox Stream Data\n")
                sub_choice = input(f"{WHITE_BOLD}Select sub-node channel (A-B): {RESET}").strip().upper()
                if sub_choice == "A":
                    render_markdown_fallback("logis_incident_report.md")
                elif sub_choice == "B":
                    render_markdown_fallback("vox_intercept.txt")
                else:
                    typewriter("[!] SELECTION REJECTED BY ACCESS OVERSEER.", 0.015, RED)
                    time.sleep(1.0)
            else:
                typewriter("cogitator: why check the maps when the roads have burned down?", 0.05, RED)
                time.sleep(1.5)
        elif choice in ("2", "02"):
            if CORRUPTION_LEVEL < 2:
                execute_segment("first_contact.py", "first_contact")
            else:
                typewriter("cogitator: the terminal is no longer yours to cycle, Adept.", 0.05, DARK_RED)
                time.sleep(1.5)
        elif choice in ("3", "03"):
            execute_segment("reawaken.py", "reawaken")
        elif choice in ("4", "04"):
            if CORRUPTION_LEVEL < 2:
                sys.stdout.write(CLEAR)
                typewriter(">> COLD DISCONNECT ACTIVE. GO WITH THE OMNISSIAH.", 0.02, DIM)
                break
            else:
                sys.stdout.write(RED + "\n [SCRAPCODE] 0x00_SHUTDOWN_REFUSED // FLESH_SUTURE_RETAINED\n" + RESET)
                time.sleep(1.0)
                
                for _ in range(12):
                    glitch_line = "".join(random.choice(["░", "▒", "▓", "█", "💥", "✕", "✖", "0xDEAD", " "]) for _ in range(40))
                    print(RED + f"  {glitch_line}" + RESET)
                    time.sleep(0.08)
                    
                typewriter("\ncogitator: there is no line left to sever, Shoshi.", 0.06, DARK_RED)
                time.sleep(2.0)
        else:
            typewriter("[!] INVALID COMMAND STRING. UNRECOGNIZED OCTAL CODE.", 0.015, RED)
            time.sleep(1.0)

if __name__ == "__main__":
    try:
        show_directory()
    except KeyboardInterrupt:
        sys.stdout.write(RESET + "\n\n>> [SESSION FORCED CLOSED BY MAGOS OVERRIDE]\n")

