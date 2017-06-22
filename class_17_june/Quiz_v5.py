'''
In this version of the program, the questions list and answers list
have been integrated together in the form of a Dictionary.
Each key is the question, and each corresponding value is the answer.
'''
questions_dictionary = {"What is Michael's surname?":"O'Sullivan", "What age is Michael?":"27", "What is Michael's favourite fish?":"Salmon"}
score = 0
#len() function also works on Dictionaries.
max_score = len(questions_dictionary)

print("Welcome to the Michael quiz!")
print("How well do you know Michael? Let's find out!")

question_number = 1

'''
We can loop over dictionaries as well;
Here, on each loop, the current key will be assigned to 
the question variable.
'''
for question in questions_dictionary:
    print(question_number,".", question)
    answer = input("Your Answer: ")
    #To get a value for a key from the dictionary the
    # dictionary_name[key] syntax is used...
    if (answer.lower() == questions_dictionary[question].lower()):
        print("Correct!")
        score += 1
    else:
        print("Wrong! The correct answer is ", questions_dictionary[question])
    question_number += 1

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
