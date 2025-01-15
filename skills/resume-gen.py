#!/usr/bin/env python3

import sys
import os
import subprocess

RESUME_TEX_FILE="/home/e/Documents/Programs/resume/EthanThomasResume.tex"

DEST_DIR = "/home/e/Downloads/ResumeSkills"

# Check if exactly one argument is provided
if len(sys.argv) != 2:
    print("Usage: resume-gen \"your, comma, separated, skills\"")
    sys.exit(1)

# Get the argument (it's the second item in sys.argv)
skills_str = sys.argv[1]

skills = skills_str.split(",")

skills = [skill.strip() for skill in skills]


lines = None
with open(RESUME_TEX_FILE, "r") as f:
    lines = f.readlines()

line_number = -1
for i in range(0, len(lines)):
    if "%%%===OTHER_SKILLS_SECTION_HERE" in lines[i]:
        line_number = i
        break

if line_number <= 0:
    print("%%%===OTHER_SKILLS_SECTION_HERE NOT FOUND")
    sys.exit(1)

skills_str = ", ".join(skills)

new_line = "\\vspace{2pt} \\newline \\small{\\textbf{Other Skills:} " + skills_str + "}\n"

lines[line_number] = new_line

if not os.path.exists(DEST_DIR):
    os.makedirs(DEST_DIR)

new_num = 1
for f in os.listdir(DEST_DIR):
    fname_no_ext = f.split(".")[0]
    last_underscore = fname_no_ext.split("_")[-1]
    try:
        num = int(last_underscore)
        pot_num = num + 1
        if pot_num > new_num:
            new_num = pot_num
    except:
        continue

new_file_name = DEST_DIR + "/" + f"EthanThomasResume_{new_num:02d}.tex"



with open(new_file_name, "w") as f:
    f.write("".join(lines))

subprocess.run(["pdflatex", "-synctex=1", "-interaction=nonstopmode", "-file-line-error", "-recorder",f"-output-directory={DEST_DIR}",  new_file_name], stdout=subprocess.DEVNULL)

for f in os.listdir(DEST_DIR):
    full_path = DEST_DIR + "/" + f
    ext = f.split(".")[-1]
    if ext != "pdf":
        os.remove(full_path)
    