
# 📘 FastAPI Mini Project

## 🧮 Build a Simple Counter API

---

## 🎯 Objective

Build a simple **FastAPI application** that acts as a counter system.

The application should maintain a single integer value in memory and expose API endpoints to manipulate and retrieve the counter value.

No database should be used.
The counter should exist only while the server is running.

---

## 📌 Requirements

### 1️⃣ Home Route

* Create a root endpoint `/`
* It should return a welcome message indicating the API is running.

---

### 2️⃣ Get Current Counter Value

* Create a GET endpoint `/counter`
* It should return the current value of the counter.
* Initially, the counter should start at **0**.

---

### 3️⃣ Increment Counter

* Create a POST endpoint `/increment`
* Each request should increase the counter by **1**
* Return the updated counter value

---

### 4️⃣ Decrement Counter

* Create a POST endpoint `/decrement`
* Each request should decrease the counter by **1**
* Return the updated counter value

---

### 5️⃣ Reset Counter

* Create a POST endpoint `/reset`
* This should reset the counter to **0**
* Return the updated counter value

