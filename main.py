import langchain
import torch
from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from transformers import GPT2Tokenizer, GPT2Model
tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
model = GPT2Model.from_pretrained('gpt2')
lc = langchain.LangChain()
llm = OpenAI()
chain = LLMChain(llm=llm, prompt=PromptTemplate.from_template("{query}"))
