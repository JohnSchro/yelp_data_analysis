import streamlit as st

# streamlit page config 
st.set_page_config(
    page_title="Yelp Restaurant Dashboard", # page title shown in browser tab
    page_icon=":plate_with_cutlery:", # page favicon shown in the browsser tab
    layout="wide", # page layout : use the entire screen
)

pages = {
    "Analysis": [
        st.Page("dashboard.py", title="Yelp Dashboard", icon="📊", default=True),
        st.Page("eda.py", title="Exploratory Data Analysis", icon="🔍"),
    ],
    "Models": [
        st.Page("models/model_1.py", title="Logistic Regression RENAME"),
        st.Page("models/model_2.py", title="Random Forest RENAME"),
        st.Page("models/model_3.py", title="XGBoost RENAME"),
    ],
}

pg = st.navigation(pages)
pg.run()
