from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.runnables import (
    RunnableBranch,
    RunnableParallel,
    RunnableLambda,
)
from langchain_core.output_parsers import StrOutputParser

from prompts import (
    PROGRAMMING_PROMPT,
    MATH_PROMPT,
    GENERAL_PROMPT,
    CLASSIFIER_PROMPT,
)
from schemas import ChatResponse

load_dotenv()

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.3,
)

structured_llm = llm.with_structured_output(ChatResponse)

classifier_chain = (
    CLASSIFIER_PROMPT
    | llm
    | StrOutputParser()
    | RunnableLambda(lambda s: s.strip().lower())
)

programming_chain = PROGRAMMING_PROMPT | structured_llm
math_chain        = MATH_PROMPT        | structured_llm
general_chain     = GENERAL_PROMPT     | structured_llm

branch = RunnableBranch(
    (lambda x: _route(x["question"]) == "programming", programming_chain),
    (lambda x: _route(x["question"]) == "math",        math_chain),
    general_chain,   
)

_route_cache: dict[str, str] = {}

def _route(question: str) -> str:
    if question not in _route_cache:
        _route_cache[question] = classifier_chain.invoke({"question": question})
    return _route_cache[question]

answer_and_keywords = RunnableParallel(
    response=branch,                                  
    keywords=RunnableLambda(
        lambda x: branch.invoke(x).keywords
    ),                                                
)

def get_response(question: str) -> dict:
    return answer_and_keywords.invoke({"question": question})