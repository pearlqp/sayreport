import streamlit as st
st.title("诗词风格选择页面")
if "fengge" not in st.session_state:
    st.session_state.fengge = ""
bt = st.button("婉约派")
if bt:
    st.session_state.fengge="婉约派"
    st.switch_page("pages/aiclever.py")
bt1 = st.button("豪放派")
if bt1:
    st.session_state.fengge="豪放派"
    st.switch_page("pages/aiclever.py")
bt2 = st.button("想象色彩")
if bt2:
    st.session_state.fengge="想象色彩"
    st.switch_page("pages/aiclever.py")