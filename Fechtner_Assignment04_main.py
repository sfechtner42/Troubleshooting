# ------------------------------------------------------------------------------------------ #
# Title: Assignment04
# Sabrina Fechtner, 05/01/2024
# ------------------------------------------------------------------------------------------ #

# PART 1: QUESTIONS
import csv

print("Part 1: Question validation:\n")

existing_content = []
existing_question_ids = [int(row["question_id"]) for row in existing_content]
question_id = max(existing_question_ids) + 2 if existing_question_ids else 10


with open('questions.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {",".join(row)}')
            line_count += 1
        print(f'\tquestion id is: {row["question_id"]} for question {row["question"]}')
        line_count += 1
        existing_content.append(row)
print(f'Processed {line_count} lines.\n')
i = 0
valid = False
selected_questions = []
for row in existing_content:
    print(f'question id is: {row["question_id"]} for question {row["question"]}')
    choice = input("Is this the correct question (y/n)? ").lower()
    if choice == 'y':
        selected_questions.append(row)
    elif choice == 'n':
        print("Okay, let's replace it")
        while True:
            new_question = input("Please input a new question: ")
            if 10 <= len(new_question) <= 30:
                selected_questions.append({"question_id": str(question_id), "question": new_question})
                question_id += 1
                break
            else:
                print("Questions must be between 10 and 30 characters")
    else:
        print("Invalid input. Please enter 'y' or 'n'.")
    choice2 = input("Is this question needed? (y/n)? ")
    if choice2.lower() == 'n':
        print("Okay. I'll remove it")
        selected_questions.remove(row)
    else:
        print("Okay. I'll write into file")
        # for row in selected_questions:
        #     selected_questions.append(row)
        #     break
print("the has been updated")
with open('questions.csv', mode='w', newline='') as question_file:
    fieldnames = ["question_id", "question"]
    question_writer = csv.DictWriter(question_file, fieldnames=fieldnames, delimiter=',', quotechar='"',
                                     quoting=csv.QUOTE_MINIMAL)
    question_writer.writeheader()
    for question in selected_questions:
        question_writer.writerow(question)

print("Part 2: Question validation:\n")

# print("Preloading answers\n")
# existing_answers = []
# with open('answers.csv', mode='r') as csv_file:
#     csv_reader = csv.DictReader(csv_file, delimiter=',')
#     line_count = 0
#     for row in csv_reader:
#         if line_count == 0:
#             print(f'Column names are {",".join(row)}')
#             line_count += 1
#         print(f'\t{row["interviewee"]} answered {row["answer"]} for question id: {row["question_id"]}')
#         line_count +=1
#         existing_content.append(row)
# print(f'Processed {line_count} lines.\n')
#
#
# existing_question_ids = [int(row["question_id"]) for row in existing_content]
# question_id = max(existing_question_ids) + 1 if existing_question_ids else 2
#
# print("Who are you interviewing?")
# interviewee_name = input("Enter your name: ")
# print(f'Hi {interviewee_name}!\n')
#
# print("Now let's add a new question\n")
#
# new_question = input("Enter a question: ")
# new_question_row = {"question_id": str(question_id), "question": new_question}
# existing_content.append(new_question_row)
#
# with open('questions.csv', mode='a', newline='') as question_file:
#     fieldnames = ["question_id", "question"]
#     question_writer = csv.DictWriter(question_file, fieldnames=fieldnames, delimiter=',', quotechar='"',
#                                      quoting=csv.QUOTE_MINIMAL)
#     question_writer.writerow(new_question_row)