import os
from shutil import *

def copy_police(target:str, name:str="pixels"):
    try:
        i=0
        folder = "/".join(os.getcwd().split("\\")) + "/" + name +"/"
        files = os.listdir(folder)

        for file in files:
            copy(folder+file, target)
            i+=1

    except Exception as e:
        return e, i
    else:
        return "Success !"