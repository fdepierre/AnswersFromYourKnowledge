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