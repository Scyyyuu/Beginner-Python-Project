# Python Quiz Game

questions = ("What is the output of the following code? print(type(5)): ",
             "Which of the following is the correct way to create a function in Python?: ", 
             "What keyword is used to exit a loop in Python?: ", 
             "Which of the following is used to comment a single line in Python?: ",
             "What will be the output of the following code?: ")

options = (("A. int", "B. float", "C. str", "D. List"), 
           ("A. function myFunction()", "B. create myFunction()", "C. def myFunction:", "D. def myFunction()"), 
           ("A. stop", "B. exit", "C. break", "D. end"), 
           ("A. // This is a comment", "B. # This is a comment", "C. /* This is a comment */", "D. <!-- This is a comment -->"), 
           ("A. HelloWorld", "B. Hello + World", "C. Hello World", "D. Hello, World!" ))

answers = ("A", "D", "C", "B", "C")
guesses = []
question_num = 0
score = 0

print ("Python Simple Quiz")
for question in questions: 
    print ("-------------------------------------------------------------------")
    print (question)
    for option in options[question_num]:
        print (option)

    guess = input ("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print ("Correct Answer!")
    else: 
        print ("Incorrect Answer!")
        print (f"The Correct Answer is: {answers[question_num]}")
    question_num += 1

print ()
print ("======================")
print ("        RESULT     ")
print ("======================")

print (f"Answers: {answers}")
print (f"Guesses: {guesses}")

score = int (score / len (questions)*100)
print (f"Total Score: {score}%")
print ()