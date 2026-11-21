"""Build the front page for Friday 20 November 2026.

Pure standard library. Draws the image with render.py and writes it to
$MAKEFUN_OUTPUT_DIR/entry.png (default: out/). Deterministic: two runs
produce byte-identical output.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from render import Canvas, save_png, wrap_text

W, H = 1024, 1024
PAPER = bytes((247, 243, 234))
INK = bytes((17, 17, 17))
NAVY = bytes((14, 42, 71))
NAVY2 = bytes((18, 38, 58))
RED = bytes((180, 35, 24))
GOLD = bytes((198, 148, 42))
TEAL = bytes((15, 118, 110))
GREY = bytes((90, 90, 86))
LIGHT = bytes((232, 226, 214))
SKY = bytes((168, 200, 224))
WHITE = bytes((255, 255, 255))
GREEN = bytes((46, 125, 50))
ORANGE = bytes((230, 126, 34))
YELLOW = bytes((241, 196, 15))

LEADS = [
    {
        "tag": "UKRAINE - WAR",
        "head": "Missiles rain on Kyiv; Poland hit too",
        "body": "Russia fired 3 missiles and 148 drones; 9 killed in Kyiv, 3 bridges hit. Two missiles fell in Poland.",
        "art": "kyiv",
    },
    {
        "tag": "MARKETS - AI ROUT",
        "head": "AI sell-off sinks Wall Street",
        "body": "S&P 500 fell 3.7%, Nasdaq 5.2% as the AI trade unravelled. Nvidia fell 14% to $125.53.",
        "art": "chart",
    },
    {
        "tag": "CLIMATE - COP31",
        "head": "COP31 runs past deadline",
        "body": "Climate talks in Antalya overran their deadline after a draft dropped all fossil-fuel language.",
        "art": "globe",
    },
]

SECONDARY = [
    ("MEXICO", "Cartel boss captured in Sinaloa",
     "Mexican forces seized FBI most-wanted fugitive Fausto Isidro Meza Flores in Guasave, Sinaloa."),
    ("INDIA", "Cyclone Akvan hits Odisha",
     "Akvan made landfall near Gopalpur with 70-80 km/h winds; 440,000 people were evacuated."),
    ("CHINA", "Trump, Xi and Putin meet in Shenzhen",
     "A trilateral summit at APEC ended with a 'peace declaration' but little concrete progress."),
    ("EUROPE", "UK and EU strike reset deal",
     "Britain and the EU agreed food-trade rules, linked carbon markets and youth mobility."),
    ("USA", "Senate passes energy bill 62-33",
     "The US Senate approved a sweeping energy-permitting overhaul; the House must still act."),
    ("GAZA", "Strike kills 3 in Gaza aid vehicle",
     "An Israeli strike killed three in a Gaza City vehicle carrying food and papers for aid workers."),
    ("USA", "California subpoenas Nvidia",
     "California subpoenaed Nvidia over China risks and investor disclosures as shares slid."),
    ("CYBER", "Card giants hit by vendor breach",
     "Visa, Mastercard and JPMorgan disclosed vendor breaches; data on 16,000 customers leaked."),
    ("USA", "Trump sacks cyber chief",
     "Trump replaced national cyber director Sean Cairncross amid a wave of tech outages."),
]

NUMBERS = [
    ("-3.7%", "S&P 500, 7th straight fall"),
    ("-14%", "Nvidia, to $125.53"),
    ("440,000", "evacuated in Odisha"),
    ("148", "drones fired at Ukraine"),
]

TIMELINE = [
    ("02:30", "Akvan landfall, Gopalpur"),
    ("03:00", "Russian barrage hits Kyiv"),
    ("13:00", "COP31 draft drops fossil fuels"),
    ("18:00", "Cartel boss seized, Sinaloa"),
    ("21:00", "Wall St closes: S&P -3.7%"),
]

BRIEFS = [
    "Estonia to shut all Russia road crossings from 1 Dec",
    "Denmark expels Russian diplomat over 'assassination plot'",
    "Saudi coalition strikes Hodeidah; Houthis fire at Riyadh",
    "Pentagon: Iran war has cost the US more than $48bn",
    "APEC ministers issue a joint statement in Shenzhen",
    "Modi to open first SCO Civilisational Dialogue Forum",
    "IEA: India drives energy growth amid Hormuz crisis",
    "India's US Treasury holdings rise to $228.2bn",
    "Tainted liquor kills at least 11 in Manipur, India",
    "Trump posthumously pardons baseball legend Pete Rose",
    "Texas botches execution of Houston jeweller's killer",
    "US Democrats move to end old deportation orders",
    "Audit: ICE paid millions for empty detention beds",
    "US sanctions scam enablers in Cambodia and Myanmar",
    "Indonesia daycare chief jailed 5 years over abuse",
    "China warns climbers on Mount Fuji after disappearance",
    "US Army delays detonating bomb chemicals after outcry",
    "GTA 6 breaks records as sales top $2.3bn",
    "Mosque set on fire in Israel after 'incitement' row",
    "Rohingya welcome UN court genocide verdict on Myanmar",
    "Brazil trial: dengue cases fall 69% with bacterium",
    "UN: free association needs no state authorisation",
    "UN warns antibiotics are failing common infections",
    "UN survey: AI is reshaping digital government",
    "India A thrash Nepal by 306 runs in Doha",
    "Bengaluru FC go top of ISL with 2-0 win",
    "India U17 reach AFC U17 Asian Cup after 0-0 draw",
    "Drone films Pochettino's first Man Utd training",
    "India bowl out New Zealand for 368; Nicholls 175",
    "South Africa beat Bangladesh by nine wickets",
    "Portugal draw Netherlands in Nations League",
    "Reports: Tom Brady buys a stake in Chelsea",
    "Verstappen on pole in Las Vegas; Antonelli fastest",
    "Pakistan seal series win over Sri Lanka",
]


def draw_kyiv(c, x, y, w, h):
    c.rect(x, y, w, h, SKY)
    c.rect(x, y + h - 18, w, 18, GREY)
    for bx, bw, bh in [(6, 26, 46), (40, 20, 62), (66, 30, 38),
                       (104, 22, 56), (134, 26, 42), (168, 20, 60),
                       (196, 24, 36), (228, 28, 52), (262, 22, 44)]:
        c.rect(x + bx, y + h - 18 - bh, bw, bh, NAVY2)
    c.circle(x + 250, y + 22, 12, YELLOW)
    c.circle(x + 250, y + 22, 18, ORANGE)
    for dx, dy in [(-22, -8), (22, -10), (-14, 14), (16, 12), (0, -20)]:
        c.line(x + 250, y + 22, x + 250 + dx, y + 22 + dy, ORANGE)
    c.line(x + 10, y + 12, x + 90, y + 26, WHITE)
    c.line(x + 14, y + 20, x + 96, y + 32, WHITE)


def draw_chart(c, x, y, w, h):
    c.rect(x, y, w, h, WHITE)
    c.hline(x + 8, y + h - 12, w - 16, GREY)
    c.vline(x + 8, y + 8, h - 20, GREY)
    pts = [(16, 16), (52, 22), (88, 18), (124, 34), (160, 30),
           (196, 48), (232, 58), (268, 66)]
    for (ax, ay), (bx, by) in zip(pts, pts[1:]):
        c.line(x + ax, y + ay, x + bx, y + by, RED)
        c.line(x + ax, y + ay + 1, x + bx, y + by + 1, RED)
    for px, py in pts:
        c.circle(x + px, y + py, 3, RED)
    c.text(x + w - 52, y + h - 11, "-14%", 1, RED, bold=True)


def draw_globe(c, x, y, w, h):
    c.rect(x, y, w, h, SKY)
    cx, cy, r = x + w // 2 - 30, y + h // 2, 34
    c.circle(cx, cy, r, TEAL)
    c.circle(cx - 10, cy - 8, 12, GREEN)
    c.circle(cx + 12, cy + 12, 10, GREEN)
    c.ring(cx, cy, r, NAVY2, 2)
    c.hline(cx - r, cy, 2 * r, NAVY2)
    c.text(x + w - 78, y + 8, "COP31", 2, NAVY, bold=True)
    c.text(x + w - 78, y + 26, "ANTALYA", 1, NAVY, bold=True)
    c.circle(x + w - 30, y + h - 22, 10, YELLOW)
    for dx, dy in [(-14, -6), (14, -8), (0, -14)]:
        c.line(x + w - 30, y + h - 22, x + w - 30 + dx, y + h - 22 + dy, ORANGE)


ART = {"kyiv": draw_kyiv, "chart": draw_chart, "globe": draw_globe}


def build():
    c = Canvas(W, H, PAPER)
    # masthead
    c.rect(0, 0, W, 100, NAVY)
    c.text_center(10, "THE WORLD IN ONE DAY", 4, WHITE, bold=True)
    c.text_center(48, "FRIDAY 20 NOVEMBER 2026", 3, GOLD, bold=True)
    c.text_center(78, "46 STORIES  -  7 REGIONS  -  ONE PAGE", 2, WHITE)
    c.text_center(106, "Every story on this page happened, or was first reported, on Friday 20 November 2026.",
                  1, INK)
    c.hline(24, 122, W - 48, INK, 2)

    # three leads
    col_w, gap = 312, 16
    for i, lead in enumerate(LEADS):
        x = 24 + i * (col_w + gap)
        y = 132
        c.text(x, y, lead["tag"], 1, RED, bold=True)
        ART[lead["art"]](c, x, y + 14, col_w, 76)
        y = y + 14 + 76 + 8
        y = c.para(x, y, lead["head"], 2, INK, 25, lh=16, bold=True)
        y += 2
        c.para(x, y, lead["body"], 2, INK, 25, lh=15)
    c.hline(24, 342, W - 48, INK, 2)

    # nine secondary stories
    for i, (tag, head, body) in enumerate(SECONDARY):
        col, row = i % 3, i // 3
        x = 24 + col * (col_w + gap)
        y = 350 + row * 74
        c.rect(x, y, 26, 26, NAVY)
        c.text(x + 8, y + 9, str(i + 4), 1, WHITE, bold=True)
        c.text(x + 34, y, tag, 1, RED, bold=True)
        c.para(x + 34, y + 11, head, 2, INK, 23, lh=15, bold=True)
        c.para(x + 34, y + 42, body, 1, INK, 46, lh=9)
    c.hline(24, 570, W - 48, INK, 2)

    # by the numbers
    c.rect(0, 576, W, 64, NAVY2)
    c.text(24, 584, "BY THE NUMBERS", 2, GOLD, bold=True)
    for i, (num, label) in enumerate(NUMBERS):
        x = 280 + i * 180
        c.text(x, 582, num, 3, WHITE, bold=True)
        c.text(x, 610, label, 1, LIGHT)
    c.hline(24, 648, W - 48, INK, 2)

    # UTC timeline
    c.text(24, 656, "THE DAY IN UTC  (times approximate)", 2, INK, bold=True)
    c.hline(60, 692, W - 120, GREY, 2)
    for i, (t, label) in enumerate(TIMELINE):
        x = 100 + i * 200
        c.circle(x, 692, 6, RED)
        c.text_center(672, t, 1, RED, bold=True, cx=x)
        for j, ln in enumerate(wrap_text(label, 22)):
            c.text_center(706 + j * 10, ln, 1, INK, cx=x)

    # briefs
    c.hline(24, 728, W - 48, INK, 2)
    c.text(24, 736, "ALSO ON 20 NOVEMBER  -  34 MORE STORIES", 2, INK, bold=True)
    for i, b in enumerate(BRIEFS):
        col = i // 17
        row = i % 17
        x = 24 + col * 500
        y = 758 + row * 11
        c.text(x, y, "%d. %s" % (13 + i, b), 1, INK)

    # footer
    c.hline(24, 950, W - 48, INK, 2)
    c.text(24, 958, "Sources: Reuters, AP, AFP, BBC, Al Jazeera, CNN, FT, UN News, IMD, Investopedia, Dawn, The Hindu.",
           1, GREY)
    c.text(24, 972, "All stories happened or were first reported on 20 November 2026. Disputed claims are attributed.",
           1, GREY)
    c.text(24, 986, "THE WORLD IN ONE DAY  -  Friday 20 November 2026  -  46 stories, 7 regions, one page",
           1, GREY)
    return c


def main():
    outdir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(outdir, exist_ok=True)
    canvas = build()
    path = os.path.join(outdir, "entry.png")
    size = save_png(canvas, path)
    print("wrote %s (%d bytes)" % (path, size))


if __name__ == "__main__":
    main()
