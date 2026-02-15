# ⭐ Flask Password Leak Checker

## 📄 Project Goal
Build a Flask web app where users can:
* Add suspicious passwords to a "Check List"
* See all added passwords
* Remove a password from the list
* (optional) Later connect it to an API like Have I Been Pwned to check if the password was leaked

This project helps you practice Flask fundamentals using a cybersecurity theme.

## ✅ Features to Build

### 🔹 1. Homepage (`/`)
* Display a list of passwords to check
* Use:
```
render_template("index.html", passwords=passwords)
```

### 🔹 2. Add Password
* A text input form
* Form uses `POST`
* After submitting → redirect to `/`

### 🔹 3. Delete a Password
* Each password entry should have a delete button
* Remove it using a POST request
* Redirect back to homepage

## 📁 Project Structure
```
password_checker/
│
├── app.py
├── templates/
│   ├── index.html
│   └── base.html (optional)
└── static/
    └── style.css (optional)
```

## 🔧 Data Structure
``` 
passwords = [
    {"id": 1, "value": "qwerty123"},
    {"id": 2, "value": "mypassword"},
]
```

## 🧪 Requirements
* Use `render_template()`
* Use Jinja2 loops:
```jinja
{% for p in passwords %}
```
* Use Jinja2 variables:
```jinja
{{ p.value }}
```
* Handle POST forms
* Use Flask routing
* Use a global Python list
* Use a simple ID generator