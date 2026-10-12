# Author : Archana Zhope
# Date : 08 October 2026
# Script : Dictonary example

jobs = [
    {"name": "DS_EXTRACT_CUSTOMER_MASTER", "status": "SUCCESS", "minutes": 10},
    {"name": "DS_EXTRACT_ACCOUNT_BALANCE", "status": "SUCCESS", "minutes": 15},
    {"name": "DS_TRANSFORM_TXN_DAILY", "status": "WARNING", "minutes": 20},
    {"name": "DS_LOAD_DWH_CUSTOMER", "status": "SUCCESS", "minutes": 25, "retries":2},
    {"name": "DS_LOAD_DWH_TXN", "status": "FAILED", "minutes": 30},
    {"name": "CTM_FILE_WATCHER_SWIFT_IN", "status": "FAILED", "minutes": 35},
    {"name": "CTM_FTP_REGULATORY_RPT", "status": "FAILED", "minutes": 40},
    {"name": "SQL_RECON_GL_BALANCE", "status": "ABORTED", "minutes": 45},
    {"name": "SH_ARCHIVE_PROCESSED_FILES", "status": "FAILED", "minutes": 50},
    {"name": "SH_PURGE_TEMP_TABLES", "status": "WARNING", "minutes": 55},
]

for job in jobs:
   print(f"{job.get('name')} | {job.get('status')} | {job.get('minutes')} minutes | retries: {job.get('retries', 0)}\n")


print("displaying failed job\n")
for job in jobs:
   if job.get('status') in ["FAILED","ABORTED"]:
      print(f"{job.get('name')} | {job.get('status')}  \n")

found = False
input_name  = input("enter job name :\n")
for job in jobs:
        if input_name.lower() == job.get('name').lower():
                print(f"job {job.get('name')} found and its status is {job.get('status')} which took {job.get('minutes')} minutes to finish" )
                found=True
                break

if found == False:
                print(f"job {input_name} not found" )

min_counter=0
for job in jobs:
       if job.get('minutes') > min_counter:
          min_counter=job.get('minutes')
          job_name=job.get('name')


print(f"job {job_name} took maximum time of {min_counter} minutes\n")
        