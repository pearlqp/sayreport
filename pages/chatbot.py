
import streamlit as st
st.title('AI应用🏔️🏔️🏔️')

col,col1,col2 = st.columns(3)
with col:
    #st.image("http://gips1.baidu.com/it/u=3679066767,3429623176&fm=3042&app=3042&f=JPEG&wm=1,huayi,0,0,13,9&wmo=0,0")
    bt = st.button("小白助手")
    if bt:
        st.switch_page("pages/小白report.py")
with col1:
    bt1 = st.button("生物悉知")
    if bt1:
        st.switch_page("pages/anquess.py")
with col2:
    bt2 = st.button("时空诗词猎人")
    if bt2:
        st.switch_page("pages/friend.py")
