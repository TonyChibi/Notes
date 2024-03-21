import speeches
from note import Note
import time

def greeting():
    print(speeches.greeting)
    for i in speeches.menu:
        print('\t'+i)
    answer=input().lower()
    return answer

def create():
    name=input(speeches.name_input)
    print(speeches.text_input)
    text="\n".join(iter(input,""))
    return Note(name,time.time(), text)