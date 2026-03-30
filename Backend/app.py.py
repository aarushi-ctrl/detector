from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import whois
from datetime import datetime
import pickle

app = Flask(__name__)
CORS(app)

model = pickle.load(open("model.pkl", "rb"))

def get_domain_age(domain):
    try:
        w = whois.whois(domain)
        creation_date = w.creation_date
        if isinstance(creation_date, list):
            creation_date = creation_date[0]
        age_days = (datetime.now() - creation_date).days
        return age_days
    except:
        return -1

def check_https(url):
    return url.startswith("https")

def check_headers(url):
    try:
        res = requests.get(url, timeout=5)
        headers = res.headers
        required = [
            "Content-Security-Policy",
            "Strict-Transport-Security",
            "X-Frame-Options"
        ]
        missing = [h for h in required if h not in headers]
        return missing
    except:
        return ["Error"]

def extract_features(url):
    return [
        len(url),
        url.count('.'),
        url.count('-'),
        1 if "@" in url else 0,
        1 if "login" in url.lower() else 0,
        1 if "verify" in url.lower() else 0,
        1 if url.startswith("https") else 0
    ]

def check_phishing(url):
    return model.predict([extract_features(url)])[0]

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.json
    url = data.get("url")

    domain = url.split("//")[-1].split("/")[0]

    score = 100
    issues = []

    if not check_https(url):
        score -= 15
        issues.append("No HTTPS")

    age = get_domain_age(domain)
    if age != -1 and age < 180:
        score -= 10
        issues.append("New domain")

    missing_headers = check_headers(url)
    if len(missing_headers) > 0:
        score -= 15
        issues.append("Missing security headers")

    if check_phishing(url):
        score -= 20
        issues.append("Phishing detected by AI")

    if score < 0:
        score = 0

    return jsonify({
        "score": score,
        "issues": issues
    })

if __name__ == "__main__":
    app.run(debug=True)