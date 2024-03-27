import speeches
from note import Note
import time

def assistant():
    message=input(f"\n{speeches.assistant}\n> ").lower()
    return message

def greeting():
    print(speeches.greeting)

def menu():
    for i in speeches.menu:
        print('\t'+i)
   


def create():
    name=name_input()
    text=text_input()
    return Note(name,time.time(), text)

def name_input():
    name=input(speeches.name_input)
    return name

def text_input():
    print(speeches.text_input)
    text="\n".join(iter(input,""))
    return text

def seek(self, option:str="find"):
    answer=input(speeches.seek(option))
    return answer

def show_names(self, *notes: Note):
    for i, note in notes:
        print(f"{i})\t{note.name}")

def show_text(self, *notes: Note):
    for i, note in notes:
        print(f"{i})\t{note.text}")
    

def approvement(swlf, name: str, option: str):
    answer=input(speeches.approvement(name,option)).lower()
    if answer is "yes" or "y":
        return True
    else:
        return False


def choose_number(self, number):
    state=True
    choise=""
    while state:
        choise=input(speeches.choise+speeches.exit)
        if choise.isdigit() and 0<choise<number:
            state=False
        elif choise.lower()=="stop":
            return ""
    return choise