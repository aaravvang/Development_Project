

## 🔐 Password Strength Checker (FastAPI + UI)

---

## 🎯 Objective

Build a **Password Strength Checker web application** using **FastAPI**.

The application should allow users to enter a password and receive feedback on its strength:

* Weak
* Medium
* Strong

The project focuses on:

* Handling form input
* String validation
* Conditional logic
* Rendering results using Jinja templates

No database is required.

---

## 📌 Functional Requirements

### 1️⃣ Home Page

Create a webpage that includes:

* Title: **Password Strength Checker**
* A form with:

  * Password input field
  * Submit button

---

### 2️⃣ User Input

* The user enters a password in the input field.
* The form sends the password to the backend using a **POST request**.

Example input:

```
hello123
MyPass@2024
abc
```

---

### 3️⃣ Password Evaluation Logic

The backend should evaluate the password based on the following criteria:

### Criteria to check:

* Length of password
* Presence of uppercase letters
* Presence of lowercase letters
* Presence of digits (0–9)
* Presence of special characters (e.g., @, #, $, %)

---

### Strength Rules (Suggested)

| Condition                                                       | Strength |
| --------------------------------------------------------------- | -------- |
| Length < 6                                                      | Weak     |
| Only letters or only numbers                                    | Weak     |
| Meets some criteria (length + mix)                              | Medium   |
| Length ≥ 8 + uppercase + lowercase + number + special character | Strong   |

---

### 4️⃣ Output

After evaluation, display:

* The entered password (optional)
* Strength result:

  * Weak
  * Medium
  * Strong

Example:

```
Password: hello123  
Strength: Medium
```

---

## 🖥️ User Interface Requirements

The UI should include:

* A heading/title
* Input field for password
* Submit button
* A result section showing strength

Example layout:

```
Password Strength Checker

[ Enter Password __________ ] [ Check ]

Result:
Strength: Strong
```

---

## 📂 Project Structure

```
password_checker/
│
├── main.py
│
└── templates/
      └── index.html
```

---

## ⚙️ Backend Responsibilities

The FastAPI backend should:

1. Serve the main HTML page.
2. Receive password input from the form.
3. Analyze the password based on defined rules.
4. Determine strength level.
5. Return result to the template.

---

## 🎨 Frontend Responsibilities

The HTML page should:

* Display the input form
* Submit password to backend
* Show the result dynamically after submission

---

## 🧪 Example Cases

| Input       | Output |
| ----------- | ------ |
| abc         | Weak   |
| hello123    | Medium |
| MyPass@2024 | Strong |
