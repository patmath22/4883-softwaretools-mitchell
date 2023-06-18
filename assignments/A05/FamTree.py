'''
Patrick Mitchell
CMPS 5883
Summer I 2023
Assignment 5

This python code creates the graphviz code that needs to be placed in the Graphviz editor
It incorporates dictionaries.
Could not get the node record to work properly, hence just used the shape square on the nodes.

'''




import graphviz
import json



with open('dwarf.json') as f:
  data=json.load(f)
  
dot = graphviz.Digraph(node_attr={'shape':'square'},comment="just the nodes")
zero=[]
one=[]
two=[]

# create generation files

genDict = {}

for person in data:
  if not person['generation'] in genDict:
    genDict[person['generation']] = []

  genDict[person['generation']].append(person['id'])
  
  '''if person['generation']=='0':
    zero.append(person['id'])

  if person['generation']=='1':
    one.append(person['id'])

  if person['generation']=='2':
    two.append(person['id'])
  '''

#print(genDict)

# print(zero)
# print(one)
# print(two)

# list of lists
#gens = [zero,one,two]

#The code commented out prints the dictionary

#for gen,pidList in genDict.items():
#  print(gen,pidList)


#for person in data:
#  if person['id'] in zero:
#    print(person['id'])

#print(genDict.keys())

''' 
You must have knowledge of the json file to know how many generations are being used. 
In this case there were 9 generation 0-8. In the future this probably should have been extracted directly
from the json file. Instead of hardcoding it.
'''
for i in range(9):
  i = str(i)
  with dot.subgraph() as subgraph:
    subgraph.attr(rank='same')
    for person in data: 
      if person['id'] in genDict[i]:
        if person['gender']=='M':
          color='blue'
        else:
          color='red'
  
        subgraph.node(person['id'], f"{person['fname']}  {person['lname']}" ,color=color)

  
# with dot.subgraph() as gen2:
#   gen2.attr(rank='same')
#   for person in data:  
#     if person['id'] in one:
#       if person['gender']=='M':
#         color='blue'
#       else:
#         color='red'

#       gen2.node(person['id'], f"<fname> {person['fname']} | <lname> {person['lname']}" ,color=color)

# with dot.subgraph() as gen3:
#   gen3.attr(rank='same')
#   for person in data:  
#     if person['id'] in two:
#       if person['gender']=='M':
#         color='blue'
#       else:
#         color='red'

#       gen3.node(person['id'], f"<fname> {person['fname']} | <lname> {person['lname']}" ,color=color)

# edges for spouses. Non-directional lines are produced
dot.attr('edge', dir='none')
for person in data:
  if person['spouseId']:
    #temp='spouseId'
    dot.edge(person['id'],person['spouseId'])

#edges for children. Arrows are created from the Mother node to the Child node.

dot.attr('edge', dir='forward')
for person in data:
  if person['motherId']:
    temp='motherId'
    dot.edge(person[temp],person['id'])

print(dot.source)