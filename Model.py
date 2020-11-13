import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report
from sklearn.svm import SVC

df = pd.read_csv("data/All-in-one2.csv")
vectorizer = TfidfVectorizer(max_features = 5000)

X = vectorizer.fit_transform(df.Summary).toarray()
enc_cl = LabelEncoder()
y = enc_cl.fit_transform(df.Classification)
X_train, X_test, y_train_clf, y_test_clf = train_test_split(X, y, random_state=42)
target_names_cl = enc_cl.inverse_transform([0, 1, 2])

clf_mnb = MultinomialNB()
clf_mnb.fit(X_train, y_train_clf)

y_pred_mnb = clf_mnb.predict(X_test)

enc_hs = LabelEncoder()
y = enc_hs.fit_transform(df['Human_Safety'])
X_train, X_test, y_train_hs, y_test_hs = train_test_split(X, y, random_state=42)
target_names_hs = enc_hs.inverse_transform([0, 1, 2])
hs_mnb = MultinomialNB()
hs_mnb.fit(X_train, y_train_hs)
y_pred_mnb = hs_mnb.predict(X_test)

enc_i = LabelEncoder()
y = enc_i.fit_transform(df['Infrastructure'])
X_train, X_test, y_train_i, y_test_i = train_test_split(X, y, random_state=42)
target_names_i = enc_i.inverse_transform([0, 1])
i_mnb = MultinomialNB()
i_mnb.fit(X_train, y_train_i)
y_pred_mnb = i_mnb.predict(X_test)

enc_c = LabelEncoder()
y = enc_c.fit_transform(df['Communication'])
X_train, X_test, y_train_c, y_test_c = train_test_split(X, y, random_state=42)
target_names_c = enc_c.inverse_transform([0, 1])
c_mnb = MultinomialNB()
c_mnb.fit(X_train, y_train_c)
y_pred_mnb = c_mnb.predict(X_test)

enc_f = LabelEncoder()
y = enc_f.fit_transform(df['Finance'])
X_train, X_test, y_train_f, y_test_f = train_test_split(X, y, random_state=42)
target_names_f = enc_f.inverse_transform([0, 1])
f_mnb = MultinomialNB()
f_mnb.fit(X_train, y_train_f)
y_pred_mnb = f_mnb.predict(X_test)

enc_con = LabelEncoder()
y = enc_con.fit_transform(df['Controllable'])
X_train, X_test, y_train_con, y_test_con = train_test_split(X, y, random_state=42)
target_names_con = enc_con.inverse_transform([0, 1])
con_mnb = MultinomialNB()
con_mnb.fit(X_train, y_train_con)
y_pred_mnb = con_mnb.predict(X_test)

def TP_calc(doc, src, verf):
    s = 2
    v = 2

    if(src == "Twitter"):
        s = 1
        if(verf == "FALSE"):
            v = 1
    t_vec = vectorizer.transform(doc)
    cl = clf_mnb.predict(t_vec)[0]
    hs = hs_mnb.predict(t_vec)[0]
    i = i_mnb.predict(t_vec)[0]
    c = c_mnb.predict(t_vec)[0]
    f = f_mnb.predict(t_vec)[0]
    con = con_mnb.predict(t_vec)[0]

    if(cl == 0):
        cl = 1
    if(cl == 1):
        cl = 0

    if(hs == 0):
        hs = 2
    if(hs == 2):
        hs = 0

    if(i == 0):
        i = 1
    if(i == 1):
        i = 0

    if(c == 0):
        c = 1
    if(c == 1):
        c = 0

    if(f == 0):
        f = 1
    if(f == 1):
        f = 0

    if(con == 0):
        con = 1
    if(con == 1):
        con = 0
    
    calc = round((0.2*hs + 0.15*con + 0.06*i + 0.06*c + 0.06*f + 0.07*cl + 0.04*s + 0.025*v)*100,2)
    return calc
