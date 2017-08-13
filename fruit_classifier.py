# -*- coding: utf-8 -*-
"""
Created on Sun Aug 13 03:20:33 2017

@author: Aditi
"""

from sklearn import tree
#170, 175, 180, 178, 182,130, 120, 130, 138, 145 weights
#smooth  9, 10, 8, 8, 7, 3, 4, 2, 5, 6
features = [[170,9],[175,10],[180,8],[178,8],[182,7],[130,3],[120,4],[130,2],[138,5]]
labels = [1, 1, 1, 1, 1, 0, 0, 0, 0]  # 1 -> apple

clf = tree.DecisionTreeClassifier()
clf = clf.fit(features,labels)

print(clf.predict([[145,6]]))
#orange 0

print(clf.predict([[172,7]]))
#apple 1