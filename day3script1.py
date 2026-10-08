# Author: Archana Zhope
# Date : 8 October 2026
# Script : List example

jobs = ["alert monitoring",
        "pre check job before patching","post check job after patching",
        "BCP/DR" ,
        "post-deployment sanity job",
        "data loader","data transformer", "extract generation"]

status = ["completed","completed with warning","failed",
          "in progress","not started",
          "retrying","aborted","cancelled"]

print(f"first job: {jobs[0]} \nlast job: {jobs[-1]} \ncount of jobs: {len(jobs)}\n")
print(f"first three jobs, slice example: {jobs[0:3]}")

jobs.append("pre-deployment sanity job")
status.append("completed with error")


print(f"\nupdated count of jobs: {len(jobs)}")
print(f"updated count of status: {len(status)}")

print(f"\n'{jobs[2]}' has status: {status[2]}\n\n")
print(jobs[9])