import mysql.connector
import streamlit as st
from streamlit_option_menu import option_menu
from OPERATIONS import *
import pandas as pd

mydb=mysql.connector.connect(
     
     host = "localhost",
     user = "root",
     database = "car_rental"
)

mycursor = mydb.cursor(dictionary=True)

st.title("CAR RENTAL MANAGEMENT")
  
# selected=option_menu(
#         menu_title = None,
#         options = ["Insert","Update","Delete","Query"],
#         orientation="vertical",
#     )
# with st.sidebar:
#     selected=option_menu(
#         menu_title="Main Menu",
#         options=["Insert","Update","Delete","Query"],
#         # icons=["car-front"]
#         menu_icon="cast",
#         # orientation="horizontal"
#     )
selected= option_menu(None, ["Insert", "Update", "Delete",'Query'], 
    icons=['house', 'cloud-upload', "list-task", 'gear'], 
    menu_icon="cast", default_index=0, orientation="horizontal",
    styles={
        "container": {"padding": "0!important", "background-color": "#"},
        "icon": {"color": "orange", "font-size": "25px"}, 
        "nav-link": {"font-size": "25px", "text-align": "left", "margin":"0px", "--hover-color": "#"},
        "nav-link-selected": {"background-color": "green"},
    }
)

if selected=="Insert":
    st.title("Insert")
    insrt(mycursor,mydb)



if selected=="Update":
    st.title("Update")
    updat(mycursor,mydb)


if selected=="Delete":
    st.title("Delete")
    delet(mycursor,mydb)


if selected=="Query":
    st.title("Query")
    quer(mycursor)
    
