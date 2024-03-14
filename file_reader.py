import os
import json
from utils import get_files_info

def read_files(folder_path, encoding='utf-8', extension = '.json'):
    # 存储所有 JSON 文件的内容
    json_data = []
    files_info = get_files_info(folder_path)
    # 遍历文件夹下的所有文件
    for info in files_info:
        file_name = info['file_name']
        file_path = info['file_path'] 
        # 如果是 JSON 文件，则读取内容
        if file_name.endswith(extension):
            with open(file_path, 'r', -1, encoding) as f:
                try:
                    data = json.load(f)
                    json_data.append({'info': info, 'data': data})
                except json.JSONDecodeError as e:
                    print(f"Error decoding JSON file '{file_name}': {e}")
    
    return json_data
