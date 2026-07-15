# 👗 FashionPulse – Customer Taste Analyzer

A modern Streamlit web application that collects customer clothing preferences and stores the responses directly in Google Sheets. This project helps analyze customer fashion trends and buying preferences in real time.

---

## 🚀 Live Demo

🔗 **Streamlit App:** [https://your-streamlit-app-url.streamlit.app](https://fashionpulse-customer-analyzer-hj2vrliftdyxdswvcbzwzk.streamlit.app/)

---

## 📌 Features

- 👤 Collect customer information
- 👕 Record clothing preferences
- 🎨 Capture favorite colors and styles
- 💰 Store customer budget
- 📊 Save responses automatically to Google Sheets
- 🌐 Fully deployed on Streamlit Cloud

---

## 🛠️ Technologies Used

- Python
- Streamlit
- Google Sheets API
- GSpread
- Google OAuth2
- Git & GitHub

---

## 📋 Customer Information Collected

The application records:

- Name
- Age
- Gender
- City
- Preferred Clothing Category
- Clothing Size
- Preferred Style
- Favorite Color
- Fabric Type
- Budget

---

## 📂 Project Structure

```
FashionPulse-Customer-Analyzer/
│
├── app.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/yourusername/FashionPulse-Customer-Analyzer.git
```

Move into the project folder

```bash
cd FashionPulse-Customer-Analyzer
```

Create a virtual environment

```bash
python -m venv venv
```

Activate the virtual environment

**Windows**

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py
```

---

## 🔐 Environment Variables

This project uses **Streamlit Secrets** to securely store Google Service Account credentials.

Create the following secret in **Streamlit Cloud**:

```toml
[gcp_service_account]
...
```

⚠️ Never upload your `credentials.json` file to GitHub.

---

## 📊 Output

All submitted customer responses are automatically stored in a connected Google Sheet, making the data available for further analysis and reporting.

---

## 🎯 Future Improvements

- Customer Dashboard
- Data Visualization
- Recommendation System
- Machine Learning-based Fashion Prediction
- Admin Login Panel

---

## 👩‍💻 Author

**Palwasha Mushtaq**

- 💼 LinkedIn: www.linkedin.com/in/palwasha-sheikh-0286a71a7
- 💻 GitHub: https://github.com/palwashamushtaq123

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.
