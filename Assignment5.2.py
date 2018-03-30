# -*- coding: utf-8 -*-
"""
Created on Fri Mar 30 12:08:50 2018

@author: singh.shivam
"""
Subjects =["Americans","Indians"]
Verbs=["Play","Watch"]
Objects=["Baseball","Cricket"]

def Make_sentance(Sub,Veb,ob):
    for s in Sub:
        for v in Veb:
            for o in ob :
                print(s,v,o)
                
 
Make_sentance(Subjects,Verbs,Objects)   

    
    
    
    