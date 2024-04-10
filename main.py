import os
from dotenv import load_dotenv
from llama_index.core import VectorStoreIndex
from llama_index.readers.web import SimpleWebPageReader


def main (url:str) -> None:
    prompt = "who is the writer and illustrator of lightnovel konosuba?"
    documents = SimpleWebPageReader(html_to_text=True).load_data(urls=[url])
    index = VectorStoreIndex.from_documents(documents=documents)
    query_engine = index.as_query_engine()
    response = query_engine.query(prompt)
    print("prompt : " ,prompt)
    print("response : ", response)
    
if __name__ == "__main__":
    load_dotenv()
    main(url="https://en.wikipedia.org/wiki/KonoSuba")