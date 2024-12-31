#quiz game

import json

with open("questions.json", "r") as file:
    content = file.read()

data = json.loads(content)

for question in data:
    print(question["question_text"])
    for index, alt in enumerate(question["alternatives"]):
        print(index + 1, "-", alt)
    user_ans = int(input("Add your answer here: "))
    question["user_choice"] = user_ans

right_ans = 0
for index, question in enumerate(data):
    if question["user_choice"] == question["answer"]:
        right_ans += 1
        res = "Correct Answer"
    else: res = "Wrong Answer"

    message = f"{index + 1} - Your answer: {question['user_choice']}, " \
              f"Correct answer: {question['answer']}"
    print(message)

result = f"Your final result is: {round(right_ans / (len(question)-1)*100,1)}%"
print(result)