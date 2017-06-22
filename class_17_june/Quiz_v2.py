questions = ["What is Michael's surname?", "What age is Michael?", "What is Michael's favourite fish?"]
answers = ["O'Sullivan", "27", "Salmon"]
score = 0
max_score = 3

print("Welcome to the Michael quiz!")
print("How well do you know Michael? Let's find out!")

'''
Keep track of what question we are on with
the question_number variable. Start by setting to first question.
We do not set to zero; most users would be confused by
"Question 0" being printed out!
'''
question_number = 1

'''
Instead of hardcoding to ask each question, get an answer,
and check if it is right three separate times as in version 1,
we use a for loop to loop through each question in the questions
list, get an answer, and check if it is right.
This way, we are avoid repeating the same code three times as in
version 1.
'''
for question in questions:
    print(question_number,".", question)
    answer = input("Your Answer: ")
    #We use question_number - 1 to index into the questions and
    #answers lists, remember list counting starts at 0.
    if (answer == answers[question_number - 1]):
        print("Correct!")
        score += 1
    else:
        print("Wrong! The correct answer is ", answers[question_number - 1])
    #Keep track! Right or wrong, in the next loop, we must
    #index to the next item in the questions and answers lists.
    question_number += 1

name = input("End of Quiz! Please enter your name: ")
print("Your score was", score, "out of", max_score)

'''
Instead of hardcoding scores out of three, we use comparison
operators to determine...
'''
#...if the player got 0 correct
if score == 0:
    print("Wow", name + ",", "you don't know Michael at all!")
#...else if the player got everything correct
elif score == max_score:
    print("Excellent work", name + ",", "you know all there is to know about Michael!")
#...else if the player got greater than or equal to 50% of questions correct
elif score >= max_score / 2:
    print("Good job", name + ",", "you know Michael reasonably well!")
#...else the player for less than 50% of questions correct
else:
    print("Could be better", name + ",", "all relationships start somewhere...")
