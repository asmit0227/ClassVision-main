import streamlit as st

def header_homes():
   
    logo ="https://i.postimg.cc/7hXS2Kk1/172f2e60-b338-44b8-a68a-9d020d4a4cfc.png"

    st.markdown(
        f"""
        <div style="display : flex; flex-direction : column; align-items:center; justify-content:center; margin-bottom:30px; margin-top:30px;">
               <img src='{logo}' style= 'height:100px;border-radius:20px;'>
               <h1 style =" text-align:center;
                color:white;
                margin:15px 0 0 0;
                padding:0;
                line-height:1;
                letter-spacing:2px;">
                  <div style="letter-spacing:8px;">
                    CLASS
                  </div>
                  <div style="letter-spacing:0px;">
                    VISION
                  </div>
             </div>
        """,
         unsafe_allow_html=True
     
    )
    

def header_dashboard():
    logo ="https://i.postimg.cc/7hXS2Kk1/172f2e60-b338-44b8-a68a-9d020d4a4cfc.png"
    st.markdown(f"""
      <div style="display : flex; align-items:center; justify-content:center; gap:10px;">
       <img src='{logo}' style= 'height:85px;border-radius:20px;'>
       <h2 style = "text-align:left; color:#5085D7"> CLASS <br/> VISION</h2>
     
     </div>
     


     """,
     unsafe_allow_html=True

    )