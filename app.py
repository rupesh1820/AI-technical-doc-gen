from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_documentation():
    try:
        data = request.json
        feature = data.get('feature', '')
        temperature = float(data.get('temperature', 0.0))
        
        if not feature.strip():
            return jsonify({'error': 'Please enter a feature description'}), 400
        
        llm = ChatOpenAI(model="gpt-4o-mini", temperature=temperature)
        
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
        result = chain.invoke({"feature": feature})
        
        return jsonify({'documentation': result.content})
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
