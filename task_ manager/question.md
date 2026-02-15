
## 📘 Flask + Supabase Mini Project

### **Task Management System**

---

## 🎯 Objective

Build a **Flask-based Task Management System** that connects to a **Supabase database** and allows users to:

* View tasks
* Add new tasks
* Update task status
* Display task data using Jinja templates

This project focuses on **backend logic, database interaction, and template rendering**, not UI design.

---

## 🗄️ Database Details

Use an existing Supabase table named **`Tasks`** with the following structure:

| Column Name | Type      | Description            |
| ----------- | --------- | ---------------------- |
| task_id     | integer   | Primary key            |
| title       | text      | Task title             |
| description | text      | Task details           |
| status      | text      | `Pending` / `Complete` |
| created_at  | timestamp | Auto-generated         |

---

## 📂 Project Structure

```
task_app/
│── app.py
│── .env
│── templates/
│    ├── base.html
│    ├── tasks.html
│    ├── add_task.html
│    ├── update_task.html
```

---

## 🔹 Task 1: Display All Tasks

### Route

```
GET /
```

### Requirements

* Fetch all rows from `Tasks` table
* Display tasks in a table using Jinja
* Show:

  * Task ID
  * Title
  * Description
  * Status

### Template

📄 `tasks.html`

---

## 🔹 Task 2: Add a New Task

### Route

```
GET /add
POST /add
```

### Requirements

* Display a form to add:

  * title
  * description
  * status
* Insert the task into Supabase on form submission
* Redirect to home page after successful insert

### Template

📄 `add_task.html`

---

## 🔹 Task 3: Update Task Status

### Route

```
GET /update
POST /update
```

### Requirements

* Allow updating task status
* Two options:

  * Mark task as `Complete`
  * Mark task as `Pending`
* Update task based on `task_id`

### Template

📄 `update_task.html`

---

## 📄 Jinja Templates to Create

### 1️⃣ `base.html`

* Common layout
* Navigation links:

  * View Tasks
  * Add Task
  * Update Task

---

### 2️⃣ `tasks.html`

* Extends `base.html`
* Displays tasks in a table
* Shows status clearly

---

### 3️⃣ `add_task.html`

* Form with:

  * Title
  * Description
  * Status dropdown
* Submit button

---

### 4️⃣ `update_task.html`

* Input for:

  * Task ID
  * Status selection
* Submit button

---

## ✅ Expected Outcomes

After completing the project:

* User can view all tasks
* User can add new tasks
* User can update existing tasks
* Supabase is used for **read, insert, update**
* Flask renders pages using Jinja templates

