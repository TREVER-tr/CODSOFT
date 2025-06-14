# face detection app
import cv2
import face_recognition

# Load Haar Cascade for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# Load a known image for recognition
known_image = face_recognition.load_image_file("known_face.jpg")
known_encoding = face_recognition.face_encodings(known_image)[0]

# Start webcam for real-time detection and recognition
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Convert frame to grayscale for detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

    # Detect faces and draw bounding boxes
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 3)

    # Face Recognition
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    for face_encoding, (top, right, bottom, left) in zip(face_encodings, face_locations):
        matches = face_recognition.compare_faces([known_encoding], face_encoding)
        name = "Unknown"
        if True in matches:
            name = "Known Face"

        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
        cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

    cv2.imshow("Face Detection & Recognition", frame)

    # Exit on 'q' key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
#recommendation app
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Sample movie dataset
data = {
    'Title': ['Inception', 'Interstellar', 'The Dark Knight', 'Titanic', 'Avatar'],
    'Description': [
        'Dreams within dreams, sci-fi thriller',
        'Space exploration, time dilation, sci-fi',
        'Superhero action movie, Batman fights Joker',
        'Romantic tragedy aboard a sinking ship',
        'Sci-fi world, aliens, adventure'
    ]
}

df = pd.DataFrame(data)

# Convert text descriptions into numerical features
vectorizer = TfidfVectorizer(stop_words="english")
tfidf_matrix = vectorizer.fit_transform(df["Description"])

# Compute cosine similarity between movies
cosine_sim = cosine_similarity(tfidf_matrix)

# Function to recommend movies based on a given title
def recommend_movie(title):
    if title not in df["Title"].values:
        return "Movie not found!"
    
    idx = df.index[df["Title"] == title][0]
    similarity_scores = list(enumerate(cosine_sim[idx]))
    sorted_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)[1:4]
    
    recommendations = [df.iloc[i[0]]["Title"] for i in sorted_scores]
    return recommendations

# Example usage
movie_title = "Inception"
print("Recommendations:", recommend_movie(movie_title))
#image captioning
import numpy as np
import tensorflow as tf
from tensorflow.keras.applications import ResNet50
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Model, load_model
from tensorflow.keras.layers import Embedding, LSTM, Dense, Input
import pickle
import cv2

# Load pre-trained ResNet50 model for feature extraction
resnet = ResNet50(weights='imagenet', include_top=False, pooling="avg")

def extract_features(image_path):
    image = load_img(image_path, target_size=(224, 224))
    image_array = img_to_array(image)
    image_array = np.expand_dims(image_array, axis=0)
    image_array /= 255.0
    return resnet.predict(image_array)

# Load vocabulary and trained LSTM model (Assume pre-trained model is available)
with open("tokenizer.pkl", "rb") as f:
    tokenizer = pickle.load(f)
model = load_model("caption_model.h5")

# Generate captions from image features
def generate_caption(image_path, max_length=20):
    features = extract_features(image_path)
    sequence = [tokenizer.word_index["startseq"]]
    
    for _ in range(max_length):
        padded_seq = pad_sequences([sequence], maxlen=max_length)
        pred = model.predict([features, padded_seq], verbose=0)
        word_idx = np.argmax(pred)
        word = tokenizer.index_word.get(word_idx, "")
        
        if word == "endseq":
            break
        sequence.append(word_idx)
    
    return " ".join([tokenizer.index_word[i] for i in sequence if i not in ["startseq", "endseq"]])

# Example usage
image_path = "sample_image.jpg"
caption = generate_caption(image_path)
print("Generated Caption:", caption)
#tic-tac-toe
import math

# Define the Tic-Tac-Toe board
board = [[' ' for _ in range(3)] for _ in range(3)]

# Check for a winner
def check_winner(board):
    for row in board:
        if row[0] == row[1] == row[2] != ' ':
            return row[0]
    
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != ' ':
            return board[0][col]
    
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]
    
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]
    
    return None

# Check if the board is full
def is_draw(board):
    return all(cell != ' ' for row in board for cell in row)

# Minimax algorithm for AI moves
def minimax(board, is_maximizing):
    winner = check_winner(board)
    if winner == 'O':
        return 10
    elif winner == 'X':
        return -10
    elif is_draw(board):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    score = minimax(board, False)
                    board[i][j] = ' '  
                    best_score = max(best_score, score)
        return best_score
    else:
        best_score = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    score = minimax(board, True)
                    board[i][j] = ' '  
                    best_score = min(best_score, score)
        return best_score

# Find the best AI move
def find_best_move():
    best_score = -math.inf
    best_move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'O'
                score = minimax(board, False)
                board[i][j] = ' '
                if score > best_score:
                    best_score = score
                    best_move = (i, j)
    return best_move

# Print the board
def print_board():
    for row in board:
        print("|".join(row))
    print("-" * 5)

# Main game loop
def play_game():
    print("Welcome to Tic-Tac-Toe! You are 'X', AI is 'O'.")
    print_board()
    
    for turn in range(9):
        if turn % 2 == 0:
            row, col = map(int, input("Enter row and column (0-2): ").split())
            if board[row][col] == ' ':
                board[row][col] = 'X'
            else:
                print("Invalid move! Try again.")
                continue
        else:
            row, col = find_best_move()
            board[row][col] = 'O'
        
        print_board()

        winner = check_winner(board)
        if winner:
            print(f"Game Over! {winner} wins!")
            return
        elif is_draw(board):
            print("It's a draw!")
            return

play_game()
#chatbot with rule based responses
import re

# Define chatbot responses
def chatbot_response(user_input):
    user_input = user_input.lower()

    # Greetings
    if re.search(r"(hi|hello|hey)", user_input):
        return "Hello! How can I assist you today?"
    
    # Farewell
    elif re.search(r"(bye|goodbye|see you)", user_input):
        return "Goodbye! Have a great day!"
    
    # Asking about the chatbot
    elif re.search(r"(who are you|what is your name)", user_input):
        return "I am a simple chatbot, here to help you!"
    
    # Weather inquiries
    elif re.search(r"(weather|temperature)", user_input):
        return "I can't fetch real-time weather yet, but it's always a good idea to check a weather website!"
    
    # Default response
    else:
        return "I'm not sure how to respond to that, but I'm happy to chat!"

# Run chatbot interaction
print("Chatbot: Hi! Type 'bye' to exit.")
while True:
    user_input = input("You: ")
    if user_input.lower() == "bye":
        print("Chatbot: Goodbye!")
        break
    print("Chatbot:", chatbot_response(user_input))
 



 
