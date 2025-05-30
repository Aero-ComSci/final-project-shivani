# final-project-shivani
final-project-shivani created by GitHub Classroom
Program Description:

Who is the program for?
This program is for kids and teens who want to discover a fun summer ice cream flavor based on their personality and preferences.

What the program does, what does it automate?
The program asks the user many multiple-choice questions and then uses the answers to recommend an ice cream flavor. It automates the process of matching user preferences to a preset list of flavor results. 

Code Samples:

Using a collection like a list
```python codecodecode
# List of ice cream flavors and scores
flavors = ["Strawberry", "Mango Sorbet", "Chocolate", "Vanilla"]
scores = [0, 0, 0, 0]  
```
Using a loop
```python codecodecode
# Find the top flavor using a loop
def find_top_flavor():
    highest = 0
    index = 0
    for i in range(len(scores)):
        if scores[i] > highest:
            highest = scores[i]
            index = i
    return flavors[index]
```
Using a function
```python codecodecode
# Function that asks a validated question and returns the answer
def get_valid_input(prompt):
    while True:
        answer = input(prompt).lower()
        if answer in ['a', 'b', 'c', 'd']:
            return answer
        else:
            print("Invalid input. Please enter only a, b, c, or d.")
```
Screenshots:
<img width="751" alt="Screenshot 2025-05-29 at 10 33 09 PM" src="https://github.com/user-attachments/assets/037a8ad4-b53d-4efd-a61f-889147e4f308" />
<img width="593" alt="Screenshot 2025-05-29 at 10 33 22 PM" src="https://github.com/user-attachments/assets/ac9b13fb-8530-42fe-9bcf-89b051db495a" />
<img width="683" alt="Screenshot 2025-05-29 at 10 33 36 PM" src="https://github.com/user-attachments/assets/7ae8b3d2-f263-44e1-851d-9784542ac87e" />

Screen recording:

https://github.com/user-attachments/assets/28dd2f06-0e73-42a4-987c-0757ff0d3873


Work log: 
5/27- I brainstormed and created the program description on the Read Me and started the code. 
5/29- I worked on and finished the code and created a video of my code working. I also updated the Read Me and the repository. 
