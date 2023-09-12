import streamlit as st

def check_usersession():
    """Returns `True` if the user had a correct password."""
    def password_entered():
            """No query params found, so check the user inputs """
            """Checks whether a password entered by the user is correct."""
            if (
                st.session_state["username"] in st.secrets["passwords"]
                and st.session_state["password"]
                == st.secrets["passwords"][st.session_state["username"]]
            ):
                st.session_state["password_correct"] = True
                del st.session_state["password"]  # don't store username + password
                del st.session_state["username"]
            else:
                st.session_state["password_correct"] = False

    def check_queryparams():
        """Returns `True` if the user had a correct password."""
        qparams=st.experimental_get_query_params()
        uid = ""
        pd = ""
        if(len(qparams)>0):
            uid=qparams['uid'][0]
            pd=qparams['pwd'][0]
            
        if(len(uid)==0):
            return
        
        if (
            uid in st.secrets["passwords"]
            and pd == st.secrets["passwords"][uid]
        ):
            st.session_state["password_correct"] = True
            #del st.session_state["password"]  # don't store username + password
            #del st.session_state["username"]
        else:
            st.session_state["password_correct"] = False
            
    check_queryparams()           
    if "password_correct" not in st.session_state:
        # First run, show inputs for username + password.
        st.text_input("Username", key="username")
        st.text_input("Password", type="password", on_change=password_entered, key="password")
        return False
    elif not st.session_state["password_correct"]:
        # Password not correct, show input + error.
        st.text_input("Username", key="username")
        st.text_input("Password", type="password", on_change=password_entered, key="password")
        st.error("😕 User not known or password incorrect")
        return False
    else:
        # Password correct.
        return True
