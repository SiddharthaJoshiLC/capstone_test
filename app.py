# Code from TDI lesson by Ana Hocevar.

import streamlit as st
import streamlit.components.v1 as components
# from database import query_db
# from plot import plot_wells

def app():
    
    # st.title("Griham - a data driven search for your next home")
    st.markdown("Welcome to Griham!")
    st.markdown("Please select SEARCH or BROWSE mode")

    if st.button('BROWSE'):
        HtmlFile = open("your_map.html", 'r', encoding='utf-8')
        source_code = HtmlFile.read() 
        print(source_code)
        components.html(source_code,width=2000,height=2000)
        # st.write(on_click=open('your_map.html'))
    if st.button('SEARCH'):
        st.write('UNDER CONSTRUCTION')
    
if __name__ == '__main__':
    app()
