import speeches
from note import Note
import time

def greeting():
    print(speeches.greeting)

def menu():
    for i in speeches.menu:
        print('\t'+i)
    answer=input().lower()
    return answer


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