import streamlit as st
from sklearn import datasets

from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier


import numpy as np

st.title("hello")

st.write("""
# Explore a classfier!
""")

dataset_name = st.sidebar.selectbox("Select dataset",("Iris", "House prices", "Wine dataset"))
st.write(dataset_name)

classifier_name =  st.sidebar.selectbox("Select classifier",("KNN", "SVM", "Random Forest"))

def get_dataset(dataset_name):
    if dataset_name == "Iris":
        data = datasets.load_iris()
    elif dataset_name == "House Prices":
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
    elif clf_name == "SVM":
        C = st.sidebar.slider("C", 0.01, 10.0)  
        params["C"] = C 
    else:
        max_depth = st.sidebar.slider("max_depth", 2, 15)
        n_estimators = st.sidebar.slider("n_estimators", 1, 100) 
        params["max_depth"]= max_depth
        params["n_estimators"] = n_estimators   
    return params 

params = add_parameter_ui(classifier_name)

def get_classifier(clf_name, params):
    
    if clf_name == "KNN":
        clf = KNeighborsClassifier(n_neighbors=params["K"])
    elif clf_name == "SVM":
        clf = SVC(C=params["C"]) 
    else:
        clf = RandomForestClassifier(n_estimators=params["n_estimators"],
                                max_depth=params["max_depth"], random_state=1234)
    return clf

clf = get_classifier(classifier_name, params)



   