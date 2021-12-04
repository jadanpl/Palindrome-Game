def palindrome(a):
    b=a.lower()
    c=""
    for d in b:
        if d.isalpha() or d.isnumeric():
            c+=d
    # method 1
    # using reversed() built-in function to cycle through the elements in the string in reverse order
    # .join() method merges all of the characters resulting from the reversed iteration into a new string
    r = ''.join(reversed(c))
    if r==c:
        print(f"'{a}' is a palindrome.")
    else:
        print(f"'{a}' is not a palindrome.")

def examples():
    palindromes = ["I love watching funny movies.",
                   "Was it a rat I saw?",
                   "Step on no pets",
                   "Sit on a potato pan, Otis",
                   "Hello, World!"]
    for phrase in palindromes:
        palindrome(phrase)

examples()

print("What is a palindrome? A string is a palindrome if it is identical forward and backward.")
print("It is a palindrome judging game, whereby you need determine whether a word or a phrase is a palindrome \nor not by typing 'Yes' or 'No'")
print("I believe you have gained some idea from the examples above.")
print("Hint: This game ignore for punctuation, capitalization, and spacing. Have fun!!!")


def test(x):
    y=x.lower()
    z=""
    for u in y:
        if u.isalpha() or u.isnumeric():
            z+=u
    # method 2: slicing
    # The slice statement means start at string length, end at position 0, move with the step -1 (or one step backward).
    sliced_string = z[::-1]
    if sliced_string==z:
        return 1
    else:
        return 0

def main():
    questions = ["Lisa Bonet ate no basil",
                 "Do you like Python?",
                 "Satan, oscillate my metallic sonatas",
                 "Do geese see God?",
                 "TOM and JERRY are BEst FriEND!",
                 "Donald Duck LOVES tomatoes.",
                 "12022021",
                 "I roamed under it as a tired nude Maori",
                 "Don't Have a Good Day, Have a Great Day",
                 "Dammit, I'm mad!"]
    print("Enter 'Yes' if it is a palindrome. Otherwise, enter 'No'.")
    index=0
    count = 0
    number = 1
    while index < len(questions):
        print(f"Question {number} : {questions[index]}")
        answer_to_question=input("Enter Your Answer: ").lower()
        if test(questions[index]) and answer_to_question=="yes":
            count+=1
            print("You are right!")
        elif not test(questions[index]) and answer_to_question=="no":
            count += 1
            print("You are right!")
        elif test(questions[index]) and answer_to_question == "no":
            count+=0
            print ("This is not the right answer.")
        index += 1
        number += 1
    score=count/len(questions)*100
    if score==100:
        print("Amazing! You answered all the {} questions correctly and gained {}%!".format(len(questions),score))
    elif score>=50:
        print(f"Not bad, you scored more than 50%. Out of {len(questions)}, you answered {count} questions correctly and gain {score}%.")
    else:
        print(f"Too bad, you scored less than 50%. Out of {len(questions)}, you only answered {count} questions correctly and gain {score}%.")

main()

