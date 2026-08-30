import html

def build_svg(dark=True):
    width = 985
    height = 510
    
    if dark:
        bg_fill = "#0d1117"
        border_stroke = "#30363d"
        ascii_fill = "#79c0ff"
        user_color = "#7ee787"
        host_color = "#79c0ff"
        cmd_color = "#e6edf3"
        key_color = "#ffa657"
        dots_color = "#30363d"
        val_default = "#a5d6ff"
        val_green = "#3fb950"
        val_yellow = "#f2cc60"
        val_purple = "#d2a8ff"
        val_cyan = "#58a6ff"
        val_white = "#f0f6fc"
    else:
        bg_fill = "#f6f8fa"
        border_stroke = "#d0d7de"
        ascii_fill = "#0969da"
        user_color = "#116329"
        host_color = "#0969da"
        cmd_color = "#24292f"
        key_color = "#bc4c00"
        dots_color = "#d0d7de"
        val_default = "#0550ae"
        val_green = "#1a7f37"
        val_yellow = "#9a6700"
        val_purple = "#8250df"
        val_cyan = "#0969da"
        val_white = "#24292f"

    ascii_art = [
        "               ,g@@@@@g,              ",
        "            ,@@@@@@@@@@@@@,           ",
        "          ,@@@@*'   '*@@@@,          ",
        "         ,@@@*  _   _  *@@@,         ",
        "        ,@@@|  (o) (o)  |@@@,        ",
        "        @@@@|     ^     |@@@@        ",
        "        @@@@ \\  '---'  / @@@@        ",
        "        @@@@@ '._____.'  @@@@@        ",
        "       ,@@@@@@@g=======g@@@@@@@,       ",
        "      ,@@@@@*[SECURITY]*@@@@@,       ",
        "     ,@@@@@|  [0xAHMAD] |@@@@@,      ",
        "     @@@@@@| [FULLSTACK]|@@@@@@      ",
        "     @@@@@@|[ASP.LARAVEL|@@@@@@      ",
        "     '@@@@@| [REACT.VUE]|@@@@@'      ",
        "      '@@@@@\\ [PTUK.CSE]/@@@@@'       ",
        "       '@@@@@@g=======g@@@@@@'        ",
        "         '*@@@@@@@@@@@@@@@*'          ",
        "            '\"\"\"\"\"\"\"\"\"\"\"\"'            ",
        "    ================================  "
    ]

    TOTAL_CHARS = 55

    info_rows = [
        ("prompt", "ahmad@PTUK", ":~$ neofetch --engineer --security", "prompt"),
        ("spec", "OS", "Linux (Debian), Windows 11", "val_default"),
        ("spec", "Host", "Palestine Technical University - Kadoorie", "val_white"),
        ("spec", "Kernel", "Computer Systems Engineering (2022-2027)", "val_yellow"),
        ("spec", "Role", "Full-Stack Developer & Security Researcher", "val_green"),
        ("spec", "Focus", "ASP.NET Core • Laravel • React • Vue.js", "val_cyan"),
        ("spec", "IDE", "VS Code, Visual Studio 2022", "val_default"),
        ("spec", "Backend", "C# (ASP.NET Core), PHP (Laravel), Python, SQL", "val_default"),
        ("spec", "Frontend", "React, Vue.js, JavaScript, HTML5, SCSS", "val_default"),
        ("spec", "Database", "MySQL, Microsoft SQL Server", "val_default"),
        ("spec", "Security", "Burp Suite, OWASP Top 10, PortSwigger, HackerOne", "val_purple"),
        ("spec", "Certifications", "OCI 2025 Certified • Web Ethical Hacking • AI/TF", "val_yellow"),
        ("spec", "Labs.Solves", "50+ Practical Web Security Labs (PortSwigger)", "val_green"),
        ("spec", "Bugs.Reported", "15+ High/Med Web Vulns Reported (HackerOne)", "val_green"),
        ("spec", "Email", "ahmadherzalla31@gmail.com", "val_default"),
        ("spec", "LinkedIn", "linkedin.com/in/ahmadherzalla12", "val_default"),
        ("spec", "Portfolio", "ahmed-herzalla0.github.io/Portfolio-scss", "val_cyan"),
        ("spec", "GitHub", "github.com/Ahmed-Herzalla0", "val_green")
    ]

    svg_lines = [
        "<?xml version='1.0' encoding='UTF-8'?>",
        f'<svg xmlns="http://www.w3.org/2000/svg" font-family="ConsolasFallback,Consolas,\'Fira Code\',\'Courier New\',monospace" width="{width}px" height="{height}px" font-size="14px">',
        "<style>",
        "@font-face {",
        "  src: local('Consolas'), local('Consolas Bold'), local('Fira Code'), local('Courier New'), local('monospace');",
        "  font-family: 'ConsolasFallback';",
        "  font-display: swap;",
        "}",
        f".key {{ fill: {key_color}; font-weight: bold; }}",
        f".val_default {{ fill: {val_default}; }}",
        f".val_green {{ fill: {val_green}; font-weight: bold; }}",
        f".val_yellow {{ fill: {val_yellow}; }}",
        f".val_purple {{ fill: {val_purple}; }}",
        f".val_cyan {{ fill: {val_cyan}; }}",
        f".val_white {{ fill: {val_white}; }}",
        f".cc {{ fill: {dots_color}; }}",
        f".prompt_user {{ fill: {user_color}; font-weight: bold; }}",
        f".prompt_host {{ fill: {host_color}; font-weight: bold; }}",
        f".cmd {{ fill: {cmd_color}; }}",
        f".ascii {{ fill: {ascii_fill}; }}",
        "text, tspan { white-space: pre; }",
        "</style>",
        f'<rect width="{width}" height="{height}" fill="{bg_fill}" rx="14" stroke="{border_stroke}" stroke-width="1.5"/>',
        f'<text x="20" y="32" class="ascii">'
    ]

    start_y = 32
    line_height = 25
    for i, line in enumerate(ascii_art):
        y = start_y + i * line_height
        safe_line = html.escape(line)
        svg_lines.append(f'<tspan x="20" y="{y}">{safe_line}</tspan>')
    svg_lines.append("</text>")

    svg_lines.append('<text x="365" y="32">')
    for i, item in enumerate(info_rows):
        y = start_y + i * line_height
        row_type = item[0]
        if row_type == "prompt":
            u_part = html.escape(item[1].split("@")[0])
            h_part = html.escape(item[1].split("@")[1])
            cmd_part = html.escape(item[2])
            svg_lines.append(
                f'<tspan x="365" y="{y}"><tspan class="prompt_user">{u_part}</tspan><tspan class="cmd">@</tspan><tspan class="prompt_host">{h_part}</tspan><tspan class="cmd">{cmd_part}</tspan></tspan>'
            )
        else:
            k = item[1]
            v = item[2]
            color_cls = item[3]
            used_len = len(k) + len(v) + 4
            num_dots = max(3, TOTAL_CHARS - used_len)
            dots = " " + ("." * num_dots) + " "
            safe_k = html.escape(k)
            safe_v = html.escape(v)
            svg_lines.append(
                f'<tspan x="365" y="{y}"><tspan class="key">{safe_k}</tspan>:<tspan class="cc">{dots}</tspan><tspan class="{color_cls}">{safe_v}</tspan></tspan>'
            )
    svg_lines.append("</text>")
    svg_lines.append("</svg>")
    
    return "\n".join(svg_lines)

if __name__ == "__main__":
    dark_svg = build_svg(dark=True)
    with open("/home/ahmad/Desktop/Ahmed-Herzalla0/dark_mode.svg", "w") as f:
        f.write(dark_svg)
    print("Wrote dark_mode.svg")

    light_svg = build_svg(dark=False)
    with open("/home/ahmad/Desktop/Ahmed-Herzalla0/light_mode.svg", "w") as f:
        f.write(light_svg)
    print("Wrote light_mode.svg")
