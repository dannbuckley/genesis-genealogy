import pygraphviz as pgv
import pandas as pd

people = pd.read_csv('people.csv')
relations = pd.read_csv('relations.csv')

a = pgv.AGraph()
for _, row in people.iterrows():
    n = row['notes']
    p = row['person']
    l = '{} [{}]'.format(p, n[n.find('(') + 6:-1] if '(' in n else n[5:])
    a.add_node(row['rowid'], label=l)

for _, row in relations.iterrows():
    rm = str(int(row['male']))
    rd = str(int(row['descendant']))
    rf = row['female']

    if rf > 0:
        # mother listed, indicate with red line
        rf = str(int(rf))
        a.add_edge(rm, rf, color='red')
        # attach descendant to mother's node with black line
        a.add_edge(rf, rd, dir='forward', arrowsize=0.7, arrowhead='empty')
    else:
        # black line from father to descendant 
        a.add_edge(rm, rd, dir='forward', arrowsize=0.7)

# draw graph to files
a.draw('tree.png', prog='dot')
a.draw('tree.svg', prog='dot')
print('Done!')