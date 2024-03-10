import streamlit as st
import pickle
import re
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
stemmer= PorterStemmer()
vectorizer=TfidfVectorizer()

vector=pickle.load(open('vectorizer.pkl','rb'))
model=pickle.load(open('pac.pkl','rb'))





def fake_news(news):
    
    input_data=[news]
    vector_form1=vector.transform(input_data)
    prediction = model.predict(vector_form1)
    return prediction



if __name__ == '__main__':
    st.title('Fake News Classifier ')
    st.subheader("Provide The News Below")
    sentence = st.text_area("Enter News", "",height=200)
    predict_bt = st.button("predict")
    if predict_bt:
        prediction_class=fake_news(sentence)
        print(prediction_class)
        if prediction_class == [0]:
            st.success('Fake')
        if prediction_class == [1]:
            st.warning('Reliable')