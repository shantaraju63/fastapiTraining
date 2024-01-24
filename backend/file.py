import os,stat
from pathlib import Path
parent="C:/Users/SGovindappa/Desktop/backend/src"
parent2="C:/Users/SGovindappa/Desktop/backend/responses"
if  os.access(parent,os.F_OK)==False:
    os.makedirs(parent)
if  os.access(parent2,os.F_OK)==False:
    os.makedirs(parent2)

f1=os.path.join(parent,"schema.py")
# Path(parent).joinpath('error.json')
# Path(parent).joinpath('relese_date.json')
# Path(parent).joinpath('main.py')

# file_name=Path(parent).joinpath('hek.py')
# pt="C:/Users/SGovindappa/Desktop/training"
# normalized_path = os.path.normpath(os.path.join(os.getcwd(), pt))
# print(normalized_path)

# os.chflags(parent,stat.UF_IMMUTABLE)
# print(os.chmod(parent,stat.S_ISUID))
# with open(file_name,"w") as file:
#     file.write("abc")
