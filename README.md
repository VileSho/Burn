# Burn (Burn ICE)
**Interactive Terminal Incident Triage & Forensic Simulation**  
**Languages:** Python (92.7%) | Bash/Shell (7.3%)  
**License:** CC0-1.0  
**Portfolio:** [vilesho.github.io](https://vilesho.github.io)

---

## Overview
**Burn** is an interactive, text-based terminal simulation game set in the grimdark universe of *Warhammer 40,000*. Players step into the cybernetic augmentations of a Tech-Priest of the Adeptus Mechanicus (`Adept-Shoshana`, Sub-level 09 Data-Sanctity Vaults), tasked with isolating, analyzing, and purging a catastrophic scrap-code infection within a localized cogitator network (`Array 0x884-M41`). 

The Omnissiah watches. Failure to excise the corruption will result in immediate servitor conversion—or worse.

---

## Cybersecurity & Engineering Concepts Demonstrated
Beyond narrative systems design, this repository serves as a functional demonstration of command-line scripting and structured security documentation:

* **CLI Execution & Process Simulation (`Python` & `Bash`):** Multi-stage terminal execution scripts (`first_contact.py`, `reawaken.py`, `canticleIV.py`, `burn_template.py`) paired with shell orchestration (`reawaken.sh`) to simulate buffer lockouts, unauthorized process IDs (`PID 0xDEAD`), and privilege escalation prompts.
* **Forensic Incident Reporting (`logis_incident_report.md`):** Structured after real-world SOC/DFIR incident reports—complete with Executive Summary, Subject Telemetry, Chain of Evidence, Forensic Timeline Reconstruction, and Technical Appendix correlating memory corruption hex markers (`0xDEADBEEF`, `0xBAADF00D`).
* **Log & Intercept Analysis (`vox_intercept.txt`):** Timestamped communication and telemetry log (`VOX-099-SCHISM`) modeling hardware shunt bypasses, thermal anomalies (`104°C`), and outbound traffic anomalies.

---

## Repository Manifest

| File | Type | Description |
| :--- | :--- | :--- |
| `reawaken.sh` | Bash Script | Primary shell launcher and environment initialization script. |
| `first_contact.py` | Python | Stage 1 runtime execution loop modeling initial anomalous buffer contact (`0x09`). |
| `reawaken.py` | Python | Stage 2 runtime loop simulating terminal containment and override sequences. |
| `canticleIV.py` | Python | Diagnostic ritual and counter-scrapcode execution module. |
| `burn_template.py` | Python | Base modular template for terminal text rendering and state handling. |
| `logis_incident_report.md` | Markdown | Post-incident forensic dossier (`REF: 0x992-M41-ALTERED`). |
| `vox_intercept.txt` | Text Log | Recovered audio/telemetry transcript (`ID: VOX-099-SCHISM`) from Sublevel 09. |

---

## Quick Start

```bash
# Clone the repository
git clone [https://github.com/VileSho/Burn.git](https://github.com/VileSho/Burn.git)
cd Burn

# Make the shell launcher executable and run
chmod +x reawaken.sh
./reawaken.sh

# Or execute individual Python simulation modules directly
python3 first_contact.py
