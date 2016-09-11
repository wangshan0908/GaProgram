# -*- coding: UTF-8 -*-

"""
这是一个遗传算法实现的文件
用遗传算法求函数最大值：
f(x)=10*sin(5x)+7*cos(4x) x∈[0,10]
@author:wangshan
"""
import math
import random
import numpy as np
import matplotlib.pyplot as plt
def b2d(b):
    sum=0
    for j in range(len(b)):
        sum+=b[j]*math.pow(2,j)
    return sum*10/1023
#为保证精确到小数点10位数
def decodechrom(pop):
    temp=[]
    for i in range(len(pop)):
        t=0
        for j in range(10):
            t+=pop[i][j]*(math.pow(2,j))
        temp.append(t)
    return temp
def calobjvalue(pop):
    temp1=[]
    objvalue=[]
    temp1=decodechrom(pop)
    for i in range(len(temp1)):
        x=temp1[i]*10/1023
        objvalue.append(10*math.sin(5*x)+7*math.cos(4*x))
    return objvalue
def calfitvalue(objvalue):
    fitvalue=[]
    temp=0.0
    Cmin=0
    for i in range(len(objvalue)):
        if(objvalue[i]+Cmin>0):
            temp=Cmin +objvalue[i]
        else:
            temp=0.0
        fitvalue.append(temp)
    return fitvalue
def best(pop, fitvalue):
    px=len(pop)
    bestindividual=[]
    bestfit=fitvalue[0]
    for i in range(1,px):
        if (fitvalue[i]>bestfit):
            bestfit=fitvalue[i]
            bestindividual=pop[i]
    return [bestindividual,bestfit]
def cumsum(fitvalue):
    #ff=[0]*len(fitvalue)
    for i in range(len(fitvalue)):
        t=0
        j=0
        while (j<=i):
            t+=fitvalue[j]
            j+=1
        fitvalue[i]=t###################!!!!!
    #return ff
def selection(pop,fitvalue):
    newfitvalue=[]
    totalfit=sum(fitvalue)
    for i in range(len(fitvalue)):
        newfitvalue.append(fitvalue[i]/totalfit)
    cumsum(newfitvalue)
    ms=[]
    poplen=len(pop)
    for i in range(poplen):
        ms.append(random.random())
    ms.sort()
    fitin=0
    newin=0
    newpop=pop
    while newin<poplen:
        if(ms[newin]<newfitvalue[fitin]) :
            newpop[newin]=pop[fitin]
            newin+=1
        else:
            fitin+=1
    pop=newpop
def crossover(pop,pc):
    poplen =len(pop)
    for i in range(poplen-1):
        if(random.random()<pc):
            cpoint = random.randint(0,len(pop[0]))
            temp1=[]
            temp2=[]
            temp1.extend(pop[i][0:cpoint])
            temp1.extend(pop[i+1][cpoint:len(pop[i])])
            temp2.extend(pop[i][cpoint:len(pop[i])])
            temp2.extend(pop[i+1][0:cpoint])
            pop[i]=temp1
            pop[i+1]=temp2
def mutation(pop,pm):
    px=len(pop)
    py=len(pop[0])
    for i in range(px):
        if(random.random()<pm):
            mpoint=random.randint(0,py-1)
            if(pop[i][mpoint]==0):
                pop[i][mpoint]=1
            else:
                pop[i][mpoint] = 0
if __name__ == "__main__":
    """
    popsize:种群大小
    """
    popsize=50
    #chromlength=10
    pc=0.6
    pm=0.0001
    results=[]
    bestindividual=[]
    bestfit=0
    fitvalue=[]
    tempop=[[]]
    pop=[[0,1,0,1,0,1,0,1,0,1] for i in range(popsize)]
    print pop
    print b2d([0,1,1,1,1,1,1,1,1])
    for i in range(100):
        objvalue=calobjvalue(pop)#f()
        fitvalue=calfitvalue(objvalue)
        [bestindividual,bestfit] =best(pop,fitvalue)
        results.append([bestfit,b2d(bestindividual)])
        selection(pop,fitvalue)
        crossover(pop,pc)
        mutation(pop,pm)
    xx=np.linspace(-5,15,1000)
    plt.figure(1)
    plt.plot(xx,10*np.sin(5*xx)+7*np.cos(4*xx))
    for v in results:
        print v
        plt.plot(v[1],v[0],"ro")
    print len(results)
    plt.show()

