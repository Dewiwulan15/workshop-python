from sklearn import datasets
from sklearn.svm import SVC
iris = datasets.load_iris()
clf = SVC()
clf.fit(iris.data, iris.target)

#output
"""
SVC()
"""

list(clf.predict(iris.data[:3]))

#output
"""
[0, 0, 0]
"""

clf.fit(iris.data, iris.target_names[iris.target])

#output
"""
SVC()
"""

list(clf.predict(iris.data[:3]))

#output
"""
['setosa', 'setosa', 'setosa']
"""