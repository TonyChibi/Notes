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
    name=input(speeches.name_input+"\n>\t")
    return name

def not_found():
    print(speeches.not_found)

def text_input():
    print(speeches.text_input)
    text="\n".join(iter(input,""))
    return text

def seek(option:str):
    answer=input(speeches.seek(option)+"\n>\t")
    return answer

def show_names( *notes: Note):
    print()
    for i, item in enumerate(notes):
        if item:
            print(f"{i+1})\t{item.name}")

def show_text( *notes: Note):
    for i, item in enumerate(notes):
        if item:
            print(f"{i+1})\t{item.name}{item.text}")
    

def approvement(name: str, option: str):
    answer=input(speeches.approvement(name,option)+"\n>\t").lower()
    if answer == "yes" or answer=="y":
        return True
    else:
        return False


def choose_number( number):
    state=True
    choise=""
    while state:
        choise=input(speeches.choise+"\n"+speeches.exit+"\n>\t")
        if choise.isdigit() and 0<int(choise)<=number:
            state=False
        elif choise.lower()=="stop":
            return "0"
    return choise