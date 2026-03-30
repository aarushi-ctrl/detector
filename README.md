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


DEMO PICTURES 
<img width="352" height="462" alt="image" src="https://github.com/user-attachments/assets/20580048-04c0-4050-81bb-89e84b0b1687" />
<img width="347" height="470" alt="image" src="https://github.com/user-attachments/assets/d2a858ea-9958-48c8-8ff7-c0220e8fe357" />
<img width="374" height="457" alt="image" src="https://github.com/user-attachments/assets/938241f6-3953-4c7e-98ef-52cd671a6e87" />


## ⚙️ Installation

### 1. Clone repo
```bash
git clone https://github.com/aarushi-ctrl/ThreatLENS.git
cd ThreatLENS
The current model is a prototype and will be improved using larger real-world phishing datasets such as PhishTank during the development phase.
Planned integration with threat intelligence APIs such as VirusTotal for enhanced detection.
