import streamlit as st
import pandas as pd
import plotly.express as px
import components.authenticate as authenticate


if authenticate.check_usersession():
    #st.set_page_config(
     #   page_title="Hello",
      #  page_icon="👋",
    #)
    st.write("# Welcome to Streamlit! 👋")
    st.sidebar.success("Select a demo above.")
    st.markdown(
        """
        Here we are trying to demonstrate 3-tier architecture , SSO enablement and scalability of the streamlit app.
    """
    
    """
   
    - Check out [My Index Page](https://adm.com)
    

      """
    )
