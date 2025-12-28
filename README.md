# SmishGuard: Security Dashboard

**The official User Interface for the SmishGuard AI System.**
This dashboard allows users to interact with the backend API, scan SMS messages in real-time, and visualize threat levels for Hate Speech, Violence, and Phishing attempts.

## Live Demo
**Try it here:** https://smishgaurd-demo.streamlit.app

## Features
* **Real-Time Analysis:** Connects instantly to the Azure Serverless Backend.
* **Visual Alerts:** Status indicators for immediate risk assessment.
* **Detailed Reporting:** Displays severity scores (0-6) for multiple threat categories.

## Tech Stack
* **Framework:** Streamlit (Python)
* **Connectivity:** HTTP Requests (REST API)
* **Hosting:** Streamlit Cloud

## How to Run Locally
If you want to run this dashboard on your own machine:

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/devrxify/SmishGaurd-Frontend.git](https://github.com/devrxify/SmishGaurd-Frontend.git)

2. **Install Dependencies:**
```bash
pip install -r requirements.txt
```

3. **Run the app:**
```bash
streamlit run app.py
```

*Part of the SmishGuard Project*