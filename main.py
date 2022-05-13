import streamlit as st
import sklearn as sklearn

st.title("hello")

st.write("""
# Explore a classfier!
""")

dataset_name = st.sidebar.selectbox("Select dataset",("Iris", "Cancer", "Wine dataset"))
st.write(dataset_name)