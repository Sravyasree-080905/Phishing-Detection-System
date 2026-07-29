# API Documentation

## Base URL

```
http://127.0.0.1:5000
```

---

## POST /predict

### Request

```json
{
   "url":"https://example.com"
}
```

### Response

```json
{
    "prediction":"PHISHING",
    "confidence":97.33,
    "risk_level":"HIGH",
    "reasons":[
        "Website uses HTTP instead of HTTPS.",
        "Contains phishing keywords."
    ]
}
```
