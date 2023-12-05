import numpy as np
import pickle
import streamlit as st

pickle_in = open("model_saved","rb")
classifier = pickle.load(pickle_in)

st.header("welcome")

def predict(age, systolic_bp, diastolic_bp, bs, body_temp, heart_rate):
    prediction = classifier.predict([[age, systolic_bp,diastolic_bp, bs, body_temp, heart_rate]])
    print(prediction)
    return prediction

def main():
    st.title("Maternal Health Rate Checker")
    age = st.number_input("Age : ",  key=1)
    systolic_bp = st.number_input("systolic_bp : ",key=2)
    diastolic_bp = st.number_input("diastolic_bp : ", key=3)
    bs = st.number_input("BS : ",key=4)
    body_temp = st.number_input("Body Temperature : ", key=5)
    heart_rate = st.number_input("heart_rate : ", key=6)

    result = ""
    if st.button("Predict"):
        result = predict(age, systolic_bp, diastolic_bp, bs, body_temp, heart_rate)
    st.success("The output is {}".format(result))


if __name__=='__main__':
    main()