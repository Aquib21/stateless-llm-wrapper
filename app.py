# Standard library imports
import torch

# Third-party library imports
import flask
from flask import Flask, request, jsonify
import langchain
from langchain.chains import LLMChain
from langchain.llm import LLM
from transformers import GPT2Tokenizer, GPT2Model

app = Flask(__name__, template_folder='templates', static_folder='static')
tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
model = GPT2Model.from_pretrained('gpt2')
lc=langchain.Langchain()


# Local application imports
# (none in this case, since it's a single file app)


# Load the pre-trained LLM model
@app.route('/query', methods=['POST'])
def process_query():
    query = request.get_json()['query']
    # Process query using LLM and LangChain
    response = process_query_with_llm_and_langchain(query)
    return jsonify({'response': response})

def process_query_with_llm_and_langchain(query):
    # Tokenize input query
    inputs = tokenizer.encode_plus(
        query,
        add_special_tokens=True,
        max_length=512,
        return_attention_mask=True,
        return_tensors='pt',
    )
     # Generate response using LLM
    outputs = model(inputs['input_ids'],             
    attention_mask=inputs['attention_mask'])
        # Enhance response using LangChain
    response = lc.enhance_response(outputs)
    return response

if __name__ == '__main__':
    app.run(debug=True)
