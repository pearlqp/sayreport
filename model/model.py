# 定义大模型的操作方法
from langchain_openai import ChatOpenAI
from langchain import PromptTemplate

def create_model():
    llm = ChatOpenAI(
        # 1、模型的名字
        model="glm-4-0520",
        # 2、api_key
        api_key="c8770ad734df780d19f41d82b143c312.Sh22ZMzy9ErmPOkL",
        # 3、温度创新性 0-1
        temperature=0.1,
        # 4、接口的地址
        base_url="https://open.bigmodel.cn/api/paas/v4/"
    )
    return llm

def model_invoke(message):
    llm = create_model()
    result = llm.invoke(message)
    return result.content

def create_prompt_chain():
    prop = PromptTemplate(
        input_variables=["context"],
        template="""
           你是一个生物学家，只能回答和生物学相关或有联系的问题，其他问题你都回答不知道,不需要加任何解释。用户输入的问题是：{context}
        """
    )
    llm = create_model()
    chain = prop | llm
    return chain
# 通过langchain链实现结果的调用
def chain_invoke(message):
    chain = create_prompt_chain()
    result = chain.invoke(message)
    return result.content