# ♟️ Gesture Controlled Chess AI

Gesture Controlled Chess AI is an interactive chess system that allows players to **play chess using hand gestures detected through a webcam**.

The project combines **Computer Vision 👁️, Artificial Intelligence 🧠, and Game Logic ♟️** to create a unique chess experience. Hand gestures are detected using **MediaPipe**, processed with **OpenCV**, and the chess game is handled using **python-chess** and **Pygame**.

The project also integrates the **Groq API ⚡** to provide AI-powered chess insights and move analysis.

---

# ✨ Features

♟️ Play chess against an **AI opponent**
🖐️ Control chess pieces using **hand gestures**
📷 **Real-time webcam** gesture detection
🧠 AI-powered **chess move analysis** using Groq API
🎮 Interactive **chess board interface** using Pygame
⚡ Fast and responsive gameplay

---

# 🧠 Technologies Used

* Python 🐍
* OpenCV – Computer vision processing
* MediaPipe – Hand tracking and gesture detection
* Pygame – Chess board interface
* python-chess – Chess game logic
* Groq API – AI-powered move analysis

---

# 📂 Project Structure

```id="x0lykl"
Chess-AI
│
├── chess AI.py
├── requirements.txt
├── README.md
└── LICENSE
```

---

# ⚙️ Installation

## 1️⃣ Clone the Repository

```id="lfa0sy"
git clone https://github.com/rsamwilson2323-cloud/Chess-AI.git
cd Chess-AI
```

---

## 2️⃣ Install Dependencies

```id="sj4p4o"
pip install -r requirements.txt
```

---

# 🔑 Groq API Setup

This project uses the **Groq API** for AI-powered chess insights.

### Step 1 — Create a Groq Account

Go to the Groq Console:

https://console.groq.com/

Sign up or log in.

---

### Step 2 — Generate an API Key

1. Open **API Keys**
2. Click **Create API Key**
3. Copy the generated key

Example:

```
gsk_xxxxxxxxxxxxxxxxxxxxxxxxx
```

---

### Step 3 — Add the API Key to the Code

Open the file:

```
chess AI.py
```

Find this section:

```id="oetg0p"
from groq import Groq

client = Groq(api_key="YOUR_API_KEY_HERE")
```

Replace it with your actual API key:

```id="wff3nh"
from groq import Groq

client = Groq(api_key="gsk_your_actual_api_key_here")
```

---

# ▶️ Usage

Run the program:

```id="u32qrs"
python "chess AI.py"
```

📷 The webcam will start automatically and begin detecting hand gestures.

To exit the program:

**Press ENTER ⏎**

---

# 🖐️ Gesture Controls

| Gesture              | Action                     |
| -------------------- | -------------------------- |
| Hand detection       | Activates gesture tracking |
| Finger movement      | Select chess pieces        |
| Gesture confirmation | Perform the move           |

⚠️ Gesture accuracy may vary depending on **lighting and camera quality**.

---

# ⚙️ How It Works

1️⃣ The webcam captures **hand movements**
2️⃣ **MediaPipe** detects and tracks hand landmarks
3️⃣ Gesture movements are converted into **chess commands**
4️⃣ The **python-chess engine** validates moves
5️⃣ The **Groq AI assistant** provides move analysis
6️⃣ **Pygame** displays the chess board and updates moves

---

# 🚀 Future Improvements

♟️ Stronger chess AI engine integration
🎙️ Voice control support
🌐 Online multiplayer mode
🤖 Improved gesture recognition accuracy
📊 AI-based move explanations

---

# 👨‍💻 Author

**Sam Wilson**

🌐 GitHub
https://github.com/rsamwilson2323-cloud

💼 LinkedIn
https://www.linkedin.com/in/sam-wilson-14b554385

---

# 📜 License

This project is licensed under the **MIT License**.
