from sklearn import tree
features=[[140,0],[130,0],[150,1],[170,1]]
label=[0,0,1,1]
clf=tree.DecisionTreeClassifier()
clf=clf.fit(features,label)
print clf.predict([[170,0]])
