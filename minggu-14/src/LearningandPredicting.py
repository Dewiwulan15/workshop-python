from sklearn import svm
clf = svm.SVC(gamma=0.001, C=100.)

clf.fit(digits.data[:-1], digits.target[:-1])

#output
"""
SVC(C=100.0, gamma=0.001)
"""

clf.predict(digits.data[-1:])

#output
'''
array([8])
'''