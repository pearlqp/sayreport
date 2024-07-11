import streamlit as st
import model.model as mm
import data.data as dd


user_id = st.session_state.get('user_id', None)  # 使用get方法以防user_id未设置
username = st.session_state.get('username', '匿名用户')

st.title("🌴🐟动植物的世界🌴")

# 显示历史消息
messages = dd.do_message_by_user_id(user_id)
if messages:
    with st.expander("历史对话"):
        for msg in messages:
            with st.chat_message(msg["role"]):
                st.write(msg["message"])
                # 如果消息包含时间戳，可以在这里显示
                # st.write(f"({msg['timestamp'][:10]})")
else:
    st.write("暂无历史对话")

col,col1 = st.columns([8,2])
with col:
    st.text("生物历史地图，带你领略生命的传奇")
with col1:
    back = st.button("返回")
    if back:
        st.switch_page("pages/chatbot.py")

# 新对话输入
input_question = st.chat_input("请输入你要询问的问题")
if input_question:
    # 显示用户消息
    with st.expander("新对话（用户）"):
        with st.chat_message("user"):
            st.write(input_question)
            # 调用模型获取响应
    result = mm.chain_invoke({"context": input_question})
    # 将用户消息和助手响应存储到数据库（这里假设已正确实现）
    dd.add_answer_message(user_id, input_question, "user")
    dd.add_answer_message(user_id, result, "assistant")
    # 显示助手消息
    with st.expander("新对话"):
        with st.chat_message("assistant"):
            st.write(result)