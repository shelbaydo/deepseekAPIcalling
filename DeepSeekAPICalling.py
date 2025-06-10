import requests
import json
api_key = 'sk-9052aa7aa92f48089b15fd204ffb0279'
url = "https://api.deepseek.com/chat/completions"
msg = [{"content":"You are a helpful assistant","role":"system"},{"content":"宋朝延续多少年,输出不超过50字","role":"user"}]
payload = json.dumps({
  "messages": msg,
  "model": "deepseek-chat",
  "stream": True,  # 启用流式输出
  "max_tokens": 60,
})
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  "Authorization": f"Bearer {api_key}"
}
# 逐块处理响应
try:
    response = requests.request("POST", url, headers=headers, data=payload, stream=True)
    response.raise_for_status()  # 检查 HTTP 错误
    for chunk in response.iter_lines(): #逐行读取流式响应
        if chunk:
            decoded_chunk = chunk.decode('utf-8').strip()  # 解码字节流为字符串
            print(decoded_chunk) 
except requests.exceptions.RequestException as e:
    print(f"\n请求失败: {e}")
