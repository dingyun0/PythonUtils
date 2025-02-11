import json
import os

file_path="example_file.txt"

if os.path.exists(file_path):
    os.remove(file_path)

def write_to_file():
    with open(file_path,"w")as file:
        file.write("hello,this is a sample text file.\n")
        file.write("this is a second line.\n")
    print("file written successfully")

def append_to_file():
    with open(file_path,"a") as file:
        file.write("this is a third line.\n")
    print("file appended successfully")

def read_entire_file():
    with open(file_path,"r") as file:
        content=file.read()
        print("entire file content:")
        print(content)

def read_file_line_by_line():
    with open(file_path,"r") as file:
        for line in file:
            print(line.strip())



json_file_path="data.json"

def write_json_file():
    data={
        "name":"alice",
        "age":25,
        "city":"new york"
    }
    with open(json_file_path,"w")as json_file:
        json.dump(data,json_file,indent=4)
    print("json file written successfully")

def read_json_file():
    with open(json_file_path,"r") as json_file:
        data=json.load(json_file)
        print("json file content:")
        print(data)

def move_file_pointer():
    with open(file_path,"r")as file:
        print(file.readline())
        file.seek(0)
        print(file.readline())
def hendle_file_error():
    try:
        with open("not_existent_file.txt","r")as file:
            content=file.read()
    except FileNotFoundError:
        print("error")
    except Exception as e:
        print(e)

if __name__ == "__main__":
    write_to_file()

    # 追加内容
    append_to_file()

    # 读取整个文件内容
    read_entire_file()

    # 逐行读取文件
    read_file_line_by_line()

    # 写入 JSON 文件
    write_json_file()

    # 读取 JSON 文件
    read_json_file()

    # 操作文件指针
    move_file_pointer()


    # 异常处理
    hendle_file_error()
