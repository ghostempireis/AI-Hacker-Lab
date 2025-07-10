def classify_http_method(request_line):
    method = request_line.split(" ")[0].upper()

    if method == "GET":
        return "GET → Safe request to read data"
    elif method == "POST":
        return "POST → Submits form data (check for login, signup)"
    elif method == "PUT":
        return "PUT → Updates data (check access control)"
    elif method == "DELETE":
        return "DELETE → Deletes data (very sensitive, needs auth)"
    else:
        return "Unknown or unsupported HTTP method"

# Test Cases
if __name__ == "__main__":
    test_requests = [
        "GET /index.php HTTP/1.1",
        "POST /login HTTP/1.1",
        "PUT /profile HTTP/1.1",
        "DELETE /user/123 HTTP/1.1",
        "HEAD /test HTTP/1.1"
    ]

    for request in test_requests:
        print(f"{request} ➤ {classify_http_method(request)}")






""" SAMPLE OUTPUT 
GET /index.php HTTP/1.1 ➤ GET → Safe request to read data  
POST /login HTTP/1.1 ➤ POST → Submits form data (check for login, signup)  
PUT /profile HTTP/1.1 ➤ PUT → Updates data (check access control)  
DELETE /user/123 HTTP/1.1 ➤ DELETE → Deletes data (very sensitive, needs auth)  
HEAD /test HTTP/1.1 ➤ Unknown or unsupported HTTP method  
"""
