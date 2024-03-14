import requests

def request_test(url,payload):
    success = False;
    try:
        response = requests.get(url)
        # 检查响应状态码是否为 200，表示请求成功
        if response.status_code == 200:
            print(f"The URL '{url}' is valid and accessible.");
            success = True;
        else:
            print(f"Warning: The URL '{url}' returned a status code of {response.status_code}.");
            success = False;
    except requests.exceptions.RequestException as e:
        print(f"Error: Failed to connect to the URL '{url}'. Exception: {e}")
    return { 'success':success, 'payload':payload }
