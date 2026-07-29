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
   "url":"http://secure-login-paypal-update.com"
}
```

### Response

```json
{
    
   confidence : 97.33
   phishing   : 1
   prediction : PHISHING
   reasons    : Website uses HTTP instead of 
                HTTPS., URL contains 
                phishing-related keywords., Domain 
                contains hyphens which may indicate 
                impersonation.
   risk_level : HIGH
}
```

### Request

```json
{
   "url":"https://google.com"
}
```

### Response

```json
{
   confidence : 88.08
   phishing   : 0
   prediction : LEGITIMATE
   reasons    : No suspicious URL characteristics 
                detected.
   risk_level : SAFE
   
}
```
