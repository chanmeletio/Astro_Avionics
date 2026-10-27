import sys

with open('c:/Users/jhfmt/Desktop/AI_Flight_Controller/New_Flight_Controller.kicad_pcb', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if '"J4"' in line:
        print(f'{i}: {line.strip()}')
