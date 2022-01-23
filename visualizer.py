import pygraphviz as pgv
import pandas as pd

people = pd.read_csv('people.csv')
relations = pd.read_csv('relations.csv')

a = pgv.AGraph()
for row in people.iterrows():
    a.add_node(row[1]['rowid'], label=row[1]['person'])

for row in relations.iterrows():
    rm = str(int(row[1]['male']))
    rd = str(int(row[1]['descendant']))
    rf = row[1]['female']

    if rf > 0:
        # mother listed, indicate with red line
        rf = str(int(rf))
        a.add_edge(rm, rf, color='red')
        # attach descendant to mother's node with black line
        a.add_edge(rf, rd)
    else:
        # black line from father to descendant 
        a.add_edge(rm, rd)

a.draw('tree.png', prog='dot')
print('Done!')