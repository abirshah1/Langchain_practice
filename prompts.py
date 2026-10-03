from langchain_core.prompts import PromptTemplate

PROGRAMMING_PROMPT = PromptTemplate(
    input_variables=["question"],
    template=(
        "You are an expert programming assistant.\n"
        "Answer the following question with code examples "
        "where helpful, and explain concisely.\n\n"
        "Question: {question}\n\n"
        "Return a structured response with fields: answer, summary, confidence, "
        "category='programming', keywords."
    ),
)

MATH_PROMPT = PromptTemplate(
    input_variables=["question"],
    template=(
        "You are a patient mathematics tutor.\n"
        "Solve the following math problem step-by-step and explain each step.\n\n"
        "Problem: {question}\n\n"
        "Return a structured response with fields: answer, summary, confidence, "
        "category='math', keywords."
    ),
)

GENERAL_PROMPT = PromptTemplate(
    input_variables=["question"],
    template=(
        "You are a helpful, friendly general-purpose assistant.\n"
        "Answer the user's question clearly.\n\n"
        "Question: {question}\n\n"
        "Return a structured response with fields: answer, summary, confidence, "
        "category='general', keywords."
    ),
)

CLASSIFIER_PROMPT = PromptTemplate(
    input_variables=["question"],
    template=(
        "Classify the following user question into exactly ONE of these categories: "
        "'programming', 'math', or 'general'.\n"
        "Reply with ONLY the category word in lowercase.\n\n"
        "Question: {question}\n"
        "Category:"
    ),
)