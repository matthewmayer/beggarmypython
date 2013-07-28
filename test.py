#!/usr/bin/python
import beggarmypython
import timeit
import random
import boto

TURNS_TO_LOG=1800

def mutate(muts,trials):
   
    
    A = 'K-KK----K-A-----JAA--Q--J-'
    B = '---Q---Q-J-----J------AQ--'
    totalturns = 0
    for t in xrange(trials):
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
            if turns>TURNS_TO_LOG:
                
                print str(turns)+":"+"".join(h1)+"/"+"".join(h2)
                sns = boto.connect_sns()
                sns.publish("arn:aws:sns:us-east-1:323036967201:bmn","Found "+str(turns),str(turns)+":"+"".join(h1)+"/"+"".join(h2))
                
            totalturns=totalturns+turns
    return float(totalturns)/float(trials)
        
sns = boto.connect_sns()
sns.publish("arn:aws:sns:us-east-1:323036967201:bmn","Spinning up new instance","It begins...")   
mutate(muts=12,trials=216*1000*1000)
sns = boto.connect_sns()
sns.publish("arn:aws:sns:us-east-1:323036967201:bmn","216 million tests complete","Complete")   
