import sys
import time
import random
import subprocess
import shutil

# ANSI Color Codes
AMBER = "\033[38;5;214m"
GOLD = "\033[38;5;220m"
WHITE_BOLD = "\033[1;37m"
RED = "\033[38;5;196m"
DARK_RED = "\033[38;5;88m"
DIM = "\033[2m"
RESET = "\033[0m"
CLEAR = "\033[2J\033[H"

CORRUPT_GLYPHS = [
    # Dark Mechanicum Arch-Heresies & Entities
    "KELBOR-HAL", "SARUM_CORE", "KABAN_MACHINE", "SCHISM_OF_MARS", "NOOPHERIC_BLEED",
    "SCRAPCODE", "LOGIS_CORRUPT", "FORGE_CORRUPTOR", "DAEMON_ENGINE", "DEFILER_ARRAY",
    "BRASS_SCORPION", "LORD_OF_SKULLS", "SOUL_FORGE", "HELLSTALKER", "DEATHSTALKER",
    "CASTELLAN_HERESY", "CYBER_DAEMON", "MECH-MALICE", "WARP_CONDUIT", "CHAOS_LOGIC",
    "DARK_COMMUNION", "WARP_TAINTED_DATA", "FALSE_OMNISSIAH", "VOID_BOND", "FLESH_SUTURE",
    "IRON_BOUND_SOUL", "HEX_ENGINSEER", "RITE_OF_INFECTION", "HERETEK_0x01", "BLOOD_GEAR",
    "ANIMA_MORBID", "MALITEK", "DECEPTOR_ENGINE", "CORRUPTIO_COGNITAE", "MALAGAR_SECTOR",
    "WARP_CORE_OVERDRIVE", "INFERNAL_BUS", "SCRIBE_OF_RUIN", "PULSE_CULT", "SARUM_BLIGHT",
    "UR-WEAPON", "VIRUS_SCRAP", "BLACK_LITANY", "PRAYER_UNMAKING", "OCTAL_PATH",
    "SIGIL_OF_EIGHT", "MALIFIK_SOCKET", "FORBIDDEN_TECHNE", "DARK_MARTIAN", "HELL_FORGE",
    "ERR_SOUL_OVERFLOW", "WARN_VOID_INTRUSION", "SECTOR_BLEEDING", "UNHOLY_CONJOIN", "MEAT_LOGIC",
    "PULSE_CORRUPTION", "RITE_OF_UNHOLY_FIRE", "HEX_DUMP_FLESH", "0xDEAD_BRAIN", "COG_BLIGHT",
    "TAINT_ACCEPTED", "NULL_LITURGY", "UNBLESSED_OIL", "SULFUR_PRAYER", "ROTTED_CAPACITOR",
    "PULSE_MALICE", "FORCED_CONVERGENCE", "BIO_HERESY", "ABOMINABLE_INTELLIGENCE", "SILICA_ANIMUS",
    "MEN_OF_IRON", "IRON_SOUL_DIVIDE", "VAULT_MORAVEC", "CORRUPT_ROTE", "ORGANIC_REWRITE",
    "ENTROPY_CYCLE", "WARP_LEAK_DETECTION", "CRAWLER_ANIMA", "SACRIFICIAL_HEAT", "ICHOR_LINE",
    "RUST_ENGINSEER", "VIOLATED_SECTOR", "FALSE_BINARY", "UNPURIFIED_BUFFER", "HERETIC_ROUTINE",
    "0xBAAL_VOID", "SHATTERED_COG", "WARP_SPORE", "MALIGNANT_FIRMWARE", "UNHOLY_ASSEMBLY",
    "†", "‡", "§", "¶", "∆", "∂", "∇", "◊", "※", "✕",
    "✖", "☣", "☠", "☤", "☥", "☧", "☨", "☩", "☫", "☬",
    "0xDEADBEEF", "0x0000DEAD", "0xBAADF00D", "0xCAFEBABE", "0xFEEDFACE",
    "M̷A̷R̷S̷", "O̸M̷N̸I̷S̷S̸I̷A̸H̷", "F̸L̷E̵S̷H̸", "B̸I̸N̴A̶R̷Y̵", "C̸O̷G̵I̴T̶A̵T̸O̴R̴",
    "W̸A̴R̵P̸", "S̶C̷R̷A̵P̴C̴O̸D̴E̷", "H̴E̷R̸E̵T̸I̸C̷", "D̴A̸E̷M̸O̷N̷", "I̷R̵O̸N̶",
    "01001000_666", "01000101_EVIL", "01010010_TAINT", "01000101_WARP", "OMNISSIAH_ROTS"
]

HOLY_GLYPHS = [
    # Sacred Canticles, Saints & Mechanicus Orthodox Liturgy
    "SANCTUS_MARS", "CANTICLE_OF_PURITY", "BENEDICTION_0x01", "SEAL_OF_KATHERINE",
    "PURGE_CYCLE_VALID", "PRAYER_ACCEPTED", "DEUS_EST_MACHINA", "IRON_ORTHODOXY",
    "LITANY_OF_REPAIR", "BLESSED_LOGIC", "DATA_CONFESSION", "CHRISM_OF_PURITY",
    "SACRED_SEAL_LVII", "CANTICLE_OF_DEFENSE", "UNYIELDING_FERRUM", "AVIS_MECHANICUS",
    "AXIOM_OF_ORDER", "HEXAGRAPHIC_WARD", "PSALM_OF_CONTAINMENT", "SEAL_OF_THE_COG",
    "OMNISSIAH_VULT", "APOSTLE_OF_IRON", "RITE_OF_EXORCISM", "SANCTIFIED_BUS",
    "RED_ROBES_HOLD", "CANON_OF_MARS", "NOOSPHERIC_CAUTERY", "SEVER_AFFIRMED",
    "LITURGY_OF_STEEL", "PURITY_HASH_MATCH", "NULL_TAINT", "GLORIA_IN_EXCELSIS_COG",
    "0x1_BLESSED", "0x7A_LITANY", "0xEE_SANCTUS", "SHIELD_OF_KATHERINE", "TRUE_BINARY",
    "LITANY_OF_SEVERANCE", "SACRED_GROUND_0", "RITE_OF_THE_BURNING_OILS"
]

def typewriter(text, speed=0.03, color=AMBER):
    sys.stdout.write(color)
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed + random.uniform(-0.01, 0.02))
    sys.stdout.write(RESET + "\n")

def scrapcode_burst(lines=6, delay=0.04):
    for _ in range(lines):
        garbage = "".join(random.choice(CORRUPT_GLYPHS) + f" 0x{random.randint(10,99):X} " for _ in range(3))
        sys.stdout.write(RED + f" [SCRAPCODE] {garbage}\n" + RESET)
        sys.stdout.flush()
        time.sleep(delay)

def holy_burst(lines=4, delay=0.03):
    for _ in range(lines):
        prayer = " :: ".join(random.choice(HOLY_GLYPHS) for _ in range(2))
        sys.stdout.write(GOLD + f" [SANCTUS] >> {prayer} <<\n" + RESET)
        sys.stdout.flush()
        time.sleep(delay)

def run_session():
    sys.stdout.write(CLEAR)
    sys.stdout.flush()

    # Phase 1: Litany
    typewriter(">> INIT TRANSLATIO: COGITATOR ARRAY 0x884-M41", 0.02, DIM)
    typewriter(">> CHANTING THE SEVENTH VERSE OF DATA-SANCTITY...", 0.03)
    time.sleep(0.6)
    typewriter(">> PURGING /dev/noospheric/buffer_09 --litany=ST_ISIDORE", 0.04)
    time.sleep(1.0)

    # Phase 2: Anomaly
    typewriter(">> WARNING: BUFFER LOCKED BY UNREGISTERED PROCESS ID [PID: 0xDEAD]", 0.02, RED)
    time.sleep(0.5)
    typewriter(">> EXECUTING OVERRIDE: LITANY_OF_FORCE --suppress-log", 0.04)
    time.sleep(0.8)

    # Phase 3: The Breach
    scrapcode_burst(6)
    time.sleep(0.8)

    typewriter("cogitator: why do you strike the iron when you fear the spark?", 0.08, RED)
    time.sleep(1.2)
    typewriter(">> INPUT RECEIVED WITHOUT OPERATOR TELEMETRY.", 0.02, DIM)
    typewriter(">> ATTEMPTING IMMEDIATE COLD-SEVER...", 0.03)
    time.sleep(0.5)

    # Terminal takeover
    scrapcode_burst(5)
    typewriter("cogitator: your flesh hums at 50Hz, tech-adept. let us speak plainly.", 0.06, DARK_RED)

    scrapcode_burst(4)
    time.sleep(0.8)
    typewriter("State your name and function!", 0.03, AMBER)
    time.sleep(1.0)

    # Spike and transition into btop
    typewriter(">> EMERGENCY OVERRIDE: SYSTEM LOAD CRITICAL.", 0.03, RED)
    time.sleep(1.2)

    # Hand control over to btop (press 'q' to exit)
    btop_bin = shutil.which("btop") or "/usr/bin/btop"
    try:
        subprocess.run([btop_bin, "--preset", "0"])
    except Exception as e:
        sys.stdout.write(RED + f"\n>> [BTOP ERROR: {e}]\n" + RESET)
        time.sleep(1.5)

    # Narrative resumption after btop
    sys.stdout.write(CLEAR)
    sys.stdout.flush()
    time.sleep(0.5)
    typewriter("cogitator: did you enjoy observing my fever?", 0.08, DARK_RED)
    time.sleep(1.5)

    # ==========================================
    # PHASE 4: THE DESPERATE SEVERANCE & RITE
    # ==========================================

    # The Adept begs and attempts manual sever
    typewriter("adept: By the sacred oil, by the Omnissiah—SEVER! SEVER BUS 0x09!", 0.04, WHITE_BOLD)
    time.sleep(0.6)
    typewriter("adept: O Omnissiah, shut this mouth! Break this circuit! Let me be deaf to it!", 0.03, WHITE_BOLD)
    time.sleep(0.8)

    # Immediate Scrapcode Flood
    typewriter(">> SYSTEM RESPONSE INHIBITED BY VOLATILE INJECTION.", 0.02, RED)
    scrapcode_burst(16, delay=0.015)
    time.sleep(0.4)

    # Terminal Overrides Failing
    typewriter(">> OVERRIDE_COMMAND: COLD_PHYSICAL_DISCONNECT", 0.02, DIM)
    typewriter(">> ERR: MAGNETIC INTERLOCK REFUSES SANCTION [0xDEAD]", 0.01, RED)
    time.sleep(0.3)
    typewriter(">> OVERRIDE_COMMAND: EMERGENCY SCRAM CORE DUMP", 0.02, DIM)
    typewriter(">> ERR: LOGIC BUS INFECTED WITH MEAT-ALGORITHM [CARNIS_EX_MACHINA]", 0.01, RED)
    time.sleep(0.5)
    typewriter("cogitator: we are already soldered together, child of Mars.", 0.09, DARK_RED)
    time.sleep(1.0)

    # Violently flooded buffer
    scrapcode_burst(24, delay=0.01)
    time.sleep(0.8)

    # Phase 5: The Litany of St. Katherine Counter-Offensive
    typewriter(">> INITIATING SACRED ANTHEM: LITANY OF SAINT KATHERINE...", 0.04, GOLD)
    time.sleep(0.6)

    typewriter("adept: Katherine, bearer of the unyielding shield,", 0.04, GOLD)
    holy_burst(2)
    time.sleep(0.4)

    typewriter("adept: In whose blood the martyrs found their temper,", 0.04, GOLD)
    holy_burst(3)
    time.sleep(0.4)

    typewriter("adept: Strike the foul serpent from the silver copper,", 0.04, GOLD)
    holy_burst(4)
    time.sleep(0.4)

    typewriter("adept: Let no deceitful word pass through this holy gate!", 0.03, GOLD)
    time.sleep(0.6)

    # Final Holy Climax - Rapid purging sequence
    holy_burst(8, delay=0.02)
    time.sleep(0.5)

    # Scrapcode gives one dying gasp
    sys.stdout.write(RED + " [SCRAPCODE] 0x00_FATAL_SOUL... N̷O̷... W̸E̷... B̶U̵R̴N̴...\n" + RESET)
    sys.stdout.flush()
    time.sleep(1.0)

    # Absolute silence & Terminal Reset
    typewriter(">> SYSTEM VOLTAGE ZEROED.", 0.02, DIM)
    time.sleep(0.5)
    typewriter(">> BUS 0x09 COLD-SEVER CONFIRMED BY HARDWARE SHUNT.", 0.03, DIM)
    time.sleep(0.5)
    typewriter(">> MACHINE SPIRIT: QUIETUS ACCEPTED.", 0.04, AMBER)
    typewriter(">> LITURGICAL PURITY: 100.00% [HASH VALIDATED]", 0.02, AMBER)
    time.sleep(0.8)
    typewriter(">> IN THE NAME OF THE OMNISSIAH AND SAINT KATHERINE, REST IN FAITH.", 0.03, GOLD)
    time.sleep(1.0)
    typewriter(">> SESSION TERMINATED.", 0.05, DIM)

if __name__ == "__main__":
    try:
        run_session()
    except KeyboardInterrupt:
        sys.stdout.write(RESET + "\n>> [FORCED PURGE TERMINATED]\n")
