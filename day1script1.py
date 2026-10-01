# Author: Archana Zhope
# Date: 01-10-2026
# script details: Script created to print variables value on standard output

job_name = "DS_LOAD_CUSTOMER"
status = "FAILED"
duration = 12.5
retries = 3

print(f"Job {job_name} has {status} after {duration * 60:.2f} seconds ( {retries} retries ).")
print(type(job_name))
print(type(status))
print(type(duration))
print(type(retries))
