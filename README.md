♟️ Gesture Controlled Chess AI

Gesture Controlled Chess AI is a computer vision–based chess game that allows players to control the chessboard using hand gestures instead of a mouse or keyboard. The system tracks hand movements using a webcam and converts them into cursor actions, creating an interactive and futuristic chess playing experience.

The project combines Computer Vision, Artificial Intelligence, and Game Development technologies. Using real-time hand tracking, players can move a virtual cursor with their index finger and perform a pinch gesture to select or move chess pieces. After the player makes a move, the AI automatically calculates its response and plays against the user.

This project demonstrates how AI and vision-based interaction systems can be integrated into traditional games to create new ways of human-computer interaction.

🚀 Features

🖐 Hand gesture chess control

🎥 Real-time hand tracking using MediaPipe

♟ Interactive chess board interface

🤖 AI opponent for automatic moves

🔴 Pinch gesture to select and move pieces

🏁 Checkmate detection

🔄 Game reset option

📷 Live camera preview during gameplay

🧠 How It Works

The webcam captures the player's hand movements.

MediaPipe Hands detects hand landmarks.

The index finger tip controls the cursor on the chess board.

A pinch gesture (thumb + index finger) acts as a click action.

When the player makes a move, the AI calculates the best response and plays automatically.

🛠 Technologies Used

Python

OpenCV

MediaPipe

Pygame

Python-Chess

Groq API (LLaMA AI)

📦 Installation
1️⃣ Clone the repository
git clone https://github.com/rsamwilson2323-cloud/Chess-AI.git
cd Chess-AI
2️⃣ Install dependencies
pip install -r requirements.txt
▶️ Run the Project
python "chess AI.py"

The application will start in fullscreen mode and activate the webcam for gesture detection.

🎮 Controls
Action	Gesture / Key
Move Cursor	Index Finger
Select Piece	Pinch Gesture
Move Piece	Pinch Again
Reset Game	SPACE
Exit Game	ENTER
📂 Project Structure
Chess-AI
│
├── chess AI.py
├── requirements.txt
├── README.md
└── LICENSE
🔮 Future Improvements

Possible upgrades for this project:

Stronger chess engine (Stockfish)

Improved gesture detection

Drag-and-drop piece movement

AI difficulty levels

Multiplayer support

UI enhancements

👨‍💻 Author

Sam Wilson

🌐 GitHub
https://github.com/rsamwilson2323-cloud

💼 LinkedIn
https://www.linkedin.com/in/sam-wilson-14b554385

⭐ Support

If you like this project:

⭐ Star the repository
🍴 Fork the project
🧠 Contribute improvements
