questions = ["What is Michael's surname?", "What age is Michael?", "What is Michael's favourite fish?"]
answers = ["O'Sullivan", "27", "Salmon"]
score = 0
max_score = 3

print("Welcome to the Michael quiz!")
print("How well do you know Michael? Let's find out!")


print("1.", questions[0])
answer_one = input("Your Answer: ")

if (answer_one == answers[0]):
    print("Correct!")
    score+=1
else:
    print("Wrong! The correct answer is ", answers[0])

print("2.", questions[1])
answer_one = input("Your Answer: ")

if (answer_one == answers[1]):
    print("Correct!")
    score+=1
else:
    print("Wrong! The correct answer is ", answers[1])

print("3. ", questions[2])
answer_one = input("Your Answer: ")

if (answer_one == answers[2]):
    print("Correct!")
    score+=1
else:
    print("Wrong! The correct answer is", answers[2])

name = input("End of Quiz! Please enter your name: ")
print("Your score was", score, "out of", max_score)

if score == 0:
    print("Wow", name + ",", "you don't know Michael at all!")
elif score == max_score:
    print("Excellent work", name + ",", "you know all there is to know about Michael!")
elif score == 2:
    print("Good job", name + ",", "you know Michael reasonably well!")
else:
    print("Could be better", name + ",", "all relationships start somewhere...")


