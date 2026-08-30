import html
from PIL import Image, ImageOps, ImageEnhance
import numpy as np

def generate_portrait_ascii():
    img = Image.open('/home/ahmad/Desktop/Ahmed-Herzalla0/avatar.jpg').convert('RGB')
    w, h = img.size

    # Crop head & shoulders
    crop = img.crop((int(w * 0.12), int(h * 0.08), int(w * 0.88), int(h * 0.96)))

    COLS = 38
    ROWS = 25

    enh = ImageEnhance.Contrast(crop).enhance(1.8)
    sharp = ImageEnhance.Sharpness(enh).enhance(2.2)
    gray = ImageOps.grayscale(sharp)
    gray_res = gray.resize((COLS, ROWS), Image.Resampling.LANCZOS)
    arr = np.array(gray_res, dtype=float)

    mask = np.zeros((ROWS, COLS), dtype=bool)
    for r in range(ROWS):
        if r < 3:
            c_min, c_max = 12, 26
        elif r < 6:
            c_min, c_max = 10, 28
        elif r < 12:
            c_min, c_max = 9, 29
        elif r < 15: # beard & chin
            c_min, c_max = 10, 28
        elif r < 18: # neck & collar
            c_min, c_max = 7, 31
        else: # suit shoulders
            c_min = max(0, 7 - (r - 17) * 2)
            c_max = min(COLS, 31 + (r - 17) * 2)
        mask[r, c_min:c_max] = True

    chars = ['@', '%', '#', 'M', 'N', 'W', 'g', 'm', 'p', 'k', 'h', 'j', 'l', '|', '*', '+', '!', '\'', '.', ' ']

    lines = []
    for r in range(ROWS):
        row_chars = []
        for c in range(COLS):
            if not mask[r, c]:
                row_chars.append(' ')
            else:
                val = arr[r, c]
                idx = int((val / 256.0) * len(chars))
                idx = min(len(chars) - 1, max(0, idx))
                row_chars.append(chars[idx])
        lines.append(''.join(row_chars))
    
    return lines

def build_svg(dark=True):
    width = "985px"
    height = "530px"
    font_size = "16px"
    
    if dark:
        bg_fill = "#161b22"
        text_fill = "#c9d1d9"
        key_fill = "#ffa657"
        val_fill = "#a5d6ff"
        add_fill = "#3fb950"
        del_fill = "#f85149"
        cc_fill = "#616e7f"
        ascii_fill = "#FFFFFF"  # Pure White
    else:
        bg_fill = "#ffffff"
        text_fill = "#24292f"
        key_fill = "#bc4c00"
        val_fill = "#0550ae"
        add_fill = "#1a7f37"
        del_fill = "#cf222e"
        cc_fill = "#8c959f"
        ascii_fill = "#1f2328"

    ascii_rows = generate_portrait_ascii()

    specs = {
        50: [(". ", "cc"), ("OS", "key"), (": ........................ ", "cc"), ("Linux (Debian), Windows 11", "value")],
        70: [(". ", "cc"), ("Host", "key"), (": ...................... ", "cc"), ("Palestine Technical University - Kadoorie", "value")],
        90: [(". ", "cc"), ("Kernel", "key"), (": .... ", "cc"), ("Computer Systems Engineering (2022-2027)", "addColor")],
        110: [(". ", "cc"), ("Role", "key"), (": ...... ", "cc"), ("Full-Stack Developer & Security Researcher", "value")],
        130: [(". ", "cc"), ("IDE", "key"), (": ........................ ", "cc"), ("VS Code, Visual Studio 2022", "value")],
        170: [(". ", "cc"), ("Languages", "key"), (".", "key"), ("Backend", "key"), (": ... ", "cc"), ("C# (ASP.NET), PHP (Laravel), Python, SQL", "value")],
        190: [(". ", "cc"), ("Languages", "key"), (".", "key"), ("Frontend", "key"), (": .. ", "cc"), ("React, Vue.js, JavaScript, HTML5, SCSS", "value")],
        210: [(". ", "cc"), ("Languages", "key"), (".", "key"), ("Database", "key"), (": .. ", "cc"), ("MySQL, Microsoft SQL Server", "value")],
        250: [(". ", "cc"), ("Security", "key"), (".", "key"), ("Tools", "key"), (": ..... ", "cc"), ("Burp Suite Pro, OWASP Top 10, DevTools", "value")],
        270: [(". ", "cc"), ("Security", "key"), (".", "key"), ("Practice", "key"), (": .. ", "cc"), ("Web Pentesting, Vulnerability Assessment", "value")],
        310: [(". ", "cc"), ("Certifications", "key"), (": ........... ", "cc"), ("OCI 2025 Networking, AI/TF, Web Ethical Hacking", "addColor")],
        330: [(". ", "cc"), ("Email", "key"), (": ...................... ", "cc"), ("ahmadherzalla31@gmail.com", "value")],
        350: [(". ", "cc"), ("LinkedIn", "key"), (": .................. ", "cc"), ("ahmadherzalla12", "value")],
        370: [(". ", "cc"), ("Portfolio", "key"), (": ................. ", "cc"), ("ahmed-herzalla0.github.io/Portfolio-scss", "value")],
        390: [(". ", "cc"), ("GitHub", "key"), (": .................... ", "cc"), ("Ahmed-Herzalla0", "value")],
        470: [(". ", "cc"), ("PortSwigger Labs", "key"), (": ........ ", "cc"), ("50+ Solved", "addColor"), (" (SQLi, XSS, CSRF, IDOR)", "cc")],
        490: [(". ", "cc"), ("HackerOne Vulns", "key"), (": ......... ", "cc"), ("15+ Reported", "addColor"), (" (High / Medium)", "cc")],
        510: [(". ", "cc"), ("Status", "key"), (": ................... ", "cc"), ("Open for Engineering & Security Roles", "addColor")]
    }

    out = []
    out.append("<?xml version='1.0' encoding='UTF-8'?>")
    out.append(f"<svg xmlns=\"http://www.w3.org/2000/svg\" font-family=\"ConsolasFallback,Consolas,monospace\" width=\"{width}\" height=\"{height}\" font-size=\"{font_size}\">")
    out.append("<style>")
    out.append("@font-face {")
    out.append("src: local('Consolas'), local('Consolas Bold');")
    out.append("font-family: 'ConsolasFallback';")
    out.append("font-display: swap;")
    out.append("-webkit-size-adjust: 109%;")
    out.append("size-adjust: 109%;")
    out.append("}")
    out.append(f".key {{fill: {key_fill}; font-weight: bold;}}")
    out.append(f".value {{fill: {val_fill};}}")
    out.append(f".addColor {{fill: {add_fill}; font-weight: bold;}}")
    out.append(f".delColor {{fill: {del_fill};}}")
    out.append(f".cc {{fill: {cc_fill};}}")
    out.append(f".ascii {{fill: {ascii_fill};}}")
    out.append("text, tspan {white-space: pre;}")
    out.append("</style>")
    out.append(f"<rect width=\"{width}\" height=\"{height}\" fill=\"{bg_fill}\" rx=\"15\"/>")
    out.append(f"<text x=\"15\" y=\"30\" fill=\"{text_fill}\">")

    for i, line in enumerate(ascii_rows):
        y = 30 + i * 20
        safe_ascii = html.escape(line)
        out.append(f'<tspan x="15" y="{y}" fill="{ascii_fill}" class="ascii">{safe_ascii}</tspan>')
        if y in specs:
            spec_parts = specs[y]
            first_txt = html.escape(spec_parts[0][0])
            first_cls = spec_parts[0][1]
            spec_str = f'<tspan x="390" y="{y}" class="{first_cls}">{first_txt}</tspan>'
            for part_text, part_cls in spec_parts[1:]:
                safe_part = html.escape(part_text)
                spec_str += f'<tspan class="{part_cls}">{safe_part}</tspan>'
            out.append(spec_str)

    out.append("</text>")
    out.append("</svg>")
    return "\n".join(out)

if __name__ == "__main__":
    for fname in ["dark_mode.svg", "dark_mode_v2.svg", "dark_mode_v3.svg"]:
        with open(f"/home/ahmad/Desktop/Ahmed-Herzalla0/{fname}", "w") as f:
            f.write(build_svg(dark=True))
    for fname in ["light_mode.svg", "light_mode_v2.svg", "light_mode_v3.svg"]:
        with open(f"/home/ahmad/Desktop/Ahmed-Herzalla0/{fname}", "w") as f:
            f.write(build_svg(dark=False))
    print("All SVGs generated with Andrew6rant portrait silhouette!")
