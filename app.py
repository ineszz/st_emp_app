#  python -m streamlit run app.py

import streamlit as st
from sklearn import svm
import pandas as pd
import numpy as np
import pickle
from PIL import Image
img = Image.open('emp_icon.png')
st.set_page_config(page_title='JEA-->Journey||Exit Angajat', page_icon=img)
clf = svm.SVC(kernel="linear")
model = pickle.load(open('model.pkl', 'rb'))

def main():
    st.markdown("""
            ## Predictie (Journey || Exit) 🧑 
            ### Introduceti caracteristicile angajatului: """)
    # col1, col2 = st.columns(2)
    # Get the input data from the user
    # with col1:
    GENUL = st.radio(
        "Alege genul 👇",
        ["feminin", "masculin"],
        )
    if GENUL == "feminin":
            st.write("Angajata")
            GEN = str('0')
    else:
            st.write("Angajat")
            GEN = str('1')
    st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

        # GEN =st.slider(str('GEN'), 0, 1, 0)
        # st.markdown('*Alegeti **0** pentru Feminin si **1** pentru Masculin*')
    VARSTA = st.text_input("VARSTA","Introduceti aici o valoare mai mare de 18")
    PROMOVARI = st.text_input("PROMOVARI","Introduceti aici o valoare")
    VECHIME_ANI = st.text_input("VECHIME_ANI","Introduceti aici o valoare")
    df = pd.DataFrame({"GEN":[GEN],"VARSTA":[VARSTA],"PROMOVARI":[PROMOVARI],"VECHIME_ANI":[VECHIME_ANI]})
    # with col2:
    st.dataframe(df.T.style.highlight_max(axis=0))
        # Make a prediction
    if st.button("Predictie scor plecare angajat"):
            prediction = model.predict(df)    
            if prediction == 1 :
                st.success('** EXIT **. Predictia spune ca angajatul are probabilitate mare de a pregati EXIT curand!')
            elif prediction == 0 :
                st.success('** JOURNEY **.Predictia spune ca angajatul nu se pregateste de EXIT.')


if __name__ == '__main__':
    main()