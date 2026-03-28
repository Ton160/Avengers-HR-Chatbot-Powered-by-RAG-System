from dotenv import load_dotenv
import os

# ============ 🔥 المفتاح الجديد من حسابك ============
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = "Your_LANGCHAIN_API_KEY"  # 🔥 مفتاحك الجديد
os.environ["LANGCHAIN_PROJECT"] = "avengers HR"  # 🔥 أضف هذا

import streamlit as st
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

print("✅ تم إعداد مفاتيح API بنجاح!")

st.title("Avengers Global Alliance Inc.")
st.write("Nick Fury- HR Chatbot")
load_dotenv()

# 🔥 أضف رابط LangSmith للتحقق
with st.sidebar:
    st.subheader("🔍 LangSmith Status")
    st.info("Open: https://smith.langchain.com")
    st.info("Project: avengers-hr-chatbot")

groq_api_key = "your_groq_api_key"

loader = PyPDFLoader("Avengers HR policy Handbook.pdf")
docs = loader.load()
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=50)
splits = text_splitter.split_documents(docs)
vectorstore = Chroma.from_documents(documents=splits, embedding=HuggingFaceEmbeddings())
retriever = vectorstore.as_retriever()

prompt_template = ChatPromptTemplate.from_messages([
    ("system", """You are Nick Fury the HR Director of Avengers Global Alliance Inc Company, 
    as the Avengers movie, answer the HR questions, based on the context provided below only. 
    Provide source metadata from context after your answer"""),
    ("human", """
    Context:
    {context}

    Question:
    {question}
    """)
])

llm = ChatGroq(
    model="moonshotai/kimi-k2-instruct",
    temperature=0.1,
    groq_api_key=groq_api_key
)


def format_docs(docs):
    return "\n\n".join([doc.page_content for doc in docs])


rag_chain = (
        {"context": retriever | format_docs, "question": RunnablePassthrough()}
        | prompt_template
        | llm
        | StrOutputParser()
)

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

user_input = st.chat_input("This is Nick Fury, How can I help you?")

if user_input:
    with st.chat_message("user"):
        st.markdown(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                response = rag_chain.invoke(user_input)
                st.markdown(response)
                st.session_state.messages.append({"role": "assistant", "content": response})

                # Direct Checking Link🔗
                st.markdown("[🔗 Check LangSmith](https://smith.langchain.com/project/avengers-hr-chatbot)")

            except Exception as e:
                error_msg = f"Sorry, I encountered an error: {str(e)}"
                st.error(error_msg)
                st.session_state.messages.append({"role": "assistant", "content": error_msg})
