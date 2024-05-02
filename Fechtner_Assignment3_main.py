# ------------------------------------------------------------------------------------------ #
# Title: Assignment03
# Sabrina Fechtner, 04/24/2024
# ------------------------------------------------------------------------------------------ #

# PART 1: QUESTIONS
import csv

print("Preloading questions\n")

existing_content = []

# Load questions
with open('questions.txt', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=',')
    for row in csv_reader:
        existing_content.append(row)

# Load answers
with open('answers.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=',')
    for row in csv_reader:
        existing_content.append(row)

# Separate questions and answers
existing_questions = []
existing_answers = []

for row in existing_content:
    if "question_id" in row:
        existing_questions.append(row)
    else:
        existing_answers.append(row)
with open('questions.txt', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {",".join(row)}')
            line_count += 1
        print(f'\tquestion id is: {row["question_id"]} for question {row["question"]}')
        line_count += 1
        #for row in csv_reader:
        existing_content.append(row)
print(f'Processed {line_count} lines.\n')

print("Preloading answers\n")
existing_answers = []
with open('answers.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {",".join(row)}')
            line_count += 1
        print(f'\t{row["interviewee"]} answered {row["answer"]} for question id: {row["question_id"]}')
        line_count +=1
        existing_content.append(row)
print(f'Processed {line_count} lines.\n')


existing_question_ids = [int(row["question_id"]) for row in existing_content]
question_id = max(existing_question_ids) + 1 if existing_question_ids else 2

print("Who are you interviewing?")
interviewee_name = input("Enter your name: ")
print(f'Hi {interviewee_name}!\n')

print("Now let's add a new question\n")

new_question = input("Enter a question: ")
new_question_row = {"question_id": str(question_id), "question": new_question}
existing_content.append(new_question_row)

with open('questions.txt', mode='a', newline='') as question_file:
    fieldnames = ["question_id", "question"]
    question_writer = csv.DictWriter(question_file, fieldnames=fieldnames, delimiter=',', quotechar='"',
                                     quoting=csv.QUOTE_MINIMAL)
    question_writer.writerow(new_question_row)


print("New question written to questions.txt\n")

# PART 2: ANSWERS

#open questions.txt
questions = []
with open('questions.txt', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=',')
    for row in csv_reader:
        questions.append(row)

# get answers
new_answers = []
for question in questions:
    answer = input(f"Question ID: {question['question_id']} - {question['question']}: ")
    new_answer = {"interviewee": interviewee_name, "question_id": question["question_id"], "answer": answer}
    new_answers.append(new_answer)

# Write new answers to answers.csv
with open('answers.csv', mode='a', newline='') as csv_file:
    fieldnames = ["interviewee", "question_id", "answer"]
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for answer in new_answers:
        csv_writer.writerow(answer)

print("Answers have been added to answers.csv")
