import ollama
import chromadb
import json

from data_from_excel import read_excel

"""toto"""
def generate_embeddings(questions):
    embeddings = []
    for question in questions:
        response = ollama.embeddings(model="llama2", prompt=question)
        embeddings.append(response["embedding"])
    return embeddings

def store_embeddings(questions, embeddings, answers):
    client = chromadb.Client()
    collection = client.create_collection(name="qa_collection")
    for i, (question, embedding, answer) in enumerate(zip(questions, embeddings, answers)):
        document = {"question": question, "answer": answer}
        json_document = json.dumps(document)
        collection.add(ids=[str(i)], embeddings=[embedding], documents=[json_document])
    return collection



   