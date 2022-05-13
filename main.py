import streamlit as st
import sklearn as sklearn
from sklearn import datasets
import numpy as np

st.title("hello")

st.write("""
# Explore a classfier!
""")

dataset_name = st.sidebar.selectbox("Select dataset",("Iris", "House prices", "Wine dataset"))
st.write(dataset_name)

classifier_name =  st.sidebar.selectbox("Select dataset",("KNN", "SVN", "Random Forest"))

def get_dataset(dataset_name):
    if dataset_name == "Iris":
        data = datasets.load_iris()
    elif dataset_name == "Prices":
        data = datasets.load_prices() 
    else:
        data = datasets.load_wine() 
    X = data.data
    y = data.target
    return X, y   

X, y = get_dataset(dataset_name)
st.write("Shape of dataset",X.shape)
st.write("Number of classes", len(np.unique(y)))

def add_parameter_ui(clf_name):
    params = dict()
    if clf_name == "KNN":
        K = st.sidebar.slider("K", 1, 15) 
        params["K"] = K
    return params 

add_parameter_ui(classifier_name)