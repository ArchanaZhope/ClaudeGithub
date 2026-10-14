# Author : Archana Zhope
# Date : 14 October 2026
# Script : Log parser version1


VALID_LEVEL = ["WARN", "INFO","ERROR"]


def parse_line(line):
   split= line.strip().split(" ",4)
   if len(split) != 5:
        return None
   if split[2] not in VALID_LEVEL:
        return None

   return {
                "date" : split[0],
                "time" : split[1],
                "level" : split[2],
                "job" : split[3],
                "message" : split[4]
            }



def read_logs(path):
    parsed = []
    skipped = 0
    bad_number = []
    try:
      with open(path,"r") as f:
        lines = f.readlines()
    except FileNotFoundError:
        print(f"File not found: {path}")
        return {
            "skipped": 0,
            "parsed": [],
            "bad_number" : []
        }  
    
    for number,line in enumerate(lines, start=1):
            result = parse_line(line)
            if result is None:
                skipped += 1  
                bad_number.append(number)
            else:
                parsed.append(result)
    return {    
            "skipped": skipped,
            "parsed" : parsed,
            "bad_number" : bad_number
        }

print("Displaying output from files")
input_path = input("enter path:    \n")
entries ={}
skipped =0
result = read_logs(input_path)

entries = result["parsed"]
skip = result["skipped"]
bad_number = result["bad_number"]
print(f"Parsed: {len(entries)}, skipped: {skip}")
print(f"bad_numbers are : {bad_number}")
total_count  =len(entries) + skip
print(total_count)

level_count  = {}
for entry in entries:
    level = entry["level"]
    level_count[level] = level_count.get(level,0) +1

print(f"levelcount :   {level_count}")



       
 