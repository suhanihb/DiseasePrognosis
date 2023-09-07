import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

train = pd.read_csv("data/Training.csv")
test = pd.read_csv("data/Testing.csv")

train = train.drop(train.columns[-1], axis = 1)

# Separate symptoms and prognosis
trainSym = train.iloc[:, : -1]
trainProg = train.iloc[:, -1]

testSym = test.iloc[:, : -1]
testProg = test.iloc[:, -1]

# Train model
model = LogisticRegression()
model.fit(trainSym, trainProg)

# Predict
testProgPred = model.predict(testSym)
accuracy = accuracy_score(testProg, testProgPred)
print("Accuracy: ", accuracy)