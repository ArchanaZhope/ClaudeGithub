# Author : Archana Zhope
# Date : 27 October 2026
# Script : learning how LLM model choose the randomness of next token based on probability and how it can be varied using temp option.
#          learning how the randomness of predicting next token can be fix using seed option. 
# Temperature : Using temperature option LLM model can predict the next token as per probability percentage.
#               where 0 is lowest temp setting to choose the next probable token with most likely probability. 
# seed: seed will provide same result for same question everytime the question is asked, it restrict the random choices of words.

#What did temperature 0 give, and what did 1.5 give, in terms of “different answers out of 5”?
#   with temp=0 it gave the same answer every time, because it always picks the most likely next token.
#   with temp=1.5 and no seed it gave 5 different answers out of 5, because high
#   temperature lets the model pick less likely words. With seed 42 it gave 1 out of 5,
#   because the seed fixes the random choices. Good for brainstorming, not for tools. 

#   Neither setting guarantees a correct answer: temp 0 only makes the answer repeatable.

#What did fixing the seed change?
# seed fix the choosing the randomness of next token irrespective how many times same question  has been asked.

# Which settings would you use for a tool that other code reads (such as a log classifier that outputs JSON), and why? 
# Say which one you’d pick for temperature and whether you’d also set a seed.
# i will set temp=0 as its reading log and classifying. classifying means it should be put in some particular category for that it needs to provide same result.
# I will be using seed as i want fix result with same randomness to generate log category. 



import requests

def ask(prompt,system="", temperature=0.8):
    
    payload ={
                "model": "llama3.2:3b",
                "prompt": prompt,
                "stream": False,
                "options": {"num_ctx": 8192, "temperature":temperature,"seed":42}, 
                "system":system
            }
# Note: ask() always sends seed 42, so even a high temperature repeats its answer.
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


question = "Name one common cause of a database deadlock, in one sentence."
print("calling model...")
for temp in [1.5]:
     answers =[] # initializing empty list with answer
     for _ in range(5):  # _ used when counter is not required without the use of actual counter value , range(5) start from 0...4
          answers.append(ask(question,temperature=temp)["answer"].strip())  # strip-remove stray spaces and newline , answers.append - will append the answer in the dict
     print("temperature", temp , "->" , len(set(answers)) , "different answer out of 5" ) #set(answers) - removes duplicates answer, and len will count the unique answer counts.
     for a in answers:
          print("  ", a)
