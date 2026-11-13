# AI Real-Time Gym Coach 🏋️

An AI-powered workout assistant that uses your webcam to track exercise form, count repetitions, monitor movement quality, and provide real-time voice coaching feedback.

This project includes a static landing page and a Streamlit-based web application for guided workout analysis.

## Features

- Real-time pose detection using MediaPipe Pose Landmarker
- Support for five exercises:
  - Squats
  - Push-ups
  - Dumbbell Biceps Curls
  - Shoulder Press
  - Lunges
- Repetition and set tracking
- Form analysis with metrics such as knee angle, elbow angle, alignment, squat depth, and balance
- AI-generated coaching using the Groq API and Llama 3.3 70B
- Text-to-speech feedback using gTTS
- Local workout history in SQLite
- Simple username-based user session tracking

## Tech Stack

| Component | Technology |
|---|---|
| UI | Streamlit |
| Camera streaming | streamlit-webrtc |
| Pose estimation | MediaPipe |
| Image processing | OpenCV |
| Numerical processing | NumPy |
| Local data storage | SQLite |
| Data handling | Pandas |
| AI coaching | Groq API |
| Text-to-speech | gTTS |
| Landing page | HTML + CSS |

## Project Structure

```text
AI-GYM Coach/
├── LandingPage/
│   ├── index.html
│   ├── style.css
│   ├── fonts/
│   ├── IMGs_add_your_own/
│   └── videos_add_your_own/
├── Main App/
│   ├── main.py
│   ├── requirements.txt
│   ├── packages.txt
│   ├── data.db
│   ├── .env
│   ├── ml_models/
│   │   └── pose_landmarker_full.task
│   ├── core/
│   │   └── base_exercise.py
│   ├── detectors/
│   │   ├── squat.py
│   │   ├── pushup.py
│   │   ├── biceps_curl.py
│   │   ├── shoulder_press.py
│   │   └── lunges.py
│   └── services/
│       ├── auth/
│       ├── coaching/
│       ├── config/
│       ├── persistence/
│       ├── state/
│       ├── tracking/
│       ├── ui/
│       └── vision/
├── README.md
└── .gitignore
```

## Requirements

- Python 3.10 or 3.11 recommended
- Webcam
- Internet connection for Groq and gTTS
- Groq API key
- Modern browser with camera permission support

## Quick Start

### 1. Clone the repository

```bash
git clone https://github.com/Nitesh-45/AI-RealTime-GYM-Coach.git
cd AI-RealTime-GYM-Coach
```

### 2. Open the app directory

```bash
cd "Main App"
```

### 3. Create a virtual environment

Windows PowerShell:

```powershell
py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1
```

If activation is blocked:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

macOS / Linux:

```bash
python3.11 -m venv .venv
source .venv/bin/activate
```

### 4. Install dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 5. Configure the Groq API key

Set the environment variable:

Windows PowerShell:

```powershell
$env:GROQ_API_KEY="your_groq_api_key"
```

macOS / Linux:

```bash
export GROQ_API_KEY="your_groq_api_key"
```

Alternatively, create a `.streamlit/secrets.toml` file in `Main App`:

```toml
GROQ_API_KEY = "your_groq_api_key"
```

### 6. Run the app

```bash
streamlit run main.py
```

Then open the local URL shown in the terminal, usually:

```text
http://localhost:8501
```

## How to Use

1. Launch the app and enter a unique username.
2. Choose an exercise from the sidebar.
3. Set the target sets and repetitions.
4. Click **Start Workout**.
5. Allow camera access and position your body clearly in frame.
6. Perform the exercise while the app analyzes your motion.
7. Use the progress section to monitor rep and set counts.
8. Click **End Workout** when finished.

## How It Works

1. Web camera frames are captured through `streamlit-webrtc`.
2. MediaPipe Pose Landmarker detects body landmarks.
3. Exercise-specific detectors calculate form metrics.
4. Repetition thresholds count reps and sets.
5. Coaching events are sent to the Groq-powered LLM.
6. gTTS converts the feedback into spoken audio.
7. SQLite stores workout data and user activity.

## Important Notes

- This is a workout assistance prototype and should not replace a qualified trainer or medical professional.
- Pose estimation depends on camera angle, lighting, and body visibility.
- AI coaching requires a valid Groq API key and an active internet connection.
- gTTS also needs internet access.
- The app is designed for local use and stores data in `Main App/data.db`.
- For production deployment, secure secrets, auth, and camera/WebRTC setup appropriately.

## Troubleshooting

### Pose model not found

Make sure you are running from the `Main App` directory and confirm that `ml_models/pose_landmarker_full.task` exists.

### Webcam not starting

- Allow camera permissions in the browser
- Close other applications using the webcam
- Use localhost or HTTPS in hosted environments

### AI voice feedback unavailable

- Check whether `GROQ_API_KEY` is set correctly
- Confirm the API key is valid and active
- Verify internet connectivity

### Dependency installation issues

- Use Python 3.10 or 3.11
- Upgrade pip before installing packages
- On Linux, install the packages listed in `Main App/packages.txt`

## Contributing

Contributions are welcome.

1. Fork the repository
2. Create a feature branch
3. Implement and test your changes
4. Open a pull request with a clear description

## License

This project is provided for educational and personal use. Add your preferred license before public distribution.

## Disclaimer

This project is intended for fitness assistance and experimentation. It does not provide medical advice or guarantee safe exercise execution in all situations.
