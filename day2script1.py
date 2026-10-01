#author : Archana Zhope
#Date : 01-10-2026
#Script Details : 

job_name = "DS_LOAD_CUSTOMER"
exit_code = int(input("Enter job status\n")) 

if exit_code == 0:
    print(f"Job {job_name} : SUCCESS.")
elif exit_code == 4:
    print(f"Job {job_name} : WARNING.")
else:
    print(f"Job {job_name} : FAILED.")

duration = int(input("Enter job duration in seconds\n"))
if duration <= 30:
   print(f"with duration {duration} seconds, short run job")
elif duration > 30 and duration <= 45:
    print(f"with duration {duration} seconds, slow job ")
else:
    print(f"with duration {duration}, long run job") 