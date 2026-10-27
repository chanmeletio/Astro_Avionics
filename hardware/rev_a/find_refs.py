import re

with open('c:/Users/jhfmt/Desktop/AI_Flight_Controller/New_Flight_Controller.kicad_pcb', 'r', encoding='utf-8') as f:
    content = f.read()

for ref in ['J4', 'J5', 'R19', 'R20']:
    pattern = r'\(footprint.*?(?=\(footprint|\Z)'
    # Find footprint blocks
    for match in re.finditer(r'\(footprint .*?\(property "Reference" "(.*?)"(.*?)\n\s*\)', content, re.DOTALL):
        if match.group(1) == ref:
            print(f"Ref: {ref}")
            print(match.group(0))
