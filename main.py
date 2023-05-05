#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 30 22:22:37 2022

@author: kurup
"""
import expert
import markov
from random import choice as choose_one
import matplotlib.pyplot as plt
import numpy as np

def get_y_w(weights,outputs,y_i,eps):
    w_1=0
    w_0=0
    for i in range(4):
        if outputs[i]==0:
            w_0+=weights[i]
            if y_i==1:
                weights[i]=weights[i]*(1-eps)
        elif outputs[i]==1:
            w_1+=weights[i]
            if y_i==0:
                weights[i]=weights[i]*(1-eps)
    if w_1  >  w_0:
        return weights,1
    else:
        return weights,0


def run_once(chain,experts,eps,T):
    weights=[1,1,1,1]
    error=[]
    error_count=0
    for ite in range(T):
        y_i=chain.get_sample()
        outputs=[]
        for exp_temp in experts:
            outputs.append(exp_temp.get_sugg())
            exp_temp.new_input(y_i, ite)
        weights,pred_y=get_y_w(weights,outputs,y_i,eps)
        chain.next_ite()
        if y_i!=pred_y:
            error_count+=1
        error.append([ite,error_count])
    ret=[]
    for exp_temp in experts:
        ret.append(exp_temp.error)
    ret.append(error)
    print(weights)
    return ret
    
    
        
def get_print_errors(cost_list):
    color_plot={1:'g',
                2:'b',
                3:'r',
                4:'c',
                5:'k',
                }
    i=1
    ret=[]
    for cost in cost_list:
        temp=np.array(cost).T
        
        if i<5:
            label_text="Expert "+str(i)
        else:
            label_text="Algorithm"
        ret.append([temp[0],temp[1],color_plot[i],label_text])
        i+=1
    return ret
    
    
        
    
def display_res(disp_list):
    fig, ax = plt.subplots(2,2)
    fig.set_size_inches(10,10)

    plt.setp(ax,yticks=np.linspace(0,600,13))
    ite=0
    for i in range(2):
        for j in range(2):
            ret=get_print_errors(disp_list[ite])
            ite+=1
            ax[i,j].set(xlabel="T", ylabel="# mistakes")
            
        
            for k in ret:
                ax[i,j].plot(k[0],k[1],color=k[2],label=k[3])

            ax[i,j].text(3, 400, f'Iteration: {ite}')    
    handles, labels = ax[0,0].get_legend_handles_labels()
    fig.legend(handles, labels, loc='upper center')        
    plt.show()
    
            
def main():
    
    disp_list=[]
    for i in range(4):
        T=1000
        chain=markov.CHAIN([0.8,0.2], choose_one([0.2,0.8]))
        exp1=expert.EXP_1()
        exp2=expert.EXP_2()
        exp3=expert.EXP_3()
        exp4=expert.EXP_4()
        experts_list=[exp1,exp2,exp3,exp4]
        
        disp_list.append(run_once(chain, experts_list, 0.1, T))
        
        del exp1
        del exp2
        del exp3
        del exp4
        del chain
    display_res(disp_list)
    
            
            
            
if __name__=="__main__":
    main()
