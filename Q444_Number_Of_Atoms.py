"""
Q444: Number of Atoms (Stack-based Parsing)
==============================================
Problem: Parse chemical formula string, return count of each atom
in sorted formatted string.

Example:
    "H2O" -> "H2O"
    "Mg(OH)2" -> "H2MgO2"
    "K4(ON(SO3)2)2" -> "K4N2O14S4"
"""
from collections import defaultdict

def count_of_atoms(formula):
    def parse(i):
        counts = defaultdict(int)
        while i < len(formula):
            if formula[i] == '(':
                inner, i = parse(i+1)
                i, num = parse_num(i)
                for atom, cnt in inner.items():
                    counts[atom] += cnt * num
            elif formula[i] == ')':
                return counts, i+1
            else:
                atom, i = parse_atom(i)
                i, num = parse_num(i)
                counts[atom] += num
        return counts, i

    def parse_atom(i):
        start = i
        i += 1
        while i < len(formula) and formula[i].islower():
            i += 1
        return formula[start:i], i

    def parse_num(i):
        start = i
        while i < len(formula) and formula[i].isdigit():
            i += 1
        return i, int(formula[start:i]) if start != i else 1

    counts, _ = parse(0)
    return ''.join(f"{atom}{counts[atom] if counts[atom]>1 else ''}" for atom in sorted(counts))

if __name__ == "__main__":
    print(count_of_atoms("H2O"))             # "H2O"
    print(count_of_atoms("Mg(OH)2"))         # "H2MgO2"
    print(count_of_atoms("K4(ON(SO3)2)2"))   # "K4N2O14S4"
