import os
import subprocess

SOURCE_FILE = "main.coin"
BUILD_DIR = "build"
OUTPUT_FILE = os.path.join(BUILD_DIR, "main.cbin")

os.makedirs(BUILD_DIR, exist_ok=True)

with open(SOURCE_FILE, "r") as file:
    source = file.readlines()

compiled = [
    "COIN_BINARY_v1",
    "==============",
    ""
]

for line in source:
    line = line.strip()

    if line.startswith("print"):
        value = line.replace("print", "", 1).strip()
        compiled.append(f"LOAD_CONST {value}")
        compiled.append("PRINT")
        compiled.append("")

    elif line.startswith("let"):
        parts = line.replace("let", "", 1).split("=")

        if len(parts) == 2:
            name = parts[0].strip()
            value = parts[1].strip()

            compiled.append(f"LOAD_INT {value}")
            compiled.append(f"STORE {name}")
            compiled.append("")

compiled.append("HALT")

with open(OUTPUT_FILE, "w") as file:
    file.write("\n".join(compiled))

print(f"Compiled -> {OUTPUT_FILE}")

if os.path.exists(OUTPUT_FILE):
    print("\nBuild successful.")
