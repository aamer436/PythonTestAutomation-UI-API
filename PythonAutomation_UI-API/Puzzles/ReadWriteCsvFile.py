import csv
import os
from _csv import reader
from pathlib import Path

result=[]
print(Path(__file__).resolve().parent.parent)
project_root=Path(__file__).resolve().parent.parent ### write parent as many times as you need to reach the project root
with open(str(project_root)+"/resources/CsvFile.csv",mode='r',encoding='utf-8') as f:
    reader=csv.reader(f)
    header=next(reader)
    print('Header -',header)
    for i in reader:
        print(i)

header = ['Name', 'Age', 'City']
rows = [
    ['Alice', 30, 'New York'],
    ['Bob', 25, 'Los Angeles'],
    ['Charlie', 35, 'Chicago']
]
with open(str(project_root)+"/output/New_CsvFile.csv",mode='w',newline="",encoding='utf-8') as f:
    writer=csv.writer(f)
    writer.writerow(header)
    writer.writerows(rows)

with open(str(project_root)+"/output/New_CsvFile.csv",mode='a',newline="",encoding='utf-8') as f:
    writer=csv.writer(f)
    writer.writerow(['A','B','C'])




