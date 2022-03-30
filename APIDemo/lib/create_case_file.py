import os
from setting import *

def create_case():
    #初始化路径
    fileList = os.listdir(DATA_PATH)
    temp_file = os.path.join(BASE_PATH, 'templates.txt')

    for f in fileList:
        #判断是否yaml文件
        if f.endswith(".yaml") or f.endswith(".yml"):
            print("Yaml 文件：", f)
            file_name = f.replace(".yaml", '').replace(".yml", '')
            methods_name = file_name.lower()
            class_name = methods_name.capitalize()
            print(file_name, methods_name, class_name)
            #读取模板文件内容，并替换里面的变量
            with open(temp_file, 'r', encoding='utf-8') as temp:
                content = temp.read() % {
                    "class_name": class_name,
                    "methods_name": methods_name,
                    "file_name": file_name
                }
            #替换后的内容，生成并写入到用例
            case_file = os.path.join(CASE_PATH, "test_%s.py" % file_name)
            with open(case_file, "w", encoding='utf-8') as wfile:
                wfile.write(content)


