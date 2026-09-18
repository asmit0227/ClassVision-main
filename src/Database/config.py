import streamlit as st
from supabase import create_client,Client

supabase = create_client(
st.secrets["project_url"],
st.secrets["project_key"]
)
