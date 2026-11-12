"""make.fun news-summary-01: world news of Wednesday 11 November 2026.

Writes one fixed English summary to /output/entry.txt (UTF-8, no network,
deterministic). MAKEFUN_OUTPUT_DIR overrides the output directory for local runs.
"""

import os

SUMMARY = """World news, Wed 11 Nov 2026

UKRAINE: Russia-Ukraine talks end in Abu Dhabi, no ceasefire; US envoy Jared Kushner says both sides agreed the "biggest" prisoner swap, Zelensky cites 1,000 each, maybe 1,200. Moscow demands all of Donbas. Kushner, Witkoff see Putin 12 Nov (France 24, Euronews).
IRAN WAR: Speaker Ghalibaf, Iran's chief negotiator, says Tehran awaits a US reply and Hormuz will "never return" to pre-war status; US blockade stays. Security chief Rezaei threatens US bases in Europe (France 24). Brent ~$92 (Euronews).
US: Democrat Scott Colom wins Mississippi's Senate seat over Cindy Hyde-Smith, state's first Black senator since Reconstruction (CNN, France 24, Al Jazeera). House blocks Hegseth impeachment over Iran war (France 24, Al Jazeera). Judge lets Trump's $10bn BBC suit proceed (Al Jazeera, Euronews).
EBOLA: Congo outbreak tops 11,042 cases, 5,387 deaths, a record (Al Jazeera, Euronews). Kenya discharges last patient, starting 42-day countdown (Al Jazeera, France 24).
SPAIN: First general strike in 14 years over housing and pay; Madrid turnout 120,000 (government) to 500,000+ (tenants' union); 70+ arrests (Euronews, France 24).
PAKISTAN: Taliban ambush in Kohat kills 10 police; 18 attackers killed (AP, Al Jazeera).
CLIMATE: COP31 leaders' summit opens in Antalya, Turkey; Macron, Merz, Meloni absent (UNFCCC, Euronews).
GAZA: Israeli strikes kill at least 5; 70,000 tents flooded; 1,622 killed since Oct 2025 truce (Al Jazeera).
EUROPE: Hoax bomb emails empty ~300 Italian schools, hit UK, Ireland (France 24). Storm Charles shuts all ~8,000 Portuguese schools (Euronews, AP). Russia bans two French lawmakers, two journalists (France 24, Euronews).
PERU: Pope Leo XIV lands in Lima, met by President Fujimori (France 24).
BRAZIL: Electoral court fines Meta R$7.5m for ignoring election court orders (France 24, AFP).
TECH: Anthropic files for US IPO at ~$1.4tn valuation (Euronews, France 24). OpenAI Q3 revenue $10bn, operating loss $10.9bn (WSJ via Euronews)."""


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(SUMMARY)


if __name__ == "__main__":
    main()
