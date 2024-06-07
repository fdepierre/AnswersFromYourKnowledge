import ollama
import chromadb
import json

from data_from_excel import read_excel

def find_closest_answer(collection, user_question):
    response = ollama.embeddings(model="llama2", prompt=user_question)
    query_embedding = response["embedding"]
    results = collection.query(query_embeddings=[query_embedding], n_results=1)
    closest_document_json = results['documents'][0].pop()  # Accéder au premier élément de la liste
    closest_document = json.loads(closest_document_json)  # Convertir la chaîne JSON en dictionnaire
    return closest_document["question"],closest_document["answer"]



   