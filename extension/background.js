chrome.tabs.onUpdated.addListener(async (tabId, changeInfo, tab) => {
    if (changeInfo.status === "loading" && tab.url?.startsWith("http")) {
        try {
            const response = await fetch(
                "https://phishing-detection-api-5-07m6.onrender.com/predict",
                {
                    method: "POST",
                    headers: { "Content-Type": "application/json" },
                    body: JSON.stringify({ url: tab.url })
                }
            );

            const result = await response.json();

            // Handle both formats safely
            const isPhishing =
                result.prediction === "PHISHING" ||
                result.result === "PHISHING" ||
                result.phishing === true;

            if (isPhishing) {
                chrome.tabs.update(tabId, {
                    url: chrome.runtime.getURL("block.html")
                });
            }

        } catch (e) {
            console.error("Phishing API error", e);
        }
    }
});
