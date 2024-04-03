import speeches
from note import Note
import time
import re
class NotesManager():
    def __init__(self, path: str="notes.txt", name: str="notes"):
        self.path=path
        self.name=name
    r_name=r'{name:'
    r_text=r'text:'
    r_date=r'time:'
    r_end=r'}'
    store=[]


    def store_file(self):
        file= open(self.path, "r",encoding = "utf-8")
        t_name=""
        t_text=""
        t_date=""
        for line in file:
            if re.match(self.r_name, line):
                t_name=line.lstrip(self.r_name)
            
            elif re.match(self.r_text,line):
                t_text=line.lstrip(self.r_text)
                line=file.__next__()
                while not re.match(self.r_date,line):
                    t_text+=line
                    line=file.__next__()
                    print(line)
                if re.match(self.r_date,line):
                    t_date=line.lstrip(self.r_date).removesuffix('\n')
                
            elif re.match(self.r_date,line):
                t_date=line.lstrip(self.r_date).removesuffix('\n')

            elif re.match(self.r_end,line):
                self.store.append(Note(t_name.strip(), float(t_date), t_text.strip()))
        
        self.filter()
        file.close()        
    
    def newNote(self):
        name=input(speeches.name_input)
        print(speeches.text_input)
        text="\n".join(iter(input,""))
        return Note(name,time.time(), text)


    def add(self, note: Note):
        with open(self.path, "a", encoding="utf-8") as file:
            file.write(f"{note}\n")
        

    def filter(self):
        self.store=sorted(self.store, key=Note.get_time_stamp)
        


    def find(self, name: str):
        res=[note for note in self.store if name in note.name]
        # for item in self.store:
        #     if item.name==name:
        #         res.append(item)
        # print(f"{res[0]}\n{res[1]}")
        return res

    
    
    def change(self, note: Note, name: str, text: str, time: int):
        note.name=name
        note.text=text
        note.time_stamp=time
        return note.name
    

    def delete(self, note: Note):
        self.store.remove(note)
        return note
    
    def update(self):
        self.filter()
        with open (self.path,"w",encoding="utf-8") as file:
            for note in self.store:
                if note:
                    file.write(f"{note}\n")
            