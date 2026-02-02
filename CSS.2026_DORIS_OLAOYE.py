#Trying to build an app that profiles researchers in line with my research interest and sections the university they are affilated to and where it is located.

import streamlit as st
import pandas as pd
import numpy as np

# Title of the app
st.title("Doris Olaoye (B.Sc, MPH)")

# Collect basic information
name = "Doris Olaoye"
field = "Public Health"
institution = "University of Benin"

# Display basic profile information
st.header("Researcher Overview")
st.write(f"**Name:** {name}")
st.write(f"**Field of Research:** {field}")
st.write(f"**Institution:** {institution}")

st.image(
    "https://cdn.pixabay.com/photo/2015/04/23/22/00/tree-736885_1280.jpg",
    caption="Nature (Pixabay)"
)


st.header("Abstract")
uploaded_file = st.file_uploader("Upload a CSV of Abstract", type="csv")

if uploaded_file:
    Abstract = pd.read_csv(uploaded_file)
    st.dataframe(Abstract)

st.header("About the Author")

st.write("Pulications")
n
st.header("Contact Information")
email = "tun4fade@gmail.com"
LnkedIn = "Doris Alabi-Olaoye"

st.write(f"You can reach {name} at {email}.")
