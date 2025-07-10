# 🤖 AI-Powered HTTP Request Classifier (Prompt)

## 👨‍💻 Real HTTP Request (Captured via Burp Suite)



---

## 🔍 GPT Prompt Instructions:

You are a cybersecurity assistant.

Analyze the above HTTP request and answer the following:

1. 🧠 What HTTP method is used?
2. 🔍 What does this request do?
3. ⚠️ Are there any security risks?
4. 🧑‍💻 What would a hacker test or look for in this request?
5. 🔐 How can this request be secured?

---

## 🧠 GPT Output (Sample):

- **Method:** `POST`
- **Purpose:** Submits login form data
- **Security Risk:** Data being sent over HTTP (not HTTPS)
- **Red Flags:** Password exposed if intercepted on open network
- **Suggestion:** Use HTTPS, validate inputs, implement rate limiting
