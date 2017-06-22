questions = ["What is Michael's surname?", "What age is Michael?", "What is Michael's favourite fish?"]
answers = ["O'Sullivan", "27", "Salmon"]
score = 0

'''
In version 3, we change the max_score variable 
to remove the hardcoding of 3 being the max score.
We can use the len() function to get the number
of items in the questions list.
This way, even if more questions added, we don't
need to manually adjust the maximum score.
'''
max_score = len(questions)

print("Welcome to the Michael quiz!")
print("How well do you know Michael? Let's find out!")

question_number = 1

for question in questions:
    print(question_number,".", question)
    answer = input("Your Answer: ")
    if (answer == answers[question_number - 1]):
        print("Correct!")
        score += 1
    else:
        print("Wrong! The correct answer is ", answers[question_number - 1])
    question_number+=1

name = input("End of Quiz! Please enter your name: ")
print("Your score was", score, "out of", max_score)

if score == 0:
    print("Wow", name + ",", "you don't know Michael at all!")
elif score == max_score:
    print("Excellent work", name + ",", "you know all there is to know about Michael!")
elif score >= max_score / 2:
    print("Good job", name + ",", "you know Michael reasonably well!")
else:
    print("Could be better", name + ",", "all relationships start somewhere...")
