import streamlit as st
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.memory import ConversationBufferMemory # 在内存中保存历史记忆的模块
from langchain.chains import ConversationChain

st.title('我的诗词仙人')
st.subheader("品古风诗词，看时空穿梭")
col,col1 = st.columns([8,2])
with col:
    st.text("蓬莱仙山，大梦三千！")
with col1:
    back = st.button("返回")
    if back:
        st.switch_page("pages/chatbot.py")

llm = ChatOpenAI(
        model="glm-4-0520",
        api_key="c8770ad734df780d19f41d82b143c312.Sh22ZMzy9ErmPOkL",
        temperature=0.5,
        base_url="https://open.bigmodel.cn/api/paas/v4/"
    )

if "gms" not in st.session_state:
    st.session_state.gms =[]

for gm in st.session_state.gms:
    with st.chat_message(gm["role"]):
        st.write(gm["context"])


# 构建记忆模块
if "memory" not in st.session_state:
    st.session_state.memory = ConversationBufferMemory()
# 通过链把三个模块给连接起来
# ConversationChain链之所以能所以历史记忆存储，主要是因为会做一件事情，会把memory记忆模块中的数据以history参数名的形式
# 封装到链的PromptTemplate提示词模板当中
temp = "现在你要扮演的是一个古代诗词创作大家，你的诗词风格是"+st.session_state.fengge+"，你只需要回答他问你的话即可，也不需要将你的角色和性格进行展示。说的话是:{input},你们的以前的对话是{history}"
prompt = PromptTemplate(
    input_variables=["input","history"],
    template=temp
)
chain = ConversationChain(
    prompt=prompt,
    llm=llm,
    memory=st.session_state.memory
)

input = st.chat_input("和古人一起写诗吧")
if input:
    with st.chat_message("user"):
        st.write(input)
    st.session_state.gms.append({"role":"user","context":input})
    # 调用大模型回答我们的问题
    result = chain.invoke(input)
    # 带有记忆的链result中没有content,
    with st.chat_message("assistant"):
        st.write(result["response"])
    st.session_state.gms.append({"role":"assistant","context":result["response"]})
