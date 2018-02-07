# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 21:28:25 2018

@author: ckent
"""

import csv
import os

csv_path = os.path.join("..","Resources", "election_data_1.csv")

listCandidates = []
with open(csv_path, mode='r') as f:
    reader = csv.reader(f, delimiter=',')  
    for n, row in enumerate(reader):
        if not n:
            continue  
        x,y,z = row
        listCandidates.append(row[2])
total = len(listCandidates)
candidateTotal = {}

print('-------------------------')
print('Election Results')
print('-------------------------')
print('Total Votes: {}'.format(total))
print('-------------------------')
for i in set(listCandidates):
    print('{}: {}% ({})'.format(i,(listCandidates.count(i)/total)*100,listCandidates.count(i)))
    candidateTotal[i]=listCandidates.count(i)
print('-------------------------')
print('Winner:{}'.format(max(candidateTotal.keys())))
print('-------------------------')

txt_path = os.path.join("..","Resources", "electionResults01.txt")

with open(txt_path,"a") as g:
   g.write('-------------------------\n')
   g.write('\nElection Results\n')
   g.write('\n-------------------------\n')
   g.write('\nTotal Votes: {}'.format(total) + "\n")
   g.write('\n-------------------------\n')
   for i in set(listCandidates):
       g.write('\n{}: {}% ({})'.format(i,(listCandidates.count(i)/total)*100,listCandidates.count(i),"\n"))
       candidateTotal[i]=listCandidates.count(i)
   g.write('\n-------------------------\n')
   g.write('\nWinner:{}'.format(max(candidateTotal.keys()),"\n"))
   g.write('\n-------------------------\n') 


