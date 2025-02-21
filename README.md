# 🚆 Train Services Web App

## 📌 Overview
This web application provides essential train services, including:
- **Coach Position Finder**: Find the exact location of a coach in a train.
- **Food Availability Checker**: Check if food services are available on a train.
- **Trip Planner**: Plan your journey with an interactive guide.
- **Traveller Guide**: Useful resources for travelers.
- **Guider Service**: Find train guides for assistance.

## 🛠️ Tech Stack
- **Frontend**: HTML, CSS, TailwindCSS, JavaScript
- **Backend**: Flask (Python)
- **Database**: MySQL (if required)
- **APIs**: Custom APIs for train-related queries

## 📂 Project Structure
```
📁 project_root/
│-- 📁 backend/
    |-- 📁 models/
        └── database.py
│   │-- 📁 routes/
│   │   └── guide.py
│   │   └── plan.py
│   │   └── svm_coach_predictor.py
│   │   └── travel.py
│   └── app.py
│   └── req.txt
│-- 📁 frontend/
│   │-- coach_position.html
│   │-- food_availability.html
│   │-- index.html
│-- README.md
```

## 🚀 Installation & Setup
### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-repo/train-services.git
cd train-services
```

### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Flask App
```bash
python app.py
```

### 4️⃣ Access the Web App
Open `http://127.0.0.1:5000/` in your browser.

## 📌 Features & Usage
### ✅ **Coach Position Finder**
1. Enter the **Train Number** and **Coach ID**.
2. Click **Check Position**.
3. The app will return the predicted coach position.

### ✅ **Food Availability Checker**
1. Enter the **Train Number**.
2. Click **Check Availability**.
3. The app will display food availability status.

### ✅ **Trip Planner / Traveller / Guider Services**
- Plan your trip, get traveler tips, and find guides.

## 🐞 Troubleshooting
- **Background image not loading?**
  - Ensure the image is in `static/images/bg.jpg`.
  - Hard refresh the browser (`CTRL + SHIFT + R`).
- **Flask not running?**
  - Check Python installation: `python --version`
  - Run `pip install -r requirements.txt`.

## ✨ Contributing
1. Fork the repo.
2. Create a new branch (`feature-xyz`).
3. Commit your changes.
4. Open a Pull Request.

## 📜 License
MIT License © 2025 Aditya

---
Happy Coding! 🚀

