# ------------------------------------------------------------------------------------------ #
# Title: Assignment04
# Sabrina Fechtner, 05/01/2024
# ------------------------------------------------------------------------------------------ #

#### BEFORE YOU BEGIN   ####
##  make sure the cursor is in the top-left of answers.csv (for some reason, it doesn't work otherwise)

#input questions
questions = []
with open('questions.csv', 'r') as questions_file:
    data = questions_file.read().strip().split('\n')[1:]
    for row in data:
        parts = row.strip().split(',')
        questions.append((int(parts[0]), parts[1]))
print(f'here are the questions: {questions}')

#input answers
answers = []
with open('answers.csv', 'r') as answers_file:
    data = answers_file.read().strip().split('\n')[1:]
    for row in data:
        parts = row.strip().split(',')
        parts[1] = int(parts[1])
        answers.append(parts)
print(answers)

#print questions and answers
for question in questions:
    for answer in answers:
        if question[0] == answer[1]:
            print(f'{answer[0]} answered {answer[2]} for question {question[1]} with ID number {question[0]}')

#Reviewing questions
selected_questions = []
existing_questions = []

with open('questions.csv', 'r') as questions_file:
    header = questions_file.readline().strip()
    for row in questions_file:
        parts = row.strip().split(',')
        existing_questions.append((int(parts[0]), parts[1]))

for row in existing_questions:
    print(f"\nQuestion ID: {row[0]} for {row[1]}: ")
    choice = input("Is this question written/displayed correctly (y/n)? ").lower()
    if choice == 'y':
        selected_questions.append(row)
    elif choice == 'n':
        print("Okay, let's replace it")
        while True:
            new_question = input("Please input a new question: ")
            if 10 <= len(new_question) <= 30:
                new_question_id = max([q[0] for q in existing_questions]) + 1
                selected_questions.append((new_question_id, new_question))
                break
            else:
                print("Questions must be between 10 and 30 characters")
    else:
        print("Invalid input. Please enter 'y' or 'n'.")

    choice2 = input("Do you want to keep this question (y/n)? ")
    if choice2.lower() == 'y':
        #selected_questions.append(row)
        print("Okay. I'll write into file")
    elif choice2.lower() == 'n':
        print("Okay. I won't save to file.")
        for row in selected_questions:
            selected_questions.remove(row)
    else:
        print("Invalid input. Please enter 'y' or 'n'.")

# Remove duplicate entries in selected_questions
selected_questions = list(set(selected_questions))
print(f'this are the updated {selected_questions}')

#the updated question file
with open('questions.csv', 'w') as questions_file:
    questions_file.write(header + '\n')
    for row in selected_questions:
        questions_file.write(f"{row[0]},{row[1]}\n")

#Part 2: The interview

# Enter new person
print("Who are you interviewing? (Capitalize first letter) ")
interviewee_name = input("Enter your name: ")
print(f'Hi {interviewee_name}!\n')

interviewee_answers = []

#email validation (I found a solution online)
import re

def is_valid_email(email):
    # Regular expression for validating an Email
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    # If the string matches the regex, it is a valid email
    return bool(re.match(regex, email))

for question in selected_questions:
    # Check if the question ID already exists in interviewee_answers
    question_id_exists = any(ans[1] == question[0] for ans in interviewee_answers)
    if not question_id_exists:
        while True:
            answer = input(f'Answer the following {question[1]}: ')
            if not answer:
                print("Invalid response. Please try again.")
                continue
            if "email" in question[1].lower():
                if is_valid_email(answer):
                    break
                else:
                    print("Invalid email. Please try again.")
            else:
                break
    interviewee_answers.append([interviewee_name] + [question[0]] + [answer])

# Remove duplicate entries in selected_questions
unique_questions = []
seen_ids = set()
for question in selected_questions:
    if question[0] not in seen_ids:
        unique_questions.append(question)
        seen_ids.add(question[0])

print(f'the previous {answers}')
print(f'the new input {interviewee_answers}')

with open('answers.csv', 'r') as answers_file:
    header2 = answers_file.readline().strip()
    for row in answers_file:
        if row.strip():
            parts = row.strip().split(',')
            existing_questions.append((parts[0], int(parts[1]), parts[2]))

with open('answers.csv', 'a', newline ='') as answers_file:
    #if answers_file.tell() == 0:
        #answers_file.write('\n')
    #answers_file.write(header2 + '\n')
    for row in interviewee_answers:
        answers.append(row)

# Part 3 Clean .csv
with open('questions.csv', 'r') as questions_file:
    data = questions_file.read().strip().split('\n')[1:]
    for row in data:
        parts = row.strip().split(',')
        questions.append((int(parts[0]), parts[1]))
print(f'here are the questions after the entire interview: {selected_questions}')

print(f'here are all the answers have the entire interview: {answers}')

# Remove any answers associated with deleted questions
valid_question_ids = set(q[0] for q in unique_questions)
updated_answers = [ans for ans in answers if ans[1] in valid_question_ids]

# Sort the answers by interviewee's names alphabetically
updated_answers.sort(key=lambda x: x[0])

# Print questions and corresponding answers
for question in unique_questions:
    print(f"\nQuestion: {question[1]}")
    print("Answers:")
    for answer in updated_answers:
        if answer[1] == question[0]:
            print(f"{answer[0]}: {answer[2]}")

# Remove any answers associated with deleted questions
valid_question_ids = set(q[0] for q in unique_questions)
updated_answers = [ans for ans in answers if ans[1] in valid_question_ids]
sorted_answers = sorted(updated_answers, key=lambda x: x[0])

# Update the answers.csv file with cleaned-up answers
with open('answers.csv', 'w') as answers_file:
    answers_file.write('interviewee,question_id,answer\n')
    # for answer in updated_answers:
    #     answers_file.write(f"{answer[0]},{answer[1]},{answer[2]}\n")
    for answer in sorted_answers:
        answers_file.write(f"{answer[0]},{answer[1]},{answer[2]}\n")