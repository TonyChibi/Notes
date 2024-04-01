import time
class Note:
    def __init__(self,name: str, time_stamp: float, text: str):
        self.name=name
        self.time_stamp=time_stamp
        self.text=text 
    def __str__(self):
        return "{name:"+self.name+"\ntext:"+self.text+"\ntime:"+str(self.time_stamp)+"\n}"
    
    def get_time_stamp(self):
        return self.time_stamp
    # def getName(self):
    #     return self.name
    def get_date(self):
        return time.ctime(self.time_stamp)
      
   
