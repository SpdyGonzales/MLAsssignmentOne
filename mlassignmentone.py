import monkdata as m
import dtree as calc
import drawtree_qt5 as draw
import random as rand
print("Assignment 1");
print(calc.entropy(m.monk1test));
print(calc.entropy(m.monk2test));
print(calc.entropy(m.monk3test));
print(" ");
print("Assignment 2");
print(calc.averageGain(m.monk1test,m.attributes[0]));
print(calc.averageGain(m.monk1test,m.attributes[1]));
print(calc.averageGain(m.monk1test,m.attributes[2]));
print(calc.averageGain(m.monk1test,m.attributes[3]));
print(calc.averageGain(m.monk1test,m.attributes[4]));
print(calc.averageGain(m.monk1test,m.attributes[5]));
print(calc.averageGain(m.monk2test,m.attributes[0]));
print(calc.averageGain(m.monk2test,m.attributes[1]));
print(calc.averageGain(m.monk2test,m.attributes[2]));
print(calc.averageGain(m.monk2test,m.attributes[3]));
print(calc.averageGain(m.monk2test,m.attributes[4]));
print(calc.averageGain(m.monk2test,m.attributes[5]));
print(calc.averageGain(m.monk3test,m.attributes[0]));
print(calc.averageGain(m.monk3test,m.attributes[1]));
print(calc.averageGain(m.monk3test,m.attributes[2]));
print(calc.averageGain(m.monk3test,m.attributes[3]));
print(calc.averageGain(m.monk3test,m.attributes[4]));
print(calc.averageGain(m.monk3test,m.attributes[5]));
print(" ");
print("Assignment 3");

t = calc.buildTree(m.monk1, m.attributes);
t2 = calc.buildTree(m.monk2,m.attributes);
t3 = calc.buildTree(m.monk3,m.attributes);
calc.check(t,m.monk1test);
calc.check(t2, m.monk2test);
calc.check(t3, m.monk3test);
#draw.drawTree(t);
#draw.drawTree(t2);
#draw.drawTree(t3);

def partition(data, fraction):
	ldata =list(data)
	rand.shuffle(ldata)
	breakPoint = int(len(ldata) * fraction)
	return ldata[:breakPoint], ldata[breakPoint:]

def pruneCheck(data, fraction):
	train, valid = partition(data,fraction)
	currTree = calc.buildTree(train,m.attributes)
	bestTree = pruneLoop(currTree, valid)
	return bestTree

def pruneLoop(currTree, valid):
	currentTree = currTree
	trees = calc.allPruned(currentTree)
	betterTree = False
	for tree in trees:
		bestTree = calc.check(currentTree, valid)
		newTree = calc.check(tree,valid)
		if newTree < bestTree:
			currentTree == tree
			betterTree == True
    	if betterTree == True:
        	pruneLoop(currentTree, valid)
    	else:
        	return currentTree

for i in [0.3,0.4,0.5,0.6,0.7,0.8]:
    print("Fraction: ",i," Monk1 ",calc.check(pruneCheck(m.monk1,i),m.monk1test))
    print("Fraction: ",i," Monk2 ",calc.check(pruneCheck(m.monk2,i),m.monk2test))
    print("Fraction: ",i," Monk3 ",calc.check(pruneCheck(m.monk3,i),m.monk3test))
