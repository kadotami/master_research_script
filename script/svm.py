from sklearn.datasets import load_digits
from sklearn.multiclass import OneVsRestClassifier
from sklearn.svm import SVC
from sklearn.cross_validation import train_test_split
from sklearn.metrics import accuracy_score

digits = load_digits()
train_x, test_x, train_y, test_y  = train_test_split(digits.data, digits.target)

C = 1.
kernel = 'rbf'
gamma  = 0.01

estimator = SVC(C=C, kernel=kernel, gamma=gamma)
classifier = OneVsRestClassifier(estimator)
classifier.fit(train_x, train_y)
pred_y = classifier.predict(test_x)

classifier2 = SVC(C=C, kernel=kernel, gamma=gamma)
classifier2.fit(train_x, train_y)
pred_y2 = classifier2.predict(test_x)

print('One-against-rest: {:.5f}'.format(accuracy_score(test_y, pred_y)))
print('One-against-One: {:.5f}'.format(accuracy_score(test_y, pred_y2)))