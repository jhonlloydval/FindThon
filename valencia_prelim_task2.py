# Demo program to showcase FindThon text analysis functionality
# VALENCIA, JHON LLOYD M.

import re

# Load the file content
with open("demo.txt", "r") as f:
    content = f.read()
    lines = content.split('\n')

print("""
╔════════════════════════[ WELCOME TO ]════════════════════════╗
                    >>> TESTER DEMO FOR <<<
███████╗██╗███╗   ██╗██████╗ ████████╗██╗  ██╗ ██████╗ ███╗   ██╗
██╔════╝██║████╗  ██║██╔══██╗╚══██╔══╝██║  ██║██╔═══██╗████╗  ██║
█████╗  ██║██╔██╗ ██║██║  ██║   ██║   ███████║██║   ██║██╔██╗ ██║
██╔══╝  ██║██║╚██╗██║██║  ██║   ██║   ██╔══██║██║   ██║██║╚██╗██║
██║     ██║██║ ╚████║██████╔╝   ██║   ██║  ██║╚██████╔╝██║ ╚████║
╚═╝     ╚═╝╚═╝  ╚═══╝╚═════╝    ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝

╚════════[ PYTHON CONSOLE-BASED TEXT FINDER USING REGEX ]═══════╝
""")

print("╔" + "═" * 70 + "╗")
print("║                        BASIC FUNCTION DEMONSTRATIONS                 ║")
print("╚" + "═" * 70 + "╝\n")

# 1. View the entire file conttent
print("┌" + "─" * 40 + "┐")
print("│          1. FILE CONTENT VIEWER        │")
print("└" + "─" * 40 + "┘")
print(content)
print("\n" + "•" * 50 + "\n")

# 2. Search for a word or sentence
print("┌" + "─" * 40 + "┐")
print("│      2. SINGLE WORD SEARCH: 'Python'   │")
print("└" + "─" * 40 + "┘")
search_word = "Python"
for i, line in enumerate(lines, 1):
    if search_word in line:
        print(f"✓ First occurrence found in Line {i}:\n  {line}")
        break
print("\n" + "•" * 50 + "\n")

# 3. Find all matches
print("┌" + "─" * 40 + "┐")
print("│        3. ALL MATCHES FOR 'Python'     │")
print("└" + "─" * 40 + "┘")
for i, line in enumerate(lines, 1):
    if "Python" in line:
        print(f"→ Line {i}: {line}")
print("\n" + "•" * 50 + "\n")

# 4. Count matches
print("┌" + "─" * 40 + "┐")
print("│         4. OCCURRENCE COUNTER          │")
print("└" + "─" * 40 + "┘")
count = sum(line.count("Python") for line in lines)
print(f"Total occurrences of 'Python': {count}")
print("\n" + "•" * 50 + "\n")

# 5. Compute total sum of numbers
print("┌" + "─" * 40 + "┐")
print("│        5. NUMERICAL SUMMATION          │")
print("└" + "─" * 40 + "┘")
numbers = []
for line in lines:
    numbers.extend(int(num) for num in re.findall(r'-?\b\d+\b', line))
print(f"Sum of all numbers: {sum(numbers)}")
print("\n" + "•" * 50 + "\n")

# 6. Find the min and max values
print("┌" + "─" * 40 + "┐")
print("│      6. MINIMUM & MAXIMUM VALUES       │")
print("└" + "─" * 40 + "┘")
if numbers:
    print(f"▼ Minimum value: {min(numbers)}")
    print(f"▲ Maximum value: {max(numbers)}")
else:
    print("× No numbers found")
print("\n" + "•" * 50 + "\n")

# 7. Calculate average
print("┌" + "─" * 40 + "┐")
print("│       7. NUMERICAL AVERAGE             │")
print("└" + "─" * 40 + "┘")
num_list = []
hand = open("demo.txt")
for line in hand:
    line = line.rstrip()
    numbers = re.findall("[0-9]+", line)

    for x in numbers:
        num_list.append(int(x))
print(f"The average is: {sum(num_list) / len(num_list)} ")
print("\n" + "•" * 50 + "\n")

# EXTENSIVE SEARCHING DEMO
print("╔" + "═" * 70 + "╗")
print("║                    EXTENSIVE SEARCHING DEMONSTRATIONS                ║")
print("╚" + "═" * 70 + "╝\n")

# String Patteerns
print("┌" + "─" * 50 + "┐")
print("│              STRING PATTERN EXAMPLES             │")
print("└" + "─" * 50 + "┘")

patterns = {
    "Exact Match": r"\bPython\b",
    "Case-Insensitive": r"(?i)python",
    "Whole Word Match": r"\bPython\b",
    "Words Starting with 'P'": r"\bP[a-zA-Z]*",
    "Words Ending with 'g'": r"[a-zA-Z]*g\b",
    "Contains 'or'": r".*or.*",
    "Alphanumeric Only": r"\b[a-zA-Z0-9]+\b",
    "5-Letter Words": r"\b\w{5}\b",
    "With Special Chars": r"[^a-zA-Z0-9\s]",
    "Words with Numbers": r"\b(?=\w*\d)(?=\w*[a-zA-Z])\w+\b"
}

for desc, pattern in patterns.items():
    print(f"\n▶ {desc} ({pattern}):")
    matches = []
    for i, line in enumerate(lines, 1):
        if re.search(pattern, line):
            matches.append(f"  └─ Line {i}: {line}")
    if matches:
        print("\n".join(matches))
    else:
        print("  └─ No matches found")
    print("." * 50)

# Number Patterns
print("\n┌" + "─" * 50 + "┐")
print("│              NUMBER PATTERN EXAMPLES             │")
print("└" + "─" * 50 + "┘")

number_patterns = {
    "0-100": r"\b(?:[1-9]?[0-9]|100)\b",
    "Even Numbers": r"\b(?:[02468])\b|\b(?:[1-9]*[02468])\b",
    "Odd Numbers": r"\b(?:[13579])\b|\b(?:[1-9]*[13579])\b",
    "Decimals": r"\b\d+\.\d+\b",
    "Percentages": r"\b\d+%",
    "Leading Zeros": r"\b0+\d+\b",
    "Positive Numbers": r"\b\d+\b",
    "Negative Numbers": r"-\d+",
    "Consecutive Numbers": r"\b(?:123|234|345|456|567|678|789|987|876|765|654|543|432|321)\b",
    "Contains Digit 9": r"\b[0-9]*9[0-9]*\b"
}

for desc, pattern in number_patterns.items():
    print(f"\n▶ {desc} ({pattern}):")
    matches = []
    for i, line in enumerate(lines, 1):
        if re.search(pattern, line):
            matches.append(f"  └─ Line {i}: {line}")
    if matches:
        print("\n".join(matches))
    else:
        print("  └─ No matches found")
    print("." * 50)

print("\n╔" + "═" * 70 + "╗")
print("║                         DEMO COMPLETED                               ║")
print("╚" + "═" * 70 + "╝")