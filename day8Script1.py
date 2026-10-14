# Author : Archana Zhope
# Date : 14 October 2026
# Script : Log parser version1

with open('logs/sample.log',"r") as f:
    lines= f.readlines()
print(f"total lines {len(lines)}\n ")



print("Level | Job")
error_lines = [] #list intialize
level_counts ={} # dict initialize
for line in lines:
    date, time, level, job, message = line.strip().split(" ",4)   
    if  level == "ERROR":
            error_lines.append(line.strip())
    print(f"{level} | {job}")
    level_counts[level] = level_counts.get(level,0) + 1

print("\nError statements:")
for stmt in error_lines:
   print(stmt)

print(level_counts)

