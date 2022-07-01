from asyncio.windows_events import NULL
import streamlit as st
import pandas as pd
from PIL import Image
import base64

Good = open(r"C:\Users\camra\env\SQ\Good.gif", "rb")
Bad = open(r"C:\Users\camra\env\SQ\Bad.gif", "rb")
contents = Good.read()
contents2= Bad.read()

data_url = base64.b64encode(contents).decode("utf-8")
data_url2 = base64.b64encode(contents2).decode("utf-8")
Good.close()
Bad.close()

List= pd.read_csv(r'C:\Users\camra\env\SQ\Words.csv',encoding = 'unicode_escape')

Words=List.Wrong.to_list()

Types=List.Type.to_list()

Text=st.text_input('Type your requirement')

TextSize=len(Text.split())

special_characters = "!#@%^&*()+?=<>/"

WrongWord=set(Text.split()).intersection(Words)

results=''
if(Text==''):
        results='Textbox is empty, Please type your requirement'
else:
  if(TextSize>4):
    if any(c in special_characters for c in Text):
        results='Special characters that are used are not allowed, Please try again'
    else:
        if (WrongWord==set() and Text!=''):
          results='The requirement is Good'
          st.markdown(
            f'<img src="data:image/gif;base64,{data_url}" alt="cat gif">',
            unsafe_allow_html=True,
          )
        elif(Text!=''):
          WrongWord2=''.join(WrongWord)
          index=Words.index(WrongWord2)
          Type=Types[index]
          results='The requirement is bad because it has '+WrongWord2+' which is a mistake of type '+Type
          st.markdown(
            f'<img src="data:image/gif;base64,{data_url2}" alt="cat gif">',
            unsafe_allow_html=True,
          )
  elif(TextSize>=1 and TextSize<=4):
    results='Incomplete requirement, Please try again'

st.text(f'{results}')