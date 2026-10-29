# Author : Archana Zhope
# Date : 27 October 2026
# Script : Callimg LLM model Ollama - system keyword use
# what a system prompt does - System prompt restrict the model behaviour to think as per role and answer as per instruction
# which role followed its instruction and which drifted : analyst role followed the instruction and support engineer role drifted and asked the business user to investigate as well as reviewer is asking to check the open transaction and locks although heading already mentioned lock detected 
# what the strict prompt achieved, with the 4 out of 5 number : The strict prompt restricted the model behaviour from assuming the answer,
#                                                               incase it did not find the correct answer. 
#                                                               Instead of giving the false result, using the strict prompt we can amend the response as "ANSWER NOT FOUND"
#           4 out 5 scenerio : model provided incorrect output as it was comparing output with space after full stop
#                               run 3 did not match: 'NOT IN LOG.'
#           5 out 5 scenerio : model provided correct result as we fix the issue by removing extra space before and after full stop and converted the text in uppercase to avoid case sensitivity issue.
#                               response_variable..strip().rstrip(".").upper()
# one thing the model got wrong or invented in these tests : Analyst role provided a sql query however in log database name was not mention.


import requests

def ask(prompt,system=""):
    
    payload ={
                "model": "llama3.2:3b",
                "prompt": prompt,
                "stream": False,
                "options": {"num_ctx": 8192},
                "system":system
            }

    try:
        response = requests.post("http://localhost:11434/api/generate", json=payload , timeout=300)
        if response.status_code == 200:
            data= response.json()
            
            return {
                    "answer": data["response"],
                    "prompt_tokens": data["prompt_eval_count"],
                    "answer_tokens" : data["eval_count"],
                    "seconds": round(data["total_duration"]/1000000000,2)
            }
        else: 
              return {
                    "answer": None,
                    "prompt_tokens": None,
                    "answer_tokens" : None,
                    "seconds": None
            }
    except requests.exceptions.RequestException as e:
             print("Request Failed:", e)
    return {
                             "answer": None,
                             "prompt_tokens": None,
                             "answer_tokens" : None,
                             "seconds": None
                     }



print("calling model...")

strict = "Answer only from the log text provided. If the answer is not in the text, reply exactly: NOT IN LOG."
log_line = "2027-01-16 03:41:45 ERROR DS_EXTRACT_CUSTOMER_MASTER Deadlock detected on table TXN_DAILY"

unanswerable = "Which user's query caused this deadlock? Log line: " + log_line
answerable = "Which table was involved? Log line: " + log_line

hits = 0
for i in range(5):
    answer = ask(unanswerable, system=strict)["answer"]
    if answer is not None and answer.strip().rstrip(".").upper() == "NOT IN LOG":
        hits += 1
        print("answerable:", ask(answerable, system=strict)["answer"])
    else:
        print("run", i + 1, "did not match:", repr(answer))
print("unanswerable: exact NOT IN LOG", hits, "out of 5")