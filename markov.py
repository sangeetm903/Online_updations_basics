#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 30 17:22:52 2022

@author: kurup
"""
import numpy as np



class CHAIN:
    def __init__(self,states,current_state):
        self.current_state=current_state
        self.states=states.copy()
        
    def get_ber_sample(self,p):
        return np.random.binomial(1, p)
    
    def next_ite(self):
        choice=self.get_ber_sample(0.05)
        #print(f'{choice}:           {self.current_state} -> ')
        if choice==1:
            self.current_state=1-self.current_state
        #print(f'{self.current_state}\n')
        return(choice)
    def get_sample(self):
        return self.get_ber_sample(self.current_state)
    def get_state(self):
        return self.current_state
        
        