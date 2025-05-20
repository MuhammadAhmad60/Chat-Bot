from flask import Flask, render_template, request, jsonify
from langchain_ollama import OllamaLLM # Correct import from the new package
from langchain.prompts import ChatPromptTemplate
from langchain.schema import StrOutputParser
from langchain.schema.runnable import RunnablePassthrough
import json

app = Flask(__name__)

# Initialize the Ollama model with the correct package
model = OllamaLLM(model="gemma:2b")

# Define the prompt template
template = """You are a helpful AI assistant named NeoChat. Answer the user's question thoughtfully and concisely.

Question: {question}

Answer:"""
prompt = ChatPromptTemplate.from_template(template)


@app.route("/")
def index():
    return render_template("index.html")   # templates/index.html

# Create the chain
chain = (
    {"question": RunnablePassthrough()} 
    | prompt
    | model
    | StrOutputParser()
)

@app.route('/api/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json()
        user_message = data.get('message', '')
        session_id = data.get('session_id', '')
        
        # Get response from the chain
        response = chain.invoke({"question": user_message})

        
        return jsonify({
            'response': response,
            'session_id': session_id
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)