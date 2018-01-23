from sklearn.datasets import  load_iris

iris=load_iris()
print(iris.feature_names)
print(iris.target_names)
# 'setosa' =0 'versicolor' =1 'virginica' =2

for i in range(len(iris.target)):
    print("Examples lable = %s features = %s" %( iris.target[i], iris.data[i]))


