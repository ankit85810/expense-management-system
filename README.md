# 💰 Expense Management System

An **Expense Management System** built using **Streamlit** for the frontend and **FastAPI** for the backend. This application helps users efficiently manage and track their expenses with an intuitive interface and real-time updates.

## ✨ Features
- Add, edit, and delete expense entries.
- Categorize expenses for better financial tracking.
- View expense summaries with insightful analytics.
- Interactive and user-friendly UI powered by Streamlit.
- FastAPI-based backend for efficient and scalable data handling.

## 📂 Project Structure
```
expense-management-system/
│-- frontend/         # Streamlit frontend application
│-- backend/          # FastAPI backend server
│-- tests/            # Test cases for both frontend and backend
│-- requirements.txt  # List of required Python packages
│-- README.md         # Project overview and setup instructions
```

## 🛠 Installation and Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/ankit85810/expense-management-system.git
   cd expense-management-system
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the FastAPI backend server**:
   ```bash
   uvicorn backend.server:app --reload
   ```

4. **Run the Streamlit frontend application**:
   ```bash
   streamlit run frontend/app.py
   ```

## 📌 Usage
- Open the Streamlit web application in your browser.
- Add new expenses by entering details such as amount, category, and date.
- View a detailed summary of expenses with interactive charts and filters.

## 🛠 Technologies Used
- **Frontend:** Streamlit
- **Backend:** FastAPI
- **Database:** SQLite/PostgreSQL (if applicable)
- **Programming Language:** Python

## 🤝 Contributing
Contributions are welcome! Feel free to submit issues or pull requests to improve the project.

## 👤 Author
Developed by [Ankit](https://github.com/ankit85810).
