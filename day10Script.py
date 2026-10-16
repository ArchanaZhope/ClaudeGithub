# Author : Archana Zhope
# Date : 14 October 2026
# Script : Log parser version1


import json
import os

VALID_LEVEL = ["WARN", "INFO","ERROR"]

# check each line contain 5 split and level is WARN, INFO, ERROR
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


# take path as input and return bad list of line number, parsed list, skipped count
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
            "bad_number" : [],
            "found": False
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
            "bad_number" : bad_number,
            "found" : True
        }

print("Displaying output from files")
input_path = input("enter path:    \n")

result = read_logs(input_path)

entries = result["parsed"]
skip = result["skipped"]
bad_number = result["bad_number"]
print(f"Parsed: {len(entries)}, skipped: {skip}")
print(f"bad_numbers are : {bad_number}")
total_count  =len(entries) + skip
print(f"total lines in file  : {total_count}")

level_count  = {}
job = []
for entry in entries:
    level = entry["level"]
    level_count[level] = level_count.get(level,0) +1
    if level == "ERROR":
        if entry["job"] not in job:
           job.append(entry['job'])




print(f"levelcount :   {level_count}")





print(f"\n\n\n Day 10 Start from here --------------------------\n\n")

summary_dict = { 
    "file_path" : input_path,
     "total_lines" : total_count,
     "parsed_count" : len(entries),
     "skipped_count" : skip,
     "skip_line_no" : bad_number,
     "level_count" : level_count,
     "error_job_list" : job

}

print(summary_dict)
if  result["found"] is not False:
   json_file= (os.path.basename(input_path).replace(".log",""))+"_summary.json"
   with open(json_file, "w") as f:
       json.dump(summary_dict, f, indent = 2)
       f.write("\n")
       print(f" {json_file} created")
   
   with open(json_file) as f:
       loaded = json.load(f)
       print(f" {json_file}  loaded")
   print(f"verification:: json loaded file result   : {loaded['error_job_list']}")
   print(loaded == summary_dict)