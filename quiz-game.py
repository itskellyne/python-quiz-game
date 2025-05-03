"""
Want our program to go through each question.
show the user the question options
each question has a possible answers but one correct answer
a user should be able to input an option number for a guess
will be given right answer
then given next question
at the end there should be a final statement of how many questions they got right

"""

class Question:
    def __init__(self, text, answers, correct_index):
        self.text = text
        self.answers = answers 
        self.correct_index = correct_index
    def display_answers(self):
        count = 0
        for answer in self.answers:
            print (f"{count}. {answer}")
            count += 1

test_question1 = Question(
    "Which of the following is an amimal?",
    ["shirt", "foot", "apple", "toy", "dog"],
    4
)

#print(test_question1.text)
#test_question1.display_answers()


#Create a list of questions

all_questions = [
  Question(
    "Poona was the original name of what sport?",
    ["Surfing", "Pickleball", "Soccer", "Badminton"],
    3
  ),
  Question(
    "How many feet separate the bases in a regulation-sized baseball diamond?",
    [100, 90, 50, 45],
    1
  ),
  Question(
    "What is Kellyne's birth year?",
    [2001, 2002, 2003, 2004],
    3
  )
]


#Full game

score = 0

# Go through each question and run code
for question in all_questions:
    #Display question and answers
    print(question.text)
    question.display_answers()
    #Ask the user for a quess
    guess = int(input("Enter the number of your guess. ")) 
    """
    Instead of converting to int() immediately which looks like:  guess = int(input("Enter the number of your guess. ")) 
    we want to validate the input by:
    try/except will TRY to run a code block, and if it can't because of error it will run the except block instead
    """
    while True:
        try:
            guess = int(guess)
            break
        except:
            guess = input("Your guess must be a number")
    #Check whether the guess is correct and print result accordingly
    if guess == question.correct_index:
        print("Good job, that's correct!")
        score += 1
    else:
        print(f"Sorry, the answer was {question.answers[question.correct_index]}")


print(f"You got {score} out of {len(all_questions)} correct!")

if score == len(all_questions):
    print("PERFECT SCORE")