
function getRecommendation() {
    const data = {
        bowler: document.getElementById("bowler").value,
        pitch: document.getElementById("pitch").value,
        length: document.getElementById("length").value,
        situation: document.getElementById("situation").value
    };

    fetch("http://127.0.0.1:5000/recommend", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(data)
    })
    .then(res => res.json())
    .then(result => {
        document.getElementById("output").innerHTML = `
            <h3>🏏 Shot: ${result.shot}</h3>
            <p>⚠️ Risk: ${result.risk}</p>
            <p>🧠 Reason: ${result.reason}</p>
            <p>🔄 Alternative: ${result.alternative}</p>
        `;
    });
}
