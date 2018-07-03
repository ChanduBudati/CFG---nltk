'''
Chandu Budati
CSCI 6350-001
Project #4
Due: 03/23/2018
File Description: This file contians all functions required to run Grammar checker program, actual grammar is in file p4grammar.fcfg
'''


from nltk import grammar, parse, tree
fname = "sents.txt" #input("file address: ")

#loading parsing grammar
cp = parse.load_parser('p4grammar.fcfg', trace = 0, parser=parse.FeatureEarleyChartParser)

#importing test data
f = open(fname, 'r')
testdata = f.readlines()
f.close()

testdata = [line.strip() for line in testdata ]
parsed = []
for sent in testdata:
    tokens = sent.split() #generating tokens
    trees = cp.parse(tokens)
    trees = list(trees)
    if(len(trees) == 0):
        parsed.append("")
        print()
    # for tree in trees:
    #     t = str(tree)
    #     t = t.replace("\n", "")
    #     print(str(index) + ": ", end = "")
    #     print(t)
    # index += 1
    else:
        t = str(trees[0]) #printing first tree from the tree list
        t = t.replace("\n", "")
        parsed.append(t)
        print(t)

f = open("parsedsents.txt", 'w') # wrinting to file
for i in parsed:
    f.write(i)
    f.write("\n")
f.close()