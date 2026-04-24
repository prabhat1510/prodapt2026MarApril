from sklearn.datasets import load_iris
from sklearn.model_selection import cross_val_score
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
from sklearn import tree
clf = DecisionTreeClassifier(random_state=0)
iris = load_iris()
#print(iris.target_names)
#print(iris.feature_names)
#print(iris.data)
#print(iris.target)


X= iris.data
y= iris.target
clf.fit(X,y)
print("Accuracy: ", clf.score(X, y))
scores = cross_val_score(clf,X,y,cv=10)
print("Cross-valiaton scores: ",scores)

print(clf.predict([[3, 5, 4, 2]]))
tree.plot_tree(clf,filled=True)
plt.show()


