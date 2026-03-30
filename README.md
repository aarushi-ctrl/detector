# 🔐 Real-Time Website Security Analyzer

A browser-based security tool that analyzes websites in real time and provides a **Security Score (0–100)** along with AI-based phishing detection and detailed risk explanations.

---

## 🚀 Features

* 🔍 Real-time website analysis
* 🔐 HTTPS security check
* 🌐 Domain age detection (WHOIS)
* 🛡️ Security headers analysis
* 🤖 AI-based phishing detection
* 📊 Security score generation (0–100)
* ⚠️ Risk classification (Safe / Medium / Dangerous)
* 🧾 Explainable results (issues shown clearly)

---

## 🧠 How It Works

1. User opens any website
2. Extension captures the URL
3. Backend analyzes:

   * HTTPS status
   * Domain age
   * Security headers
   * URL patterns
   * AI phishing prediction
4. System generates:

   * Security Score
   * Risk level
   * List of issues

---

## 📊 Security Score System

| Factor           | Weight    |
| ---------------- | --------- |
| HTTPS            | 15        |
| Domain Age       | 10        |
| Security Headers | 15        |
| AI Detection     | 20        |
| Other Checks     | Remaining |

---

## 🏗️ Tech Stack

**Frontend (Extension):**

* HTML
* CSS
* JavaScript

**Backend:**

* Python (Flask)

**Machine Learning:**

* Scikit-learn (Random Forest)

**Libraries & APIs:**

* requests
* python-whois
* flask-cors

---

## 📁 Project Structure

```
security-analyzer/
│── backend/
│   │── app.py
│   │── ml_model.py
│   │── model.pkl
│   │── requirements.txt
│
│── extension/
│   │── manifest.json
│   │── popup.html
│   │── popup.js
│   │── style.css
│
│── README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```
git clone https://github.com/your-username/security-analyzer.git
cd security-analyzer
```

---

### 2️⃣ Setup Backend

```
cd backend
pip install -r requirements.txt
python ml_model.py
python app.py
```

Backend will run on:

```
http://127.0.0.1:5000
```

---

### 3️⃣ Load Chrome Extension

1. Open Chrome
2. Go to:

   ```
   chrome://extensions/
   ```
3. Enable **Developer Mode**
4. Click **Load Unpacked**
5. Select the `extension/` folder

---


## 🎯 Example Output

```
🔐 Security Score: 72/100
⚠️ Status: Medium Risk

Issues:
- Missing security headers
- New domain
```

---

## 🔮 Future Improvements

* Integration with threat intelligence APIs (VirusTotal)
* Advanced ML model using real datasets
* Real-time script behavior analysis
* Deployment as a public API
* Browser-wide automatic scanning

---

## 🤝 Contribution

Contributions are welcome!
Feel free to fork this repository and submit a pull request.

---

## 📜 License

This project is open-source and available under the MIT License.

---

## 👩‍💻 Author

Developed by  Aarushi Srivastava a B.Tech CSE student passionate about:

* Cybersecurity
* Artificial Intelligence
* Full-stack development

---

⭐ If you like this project, consider giving it a star!
