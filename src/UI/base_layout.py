import streamlit as st

def style_base_background():
  st.markdown("""
    <style>
       .stApp{
        background : #8DA1FF  !important;
            }

        .stApp div[data-testid="stColumn"]{
            background-color : #C7D5F0 !important;
            padding : 2.5rem !important;
            border-radius : 5rem !important;
        }    
    </style>
       """,

       unsafe_allow_html=True)


def style_base_all():
  st.markdown("""
    <style>
       .stApp{
        background : #E0E3ff  !important;
            }
    </style>
       """,

       unsafe_allow_html=True)
  
def style_base_layout():
  st.markdown("""
    <style>
      @import url('https://fonts.googleapis.com/css2?family=Alfa+Slab+One&family=Black+Ops+One&family=Outfit:wght@100..900&display=swap');
      @import url('https://fonts.googleapis.com/css2?family=Black+Ops+One&family=Outfit:wght@100..900&display=swap');
      @import url('https://fonts.googleapis.com/css2?family=Climate+Crisis:YEAR@1979&family=Montserrat:ital@0;1&display=swap');
      @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@100..900&display=swap');
        /* hide top bar of streamlit */
           #MainMenu,border{
             visibility : hidden;
             }  
           
         .block-container {
            padding-top : 1.5rem !important;
            }
          
          h1{
             font-family : "Alfa Slab One" , sans-serif !important;
             font-size : 4.5rem !important;
             line-height : 2.4rem important;
             margin-bottom : 0rem !important
             } 
          h2{
                font-family : "Black Ops One" , sans-serif !important;
                font-size : 2.5rem !important;
                line-height : 0.8 !important;
                margin-bottom : 0rem !important;
                display: flex !important;
                justify-content: center !important; /* Left-Right se center karega */
                align-items: center !important;     /* Top-Bottom se center karega */
}
                 } 
          h3,h4,p{
             font-family : "Outfit" , sans-serif !important
          }
          button{
                     border-radius :1.5rem !important;
                     background : #5865F2 !important;
                     color : white !important;
                     padding : 10px 20px !important;
                     border : none !important;
                     transition : transform 0.25s ease-in-out !important;
                     }       
         button[kind="secondary"]{
                     border-radius :1.5rem !important;
                     background : #EB459E !important;
                     color : white !important;
                     padding : 10px 20px !important;
                     border : none !important;
                     transition : transform 0.25s ease-in-out !important;
           }  
         button[kind="tertiary"]{
                      border-radius :1.5rem !important;
                      background : black !important;
                      color : white !important;
                      padding : 10px 20px !important;
                      border : none !important;
                      transition : transform 0.25s ease-in-out !important;
                      }  
         button:hover{
            transform : scale(1.05)
         }            
        
                      
    </style>
       """,

       unsafe_allow_html=True)  

  
    