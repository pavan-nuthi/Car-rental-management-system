import streamlit as st
import pandas as pd
import mysql.connector
from streamlit_option_menu import option_menu


def insrt(mycursor,mydb):
    selected=option_menu(
        menu_title = "Choose the table",
        options = ["CAR","LOCATION"],
        orientation="horizontal",
    )
    if(selected=="CAR"):
        with st.form(key="form1"):
            reg_no=st.text_input(label='Enter the registration no of the car')
            model=st.text_input('Enter the model of the car')
            make=st.text_input('Enter the make of the car')
            avail=st.text_input('Enter the availability flag')
            submit=st.form_submit_button("Insert")

    if(selected=="LOCATION"):
        with st.form(key="form2"):      
            lid=st.text_input('Enter the LOCATION_ID')
            ln=st.text_input('Enter the LOCATION name')
            s=st.text_input('Enter the street')
            c= st.text_input('Enter the city')
            p=st.text_input('Enter the state')
            pi=st.text_input('Enter the pincode')
            submit=st.form_submit_button("Insert")
    
    if(submit):
        if(selected=="CAR"):
            str1=f"insert into CAR_DETAILS values ('{reg_no}','{model}','{make}','{avail}')"
        else:
            str1=f"insert into LOCATION_DETAILS values ({lid},'{ln}','{s}','{c}','{p}',{pi})"
        try:
            mycursor.execute(str1)
            st.info("Insertion successful!!")
            mydb.commit()
        except mysql.connector.Error as e:
            st.warning(e)

def quer(mycursor):
    with st.form(key="form1"):
        str1=st.text_area("Enter the query here:")
        submit=st.form_submit_button("Submit")
        if(submit):
            try:
                mycursor.execute(str1)
                df=pd.DataFrame(mycursor.fetchall())
                st.table(df)
            except mysql.connector.Error as e:
                st.warning(e)


def updat(mycursor,mydb):
    st.subheader("Update operation is available for BOOKING table")
    mycursor.execute("Select * from BOOKING_DETAILS")
    st.write("Before updation the table is")
    df=pd.DataFrame(mycursor.fetchall())
    st.table(df)
    with st.form("form1"):
        str2="SELECT EXISTS (SELECT 1 FROM BOOKING_DETAILS)"
        mycursor.execute(str2)
        if(mycursor.fetchone()['EXISTS (SELECT 1 FROM BOOKING_DETAILS)']):
            select=st.selectbox("Select the booking to be updated(id)",df['BOOKING_ID'])
            status=st.selectbox("Select the booking status to which it has to be changed to",('B','W'))
            plid=st.text_input("Enter the pickup location id of booking to which is has to be changed to")
            dlid= st.text_input("Enter the drop location id of booking to which it has to chaged to")
            #pdate=st.date_input("Enter the new pickup date of booking to which is has to be changed to")
            #ddate= st.date_input("Enter the new drop date of booking to which it has to changed to")
            amount=st.text_input("Enter the new amount of booking to which it has to be changed to")
            submit=st.form_submit_button("Update")
            if(submit):
                str1=f"update BOOKING_DETAILS set BOOKING_STATUS='{status}',PICKUP_LID={plid},amount={amount},DROP_LID={dlid} where BOOKING_ID={select}"
                try:
                    mycursor.execute(str1)
                    mydb.commit()
                    st.info("Updation successful")
                    st.write("After updation the table is")
                    mycursor.execute("Select * from BOOKING_DETAILS")
                    df=pd.DataFrame(mycursor.fetchall())
                    st.table(df)
                except mysql.connector.Error as e:
                    st.warning(e)


def delet(mycursor,mydb):
    st.subheader("Delete operation is available for BOOKING table")
    mycursor.execute("Select * from  BOOKING_DETAILS")
    st.write("Before deletion the booking table is")
    df=pd.DataFrame(mycursor.fetchall())
    st.table(df)
    with st.form("form1"):
        str2="SELECT EXISTS (SELECT 1 FROM BOOKING_DETAILS)"
        mycursor.execute(str2)
        if(mycursor.fetchone()['EXISTS (SELECT 1 FROM BOOKING_DETAILS)']):
            select=st.selectbox("Select the booking to be deleted from the id(IDs)",df['BOOKING_ID'])
            submit=st.form_submit_button("Delete")
            if(submit):
                    str1=f"delete from BOOKING_DETAILS where BOOKING_ID= {select}"
                    mycursor.execute(str1)
                    mydb.commit()
                    st.info("Deletion successful")
                    st.write("After deletion")
                    mycursor.execute("Select * from BOOKING_DETAILS")
                    df=pd.DataFrame(mycursor.fetchall())
                    st.table(df)
        
        
