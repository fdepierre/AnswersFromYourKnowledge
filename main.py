import embeddings_management as ge
import data_from_excel as de
import embeddings_storage as es
import os

if __name__ == "__main__":
    
    relative_file_path = "./data/testing_data.xlsx"
    absolute_file_path = os.path.abspath(relative_file_path)
    data_reader = de.DataFromExcel(absolute_file_path)
    questions, answers = data_reader.read_excel()
    
    embedding_generator = ge.EmbeddingsManagement(model_name="llama2")
    embeddings = embedding_generator.generate_embeddings(questions)
    
    storage = es.StoreEmbeddings(collection_name="qa_collection")
    collection = storage.store_embeddings(questions, embeddings, answers)
    
    user_question = "Qu'est ce que la culture agroforestière ?"
    query_embedding = embedding_generator.get_query_embedding(user_question)
    
    question, answer = storage.find_closest_answer(query_embedding)
    print("question utilisateur:", user_question, "question trouvée", question, "Réponse trouvée :", answer)
