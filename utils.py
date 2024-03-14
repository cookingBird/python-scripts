import os

def get_files_info(folder_path):
    files_info = []
    
    # 遍历文件夹中的所有文件和子文件夹
    for root, dirs, files in os.walk(folder_path):
        for file_name in files:
            # 获取文件的完整路径
            file_path = os.path.join(root, file_name)
            # 分割文件名和扩展名
            base_name, file_extension = os.path.splitext(file_name)
            # 将文件信息添加到列表中
            files_info.append({
                'file_name': file_name,
                'file_path': file_path,
                'base_name': base_name,
                'file_extension': file_extension[1:]  # 去除扩展名前面的点号
            })
    
    return files_info