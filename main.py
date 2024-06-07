from data_from_excel import * 
from find_similarity import *
from generate_embeddings import *


if __name__ == "__main__":
   
    file_path = "./data/testing_data.xlsx" 
    questions, answers = read_excel(file_path)
    
    # Générer des embeddings pour les questions
    embeddings = generate_embeddings(questions)
    
    # Stocker les embeddings dans Chroma
    collection = store_embeddings(questions, embeddings, answers)
    
    # Exemple de question utilisateur
    user_question = "Qu'est ce que la culture agroforestière ?"

    
    # Trouver la réponse la plus proche
    question, answer = find_closest_answer(collection, user_question)
    print("question utilisateur:", user_question, "question trouvée", question, "Réponse trouvée :", answer)
   