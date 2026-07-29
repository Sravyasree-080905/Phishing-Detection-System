chrome.tabs.onUpdated.addListener(async (tabId, changeInfo, tab) => {

    if (changeInfo.status === "loading" && tab.url?.startsWith("http")) {

        try {

            const response = await fetch(
                "http://127.0.0.1:5000/predict",
                {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json"
                    },
                    body: JSON.stringify({
                        url: tab.url
                    })
                }
            );

            const result = await response.json();

            // Save the prediction details
            chrome.storage.local.set({

                confidence: result.confidence,

                risk_level: result.risk_level,

                prediction: result.prediction,

                reasons: result.reasons

            });

            // Block only phishing websites
            if (result.prediction === "PHISHING") {

                chrome.tabs.update(tabId, {

                    url: chrome.runtime.getURL("block.html")

                });

            }

        }

        catch (e) {

            console.error("API Error:", e);

        }

    }

});