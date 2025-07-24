# 🌐 Day 5 Log – AI + Bug Bounty Master Plan 🚀

🗓️ **Date:** 25 July 2025  
🎯 **Focus:** XSS Labs + Reporting + Hackathon Research + GitHub Portfolio

---

## ✅ Tasks Completed:

### 🔹 1. XSS Labs Solved on PortSwigger:
- [x] Reflected XSS into attribute with angle brackets HTML-encoded
- [x] Stored XSS in anchor `href` with double quotes HTML-encoded
- [x] Reflected XSS into a JavaScript string with angle brackets HTML-encoded

📌 **Payload Examples Used**:
```js
"><script>alert(1)</script>
";alert(1);//  
'+alert(1)+'
