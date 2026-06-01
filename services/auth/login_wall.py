import streamlit as st
from services.persistence.exercise_repository import get_or_create_user

def render_login_wall():
    if st.session_state.get('user_id') is not None:
        return True
    
    st.markdown("""
<div style="
text-align:center;
padding:25px;
border-radius:20px;
background:linear-gradient(135deg,#0f172a,#1e293b);
margin-bottom:20px;
">
<h1 style="color:white;">
🏋️ AI Gym Coach
</h1>

<p style="color:#cbd5e1;font-size:18px;">
Real-Time Pose Detection • AI Voice Coaching • Rep Tracking
</p>
</div>
""", unsafe_allow_html=True)
    

    with st.form('login_form', clear_on_submit=False):
        username=st.text_input("name (unique)",placeholder="unique name e.g Sharma")
        submit_button=st.form_submit_button('start session',width='stretch')


    

    if submit_button:
        if not username:
            st.error("Name cannot be empty.")
            return False
        

        user= get_or_create_user(username)
        
        st.session_state['user_id']= user['id']
        st.session_state['username'] = user['username']
    

        st.rerun()


    return False  


