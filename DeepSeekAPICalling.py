import requests  # 导入requests库，用于发送HTTP请求
import json  # 导入json库，用于处理JSON数据
api_key = 'sk-9052aa7aa92f48089b15fd204ffb0279'  # 设置API密钥
url = "https://api.deepseek.com/chat/completions"  # 设置DeepSeek API的端点URL
msg = [{"content":"You are a helpful assistant","role":"system"},{"content":"宋朝延续多少年","role":"user"}]  # 定义对话消息列表
payload = json.dumps({  # 构建API请求的负载数据
  "messages": msg,  # 设置消息内容
  "model": "deepseek-chat",  # 指定使用的模型
  "stream": True,  # 启用流式输出
  "max_tokens": 100,  # 设置最大生成token数
})
headers = {  # 设置HTTP请求头
  'Content-Type': 'application/json',  # 指定内容类型为JSON
  'Accept': 'application/json',  # 指定接受的响应类型为JSON
  "Authorization": f"Bearer {api_key}"  # 设置认证信息
}
# 逐块处理响应
try:  # 开始异常处理
    response = requests.request("POST", url, headers=headers, data=payload, stream=True)  # 发送POST请求并获取响应
    response.raise_for_status()  # 检查HTTP响应状态
    for chunk in response.iter_lines():  # 逐行读取流式响应
        if chunk:  # 如果chunk不为空
            decoded_chunk = chunk.decode('utf-8').strip()  # 解码字节流为字符串并去除空白
            if decoded_chunk.startswith("data: "):  # 检查是否是数据行
                try:  # 开始JSON解析异常处理
                    data_str = decoded_chunk[6:]  # 提取JSON数据部分
                    if data_str == "[DONE]":  # 检查是否接收完成
                        break  # 如果完成则退出循环
                    json_data = json.loads(data_str)  # 解析JSON数据
                    if json_data.get("choices"):  # 检查是否包含选择项
                        content = json_data["choices"][0].get("delta", {}).get("content", "")  # 获取生成的内容
                        print(content, end="", flush=True)  # 打印内容，不换行并立即刷新输出
                except json.JSONDecodeError:  # 捕获JSON解析错误
                    continue  # 继续处理下一个数据块
except requests.exceptions.RequestException as e:  # 捕获请求异常
    print(f"\n请求失败: {e}")  # 打印错误信息
