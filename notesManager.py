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
                
                #     for line in file:
                #         t_text+=line

            elif re.match(self.r_date,line):
                t_date=line.lstrip(self.r_date).removesuffix('\n')

            elif re.match(self.r_end,line):
                self.store.append(Note(t_name, float(t_date), t_text))


        # for line in file:
        #     match line:
        #         case self.r_name:
        #             t_name=line.lstrip(self.r_name)
                
        #         case self.r_text:
        #             t_text=line.lstrip(self.r_text)
        #             while(line!=t_date):
        #                 for line in file:
        #                     t_text.join(line)

        #         case self.r_date:
        #             t_date=line.lstrip(self.r_date)

        #         case r'^}':
        #             self.store.push(Note(t_name,int(t_date),t_text))
        #             t_name=""
        #             t_text=""
        #             t_date=""
        file.close()        
    
    def newNote(self):
        name=input(speeches.name_input)
        print(speeches.text_input)
        text="\n".join(iter(input,""))
        return Note(name,time.time(), text)
   

    def add(self, note: Note):
        with open(self.path, "a", encoding="utf-8") as file:
            file.write(f"{note}\n")
        
       
    
    def all(self):
        for note in self.store:
            print (f"{note.name}")



    def find(self, name: str):
        res=[]
        for item in self.store:
            if item.name==name:
                res.append(item)
        return res
        # for i in res:
        #     print(f"{i.name}:\n\t{i.text[0,20]}")
    
    
    def change(self):
        return
    

    def delete(self):
        return