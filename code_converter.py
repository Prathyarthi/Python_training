import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.environ.get("API_KEY"))

model = genai.GenerativeModel('gemini-1.5-flash')

# code = '''n = 5
# for i in range(n):
#     print(" "*(n-i) + "* "*(i+1))'''

code = '''chocolates = list(map(int,input("Enter number of chocolates in each jar: ").split()))
N = len(chocolates)
count = 0

for i in chocolates:
    if i==0:
        continue
    if i%3==0:
        count = count + (i//3)
    else:
        count = count + (i//3) + 1

print(count)'''

language = ""

print("1. Javascript \n2. Java \n3. C++ \n4. C \n5. Python")
choice = input("Enter choice: ")
if choice=="1":
    language = 'javascript'

if choice=="2":
    language = 'Java'

if choice=="3":
    language = 'C++'

if choice=="4":
    language = 'C'

if choice=="5":
    language = 'Python'

prompt = f"Convert this code {code} to {language}"

response = model.generate_content(prompt)

if response and response.candidates:
    converted_code = response.candidates[0].content.parts[0].text
    print(converted_code)
else:
    print("No valid response received.")
