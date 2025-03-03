import os
from langchain_community.chat_models import ChatOpenAI
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.schema import HumanMessage
from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

llm = ChatOpenAI(
    api_key=api_key,
    temperature=0.7,
    model_name="gpt-3.5-turbo",
    streaming=True,
    callbacks=[StreamingStdOutCallbackHandler()]
)

messages = [HumanMessage(content="What is the smell of rain")]
llm(messages)
