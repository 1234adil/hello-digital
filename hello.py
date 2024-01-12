from PIL import Image
import requests
import streamlit as st

st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")

# ----- LOAD ASSETS -----
my_photo1 = Image.open("my_photo1.png")
my_photo2 = Image.open("my_photo2.png")


# ----- PROJECTS -----
with st.container():
    st.write("-----")
    st.header("My Projects")
    st.write('##')
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image("my_photo1.png")
    with text_column:
        st.subheader("Investment and EPC services")
        st.write(
            """ 
            I offer you Investment & EPC services: 
            - Potential investment projects and funded projects 
            - Potential investment projects 
            - Developing potential projects 
            """
        )
        st.markdown("[Learn more >](https://adilahmadzada.dorik.io/)")

with st.container():
    st.write("-----")
    st.header("My Projects")
    st.write('##')
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image("my_photo2.png")
    with text_column:
        st.subheader("Warehouse and Logistics")
        st.write(
            """ 
            I offer you Warehouse & Logistics: 
            - We open new warehouse for our customers 
            - We deliver products to local and foreign customers 
            - We do ship repair, vessel maintenance, ship transportation 
            """
        )
        st.markdown("[Learn more >](https://adilahmadzada.dorik.io/)")