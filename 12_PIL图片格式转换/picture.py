from PIL import Image
import os

input_folder="./input"
output_folder="./output"
target_format="png"
os.makedirs(output_folder,exist_ok=True)
for i in os.listdir(input_folder):
    print(i)
    if i.lower().endswith(('jpg','jpeg','png','gif','bmp')):
        img_path=os.path.join(input_folder,i)
        img=Image.open(img_path)

        new_name=os.path.splitext(i)[0]+"."+target_format.lower()
        output_path=os.path.join(output_folder,new_name)
        img.save(output_path,format=target_format)
        print(f"已转换：{img_path} 为 {output_path}")
