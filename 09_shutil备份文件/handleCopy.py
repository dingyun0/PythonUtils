import os
import shutil
from datetime import datetime

def backup_files(source_dir, backup_dir):
    """
    备份文件夹中的文件
    source_dir: 源文件夹路径
    backup_dir: 备份文件夹路径
    """
    try:
        # 获取当前日期作为备份文件夹名
        today = datetime.now().strftime("%Y-%m-%d")
        backup_path = os.path.join(backup_dir, today)
        
        # 如果备份目录不存在，创建它
        if not os.path.exists(backup_path):
            os.makedirs(backup_path)
            
        # 遍历源文件夹
        for root, dirs, files in os.walk(source_dir):
            for file in files:
                source_file = os.path.join(root, file)
                # 计算目标路径
                rel_path = os.path.relpath(root, source_dir)
                target_dir = os.path.join(backup_path, rel_path)
                
                # 确保目标目录存在
                if not os.path.exists(target_dir):
                    os.makedirs(target_dir)
                    
                # 复制文件
                target_file = os.path.join(target_dir, file)
                shutil.copy2(source_file, target_file)
                print(f"已备份: {source_file} -> {target_file}")
                
        print(f"\n备份完成！文件已保存到: {backup_path}")
        
    except Exception as e:
        print(f"备份过程中出错: {str(e)}")

if __name__ == "__main__":
    # 设置源文件夹和备份文件夹路径
    source_directory = "a"  # 源文件夹
    backup_directory = "b"  # 备份文件夹
    
    # 执行备份
    backup_files(source_directory, backup_directory)

