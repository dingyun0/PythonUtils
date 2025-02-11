import csv
filename="./csvfile.csv"
try:
    with open(filename,"r",encoding="utf-8")as file:
        reader=csv.DictReader(file)
        for row in reader:
            a=row["A"]
            b=row["B"]
            c=row["C"]
            print(f"A:{a},B:{b},C:{c}")
except FileNotFoundError:
    print(f"文件{filename}未找到")
except Exception as e:
    print(f"读取文件时发生错误：{e}")

