# ⭐ Flask To-Do List Web App (Beginner Project)

## 📌 Project Goal

Build a small web app where users can **add tasks**, **view tasks**, and **delete tasks** — using **HTML templates** rendered by Flask.

---

## ✅ Features You Will Build

- Home page showing all tasks — `index.html`
- Form to add a new task — same page or a separate page
- Delete a task (GET or POST)
- Store tasks in a simple list (in-memory) or optionally SQLite

---

## 📁 Project Structure (important)


todo_app/
│
├── app.py
├── templates/
│   ├── index.html
│   └── base.html      (optional)
└── static/
    └── style.css      (optional)


---

## 🧪 Requirements for the Project

- Use **render_template**
- Use Jinja2 variables (`{{ }}`) and loops (`{% for %}`)
- Use **POST form submission**
- Use **Flask routing**

---

## 💡 Example Tasks Shown on Screen

- Buy groceries 🛒  
- Finish homework ✍️  
- Walk the dog 🐶  
- Practice Python 🐍  

---

# 📜 Sample Question (copy for practice)

## 📄 Project: Flask To-Do List App

Create a Flask web application that lets the user manage a simple To-Do list.

---

### Your application must include:

#### 🔹 1. Homepage (`/`)
- Show all tasks inside an HTML template (`index.html`)
- Use:
  ```python
  render_template("index.html", tasks=tasks)


🔹 2. Add Task

A form with method="POST" to add a new task

After adding → redirect back to home

🔹 3. Delete Task

Next to each task show a delete button

When clicked → remove the task from the list

🔹 4. Templates

You must use:

index.html

optional: base.html for common layout

🔹 5. Data

Use a Python list:

tasks = []