import os
import json
TASK_FILE="tasks.json"

def load_tasks():
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE,"r",encoding="utf-8")as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    with open(TASK_FILE,"w",encoding="utf-8")as file:
        json.dump(tasks,file,indent=4)

def display_tasks(tasks):
    if not tasks:
        print("当前没有任务")
    else:
        for index,task in enumerate(tasks):
            status="完成" if task["completed"] else "未完成"
            print(f"{index+1}.{task['name']} - {status}")

def add_task(tasks,task_name):
    tasks.append({"name":task_name,"completed":False})
    save_tasks(tasks)
    print(f"任务 '{task_name}' 已添加")

def delete_task(tasks,task_index):
    print("1111",task_index)
    if 0<task_index<=len(tasks):
        removed_task=tasks.pop(task_index-1)
        save_tasks(tasks)
        print(f"任务 '{removed_task['name']}' 已删除")
    else:
        print("无效的任务编号")

def mark_completed(tasks,task_index):
    if 0<task_index<=len(tasks):
        tasks[task_index-1]["completed"]=True
        save_tasks(tasks)
        print(f"任务 '{tasks[task_index-1]['name']}' 已标记为完成")
    else:
        print("无效的任务编号")

def todoList():
    tasks=load_tasks()
    while True:
        print("欢迎使用待办事项列表")
        print("1.查看任务")
        print("2.添加任务")
        print("3.删除任务")
        print("4.标记任务为完成")
        print("5.退出")
        choice=input("请选择操作：1/2/3/4/5:")
        if choice=="1":
            display_tasks(tasks)
        elif choice=="2":
            task_name=input("请输入任务名称：")
            add_task(tasks,task_name)
        elif choice=="3":
            try:
                task_index=int(input("请输入要删除的任务编号："))
                delete_task(tasks,task_index)
            except ValueError:
                print("请输入有效的任务编号")
        elif choice=="4":
            display_tasks(tasks)
            try:
                task_index=int(input("请输入要标记为完成的任务编号："))
                mark_completed(tasks,task_index)
            except ValueError:
                print("请输入有效的任务编号")
        elif choice=="5":
            print("感谢使用，再见！")
            break
        else:
            print("无效的选择，请重新输入")

if __name__=="__main__":
    todoList()