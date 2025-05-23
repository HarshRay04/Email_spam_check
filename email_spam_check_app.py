import streamlit as st
import pickle
import nltk
import string
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

ps = PorterStemmer() 


def transform_text(text):
    text = text.lower()
    text = nltk.wordpunct_tokenize(text)
    y = []
    for i in text:
        if i.isalnum():
            y.append(i)

    text = y[:]
    y.clear()
    
    for i in text:
          if i not in stopwords.words('english') and i not in string.punctuation:
              y.append(i)

    text = y[:]
    y.clear()
    for i in text:
        y.append(ps.stem(i))
    return " ".join(y)

tfidf = pickle.load(open('vectorizer.pkl','rb'))
model = pickle.load(open('mnb_model.pkl','rb'))

st.title("Email/SMS Spam Classifier")

input_sms = st.text_area("Enter the Message")

if st.button("predict") :
    #process
 
    transformed_sms = transform_text(input_sms)

    #vectorise
    vector_input = tfidf.transform([transformed_sms])

    #predict
    result = model.predict(vector_input)[0]

    #display

    if result == 1:
        st.header("Spam")
    else : 
        st.header("Not Spam")