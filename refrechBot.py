import difflib
import json
from pickle import dump,load
def knowledgeBase(file:str):
    knowledgebase=open(file,"r")
    data:dict=json.load(knowledgebase)
    knowledgebase.close()
    return data

def get_answer(Dquestion:str,data:dict):
    for q in data["questions"]:
        if q["question"]==Dquestion:
            return q["answer"]
    
    
    
def FindBestMatch(dataQ:list,Uquestion:str):
    answer:list=difflib.get_close_matches(Uquestion,dataQ,1,cutoff=0.8)
    return answer[0] if answer else None 

def AddData(answer:str,question:str,data:dict,file):
    knowledgebase=open(file,"w")
    nanswer=dict()
    nanswer["question"]=question
    nanswer["answer"]=answer
    data["questions"].append(nanswer)
    json.dump(data,knowledgebase,indent=2)
    knowledgebase.close()


def bot():
    while True:
        file="test.json"
        data:dict=knowledgeBase(file)
        Uquestion=input("how can i help uu?  ")
        if(Uquestion.lower()=="quit"):
            break
            
        Dquestion=FindBestMatch([q["question"] for q in data["questions"]],Uquestion) 
        if not(Dquestion==None):
            answer=get_answer(Dquestion,data)
            print(answer)
        else:
            Uanswer=input("i dont know the answer can u teach me ")
            AddData(Uanswer,Uquestion,data,file)
            print("vraiment ya3tik saha !")
bot()      
 
    
    
