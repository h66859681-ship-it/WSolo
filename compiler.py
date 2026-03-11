import subprocess
import os
import time

ConsolePass = False

open('work.py', 'w').close()

try:
    with open('program.ws', 'r', encoding='utf-8') as file:
        for line_num, line in enumerate(file, start=1):
            com = line.strip()
            if not com:
                continue
            
            time.sleep(0.01)
            execom = com.split()
            cmd = execom[0]
            
            if cmd == "run":
                if os.path.exists('work.py'):
                    subprocess.run(['python', 'work.py'])
                
            elif cmd == "use":
                if len(execom) > 1 and execom[1] == "<System>":
                    with open('work.py', 'a', encoding='utf-8') as f_out:
                        f_out.write('from math import *\nfrom zona import *\n')
                elif len(execom) > 1 and execom[1] == "<gameengine>":
                    with open('work.py', 'a', encoding='utf-8') as f_out:
                        f_out.write('import pgzrun\n')
                elif len(execom) > 1 and execom[1] == "<time>":
                    with open('work.py', 'a', encoding='utf-8') as f_out:
                        f_out.write('import time\n')
                elif len(execom) > 1 and execom[1] == "<videoplayer>":
                    with open('work.py', 'a', encoding='utf-8') as f_out:
                        f_out.write('import cv2\n')
                elif len(execom) > 1 and execom[1] == "<pygame>":
                    with open('work.py', 'a', encoding='utf-8') as f_out:
                        f_out.write('import pygame\n')
                elif len(execom) > 1 and execom[1] == "pass":
                    if execom[2] == "*":
                        if execom[3] == "Console":
                            ConsolePass = True
            elif cmd == "game.run":
                with open('work.py', 'a', encoding='utf-8') as f_out:
                    f_out.write(f'pgzrun.go()\n')
            elif cmd == 'tab':
                with open('work.py', 'a', encoding='utf-8') as f_out:
                    f_out.write(f'\t')
            elif cmd == "func":
                with open('work.py', 'a', encoding='utf-8') as f_out:
                    f_out.write(f'def {execom[1]}{execom[2]}:')
            elif cmd == "line":
                with open('work.py', 'a', encoding='utf-8') as f_out:
                    f_out.write(f'\n')
            elif cmd == "space":
                with open('work.py', 'a', encoding='utf-8') as f_out:
                    f_out.write(f' ')
            elif cmd == "var":
                with open('work.py', 'a', encoding='utf-8') as f_out:
                    f_out.write(f'{execom[1]} = {com[6:].replace(execom[1], "")}\n')
            elif cmd == "workwrite":
                with open('work.py', 'a', encoding='utf-8') as f_out:
                    f_out.write(f'{com.replace("workwrite ", "")}')
            elif cmd == "if":
                if execom[1] == "cond":
                    cond = com.replace("if cond ","")
                    with open('work.py', 'a', encoding='utf-8') as f_out:
                        f_out.write(f'if {cond}:\n')
            elif cmd == "while":
                if execom[1] == "cond":
                    cond = com.replace("while cond ","")
                    with open('work.py', 'a', encoding='utf-8') as f_out:
                        f_out.write(f'while {cond}:\n')
            elif cmd == "time":
                timeofsleep = execom[1]
                with open('work.py','a', encoding='utf-8') as f_out:
                    f_out.write(f'time.sleep({timeofsleep})\n')
            elif cmd == "exit":
                break
            elif ConsolePass == False:
                if cmd == "Console.New.Text":
                    if execom[1] == "=":
                        payload = com[18:].strip()
                        with open('work.py', 'a', encoding='utf-8') as f_out:
                            f_out.write(f'print({payload})\n')
            elif ConsolePass ==  True:
                if execom[1] == "=":
                    if cmd == "New.Text":
                        payload = com[10:].strip()
                        with open('work.py', 'a', encoding='utf-8') as f_out:
                            f_out.write(f'print({payload})\n')
except FileNotFoundError:
    print("Файл program.ws не найден!")
    input()
