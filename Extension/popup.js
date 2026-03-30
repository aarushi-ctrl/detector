chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {
    let url = tabs[0].url;

    document.getElementById("url").innerText = url;

    fetch("http://127.0.0.1:5000/analyze", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ url: url })
    })
    .then(res => res.json())
    .then(data => {
        let score = data.score;

        document.getElementById("score").innerText = "Score: " + score;

        let status = "";
        if (score >= 80) status = "Safe ✅";
        else if (score >= 50) status = "Medium Risk ⚠️";
        else status = "Dangerous ❌";

        document.getElementById("status").innerText = status;
        document.getElementById("issues").innerText =
            "Issues: " + data.issues.join(", ");
    });
});