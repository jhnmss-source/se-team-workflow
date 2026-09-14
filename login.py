def login(username, password):
    if username == "admin" and password == "1234":
        return "Authentication successful"
    else:
        return "Authentication failed"git add login.py