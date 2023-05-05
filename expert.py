#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 30 18:06:31 2022

@author: kurup
"""

from abc import ABC,abstractmethod
#import markov




class EXP(ABC):
    
    @abstractmethod
    def get_sugg(self):
        pass

    @abstractmethod
    def new_input(self,y_i):
        pass
    
    @abstractmethod
    def another_one(self):
        pass
    
class EXP_1(EXP):
    def __init__(self):
        self.sugg_i=0
        self.error_count=0
        self.error=[]
    def get_sugg(self):
        return self.sugg_i
    
    def new_input(self,y_i,i):
        if self.sugg_i!=y_i:
            self.error_count+=1
        self.error.append([i,self.error_count])
        return
    
    def another_one(self):
        return
        
class EXP_2(EXP):
    def __init__(self):
        self.sugg_i=1
        self.error_count=0
        self.error=[]
    def get_sugg(self):
        return self.sugg_i
    
    def new_input(self,y_i,i):
        if self.sugg_i!=y_i:
            self.error_count+=1
        self.error.append([i,self.error_count])
        return
    
    def another_one(self):
        return
    
    
        
class EXP_3(EXP):
    def __init__(self):
        self.sugg_i=1
        self.error_count=0
        self.error=[]
        self.count_1=0
        self.count_0=0
    def get_sugg(self):
        if self.count_0>self.count_1:
            self.sugg_i=0
            return 0
        else:
            self.sugg_i=1
            return 1
    
    def new_input(self,y_i,i):
        if y_i==1:
            self.count_1+=1
        elif y_i==0:
            self.count_0+=1
            
        if self.sugg_i!=y_i:
            self.error_count+=1
        self.error.append([i,self.error_count])
    
    def another_one(self):
        self.sugg_i=1
        self.error_count=0
        self.error=[]
        self.count_1=0
        self.count_0=0

class EXP_4(EXP):
    def __init__(self):
        self.sugg_i=1
        self.error_count=0
        self.error=[]
        self.last_10=[]
    def get_sugg(self):
        if self.last_10.count(0)>self.last_10.count(1):
            self.sugg_i=0
            return 0
        else:
            self.sugg_i=1
            return 1
    
    def new_input(self,y_i,i):
        if len(self.last_10)>=10:
            self.last_10.pop()
        self.last_10.insert(0, y_i)
            
        if self.sugg_i!=y_i:
            self.error_count+=1
        self.error.append([i,self.error_count])
    
    def another_one(self):
        self.sugg_i=1
        self.error_count=0
        self.error=[]
        self.last_10=[]