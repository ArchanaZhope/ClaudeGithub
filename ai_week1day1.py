import requests
payload ={
    "model": "llama3.2:3b",
    "prompt": "In one sentence, what is a cron job?",
    "stream": False,
}

response = requests.post("http://localhost:11434/api/generate", json=payload , timeout=120)
print(response.status_code)
data= response.json()
print(data["response"])
print(list(data.keys()))
print("prompt token:", data["prompt_eval_count"])
print("answer tokens", data["eval_count"])
print("total seconds:", round(data["total_duration"]/1000000000,2))
print((data["done_reason"]))
print((data["context"]))
print("total seconds:", round(data["load_duration"]/1000000000,2))
speed = data["eval_count"] / (data["eval_duration"] / 1_000_000_000)
print("tokens per second:", round(speed, 1))