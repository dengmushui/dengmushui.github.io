

url = "https://api.tigerbot.com/bot-service/ai_service/gpt"

headers = {
  'Authorization': 'Bearer ' + API_KEY
}

payload = {
  "text": "中国的首都",
  "modelVersion": "tigerbot-7b-sft"
}

response = requests.post(url, headers=headers, json=payload)
print(response.text)