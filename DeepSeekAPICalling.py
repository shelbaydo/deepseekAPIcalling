import requests
import json
api_key = 'sk-9052aa7aa92f48089b15fd204ffb0279'
url = "https://api.deepseek.com/chat/completions"
msg = [{"content":"You are a helpful assistant","role":"system"},{"content":"你好，今天星期几","role":"user"}]
payload = json.dumps({
  "messages": msg,
  "model": "deepseek-chat",
})
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  "Authorization": f"Bearer {api_key}"
}
response = requests.request("POST", url, headers=headers, data=payload)
print(response.text)
