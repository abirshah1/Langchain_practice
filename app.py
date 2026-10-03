import streamlit as st
from chatbot import get_response

st.set_page_config(page_title="LangChain Chatbot", layout="wide")
st.title("LangChain Chatbot")
st.caption("RunnableBranch • RunnableParallel • Pydantic Structured Output")

if "messages" not in st.session_state:
    st.session_state.messages = []   

with st.sidebar:
    st.header("Controls")
    if st.button("Clear Chat"):
        st.session_state.messages = []
        st.rerun()
    st.markdown("---")
    st.markdown("**Try:**")
    st.markdown("- *Write a Python function to reverse a string*")
    st.markdown("- *Solve x^2 - 5x + 6 = 0*")
    st.markdown("- *What is the capital of Japan?*")

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

user_input = st.chat_input("Ask me anything…")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):
        with st.spinner("Thinking…"):
            try:
                result = get_response(user_input)
                resp = result["response"]        
                keywords = result["keywords"]

                st.markdown(f"###Answer\n{resp.answer}")
                st.markdown(f"**Summary:** {resp.summary}")
                st.markdown(
                    f"**Category:** `{resp.category}` &nbsp;|&nbsp; "
                    f"**Confidence:** `{resp.confidence:.2f}`"
                )
                st.markdown(
                    "**Keywords:** " + ", ".join(f"`{k}`" for k in keywords)
                )

                st.session_state.messages.append({
                    "role": "assistant",
                    "content": (
                        f"**Answer:** {resp.answer}\n\n"
                        f"**Summary:** {resp.summary}\n\n"
                        f"**Category:** {resp.category} | "
                        f"**Confidence:** {resp.confidence:.2f}\n\n"
                        f"**Keywords:** {', '.join(keywords)}"
                    ),
                })
            except Exception as e:
                st.error(f"Error: {e}")