import html

user_ascii = '''=========+++++*****+++=====+++++==----=+++++=----------------:::-------::-------
=-====++++++*******+++====+++++++=-----=---::-----------------:::::-------------
=====+++++++********++====+++*+--==::.::::...........:==++++=----:------------::
====++++++++********+++===+***+++-.. ..................::+++===--------------:::
=====+++++++*********+++=-===-:..   .......................:======---:::::::::::
===========+++****++++--.=*-.            ............    .. .:===---::::::::::--
==------====+++++++++:-..-                      ......         :-----:::::::::--
---------=====++++===-...    .:-::::::::::::...::...            :-------::::::::
-------==========+++-..    -==++++*++++++****#****++===--:.     .:-------:::::::
==============++====-:.  .-++++++******###############****=-.   ..:-----::::::::
++++++++==========+=-....:-+++++*********##############****+:... ..::::::::::--:
++****++++++======-:.....:-++++***********#***#######*******-.  ...::::::::::---
*******+++++====---:....:-=++++*****##################*****+=:....::::::::::::-:
+*****+++++=====---:::.:-=++++******##################******=-:...::::::::::::::
++++++++++=======--:::=+++++++==+++******###**#########*****=-::..::::::::::::::
====+++++++++====--::=*+++=:.:::.... ..:=+**++=-------==*****+=:..::::::::::::::
======+++++++==+*+-:=**+.  -========--::-==++-:..::::--:::=***+:..::::::::::::::
======++++++====:==:-*++=:--:::-...-::-::+**:-=::::--=-++-.  -=:.:::::::::::::::
======+++++====+=+=-+*+++==+====------=-:**+.+=---:.:=:--=:-===.=**=::::::::::::
===============+===:+**+**-****+++++++=.+###-=*++=--===++*:++*+:+=--::::::::::.:
+==============++=-:+******=***###**+--**###*-+**##******=+***+-*+=-::::::::::::
++================-:=**+++++++====---++*####**=-+#####*+=*****+:+*+:::::::::::::
+++===========---+=:-+++++++++***++===:-++++=+*+=++****#******=-**-:::::::::::::
++===========----++:-===++++++++==+==-.::-:::-+#*++********+++:=*=::::::::::::::
++==========-----==:----===++=-::.:::::---::::=+**+++******+=-.=-:::::::::::::::
=========----------:--:-:-===-....::::::--------::--=+++++++=::+::::::::::::::::
========-----------:----:::-=-::======++++*+*+-....:=+=+=-==-:.:::::::::::::::::
++++====-------:::::-----::--::-++=-::..::----==+-:-+==-----::::::::::::::::::::
+++++====-----::::::-:-::..::..:-====--===-=++++=-::===----:::::::::::::::::::::
*+++++====-----:::::--::..... ...:::--===+++++=-:.::--::::::::::::::::..:::::::-
*+++++++==-----:::::-=.....    ......::::-::::::.......:::..:::::::::...:::::---
*+++++====-----:::::++:..             ..........    ......::::::::::::...:::--==
**++++====------::--%==:.                           .  ..-=::---:::::....:::--==
*++++++===-------=:+%#==-:.          ....         .....:-##::----:::::...:::--==
***++++===----:-=-.#%###=--::........::::.............=#%%%-:-----::::...:::---=
*****+++=====--=-..####%##+-----::......:...........+%%%%%%-::::--::::....:::---
*****+=:..:---=-:..*##%%%%%##+-----:::::::::::::-+#%%%%%%%#:::::::::--::..::::--
*+-:.....::::---:..=##%%%%%%%###=-------------+#%%%%%%%%%%=::::::::::..:::::::--
::.....::..:::::...-*##%%%%%%%%%###========+%%%%%%%%%%%%%#::::::::::::....::::--
::::..:::.::::....:-*###%%%%%%%%%%%*+*#***%%%%%%%%%%%%%%%=::-:::::::::::...:::::
:::...::::::......::*##%%%%%%%%%=::.....::::=%%%%%%%%%%%#=:--:::::::::::::::::::
::::.....:.:.....:::+##%%%%%%%+.....::::::::..-%%%%%%%%%*-:--::::::::::..:::::::
::::::...::::....:::**%%%%%%*===-....:::-:...---+%%%%%%%+::---::::::::::::::::::
:::::::::.:::....:::*##%%%#*####*+-...:-::.+###**+*%%%%*+::-----::::::::::::::::
:.::::::::::......::+%####%%%%%####+...:.:*%%%%%%%###%##=:---:::::::::::::::::::'''

def build_svg(dark=True):
    width = 1120
    height = 640
    
    if dark:
        bg_fill = "#161b22"
        text_fill = "#c9d1d9"
        key_fill = "#ffa657"
        val_fill = "#a5d6ff"
        add_fill = "#3fb950"
        del_fill = "#f85149"
        cc_fill = "#616e7f"
        ascii_fill = "#FFFFFF"  # PURE WHITE
        border_stroke = "#30363d"
    else:
        bg_fill = "#ffffff"
        text_fill = "#24292f"
        key_fill = "#bc4c00"
        val_fill = "#0550ae"
        add_fill = "#1a7f37"
        del_fill = "#cf222e"
        cc_fill = "#8c959f"
        ascii_fill = "#1f2328"
        border_stroke = "#d0d7de"

    ascii_lines = user_ascii.strip().split('\n')

    specs_list = [
        [("ahmad@PTUK:~$ neofetch --engineer --security", "addColor", add_fill)],
        [("OS", "key", key_fill), (": ........................ ", "cc", cc_fill), ("Linux (Debian), Windows 11", "val", val_fill)],
        [("Host", "key", key_fill), (": ...................... ", "cc", cc_fill), ("Palestine Technical University - Kadoorie", "val", val_fill)],
        [("Kernel", "key", key_fill), (": .... ", "cc", cc_fill), ("Computer Systems Engineering (2022-2027)", "addColor", add_fill)],
        [("Role", "key", key_fill), (": ...... ", "cc", cc_fill), ("Full-Stack Developer & Security Researcher", "val", val_fill)],
        [("Focus", "key", key_fill), (": ..... ", "cc", cc_fill), ("ASP.NET Core • Laravel • React • Vue.js", "val", val_fill)],
        [("IDE", "key", key_fill), (": ........................ ", "cc", cc_fill), ("VS Code, Visual Studio 2022", "val", val_fill)],
        [("Backend", "key", key_fill), (": ... ", "cc", cc_fill), ("C# (ASP.NET), PHP (Laravel), Python, SQL", "val", val_fill)],
        [("Frontend", "key", key_fill), (": .. ", "cc", cc_fill), ("React, Vue.js, JavaScript, HTML5, SCSS", "val", val_fill)],
        [("Database", "key", key_fill), (": .. ", "cc", cc_fill), ("MySQL, Microsoft SQL Server", "val", val_fill)],
        [("Security.Tools", "key", key_fill), (": ..... ", "cc", cc_fill), ("Burp Suite Pro, OWASP Top 10, DevTools", "val", val_fill)],
        [("Security.Practice", "key", key_fill), (": .. ", "cc", cc_fill), ("Web Pentesting, Vulnerability Assessment", "val", val_fill)],
        [("Certifications", "key", key_fill), (": ........... ", "cc", cc_fill), ("OCI 2025 Certified • AI/TF • Web Ethical Hacking", "addColor", add_fill)],
        [("PortSwigger Labs", "key", key_fill), (": ........ ", "cc", cc_fill), ("50+ Solved", "addColor", add_fill), (" (SQLi, XSS, CSRF, IDOR)", "cc", cc_fill)],
        [("HackerOne Vulns", "key", key_fill), (": ......... ", "cc", cc_fill), ("15+ Reported", "addColor", add_fill), (" (High / Medium)", "cc", cc_fill)],
        [("Email", "key", key_fill), (": ...................... ", "cc", cc_fill), ("ahmadherzalla31@gmail.com", "val", val_fill)],
        [("LinkedIn", "key", key_fill), (": .................. ", "cc", cc_fill), ("ahmadherzalla12", "val", val_fill)],
        [("Portfolio", "key", key_fill), (": ................. ", "cc", cc_fill), ("ahmed-herzalla0.github.io/Portfolio-scss", "val", val_fill)],
        [("GitHub", "key", key_fill), (": .................... ", "cc", cc_fill), ("Ahmed-Herzalla0", "addColor", add_fill)],
        [("Status", "key", key_fill), (": ................... ", "cc", cc_fill), ("Open for Engineering & Security Roles", "addColor", add_fill)]
    ]

    out = []
    out.append("<?xml version='1.0' encoding='UTF-8'?>")
    out.append(f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}px" height="{height}px" viewBox="0 0 {width} {height}">')
    out.append("<style>")
    out.append("@font-face {")
    out.append("  src: local('Consolas'), local('Consolas Bold'), local('Fira Code'), local('Courier New'), local('monospace');")
    out.append("  font-family: 'ConsolasFallback';")
    out.append("  font-display: swap;")
    out.append("}")
    out.append(".ascii {")
    out.append("  font-family: 'ConsolasFallback', Consolas, 'Fira Code', 'Courier New', monospace;")
    out.append(f"  fill: {ascii_fill} !important;")
    out.append("  font-size: 10.5px;")
    out.append("  letter-spacing: 0px;")
    out.append("}")
    out.append(".specs {")
    out.append("  font-family: 'ConsolasFallback', Consolas, 'Fira Code', 'Courier New', monospace;")
    out.append("  font-size: 14px;")
    out.append("}")
    out.append(f".key {{ fill: {key_fill}; font-weight: bold; }}")
    out.append(f".val {{ fill: {val_fill}; }}")
    out.append(f".addColor {{ fill: {add_fill}; font-weight: bold; }}")
    out.append(f".delColor {{ fill: {del_fill}; }}")
    out.append(f".cc {{ fill: {cc_fill}; }}")
    out.append("text, tspan { white-space: pre; }")
    out.append("</style>")
    out.append(f'<rect width="{width}" height="{height}" fill="{bg_fill}" rx="14" stroke="{border_stroke}" stroke-width="1.5"/>')
    
    # Left ASCII art block with explicit fill on every tspan
    out.append(f'<text x="18" y="24" fill="{ascii_fill}" class="ascii">')
    for i, line in enumerate(ascii_lines):
        y = 24 + i * 13.3
        safe_line = html.escape(line)
        out.append(f'<tspan x="18" y="{y:.1f}" fill="{ascii_fill}">{safe_line}</tspan>')
    out.append('</text>')

    # Right Neofetch Specs block with explicit fill attributes
    out.append(f'<text x="560" y="45" fill="{text_fill}" class="specs">')
    spec_start_y = 45
    spec_line_height = 29.5
    for i, row in enumerate(specs_list):
        y = spec_start_y + i * spec_line_height
        if len(row) == 1:
            safe_text = html.escape(row[0][0])
            cls_name = row[0][1]
            color_hex = row[0][2]
            out.append(f'<tspan x="560" y="{y:.1f}" fill="{color_hex}" class="{cls_name}">{safe_text}</tspan>')
        else:
            first_txt = html.escape(row[0][0])
            first_cls = row[0][1]
            first_hex = row[0][2]
            spec_str = f'<tspan x="560" y="{y:.1f}"><tspan fill="{first_hex}" class="{first_cls}">{first_txt}</tspan>'
            for part_text, part_cls, part_hex in row[1:]:
                safe_part = html.escape(part_text)
                spec_str += f'<tspan fill="{part_hex}" class="{part_cls}">{safe_part}</tspan>'
            spec_str += '</tspan>'
            out.append(spec_str)
    out.append('</text>')
    out.append('</svg>')
    
    return '\n'.join(out)

if __name__ == "__main__":
    dark_svg = build_svg(dark=True)
    with open("/home/ahmad/Desktop/Ahmed-Herzalla0/dark_mode_v2.svg", "w") as f:
        f.write(dark_svg)
    with open("/home/ahmad/Desktop/Ahmed-Herzalla0/dark_mode.svg", "w") as f:
        f.write(dark_svg)
    print("Wrote dark_mode_v2.svg")

    light_svg = build_svg(dark=False)
    with open("/home/ahmad/Desktop/Ahmed-Herzalla0/light_mode_v2.svg", "w") as f:
        f.write(light_svg)
    with open("/home/ahmad/Desktop/Ahmed-Herzalla0/light_mode.svg", "w") as f:
        f.write(light_svg)
    print("Wrote light_mode_v2.svg")
