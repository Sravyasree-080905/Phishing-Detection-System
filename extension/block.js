chrome.storage.local.get(
["confidence","risk_level","prediction","reasons"],
function(data){

const score = data.confidence || 90;
const risk = data.risk_level || "HIGH";
const prediction = data.prediction || "PHISHING";

const badge = document.querySelector(".risk-badge");
const title = document.getElementById("predictionTitle");
const riskText = document.getElementById("riskText");
const riskFill = document.getElementById("riskFill");
const riskScore = document.getElementById("riskScore");
const scanTime = document.getElementById("scanTime");
const list = document.getElementById("reasonList");

if(prediction === "PHISHING"){
    title.innerHTML = "🚨 Phishing Website Detected";
}else{
    title.innerHTML = "✅ Legitimate Website";
}

riskText.innerHTML = "Risk Level : " + risk;
badge.innerHTML = risk;

if(risk === "HIGH"){

    badge.style.background = "rgba(255,0,0,.15)";
    badge.style.color = "#ff4d4d";
    riskFill.style.background = "linear-gradient(90deg,#ff4d4d,#ff0000)";

}
else if(risk === "MEDIUM"){

    badge.style.background = "rgba(255,165,0,.18)";
    badge.style.color = "orange";
    riskFill.style.background = "linear-gradient(90deg,#ffb347,#ff9800)";

}
else{

    badge.style.background = "rgba(0,255,127,.18)";
    badge.style.color = "#00ff99";
    riskFill.style.background = "linear-gradient(90deg,#00ff99,#00c853)";

}

riskFill.style.width = score + "%";

riskScore.innerHTML = "Detection Confidence : " + score + "%";

scanTime.innerHTML = "Scanned at : " + new Date().toLocaleTimeString();

list.innerHTML = "";

if(data.reasons && data.reasons.length > 0){

    data.reasons.forEach(reason => {

        const li = document.createElement("li");
        li.textContent = reason;
        list.appendChild(li);

    });

}

});