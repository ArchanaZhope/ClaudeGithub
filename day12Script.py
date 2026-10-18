# Author : Archana Zhope
# Date : 18 October 2026
# Script : Log parser version2



import json
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

log_path ="logs/generated.log"
result = read_logs(log_path)
print(len(result["parsed"]))

errors_per_job = {}
for line in result["parsed"]:
    if line["level"] == "ERROR":
        job = line["job"]
        errors_per_job[job] = errors_per_job.get(job, 0) +1 
print(errors_per_job)
ranked_job=sorted(errors_per_job.items(), key=lambda pair: pair[1] , reverse=True)
print(ranked_job)
print(ranked_job[:5])

errors_per_message={}
for line in result["parsed"]:
    if line["level"] == "ERROR":
        message = line["message"]
        errors_per_message[message] = errors_per_message.get(message, 0) +1 
print(errors_per_message)
ranked_message=sorted(errors_per_message.items(), key=lambda pair: pair[1] , reverse=True)
print("\n\n")
print(ranked_message)
print(ranked_message[:5])

analysis = {
    "source_file" : log_path ,
    "total_errors" : sum(errors_per_job.values()),
    "top_job" : ranked_job[:5],
    "top_message": ranked_message[:5]   
}

print(analysis)

with open("logs/highest_error.json","w") as f:
    json.dump(analysis, f, indent = 2)
    f.write("\n")
    print(f" logs/highest_error.json created")