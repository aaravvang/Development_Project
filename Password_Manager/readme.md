
# 🔐 Flask Project: Password Encrypter API

## 📝 Problem Statement

Create a **Flask API** that securely **encrypts a password** using a provided **encryption key**.

## ✅ Requirements

- The API should expose a **POST** endpoint `/encrypt`.
- It should accept two parameters:
  - `password` (string): The plain-text password to encrypt.
  - `key` (string): The encryption key to use for encryption.
- It should return the encrypted password.


## 💡 Bonus

- Add a `/decrypt` endpoint to reverse the encryption using the same key.
- Handle edge cases like missing fields or incorrect key format gracefully.
