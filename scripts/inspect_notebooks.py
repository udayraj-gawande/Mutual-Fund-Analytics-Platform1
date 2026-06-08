import json
import sys

# Reconfigure stdout to use utf-8
sys.stdout.reconfigure(encoding='utf-8')

def print_nb_code(nb_path):
    print(f"\n========================================\nCode Cells for: {nb_path}")
    with open(nb_path, "r", encoding="utf-8") as f:
        nb = json.load(f)
    
    code_cell_idx = 0
    for cell in nb.get("cells", []):
        if cell.get("cell_type") == "code":
            code_cell_idx += 1
            source = "".join(cell.get("source", []))
            print(f"--- Cell {code_cell_idx} ---")
            print(source)

print_nb_code("notebook/04_performance_analytics.ipynb")
print_nb_code("notebook/05_advanced_analytics.ipynb")
