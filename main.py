import streamlit as st
import sklearn as sklearn
from sklearn import datasets
import numpy as np

st.title("hello")

st.write("""
# Explore a classfier!
""")

dataset_name = st.sidebar.selectbox("Select dataset",("Iris", "Cancer", "Wine dataset"))
st.write(dataset_name)

classifier_name =  st.sidebar.selectbox("Select dataset",("KNN", "SVN", "Random Forest"))

def get_dataset(dataset_name):
    if dataset_name == "Iris":
        data = datasets.load_iris()
    elif dataset_name == "Cancer":
        data = datasets.load_cancer() 
    else:
        data = datasets.load_wine() 
    X = data.data
    y = data.target
    return X, y   

X, y = get_dataset(dataset_name)
st.write("Shape of dataset", X.shape)          
