import openpyxl
import ollama
import chromadb
import json

def read_excel(file_path):
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook.active
    questions = []
    answers = []
    for row in sheet.iter_rows(min_row=2, values_only=True):
        questions.append(row[0])
        answers.append(row[1])
    return questions, answers


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

def find_closest_answer(collection, user_question):
    response = ollama.embeddings(model="llama2", prompt=user_question)
    query_embedding = response["embedding"]
    results = collection.query(query_embeddings=[query_embedding], n_results=1)
    closest_document_json = results['documents'][0].pop()  # Accéder au premier élément de la liste
    closest_document = json.loads(closest_document_json)  # Convertir la chaîne JSON en dictionnaire
    return closest_document["question"],closest_document["answer"]



if __name__ == "__main__":
   
    file_path = "data.xlsx" 
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
   