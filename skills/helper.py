import sys
import subprocess
file = "skills.txt"


if __name__ == "__main__":
    lines = None
    with open(file, 'r') as f:
        lines = f.readlines()

    all_skills = []
    for line in lines:
        line = line.strip()
        
        skills = line.split(",")
        for skill in skills:
            all_skills.append(skill.strip())


    #print(all_skills)

    for skill in all_skills:
        try:
            subprocess.run(["wl-copy", skill])
            print(f"Copied '{skill}'")
            s = input()

        except KeyboardInterrupt:
            break
   
    print("All done.") 
