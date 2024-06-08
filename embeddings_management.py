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

    def get_query_embedding(self, user_question):
        response = ollama.embeddings(model=self.model_name, prompt=user_question)
        return response["embedding"]
        
        
        