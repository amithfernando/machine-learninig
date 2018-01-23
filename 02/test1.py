from sklearn.datasets import  load_iris
from sklearn import tree

iris=load_iris()

x=iris.data
y=iris.target

from sklearn.cross_validation import  train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=.5)

my_clasifier=tree.DecisionTreeClassifier()
my_clasifier=my_clasifier.fit(x_train,y_train)

predictions= my_clasifier.predict(x_test)

#print(predictions)

from sklearn.metrics import accuracy_score
print(accuracy_score(y_test,predictions))


