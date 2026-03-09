♟️ Gesture Controlled Chess AI
A gesture-controlled Chess AI system that allows players to play chess using hand gestures detected through a webcam.
The project combines Computer Vision, Artificial Intelligence, and Game Logic to create an interactive chess experience. Hand gestures are detected using MediaPipe, processed with OpenCV, and the chess game is managed using python-chess and Pygame.
Additionally, the project integrates the Groq API to provide AI-powered chess insights and move analysis.
🚀 Features
♟️ Play chess against an AI opponent
🖐️ Control chess pieces using hand gestures
📷 Real-time webcam-based gesture detection
🧠 AI-powered chess analysis using Groq API
🎮 Interactive chess board using Pygame
⚡ Fast and responsive gameplay
🧠 Technologies Used
Python
OpenCV – Computer vision processing
MediaPipe – Hand tracking and gesture detection
Pygame – Chess board interface
python-chess – Chess game logic
Groq API – AI-powered move analysis

📂 Project Structure

Chess-AI
│
├── chess AI.py          # Main application
├── requirements.txt     # Required libraries
├── README.md            # Project documentation
└── LICENSE              # License file

⚙️ Installation
1. Clone the Repository
Bash

git clone https://github.com/rsamwilson2323-cloud/Chess-AI.git

cd Chess-AI
2. Install Required Libraries
Bash

pip install -r requirements.txt

🔑 Groq API Setup
This project uses the Groq API for AI-powered chess insights

Step 1 – Create a Groq Account
Go to the Groq Console:
https://console.groq.com/�
Sign up or log in.

Step 2 – Generate an API Key
Open API Keys
Click Create API Key
Copy the generated key

Example:
gsk_xxxxxxxxxxxxxxxxxxxxxxxxx

Step 3 – Add the API Key to the Code
Open the file:

chess AI.py
Find this section:
Python

from groq import Groq

client = Groq(api_key="YOUR_API_KEY_HERE")
Replace it with your actual API key:
Python

from groq import Groq

client = Groq(api_key="gsk_your_actual_api_key_here")

▶️ Running the Project
Run the program using:
Bash

python "chess AI.py"
The webcam will start and the gesture recognition system will begin detecting hand movements.

🖐️ Gesture Controls
Gesture
Action
Hand detection
Activates gesture tracking
Finger movement
Select chess pieces
Gesture confirmation
Perform the move
Gesture recognition may vary depending on lighting and camera quality.

⚙️ How It Works
The webcam captures hand gestures.
MediaPipe detects and tracks hand landmarks.
Gesture movements are converted into chess commands.
The python-chess engine validates the moves.
The AI assistant provides move analysis.
Pygame displays the chess board and updates moves.

💡 Future Improvements
♟️ Stronger chess AI engine integration
🎙️ Voice control support
🌐 Online multiplayer mode
🤖 Improved gesture recognition accuracy
📊 AI-based move explanations

📜 License
This project is licensed under the MIT License.

👨‍💻 Author

Sam Wilson

🔗 GitHub
https://github.com/rsamwilson2323-cloud

🔗 LinkedIn
https://www.linkedin.com/in/sam-wilson-14b554385
