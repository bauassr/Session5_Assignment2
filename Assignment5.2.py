# -*- coding: utf-8 -*-
"""
Created on Fri Mar 30 12:08:50 2018

@author: singh.shivam
"""
Subjects =["Americans","Indians"]
Verbs=["Play","Watch"]
Objects=["Baseball","Cricket"]
class Sentence:
    def __init__(self,Sub,Veb,Obj):
        self.__Sub=Sub
        self.__Veb=Veb
        self.__Obj=Obj
     
    def __str__(self):
        return "%s %s %s." \
               %(self.__Sub,self.__Veb,self.__Obj)
    

def Make_sentance(Sub,Veb,ob):
    for s in Sub:
        for v in Veb:
            for o in ob :
                Sen= Sentence(s,v,o)
                print(Sen)
 
Make_sentance(Subjects,Verbs,Objects)   

    
    
    
    
    
