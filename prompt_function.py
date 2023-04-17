import os
import json
from langchain.chat_models import ChatOpenAI
from langchain import (
    PromptTemplate, LLMChain, OpenAI
)
from langchain.chains import AnalyzeDocumentChain
from langchain.prompts.chat import (
    ChatPromptTemplate, SystemMessagePromptTemplate,
    AIMessagePromptTemplate, HumanMessagePromptTemplate,
)
from langchain.chains.question_answering import load_qa_chain
from langchain.schema import AIMessage, HumanMessage, SystemMessage


class Chatbot:
    def __init__(self):
        with open('secrets.json') as f:
            secrets = json.load(f)

        os.environ["OPENAI_API_KEY"] = secrets['OPENAI_API_KEY']

        self.llm = OpenAI(temperature=0)

        with open("model_input/mh_advice.txt", encoding='utf-8') as f:
            self.dating_advice = f.read()

        self.qa_chain = load_qa_chain(self.llm, chain_type="map_reduce")
        self.qa_document_chain = AnalyzeDocumentChain(combine_docs_chain=self.qa_chain)

    def run_qa(self, question):
        return self.qa_document_chain.run(input_document=self.dating_advice, question=question)

    