from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

from app.config import settings
from app.prompts import MAP_PROMPT_TEMPLATE, COMBINE_PROMPT_TEMPLATE

def build_llm():
    return ChatGoogleGenerativeAI(
        model = settings.GEMINI_MODEL,
        gemini_api_key = settings.GEMINI_API_KEY,
        temperature = 0
    )

def build_map_chain():
    prompt = ChatPromptTemplate.from_template(MAP_PROMPT_TEMPLATE)
    llm = build_llm()
    parser = StrOutputParser()
    return prompt | llm | parser

def build_combine_chain():
    prompt = ChatPromptTemplate.from_template(COMBINE_PROMPT_TEMPLATE)
    llm = build_llm()
    parser = StrOutputParser()
    return prompt | llm | parser