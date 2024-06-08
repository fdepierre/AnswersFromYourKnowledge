import chromadb
import json

class StoreEmbeddings:
    def __init__(self, collection_name):
        self.collection_name = collection_name
        self.client = chromadb.Client()
        self.collection = self.client.create_collection(name=self.collection_name)

    def store_embeddings(self, questions, embeddings, answers):
        for i, (question, embedding, answer) in enumerate(zip(questions, embeddings, answers)):
            document = {"question": question, "answer": answer}
            json_document = json.dumps(document)
            self.collection.add(ids=[str(i)], embeddings=[embedding], documents=[json_document])
        return self.collection


    def find_closest_answer(self, query_embedding):
        results = self.collection.query(query_embeddings=[query_embedding], n_results=1)
        closest_document_json = results['documents'][0].pop()
        closest_document = json.loads(closest_document_json)
        return closest_document["question"], closest_document["answer"]