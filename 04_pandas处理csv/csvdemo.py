import pandas as pd


def analyze_csv(file_path):
    data=pd.read_csv(file_path)
    print("数据概况",data.describe())
    print("\n每列的统计值：")
    for colum in data.columns:
        col_data=data[colum]
        print(f"{colum}:")
        print(f"最小值：{col_data.min()}")
        print(f"最大值：{col_data.max()}")
        print(f"均值：{col_data.mean()}")
        print(f"标准差：{col_data.std()}")

file_path="csvfile.csv"
analyze_csv(file_path)
