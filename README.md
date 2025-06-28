# Delay 🦙 ```delayllamma.streamlit.app```

A web application that leverages cutting-edge AI/ML (using OpenAI’s Gemini API) to predict flight delays and generate tailored advisory notes for stakeholders in the aviation industry — including airport ground staff, airline operators, pilots, and passengers.

---

## 🔥 Features

- **Predict flight delays** based on dynamic input parameters like temperature, wind speed, and visibility.  
- Generate **customized advisory notes** for multiple aviation stakeholders.  
- Beautiful, responsive **Streamlit frontend** with intuitive input sliders and sleek dark-themed cards.  
- Interactive UI with **hover glow effects** and aircraft background imagery for an immersive experience.  
- Downloadable advisory reports for offline use.  
- Powered by FastAPI backend integrating OpenAI Gemini API for advanced AI inference.

---

## 🛠️ Tech Stack

- **Backend:** FastAPI  
- **Frontend:** Streamlit  
- **AI Integration:** OpenAI Gemini API  
- **Hosting/Deployment:** Streamlit Cloud (or your preferred cloud platform)  
- **Version Control:** Git + GitHub

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8+  
- `pip` package manager  
- Gemini API Key (with Gemini access)

### Installation

1. Clone the repo:
   ```bash
   git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
   cd YOUR_REPO_NAME
2. Create and activate a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   .\venv\Scripts\activate   # Windows
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
4. Set your Gemini API key as an environment variable:
   ```bash
   export Gemini_API_KEY="your_api_key_here"      # Linux/macOS
   set Gemini_API_KEY="your_api_key_here"         # Windows

### Running Locally
Start the backend FastAPI server:
```bash
python -m uvicorn app:app --reload
```
Run the Streamlit frontend:
```bash
python -m streamlit run frontend_app.py
```
Open your browser at ```http://localhost:8501``` to interact with the app.

### 📝 Usage
1. Adjust the weather parameters using the sliders (temperature, wind speed, visibility).
2. Click Predict Delay and Generate Advisory.
3. View the predicted delay time and detailed advisory notes for airport ground staff, airline operators, pilots, and passengers.
4. Download the advisory report as a text file.

### 📁 Project Structure
```bash
.
├── app.py              # FastAPI backend server
├── frontend_app.py     # Streamlit frontend UI
├── requirements.txt    # Python dependencies
├── README.md           # Project documentation
└── .gitignore          # Git ignore rules
```

### 🌍 UN Sustainable Development Goals (SDGs)
This project aligns primarily with:
SDG 9: Industry, Innovation and Infrastructure — by enhancing aviation operational efficiency using AI.
SDG 11: Sustainable Cities and Communities — by improving transportation reliability and passenger experience.

### 🙌 Contribution
Feel free to fork the repo, create branches for new features or fixes, and submit pull requests.
Open issues for bugs or feature requests are also welcome.

### 📞 Contact
For questions or collaboration opportunities, please contact saadlacas@gmail.com | anthonyma59727@gmail.com | thomas.wang0421@gmail.com | Emrannkemall@gmail.com
