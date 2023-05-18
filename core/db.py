from tinydb import TinyDB,Query
from tinydb.table import Document
db=TinyDB("core/db.json",indent=4)

class DB:
    
    def __init__(self):
        self.user=db.table("Users")
        self.question=db.table("Text_to_image")
        self.image=db.table("Image url")

    def add_user(self,chat_id: int,username: str, full_name: str,longue_code: str="uz"):
        
        if self.user.contains(doc_id=chat_id):
            
            return True
    
        else:  
            
            self.user.insert(Document({"Full_name":full_name,"Username":username,"cn_code":longue_code},doc_id=chat_id))
            
            return False
  
    def add_task(self,chat_id,full_name: str,task: str):
        
        if self.question.contains(doc_id=chat_id):
            
            from pprint import pprint
            pprint(self.question.get(doc_id=chat_id))
            
            update: list=self.question.get(doc_id=chat_id)["Question"]
            update.append(task)
            
            self.question.update({"Question":update},doc_ids=[chat_id])
            
        else:
        
            self.question.insert(Document({"Full_name":full_name,"Question":[task]},doc_id=chat_id))
            
            
        
        
    def add_image(self,chat_id:str,image_url: list):
        if self.image.contains(doc_id=chat_id):
            
            update: list=self.image.get(doc_id=chat_id)["Images"]
            update.append(image_url)
            self.image.update({"Images":update},doc_ids=[chat_id])            
        else:
            self.image.insert(Document({"Images":[image_url]},doc_id=chat_id))
        
    def get_code(self,chat_id: int):
        
        return self.user.get(doc_id=chat_id)["cn_code"]
        
    