import os
import polices.frame_collector as fr_coll


def normalize(name:str):
    forbidden=["/", " " ,"\"", "'", "!", ":", ",", "*", "\\"]
    replaced={"é":"e","è":"e","à":"a","ç":"c","ù":"u","ï":"i","î":"i"}
    normalized=[]
    for l in name.lower():
        if l in forbidden:normalized.append("_")
        elif l in replaced.keys():normalized.append(replaced[l])
        else:normalized.append(l)
    return "".join(normalized)

def create_file(path, name, content=None):
    with open(path+"/"+name,"x") as f:
        if content:
            f.write(content)


name = input("Name of the game : ")
path = input("Path of th game ('.' if in current directory) : ")
author = input("Votre nom : ")
authoremail = input("Your e-mail : ")
gamelicense = input("License of that game : ")

name_normalized = normalize(name)
root = path.strip()+"/"+name_normalized




SETUP = """
setup = {
    "general informations": {
        "name": '"""+ name +"""',
        "path": '"""+ root +"""',
        "version": '0.0.0',
        "author": ['"""+ author +"""', """+ authoremail +"""],
        "license": '"""+ gamelicense +"""'
    },

    "your setups (example)": {
        "tick": 10,
        "step": 50
    }
}
"""


MAIN = """
from setup import *

class Game():
    def __init__(self, setup:dict):
        self.setup = setup
        self.game = True
    
    def mainloop(self, *args, **kwargs):
        '''Your looping function'''
        while self.game:
            self.main()
    
    def main(self):
        '''Your main looped function'''
        pass


if __name__=="__main__":
    game = Game(setup)
    game.mainloop()
"""



pwd=root

#* ROOT ORGANISATION
os.mkdir(pwd)
os.mkdir(pwd+"/elements")
os.mkdir(pwd+"/save_system")
create_file(pwd, "main.py", MAIN)
create_file(pwd, "setup.py",SETUP)

#* ELEMENTS ORGANISATION
pwd=root+"/elements"
os.mkdir(pwd+"/backgrounds")
os.mkdir(pwd+"/fields+tiles")
os.mkdir(pwd+"/sprites")
os.mkdir(pwd+"/texts")
os.mkdir(pwd+"/sounds")
os.mkdir(pwd+"/other")

#* BACKGROUNDS ORGANISATION
pwd=root+"/elements/backgrounds"
create_file(pwd, "background.py")

#* FIELDS & TILES ORGANISATION
pwd=root+"/elements/fields+tiles"
os.mkdir(pwd+"/fields")
os.mkdir(pwd+"/tiles")

#* FIELDS ORGANISATION
pwd=pwd+"/fields"
create_file(pwd, "fields.py")

#* TILES ORGANISATION
pwd=root+"/elements/fields+tiles/tiles"
create_file(pwd, "tiles.py")

#* SPRITES ORGANISATION
pwd=root+"/elements/sprites"
create_file(pwd, "sprites.py")
os.mkdir(pwd+"/objects")
os.mkdir(pwd+"/characters")
os.mkdir(pwd+"/other")

#* CHARACTERS ORGANISATION
pwd=pwd+"/characters"
create_file(pwd,"characters.py")
os.mkdir(pwd+"/0_main_character")

#* MAIN_CHARACTER EXEMPLE
pwd=pwd+"/0_main_character"
create_file(pwd,"main_character.py")
os.mkdir(pwd+"/textures")

#* OBJECTS ORGANISATION
pwd=root+"/elements/sprites/objects"
create_file(pwd,"objects.py")
os.mkdir(pwd+"/0_stone_rock")

#* OBJECT EXEMPLE
pwd=root+"/elements/sprites/objects/0_stone_rock"
create_file(pwd,"stone_rock.py")
os.mkdir(pwd+"/textures")

#* TEXTS ORGANISATION
pwd=root+"/elements/texts"
create_file(pwd,"polices.py")
os.mkdir(pwd+"/0_style_pixels")

#* POLICE EXEMPLE
pwd=pwd+"/0_style_pixels"
create_file(pwd,"pixels.py")
os.mkdir(pwd+"/chars")

#* COPY DEFAULT POLICE
pwd=pwd+"/chars"
fr_coll.copy_police(pwd, "pixels")

#* SAVE SYSTEM ORGANISATION
pwd=root+"/save_system"
create_file(pwd,"save.py")
