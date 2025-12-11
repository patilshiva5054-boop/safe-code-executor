# Safe Code Executor - Simple Learning Project

This project lets you **run Python code safely** using Docker.  
You send some Python code to the API, and it gives you the result back.

---

## What It Does

- You give it Python code.  
- It runs the code in a safe environment (Docker).  
- It shows you the output.  
- It stops dangerous code from breaking your system.

Example:

- **Input:**  
```python
print("Hello World")
Output:

nginx
Copy code
Hello World
How to Set Up
Clone this project:

bash
Copy code
git clone https://github.com/<your-username>/safe-code-executor.git
cd safe-code-executor
Install required packages:

bash
Copy code
pip install -r requirements.txt
Make sure Docker is installed and running.

Start the API:

bash
Copy code
python app.py
How to Use
Run Python Code
Send a POST request to /run with code:

Example request:

json
Copy code
{
  "code": "print(2 + 2)"
}
Example response:

json
Copy code
{
  "output": "4"
}
Run Multiple Files (Optional)
Upload a .zip of Python files to /run-zip

Safety Features
Stops long code after 10 seconds

Limits memory to 128 MB

No internet access inside code

Read-only files (code can’t change important files)

Limits code size to 5000 characters

Testing Ideas
Normal code:

python
Copy code
print("Hello")
for i in range(3):
    print(i)
Dangerous code (will be stopped safely):

python
Copy code
while True:
    pass

x = "a" * 1000000000

import requests
requests.get("http://evil.com")
What You Learn
How to run code safely in Docker

How to stop dangerous code

Docker security basics: memory, time, network limits

How to explain your project clearly

Optional Web Page
A simple page where you can type code, click Run, and see output.

Extra Ideas
Add support for JavaScript

Make the web page nicer

Save previous code runs

Run multiple containers at the same time

Author: Your Name
License: MIT

pgsql
Copy code

---

This version is **short, simple, and easy to read**.  

If you want, I can now also give you the **exact commands to create this `README.md` and push it to GitHub** step by step.  

Do you want me to do that
