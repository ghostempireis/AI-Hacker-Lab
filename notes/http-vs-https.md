# HTTP vs HTTPS – Bug Bounty & Security Researcher Notes

---

## 🔍 What is HTTP?

**HTTP** stands for HyperText Transfer Protocol.  
It is the foundation of web communication — used to send and receive data between client (browser) and server.

- **Default Port:** 80
- **Encryption:** ❌ None (plain text)
- **Protocol:** Stateless, text-based
- **Use Case:** General browsing on static/informational websites

---

## 🔐 What is HTTPS?

**HTTPS** is HTTP with security — achieved by wrapping the protocol inside SSL/TLS encryption.

- **Default Port:** 443
- **Encryption:** ✅ Yes (TLS/SSL)
- **Key Feature:** Confidentiality, Integrity, Authenticity
- **Use Case:** Any sensitive transmission — login forms, banking, session handling

---

## ⚔️ Hacker's View: What to Look For

| 🔎 Issue                         | 📌 Description |
|----------------------------------|----------------|
| 🔓 **Cleartext Credentials**     | HTTP sends login data unencrypted; visible to attackers |
| 🍪 **Insecure Cookies**          | Cookies without `Secure` flag may leak over HTTP |
| ⚠️ **Mixed Content**             | Secure page loading HTTP scripts/images opens attack surface |
| ⛓ **Weak TLS Config**           | Outdated ciphers or expired certs can be exploited |
| 🔁 **No Redirect to HTTPS**      | HTTP fallback may allow downgrade/MITM attacks |

---

## 🧪 How to Test (Burp Suite + Manual)

- **Step 1:** Intercept login form on an HTTP site
- **Step 2:** Look for session cookies in responses
- **Step 3:** Check if `Secure`, `HttpOnly`, and `SameSite` flags are applied
- **Step 4:** Observe if any JS/CSS/Image files are being loaded via `http://`
- **Step 5:** Use tools like:
  - `testssl.sh`
  - `sslyze`
  - `Qualys SSL Labs`

---

## 🔐 Certificate Behavior

- Trusted HTTPS websites have certs issued by a CA (Certificate Authority)
- Browsers warn users if:
  - Self-signed cert is used
  - Certificate is expired
  - Domain mismatch occurs

---

## 🧠 Pro-Tip for Bug Hunters

> A login page served over `HTTP` or submitting to an `HTTP` endpoint is a serious misconfiguration and should be reported.

Also:
- Check if redirect from HTTP to HTTPS is **automatic and strict**
- Look for improper or missing `Strict-Transport-Security` headers

---

## 🔁 Quick Comparison Table

| Feature        | HTTP              | HTTPS                     |
|----------------|-------------------|----------------------------|
| Port           | 80                | 443                        |
| Encryption     | ❌ None           | ✅ TLS/SSL                 |
| Safe for Auth? | ❌ No             | ✅ Yes                     |
| Vulnerable to? | MITM, Sniffing    | Misconfigurations (if any)|
| Used For       | Static sites      | Login, payments, APIs     |

---

## 📌 Real-World Exploitable Bugs (Examples)

- Credential leakage on `http://login.site.com`
- Cookies without `Secure` + `HttpOnly`
- API responses served over HTTP on a HTTPS page (Mixed Content)
- TLSv1.0/SSLv3 enabled — weak cipher usage
- Missing `HSTS` header allowing HTTPS stripping

---

## 🧠 Summary

Knowing how HTTP and HTTPS work is **foundational for bug bounty hunting**. Many **critical bugs** like insecure transmission, cookie theft, and session hijacking stem from poor HTTPS implementation.

Always test:
- Transport security
- Cookie flags
- Certificate validation
- Content sources (JS/images/scripts)


