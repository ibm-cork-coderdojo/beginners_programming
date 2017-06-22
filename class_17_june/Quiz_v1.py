#Create the list of questions
questions = ["What is Michael's surname?", "What age is Michael?", "What is Michael's favourite fish?"]
#Create the list of answers to each question
answers = ["O'Sullivan", "27", "Salmon"]
#Set the initial player score to 0 (we use this to keep track of score)
score = 0
#Set the maximum score to 3 (one point for each of the three questions)
max_score = 3

print("Welcome to the Michael quiz!")
print("How well do you know Michael? Let's find out!")

#Print the first question from the questions list
print("1.", questions[0])
#Ask the player for an answer
answer_one = input("Your Answer: ")
'''
If the answer provied by the player is equal to the first answer
in the answers list (i.e. they gave the right answer), add one
to the player score. Else, they gave the wrong answer, no points!
'''
if (answer_one == answers[0]):
    print("Correct!")
    score+=1
else:
    print("Wrong! The correct answer is ", answers[0])
'''
Print the second question from the questions list,
and ask the player for an answer
'''
print("2.", questions[1])
answer_one = input("Your Answer: ")
'''
As with the first question, check did they get it right,
and give a point if they did
'''
if (answer_one == answers[1]):
    print("Correct!")
    score+=1
else:
    print("Wrong! The correct answer is ", answers[1])

'''
Print the third question from the questions list,
and ask the player for an answer
'''
print("3. ", questions[2])
answer_one = input("Your Answer: ")

'''
As with the first and second questions, check did they get it right,
and give a point if they did
'''
if (answer_one == answers[2]):
    print("Correct!")
    score+=1
else:
    print("Wrong! The correct answer is", answers[2])

'''
Get the player's name, and tell him/her how many
they got right out of the max of three.
'''
name = input("End of Quiz! Please enter your name: ")
print("Your score was", score, "out of", max_score)

#If the player got zero points...
if score == 0:
    print("Wow", name + ",", "you don't know Michael at all!")
#Else if the player got full points (3)...
elif score == max_score:
    print("Excellent work", name + ",", "you know all there is to know about Michael!")
#Else if the player got 2 points...
elif score == 2:
    print("Good job", name + ",", "you know Michael reasonably well!")
#Else the player got 1 points...
else:
    print("Could be better", name + ",", "all relationships start somewhere...")


