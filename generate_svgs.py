import html

raw_user_ascii = '''                                                                :--=---=-:--:...                                                            
                                                         :=:..+*:--*-::... .   :..:.:.                                                      
                                                     +#.-+#*#. .. .......   ... .  . :.::                                                   
                                                 :**-%%==-==..    ....... .. . ..:..:...: .:.                                               
                                               + .+##:.-    .:...:.::.::... . ... :::::. ......                                             
                                            -## *= *+:......   .. ...  ...::...:.   . .. ...   ..                                           
                                           -:.  -#-..               .  ...:.    ...  .     ..  : ::                                         
                                          =.+: .*                              .::...            .  .                                       
                                         -=:.          .::.   . .......        ..        .        .  .                                      
                                        +=-=..     ...-=++++====-===-========++===-:.. ...          ...                                     
                                        =-:.      :=++++++++*+++********#######*****+++++++=-:.    .:.:.                                    
                                        -+::  .  .=++++++++******#**###################*****++-. ..  ...                                    
                                       =*:*.=.  .:+++++++++***********##################*#*****-...:  ...                                   
                                       =-:-:....:==+++++*******************############********=:.. . ..                                    
                                      --:.:....:--=++++++*********#*#**#*##**######************=:.  ....                                    
                                      ::::.....-:=++++++********#######################********+=:.  ...                                    
                                       :..:::.:-=+++++++*******########################*#******==-:....:                                    
                                       ::::::-=+++++++*************#####################*******=---:....                                    
                                       :::-:+*+++++++-.::::--==++++*************###########*****+=-:....                                    
                                       :.-:+**++==:..:-:::..      .:=+++***+==:...:::::-:-+*******+::...                                    
                                    %+=--#%%%#%    -=++++++++=--- ::-+****+--::.:--*+=:-:..::******:...                                     
                                   +=++=::-#*+==  ===-:-:....::::--:  :=:   =-----=+++++*++.   ..**-..:                                     
                                  +=-=+==-*#++++= =--:::-=...+==:--= =++++ +=-::.:..:.:-:====   ----+. +                                    
                                  +==+++=:#*+++++ ++=========---==+- +*##- *+==--=-..+-:.:==+ +==+*:.*#***                                  
                                  *==++=:=#****** ***+++++++++++++= +*###*.=**+==----====++** *****-=*=-:+                                  
                                  =++=--:+********.*************++ +**####* ****************.#*#***=-*+==-                                  
                                   ++=--:=*#***+****:**#####**+= :+**#####** ***#########*#.##*****-+**=+                                   
                                   =+++-:-+**+*+++++*++++++=+=--**+*#######*#-= =#######=.##*******:-+*+*                                   
                                    ++=*:++*+++++++++******++++=+===++***++***===++++***#*#*******=.+***                                    
                                     +*+::-+=++++++++++*+++++++==--------:::-+**++*****#*********+-.***-                                    
                                     +**:----+=++++++++++==+++=-:....:-:::-+***#*+++**********+*+=..**#                                     
                                      -=-:-=---=-==+++==:.....-.::=++-::--:::=++*++++++********+=-.:*+                                      
                                        --=-:--:-====+=..  .----------======+:::::===+++*++**+===::**                                       
                                        ::--:--:::--==-...:----======-----:..:::.. :-+++++===+==:..:                                        
                                        :::-=---:::==-:.:==+========+=+=++++===-:..:-++==---==-::.:                                         
                                         -+-:-::-:--=-.:-+++===-::.. ..::---=++++=.:=++==--=--=:::                                          
                                         :=----:::::-: .:-==++++=---==::--=++++===..=++==---:--:.:                                          
                                          +:::-:... .   .:.:------*+=+*+*##**+=-:.:..==-:=---::.:                                           
                                          :-.:::. . .  .....:::::-:-====-=:-=--:: ::.:.::.--::.:                                            
                                          =+..... .       ......::::.:--..:=-::... ...:..::.:..                                             
                                           *=.... ..        ...   ....... ......     . . .....:                                             
                                         @%*+=:  ...                                 . .....:=                                              
                                        -:%*+=--:..                       .        ..   . .:+%:=                                            
                                       :.%%%#===-:.        ..    .....      .      .  ...:-+%%+::                                           
                                     --..%%%%%#==-=-... .. .... ::.:::... .   .   . ...:==%%%%%:::                                          
                                   ===:..%%%%%%%#------:-.... ::.::.:.. .. ......   ..-+%%%%%%%:::::                                        
                                 ====-:..#%%%%%%%%%#---------:.....  .   :.  ...:.:=-%%%%%%%%%%::::::-:                                     
                           -:..=--=--:...+#%%%%%%%%%%##:-=-=-------:-:-:::--------%%%%%%%%%%%%:::::::::-:..:-                               
                      -:.....:::-----:....##%%%%%%%%%%%%##:-----===-=----------%%%%%%%%%%%%%%#::::::::::::.....:::-                         
                 ---:........::::--::.....=##%%%%%%%%%%%%%%#*-=====-===-===-%%%%%%%%%%%%%%%%%:::::::::::::::......::::---                   
            -==-::........::..:::-::.......*##%%%%%%%%%%%%%%%%%#===+=+===#%%%%%%%%%%%%%%%%%%+.:::::::::::::::........::::::----             
       ===--:::.........:::...::::.........+###%%%%%%%%%%%%%%%%%=*#%%%%%%%%%%%%%%%%%%%%%%%%#:.:::::::::::::::::........::.:::::::---        
  ===---:::............::....::::..........*###%%%%%%%%%%%%%*::......:::: %%%%%%%%%%%%%%%%#+::::::::::::::::::::........::.::::::::::-----  
==--:::::............:....:.::.............=###%%%%%%%%%%%:.:.::.::...:--:-:-%%%%%%%%%%%%%#*::::::::::.:::::::::::.........::..:::.::::::::-
-::::::.:.............  ...................:##%%%%%%%%%%- .....::.::::::::..  +%%%%%%%%%%%#:.::::::::::::::::::.  ...........:..::::::::::::
.:.......................  .................-#%%%%%%%%--==......::::::-::...====#%%%%%%%%%#:::::::::::::.::: ................:....::.:::::::
........:...:...............................#=%%%%%%=+****+=.....:::-::...===+**++%%%%%%%#-:::::::::::::::::::::::::.......:.....:.:.:.:::::
..................:........:....:.........::=#+%%%*########**+....::-::.:########**+%%%%%+:::::::::::::::::::::::::::.......:..::.:..:::::::
:.....:..:...:...........................:.::##*#%%%%%%%######*.....::..#%%%%%%%%%%%%*%%*#.::::::::::::.:::::.::.::::.::..:.::.:...:::::::::
......:...:.:..... ..........:..:..........::%%%%%%%%%%%%######:.::::-:+%%%%%%%%%%%%%%%%#+:::::::::::::::. .::::::::.....::.....::.:::.:::.:
.......:.......... ........................::%%%%%%%%%%%%%%###+...::::::%%%%%%%%%%%%%%%%#.::::::::::::::::.::.::.::..::::....:..::::::::::::
.........:..:..:... ......................:.::%%%%%%%%%%%%%##-...::::.:::%%%%%%%%%%%%%%##.:::::::::::::::::::::.::.::::..:.:::::::::::::::::
..........:.......:.............:...........::%%%%%%%%%%%%%#-..:.:-:::::::%%%%%%%%%%%%%#::::::::::::::::::::::::::.::::.::..::.:::::::::::::
:.....:......:..........:..................:::%%%%%%%%%%%%##:...:::-::-::::%%%%%%%%%%%%#.::::::::::::::::::::::::..::..:::::::::::::::::::::
:......:.:........... :.....................:::%%%%%%%%%%%#::.:.:::--:-::::*%%%%%%%%%%#+.:::::::::::::::::::::::.::::::.::::::::::::::::::::
:...........:...............:..:............:::%%%%%%%%%%#-:::..::::--:--::-%%%%%%%%%%#.:::::::::::::::::::.:::.::::::::.::::::::::::::::..:
......:.......::.........::.:................::*%%%%%%%%%#.::::::::-::-::::-%%%%%%%%%##.:::::::::::::::..:::::..:.:::::::.:::::::::.::::::::
.............:...:....: ...:.::...:........:.:::%%%%%%%%%#::..:.::::::--::-:#%%%%%%%%#.::::::::::::::::::::::-..::::::::::::::::::...:.:::..
............:.........:. :..:.:..............:::%%%%%%%%#.:::::::::::::::-::.%%%%%%%%#.::::::::::::::::::::::.:..::::::.::::::::::.::::.::..
..............:.....::.......:................:::%%%%%%%#.::..:::::::::--:-::%%%%%%%#.::::::::::::::::::::::..:::::::.::::::::::::.:::..:.:.
.................:.:.::.:.....:...::..........:::%%%%%%%#:::::::::-::--:--:-:#%%%%%##.:::::::::::.:::::::::.:::::::::::::::::::::.::::.::...'''

def build_svg(dark=True):
    width = 1200
    height = 730
    
    if dark:
        bg_fill = "#161b22"
        text_fill = "#c9d1d9"
        key_fill = "#ffa657"
        val_fill = "#a5d6ff"
        add_fill = "#3fb950"
        del_fill = "#f85149"
        cc_fill = "#616e7f"
        ascii_fill = "#FFFFFF"  # White
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

    ascii_lines = [l.rstrip() for l in raw_user_ascii.split('\n')]

    TOTAL_CHARS = 46

    # Optimized and shortened Neofetch specs to fit perfectly without overflow
    specs = [
        ("prompt", "ahmad@PTUK", ":~$ neofetch --engineer --security", add_fill, "addColor"),
        ("spec", "OS", "Linux (Debian), Windows 11", val_fill, "val"),
        ("spec", "Host", "PTUK (Palestine Technical Univ)", val_fill, "val"),
        ("spec", "Kernel", "Computer Systems Eng (2022-2027)", add_fill, "addColor"),
        ("spec", "Role", "Full-Stack Dev & Security Researcher", val_fill, "val"),
        ("spec", "Focus", "ASP.NET Core • Laravel • React • Vue", val_fill, "val"),
        ("spec", "IDE", "VS Code, Visual Studio 2022", val_fill, "val"),
        ("spec", "Backend", "C# (ASP.NET), PHP (Laravel), SQL", val_fill, "val"),
        ("spec", "Frontend", "React, Vue.js, JavaScript, SCSS", val_fill, "val"),
        ("spec", "Database", "MySQL, Microsoft SQL Server", val_fill, "val"),
        ("spec", "Security.Tools", "Burp Suite Pro, OWASP Top 10", val_fill, "val"),
        ("spec", "Security.Practice", "Web Pentesting & Bug Hunting", val_fill, "val"),
        ("spec", "Certifications", "OCI 2025 • AI/TF • Ethical Hacking", add_fill, "addColor"),
        ("spec", "PortSwigger Labs", "50+ Solved (SQLi, XSS, CSRF)", add_fill, "addColor"),
        ("spec", "HackerOne Vulns", "15+ Reported (High / Med)", add_fill, "addColor"),
        ("spec", "Email", "ahmadherzalla31@gmail.com", val_fill, "val"),
        ("spec", "LinkedIn", "ahmadherzalla12", val_fill, "val"),
        ("spec", "Portfolio", "ahmed-herzalla0.github.io/Portfolio-scss", val_fill, "val"),
        ("spec", "GitHub", "Ahmed-Herzalla0", add_fill, "addColor"),
        ("spec", "Status", "Open for Dev & Security Roles", add_fill, "addColor")
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
    out.append("  font-size: 7.5px;")
    out.append("  letter-spacing: 0px;")
    out.append("}")
    out.append(".specs {")
    out.append("  font-family: 'ConsolasFallback', Consolas, 'Fira Code', 'Courier New', monospace;")
    out.append("  font-size: 13.5px;")
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
    out.append(f'<text x="14" y="20" fill="{ascii_fill}" class="ascii">')
    for i, line in enumerate(ascii_lines):
        y = 20 + i * 9.7
        safe_line = html.escape(line)
        out.append(f'<tspan x="14" y="{y:.1f}" fill="{ascii_fill}">{safe_line}</tspan>')
    out.append('</text>')

    # Right Neofetch Specs block starting at x="635"
    out.append(f'<text x="635" y="60" fill="{text_fill}" class="specs">')
    spec_start_y = 60
    spec_line_height = 32.0
    for i, item in enumerate(specs):
        y = spec_start_y + i * spec_line_height
        if item[0] == "prompt":
            u_part = html.escape(item[1])
            cmd_part = html.escape(item[2])
            out.append(f'<tspan x="635" y="{y:.1f}"><tspan fill="{add_fill}" class="addColor">{u_part}</tspan><tspan fill="{val_fill}">{cmd_part}</tspan></tspan>')
        else:
            k = item[1]
            v = item[2]
            color_hex = item[3]
            cls_name = item[4]
            used_len = len(k) + len(v) + 4
            num_dots = max(3, TOTAL_CHARS - used_len)
            dots = " " + ("." * num_dots) + " "
            safe_k = html.escape(k)
            safe_v = html.escape(v)
            safe_dots = html.escape(dots)
            out.append(f'<tspan x="635" y="{y:.1f}"><tspan fill="{key_fill}" class="key">{safe_k}</tspan><tspan fill="{cc_fill}" class="cc">:{safe_dots}</tspan><tspan fill="{color_hex}" class="{cls_name}">{safe_v}</tspan></tspan>')
    out.append('</text>')
    out.append('</svg>')
    
    return '\n'.join(out)

if __name__ == "__main__":
    for fname in ["dark_mode.svg", "dark_mode_v7.svg"]:
        with open(f"/home/ahmad/Desktop/Ahmed-Herzalla0/{fname}", "w") as f:
            f.write(build_svg(dark=True))
    for fname in ["light_mode.svg", "light_mode_v7.svg"]:
        with open(f"/home/ahmad/Desktop/Ahmed-Herzalla0/{fname}", "w") as f:
            f.write(build_svg(dark=False))
    print("SVGs v7 generated successfully!")
