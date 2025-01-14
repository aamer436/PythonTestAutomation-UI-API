import os
from pathlib import Path

result=[]
print(Path(__file__).resolve().parent.parent)
project_root=Path(__file__).resolve().parent.parent ### write parent as many times as you need to reach the project root
with open(str(project_root)+"/resources/TextFile.txt",mode='r',encoding='utf-8') as f:
    for i in f.readlines():
        print(i,end="")
        result.append(i)

with open(str(project_root)+"/output/MyFile.txt",mode='w',encoding='utf-8') as f:
    f.writelines(result)

with open(str(project_root)+"/output/MyFile.txt",mode='a',encoding='utf-8') as f:
    f.write("\n")
    f.write("New Line addition")