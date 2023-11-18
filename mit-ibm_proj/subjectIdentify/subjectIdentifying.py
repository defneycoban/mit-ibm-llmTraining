import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report


def identify_subject(new_question):
    df = pd.read_csv('/Users/yuhanyang/Desktop/mit-ibm_proj/subjectIdentify/subjectData3.csv')
    df.head()

    X = df['question']
    y = df['subject']

    tfidf_vectorizer = TfidfVectorizer()
    X_tfidf = tfidf_vectorizer.fit_transform(X)

    X_train, X_test, y_train, y_test = train_test_split(X_tfidf, y, test_size=0.2, random_state=42)

    model = LogisticRegression(max_iter=1000, random_state=42)
    model.fit(X_train, y_train)

    # y_pred = model.predict(X_test)
    # accuracy = accuracy_score(y_test, y_pred)

    # report = classification_report(y_test, y_pred)

    predicted_subject = model.predict(tfidf_vectorizer.transform(new_question))

    return predicted_subject[0]

    # print(predicted_subject)
    # print(accuracy)



