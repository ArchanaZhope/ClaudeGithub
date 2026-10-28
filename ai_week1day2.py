# Author : Archana Zhope
# Date : 27 October 2026
# Script : Callimg LLM model Ollama via function call



import requests

def ask(prompt):
    
    payload ={
                "model": "llama3.2:3b",
                "prompt": prompt,
                "stream": False,
                "options": {"num_ctx": 8192},
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
    except requests.exceptions.RequestException:
            return {
                             "answer": None,
                             "prompt_tokens": None,
                             "answer_tokens" : None,
                             "seconds": None
                     }

with open("logs/generated.log") as f:
    all_lines = f.readlines()

#for n in [10, 50, 200]:
#    text = "".join(all_lines[:n])
#    result = ask("Summarize these log lines in two sentences:\n" + text)
#    print(n, "lines:", result["prompt_tokens"], "prompt tokens,", result["seconds"], "seconds")


#print(ask("In one sentence, what is a cron job?"))

text = "".join(all_lines[:200])
prompt = "The secret code word is PINEAPPLE.\n" + text + "\nWhat is the secret code word? Answer with the word only."
result = ask(prompt)
print(result["prompt_tokens"], "prompt tokens")
print(result["answer"])