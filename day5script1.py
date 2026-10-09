# Author: Archana Zhope
# Date : 9 October 2026
# Script : Mini project

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

statuses = [
    "SUCCESS",
    "SUCCESS",
    "WARNING",
    "SUCCESS",
    "FAILED",
    "FAILED",
    "FAILED",
    "ABORTED",
    "FAILED",
    "WARNING",
]

failed_status = ["FAILED", "ABORTED"]
failed_count = 0
success_count = 0
warning_count = 0
failed_jobs=[]
for i in range(len(jobs)):
  if statuses[i] in failed_status:
    failed_count += 1
    failed_jobs.append(jobs[i])
  elif statuses[i] == "SUCCESS":
    success_count += 1
  elif statuses[i] == "WARNING":
    warning_count += 1  

print(f"{len(jobs)} jobs: {success_count} success, {failed_count} failed, {warning_count} warning\n")

for i in range(len(failed_jobs)):
    print(f"Failed job {i+1}: {failed_jobs[i]}\n")

print(f"success jobs rate in percentage: {success_count/len(jobs)*100:.1f}%")

if failed_count == 0:
    print("All OK, No failed jobs")
elif failed_count < len(jobs)/2:
    print("ATTENTION: Some jobs failed, please check the logs for details")
elif failed_count >= len(jobs)/2:
    print("CRITICAL: More than half of the jobs failed, please check the logs for details")   

while True:
   user_input = input("Enter job name (or quit) :  ")
   if user_input.lower() == "quit":
       print("Exiting the program.")
       break
   
   if user_input.lower() in [job.lower() for job in jobs]:
        print(f"Job {jobs[[job.lower() for job in jobs].index(user_input.lower())]} has status: {statuses[[job.lower() for job in jobs].index(user_input.lower())]}")
   else:
         print("Job not found.")

   