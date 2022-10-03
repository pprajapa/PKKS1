from PIL import Image
import streamlit as st
import sqlite3
import pandas as pd
import numpy as np

conn = sqlite3.connect('data.db', check_same_thread=False)
cur = conn.cursor()

st.set_page_config(page_title="Prajapati Kumbhkar Kalakar Sangh", page_icon=":tada:", layout="wide")
img_logo = Image.open("images/PKKS.JPG")
# --- HEADER SECTION --- #
with st.container():
    text_column, img_column = st.columns((2,1))
    with img_column:
        st.image(img_logo)
    with text_column:
        st.title("Prajapati Kumbhkar Kalakar Sangh")
        st.header("Information Collected")

cur.execute("SELECT ROWID, NAME,RELATIONNAME, INSERT_TS from FAMILY_DTL;")
rows = cur.fetchall()

df = pd.DataFrame(rows, columns=("SNo.", "Name", "Father's/Husband's Name" , "DateTime"))
st.dataframe(df)
# st.table(df)
# Print results.
#st.write(f"SNo. | Name")
# for row in rows:
#     st.write(f"{row[0]}.{row[1]}")
#
#
# df = pd.DataFrame(
#     np.random.randn(10, 5),
#     columns=('col %d' % i for i in range(5)))
#
# st.table(df)