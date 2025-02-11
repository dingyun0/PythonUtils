import os


folder_path="/projects/PythonUtils/"
dd=os.listdir(folder_path)

prefix=""

exclude_files=[".conda",".env","README.md"]

floders=[
    f for f in os.listdir(folder_path)
    if os.path.isdir(os.path.join(folder_path,f)) and not any(f.endswith(ext)for ext in exclude_files)
]
floders.sort(key=lambda f:os.path.getctime(os.path.join(folder_path,f)))
for index,foldername in enumerate(floders):
    new_name=f"{prefix}{index+1:02d}"
    old_path=os.path.join(folder_path,foldername)
    new_path=os.path.join(folder_path,new_name)
    os.rename(old_path,new_path)
    print(f"重命名文件{foldername}为{new_name}")
print("重命名完成")

