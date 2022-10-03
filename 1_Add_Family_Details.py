from datetime import datetime
from PIL import Image
import streamlit as st
import sqlite3

# print(datetime.date(datetime(2002, 2, 4)))


conn = sqlite3.connect('data.db', check_same_thread=False)
cur = conn.cursor()

st.set_page_config(page_title="Prajapati Kumbhkar Kalakar Sangh", page_icon=":tada:", layout="wide")
img_logo = Image.open("images/PKKS.JPG")
# --- HEADER SECTION --- #
with st.container():
    text_column, img_column = st.columns((2, 1))
    with img_column:
        st.image(img_logo)
    with text_column:
        st.title("Prajapati Kumbhkar Kalakar Sangh")
        st.header("Family Data Collection")


def form():
    with st.form(key="Information Form"):
        name = st.text_input("Name")
        gender = st.radio("Gender", ('Male', 'Female'))
        dob = st.date_input("Date of Birth", min_value=datetime.date(datetime(1945, 1, 1)))
        mobile = st.text_input("Mobile Number ", placeholder=9876543210)
        relationname = st.text_input("Father's/Husband's Name")
        relation = st.radio("Relation", ('Father', 'Husband'))
        marital_status = st.radio('Marital Status', ('Married', 'Un-Married'))
        spouse = st.text_input("Spouse's/Wife's Name")
        children_count = st.number_input("Number of Children", 0, 10)
        children_details = st.text_area("Children Details", placeholder="Name of the child, Age, Qualification")

        # marital_status = st.selectbox('Marital Status', ('Married', 'Un-Married'))

        occupation = st.text_input("Occupation ")
        present_address = st.text_area("Present Address ")
        permanent_address = st.text_area("Permanent Address ")
        qualification = st.text_area("Qualification ")

        # st.write('You selected:', gender)
        submission = st.form_submit_button(label="Submit")

        if submission:
            addData(name, gender, dob, mobile, relationname, relation, marital_status, spouse,
                    children_count, children_details, occupation, present_address, permanent_address,
                    qualification)


def addData(name, gender, dob, mobile, relationname, relation, marital_status, spouse, children_count,
            children_details, occupation, present_address, permanent_address, qualification):
    # cur.execute("DROP TABLE IF EXISTS FAMILY_DTL;")
    cur.execute("CREATE TABLE IF NOT EXISTS FAMILY_DTL (NAME TEXT(50), GENDER VARCHAR(6), "
                "DOB TEXT(10), MOBILE TEXT(14), RELATIONNAME TEXT(50), RELATION TEXT(7), "
                "MARITAL_STATUS TEXT(10), SPOUSE TEXT(50), CHILDREN_COUNT NUMERIC(2), CHILDREN_DETAILS TEXT(200),"
                "OCCUPATION TEXT(50), PRESENT_ADDRESS TEXT(100), PERMANENT_ADDRESS TEXT(100), "
                "QUALIFICATION TEXT(100), INSERT_TS TEXT(30));")
    cur.execute("INSERT INTO FAMILY_DTL VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,datetime(CURRENT_TIMESTAMP, 'localtime'));",
                (name, gender, dob, mobile, relationname, relation, marital_status, spouse,
                 children_count, children_details, occupation, present_address, permanent_address,
                 qualification))
    conn.commit()
    conn.close()
    st.success("Successfully Submitted")


form()
