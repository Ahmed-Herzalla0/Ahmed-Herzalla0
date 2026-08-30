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
        ascii_fill = "#79c0ff"
        border_stroke = "#30363d"
    else:
        bg_fill = "#f6f8fa"
        text_fill = "#24292f"
        key_fill = "#bc4c00"
        val_fill = "#0550ae"
        add_fill = "#1a7f37"
        del_fill = "#cf222e"
        cc_fill = "#8c959f"
        ascii_fill = "#0969da"
        border_stroke = "#d0d7de"

    ascii_lines = user_ascii.strip().split('\n')

    # Specs on right: (key, dots, value, val_class)
    # Start y around 60, line-height 28px for specs
    specs_list = [
        [("ahmad@PTUK:~$ neofetch --engineer --security", "addColor")],
        [("OS", "key"), (": ........................ ", "cc"), ("Linux (Debian), Windows 11", "val")],
        [("Host", "key"), (": ...................... ", "cc"), ("Palestine Technical University - Kadoorie", "val")],
        [("Kernel", "key"), (": .... ", "cc"), ("Computer Systems Engineering (2022-2027)", "addColor")],
        [("Role", "key"), (": ...... ", "cc"), ("Full-Stack Developer & Security Researcher", "val")],
        [("Focus", "key"), (": ..... ", "cc"), ("ASP.NET Core • Laravel • React • Vue.js", "val")],
        [("IDE", "key"), (": ........................ ", "cc"), ("VS Code, Visual Studio 2022", "val")],
        [("Backend", "key"), (": ... ", "cc"), ("C# (ASP.NET), PHP (Laravel), Python, SQL", "val")],
        [("Frontend", "key"), (": .. ", "cc"), ("React, Vue.js, JavaScript, HTML5, SCSS", "val")],
        [("Database", "key"), (": .. ", "cc"), ("MySQL, Microsoft SQL Server", "val")],
        [("Security.Tools", "key"), (": ..... ", "cc"), ("Burp Suite Pro, OWASP Top 10, DevTools", "val")],
        [("Security.Practice", "key"), (": .. ", "cc"), ("Web Pentesting, Vulnerability Assessment", "val")],
        [("Certifications", "key"), (": ........... ", "cc"), ("OCI 2025 Certified • AI/TF • Web Ethical Hacking", "addColor")],
        [("PortSwigger Labs", "key"), (": ........ ", "cc"), ("50+ Solved", "addColor"), (" (SQLi, XSS, CSRF, IDOR)", "cc")],
        [("HackerOne Vulns", "key"), (": ......... ", "cc"), ("15+ Reported", "addColor"), (" (High / Medium)", "cc")],
        [("Email", "key"), (": ...................... ", "cc"), ("ahmadherzalla31@gmail.com", "val")],
        [("LinkedIn", "key"), (": .................. ", "cc"), ("ahmadherzalla12", "val")],
        [("Portfolio", "key"), (": ................. ", "cc"), ("ahmed-herzalla0.github.io/Portfolio-scss", "val")],
        [("GitHub", "key"), (": .................... ", "cc"), ("Ahmed-Herzalla0", "addColor")],
        [("Status", "key"), (": ................... ", "cc"), ("Open for Engineering & Security Roles", "addColor")]
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
    out.append(f"  fill: {ascii_fill};")
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
    
    # Left ASCII art block
    out.append('<text x="18" y="24" class="ascii">')
    for i, line in enumerate(ascii_lines):
        y = 24 + i * 13.3
        safe_line = html.escape(line)
        out.append(f'<tspan x="18" y="{y:.1f}">{safe_line}</tspan>')
    out.append('</text>')

    # Right Neofetch Specs block
    out.append('<text x="560" y="45" class="specs">')
    spec_start_y = 45
    spec_line_height = 29.5
    for i, row in enumerate(specs_list):
        y = spec_start_y + i * spec_line_height
        if len(row) == 1:
            safe_text = html.escape(row[0][0])
            cls_name = row[0][1]
            out.append(f'<tspan x="560" y="{y:.1f}" class="{cls_name}">{safe_text}</tspan>')
        else:
            first_txt = html.escape(row[0][0])
            first_cls = row[0][1]
            spec_str = f'<tspan x="560" y="{y:.1f}"><tspan class="{first_cls}">{first_txt}</tspan>'
            for part_text, part_cls in row[1:]:
                safe_part = html.escape(part_text)
                spec_str += f'<tspan class="{part_cls}">{safe_part}</tspan>'
            spec_str += '</tspan>'
            out.append(spec_str)
    out.append('</text>')
    out.append('</svg>')
    
    return '\n'.join(out)

if __name__ == "__main__":
    dark_svg = build_svg(dark=True)
    with open("/home/ahmad/Desktop/Ahmed-Herzalla0/dark_mode.svg", "w") as f:
        f.write(dark_svg)
    print("Wrote dark_mode.svg")

    light_svg = build_svg(dark=False)
    with open("/home/ahmad/Desktop/Ahmed-Herzalla0/light_mode.svg", "w") as f:
        f.write(light_svg)
    print("Wrote light_mode.svg")
