import dataset
from sklearn import datasets
iris=datasets.load_iris()

X=iris.data # features
y=iris.target # label

from sklearn.cross_validation import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.5)
#from sklearn import tree
from sklearn.neighbors import KNeighborsClassifier
clf=KNeighborsClassifier()
#clf=tree.DecisionTreeClassifier()
clf=clf.fit(X_train,y_train)
predictions=clf.predict(X_test)
from sklearn.metrics import accuracy_score
print accuracy_score(y_test,predictions) 
