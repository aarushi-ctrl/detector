# 🔐 ThreatLENS  
### See threats before they see you

ThreatLENS is a real-time browser-based web security analyzer that evaluates website safety using **AI + security checks**.

It provides a **Security Score (0–100)** along with clear explanations to help users understand potential risks before interacting with websites.

---

## 🚀 Features

- 🔍 Real-time website analysis  
- 🤖 AI-based phishing detection  
- 🔐 HTTPS security validation  
- 🌐 Domain age detection  
- 🛡️ Security headers analysis  
- 📊 Security score system (0–100)  
- ⚠️ Risk classification (Safe / Medium / Dangerous)  
- 🧾 Explainable results  

---

## 🧠 How It Works

1. User opens a website  
2. Extension captures the URL  
3. Backend analyzes:
   - HTTPS status  
   - Domain age  
   - Security headers  
   - URL patterns  
   - AI phishing prediction  
4. System returns:
   - Security Score  
   - Risk Level  
   - Issues detected  

---

## 🏗️ Architecture

Extension → Backend API → ML Model  

---

## 📊 Security Score System

| Factor | Weight |
|--------|--------|
| HTTPS | 15 |
| Domain Age | 10 |
| Security Headers | 15 |
| AI Detection | 20 |
| URL Patterns | 15 |

## ⚙️ Installation

### 1. Clone repo
```bash
git clone https://github.com/aarushi-ctrl/ThreatLENS.git
cd ThreatLENS
