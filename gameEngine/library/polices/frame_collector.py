import os
from shutil import *

def copy_police(target:str, name:str="pixels"):
    try:
        folder = "/home/gator/dev/python/gameEngine/library/polices/"+name+"/"
        files = os.listdir(folder)

        i=0
        for file in files:
            copy(folder+file, target)
            i+=1

    except Exception as e:
        return e, i
    else:
        return "Success !"