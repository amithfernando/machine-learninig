from sklearn import tree

# weight   texture    label
# 140       smooth     apple
# 130       smooth     apple
# 150       bumpy      orange
# 140       bumpy      orange

# apple = 0, orange = 1
# smooth = 1 , bumpy = 0


features = [[140,1],[130,1],[150,0],[170,0]]
lables=[0,0,1,1]
clf=tree.DecisionTreeClassifier()
clf=clf.fit(features,lables)
print(clf.predict([[120,1]]))
