#!/usr/bin/python
import beggarmypython
import timeit
import random

def mutate(muts,trials):
   
    
    A = 'K-KK----K-A-----JAA--Q--J-'
    B = '---Q---Q-J-----J------AQ--'
    totalturns = 0
    for t in range(trials):
        h = list(A)+list(B)
        for i in range(muts):
            p = random.randint(0,52-1)
            q = random.randint(0,52-1)

            g = list(h)
    
            g[p]=h[q]
            g[q]=h[p]

            h = g 


        h1 = h[0:26]
        h2 = h[26:]

        if h1!=list(A) or h2!=list(B):
            (turns,tricks) = beggarmypython.play((h1,h2))
            if turns>3000:
                print str(turns)+":"+"".join(h1)+"/"+"".join(h2)
            totalturns=totalturns+turns
    return float(totalturns)/float(trials)
        
    
print mutate(muts=12,trials=1000000000)