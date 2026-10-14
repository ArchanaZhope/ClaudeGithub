# Author : Archana Zhope
# Date : 12 October 2026
# Script : function example

jobs = [
    {"name": "DS_EXTRACT_CUSTOMER_MASTER", "status": "SUCCESS", "minutes": 10},
    {"name": "DS_EXTRACT_ACCOUNT_BALANCE", "status": "SUCCESS", "minutes": 15},
    {"name": "DS_TRANSFORM_TXN_DAILY", "status": "WARNING", "minutes": 20},
    {"name": "DS_LOAD_DWH_CUSTOMER", "status": "SUCCESS", "minutes": 90},
    {"name": "DS_LOAD_DWH_TXN", "status": "FAILED", "minutes": 30},
    {"name": "CTM_FILE_WATCHER_SWIFT_IN", "status": "FAILED", "minutes": 35},
    {"name": "CTM_FTP_REGULATORY_RPT", "status": "FAILED", "minutes": 40},
    {"name": "SQL_RECON_GL_BALANCE", "status": "ABORTED", "minutes": 45},
    {"name": "SH_ARCHIVE_PROCESSED_FILES", "status": "FAILED", "minutes": 50},
    {"name": "SH_PURGE_TEMP_TABLES", "status": "WARNING", "minutes": 55},
]

FAILED_STATUSES = ["FAILED"]
def is_failed(job1):
      if job1.get('status') in FAILED_STATUSES: 
            return True 
      else: 
            return False


def find_job(jobs_list, job_name):
    for job in jobs_list:
        if job.get('name').lower() == job_name.lower():
            return job

def summarize(jobs):
  total_count = 0
  success_count = 0
  warning_count = 0
  failed_count = 0

  for job in jobs:
            if job.get('status') == 'SUCCESS':
                success_count +=1 
                total_count +=1
            elif job.get('status') == 'WARNING':
                warning_count +=1
                total_count +=1
            elif is_failed(job):
                failed_count +=1
                total_count +=1

  return  {
   "total": total_count , 
   "success": success_count,
   "failed" : failed_count,
   "warning" : warning_count
          }

def slowest_job(jobs):
     slowest  = None
     for job in jobs:
          if slowest is None or job.get('minutes') > slowest.get('minutes'):
               slowest =job 
     return slowest


def display_job(job):
    if job is None:
        print("Job not found")
    else:
        print(
            f"Job {job.get('name')} found with status "
            f"{job.get('status')} and took "
            f"{job.get('minutes')} minutes to finish"
        )


job =find_job(jobs, "sql_recon_gl_balance")
display_job(job)

job =find_job(jobs, "DS_FAKE_JOB")
display_job(job)

job =find_job(jobs, "DS_EXTRACT_CUSTOMER_MASTER")
display_job(job)

slowest = slowest_job(jobs)
print(f"slowest job is {slowest.get('name')} with duration {slowest.get('minutes')}\n \n")

summary = summarize(jobs)
print(f"{summary}\n\n")
        
for job in (jobs[4], jobs[7], jobs[0]):
    print(f"Job {job['name']} has {job['status']} status: {is_failed(job)}")