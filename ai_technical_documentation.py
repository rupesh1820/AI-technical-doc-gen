from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

prompt = ChatPromptTemplate.from_template("""
You are an expert Technical Documentation Generator.

Convert the following feature description into professional Markdown documentation.

Include:
- Overview
- Objectives
- Functional Requirements
- System Architecture
- Workflow
- API Design
- Database Design
- Security
- Testing
- Deployment
- Future Enhancements

Feature:
{feature}
""")

chain = prompt | llm

feature = input("Enter Feature Description: ")

result = chain.invoke({"feature": feature})

print(result.content)

