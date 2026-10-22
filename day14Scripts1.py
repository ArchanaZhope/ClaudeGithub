    # Author : Archana Zhope
    # Date : 22 October 2026
    # Script : Mini project


import requests
import json
import time
services = [
        "https://jsonplaceholder.typicode.com/todos/1",
        "https://jsonplaceholder.typicode.com/users/1",
        "https://jsonplaceholder.typicode.com/todos/99999",
        "https://httpstat.us/500",
        "https://this-host-does-not-exist-12345.com",
    ]
print(len(services))

def check_service(url):
        start = time.time()
        try:
                response = requests.get(url, timeout=5)
                seconds = time.time() - start
                if response.status_code == 200:
                    status= "UP"
                else:
                    status = "DOWN"

                return {"url": url, "status": status,"code": response.status_code,  "seconds": round(seconds,2)}
        except requests.exceptions.RequestException:
                seconds = time.time() - start
                return {"url": url, "status": "DOWN","code": None,  "seconds": round(seconds,2)}
def check_with_retry(url):
        retry=1
        result = check_service(url)
        if result["code"] == None or result["code"] >=500:
            time.sleep(1)
            retry+=1
            result = check_service(url)
            result["attempts"] = retry
            return  result
        result["attempts"] = retry
        return result

print(f"{'status':<5}    {'code':<10}     {'seconds':<5}      {'url':<55}    retry  ")
print("-" * 110)
all_results=[]
for url in services :
    result = check_with_retry(url)
    all_results.append(result)
    note=""
    if result["attempts"] > 1:
        note = result["attempts"]
    print(f"{result["status"]:<5}    {str(result["code"]):<10}     {result["seconds"]:<5}      {result["url"]:<55}        {note}")

with open('api_response.json', "w") as f:
    json.dump(all_results, f, indent = 2)
    f.write("\n")
    print(f" api_response.json created")
        
        