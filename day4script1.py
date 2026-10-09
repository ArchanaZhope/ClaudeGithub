# Author : Archana Zhope
# Date : 9 October 2026
# Script : for Loop , break , list example

jobs = [ 
            "alert monitoring",
            "pre check job before patching",
            "post check job after patching",
            "BCP/DR" ,
            "post-deployment sanity job",
            "data loader",
            "data transformer",
            "extract generation"
        ] 

statuses = [
                "completed",
                "warning",
                "failed",
                "failed",
                "completed",
                "warning",
                "aborted",
                "cancelled"
            ]

print(f"2. printing all jobs\n")
for i in range(len(jobs)):
    print(f"Job: {jobs[i]} | Status: {statuses[i]}\n")

print(f"3. printing failed jobs\n")
for i in range(len(jobs)):
    if statuses[i] == "failed" or statuses[i] == "aborted" or statuses[i] == "cancelled":
        print(f"Job: {jobs[i]} has {statuses[i]}. Please check the logs for details.\n")

print(f"4. printing failed jobs counts\n")
failed_count =0
for i in range(len(jobs)):
    if statuses[i] == "failed" or statuses[i] == "aborted" or statuses[i] == "cancelled":
        failed_count =failed_count +1
    
print(f"{failed_count} of {len(jobs)} jobs failed\n")

print(f"5. printing 1st failure\n")
for i in range(len(jobs)):
    if statuses[i] == "failed" or statuses[i] == "aborted" or statuses[i] == "cancelled":
        print(f"first job failed: {jobs[i]} and its status is {statuses[i]}\n")
        break


success_count =0
for i in range(len(jobs)):
    if statuses[i] == "completed":
        success_count =success_count +1
#print(f"total success jobs: {success_count}\n")

warning_count =0
for i in range(len(jobs)):
    if statuses[i] == "warning":
        warning_count =warning_count +1

#print(f"total warning jobs: {warning_count}\n")

print(f"extension task")
print(f"{len(jobs)} jobs: {success_count} success, {failed_count} failed, {warning_count} warning\n")



