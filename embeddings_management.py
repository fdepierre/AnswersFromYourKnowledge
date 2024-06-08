import ollama
import json
 
class EmbeddingsManagement:
    def __init__(self, model_name):
        self.model_name = model_name

    def generate_embeddings(self, questions):
        embeddings = []
        for question in questions:
            response = ollama.embeddings(model=self.model_name, prompt=question)
            embeddings.append(response["embedding"])
        return embeddings 

        
    def find_closest_answer(self, collection, user_question):
            response = ollama.embeddings(model=self.model_name, prompt=user_question)
            query_embedding = response["embedding"]
            results = collection.query(query_embeddings=[query_embedding], n_results=1)
            closest_document_json = results['documents'][0].pop()
            closest_document = json.loads(closest_document_json)
            return closest_document["question"], closest_document["answer"]
        
        