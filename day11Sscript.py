# Author: Archana Zhope
# Date : 9 October 2026
# Script : Mini project

import random
import sys
from datetime import datetime, timedelta

jobs = [
                    "DS_EXTRACT_CUSTOMER_MASTER",
                    "DS_EXTRACT_ACCOUNT_BALANCE",
                    "DS_TRANSFORM_TXN_DAILY",
                    "DS_LOAD_DWH_CUSTOMER",
                    "DS_LOAD_DWH_TXN",
                    "CTM_FILE_WATCHER_SWIFT_IN",
                    "CTM_FTP_REGULATORY_RPT",
                    "SQL_RECON_GL_BALANCE",
                    "SH_ARCHIVE_PROCESSED_FILES",
                    "SH_PURGE_TEMP_TABLES",
                ]

messages = {
    "INFO": [
        "Job started",
        "Job finished successfully",
        "File received",
        "Purge completed",
        "Row count matches source",
        "Checkpoint saved",
    ],
    "WARN": [
        "Retry 1 of 3 started",
        "Row count differs from previous run",
        "Job running longer than average",
        "Disk usage above 80 percent",
        "Reject file not empty",
    ],
    "ERROR": [
        "Connection timeout after 30s",
        "FTP login failed for user svc_rpt",
        "ORA-01555 snapshot too old",
        "File not found in landing directory",
        "Abnormal termination with exit code 8",
        "Deadlock detected on table TXN_DAILY",
    ],
}

def parse_line(line):
   split= line.strip().split(" ",4)
   if len(split) != 5:
        return None
   if split[2] not in ["WARN", "INFO","ERROR"]:
        return None

   return {
                "date" : split[0],
                "time" : split[1],
                "level" : split[2],
                "job" : split[3],
                "message" : split[4]
            }


def make_log_line(when):
         level = random.choice(["INFO","INFO","ERROR","INFO", "WARN","INFO","INFO", "WARN","INFO","INFO", "WARN"])
         message = random.choice(messages[level])
         job = random.choice(jobs)
        # when1 = datetime(when)
         stamp = when.strftime("%Y-%m-%d %H:%M:%S")
         return f"{stamp} {level} {job} {message}" 




  
if len(sys.argv) != 2:
    print("Usage: python3 day11Sscript.py <count>")
    sys.exit(1)
try:
    count = int(sys.argv[1])
except ValueError:
        print("Count must be whole number")
        sys.exit(1)

if count <= 0:
        print("Count should be greater than 0")
        sys.exit(1)

print(f"You asked for {count} lines")
log_line = []
when = datetime(2027, 1, 16, 3, 35, 5)
for _ in range(count):
            line = make_log_line(when)
            log_line.append(line)
            if parse_line(line) is None:
                print("log failed to parse")   
            when = when + timedelta(seconds= random.randint(5,60))


with open("logs/generated.log","w") as f:
            for logline in log_line:
                f.write(logline + "\n")
print("File updated with logs")

