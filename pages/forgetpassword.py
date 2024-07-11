
'''
import streamlit as st
import data.data as dd
# 设置页面的标签页的名字和icon
st.set_page_config(
    page_title="忘记密码",
    page_icon="🔒"
)
st.title("忘记密码")

#username = st.text_input("请输入手机号")
#password = st.text_input("请输入密码",type="password")
#repass = st.text_input("请再次输入密码",type="password")
#forgotPasswordFlag = st.button("忘记密码？请修改")
phone_number = st.text_input("请输入您的手机号")
# 用户输入新密码和确认密码
new_password = st.text_input("请输入新密码", type="password")
confirm_password = st.text_input("请再次输入新密码", type="password")

# 修改密码按钮
update_password_button = st.button("修改密码")
'''

import streamlit as st
import time
import data.data as dd

# 设置页面的标签页的名字和icon
st.set_page_config(
    page_title="忘记密码",
    page_icon="🔒"
)

st.title("忘记密码")
# 用户输入手机号
phone_number = st.text_input("请输入您的手机号")
# 用户输入新密码和确认密码
new_password = st.text_input("请输入新密码", type="password")
confirm_password = st.text_input("请再次输入新密码", type="password")
# 修改密码按钮
update_password_button = st.button("修改密码")
# 定义修改密码的函数
def update_password(phone_number, new_password, confirm_password):
    # 校验两次密码是否一致
    if new_password != confirm_password:
        st.error("两次输入的密码不一致，请重新输入！")
        return
    # 根据手机号查询用户信息
    user = dd.query_user_by_username(phone_number)
    if user is None:
        st.error("手机号未注册，请先注册")
        return
    # 更新密码
    if dd.update_password_by_user_id(user['user_id'], new_password):
        st.success("密码修改成功，请使用新密码登录。")
        time.sleep(2)
        st.switch_page("login.py")
    else:
        st.error("密码修改失败，请稍后重试。")
# 如果修改密码按钮被点击
if update_password_button:
    if phone_number and new_password and confirm_password:
        update_password(phone_number, new_password, confirm_password)
    else:
        st.error("请填写所有必要的信息。")
