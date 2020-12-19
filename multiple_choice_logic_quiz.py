


score = 0
total_number_of_questions = 10
answers_for_questions = ['d', 'a', 'c', 'd', 'a', 't', 't', 'f', 't', 't']



user_name = input('Welcome to the logic survey exam. Can I get your name? ')



intro_ = input('Hello, ' + user_name + '! ' 'Would you like to take our logic quiz.\n (Select Y or N) Y or N\n')





if intro_ == "Y":
    input("Great, let's continue.(Please press ENTER.)")
elif intro_ == "y":
    input("Great, let's continue.(Please press ENTER.)")
elif intro_ == "N":
    exit('Okay! See you later then.')
elif intro_ == "n":
    exit("Okay! See you later then.")
else:
    input('ERROR! Please enter a valid entry. (Press ENTER to reset)')





answer_to_intro_ = input('Before we start, would you like to provide your email so that we can notify you about '
                             'any upcoming events held by the philosophy department?\n (Enter \'Y\' or \'N\') Y or N\n')
if answer_to_intro_ == "Y":
    input("Great, please enter your email:\n"
          "")


elif answer_to_intro_ == "y":
    input("Great, please enter your email:\n"
          "")
    input('Thank you! You\'ll be given five multiple choice questions and five true or false questions. '
          '(Press ENTER to continue)')
elif answer_to_intro_ == "N":
    input('Alright! You\'ll be given five multiple choice questions and five true or false questions.'
          '(Press ENTER to continue)')
elif answer_to_intro_ == "n":
    input('Alright! You\'ll be given five multiple choice questions and five true or false questions.'
          '(Press ENTER to continue)')
else:
    input("ERROR! Please enter a valid entry. (Press ENTER to reset.)")



question_1 = input('\n Modus Tollus is:\n(CHOOSE a, b, c, or d)'
                    '\na) p -> q, p, ergo: q\nb) p -> q, -p, ergo: -q'
                    '\nc) a -> b, b -> c, ergo: a -> c\nd) p -> q, -q, ergo: -p'
                    '\n'
                    '\nENTER ANSWER HERE: ')
if question_1 == 'd':
    input('CORRECT! (Press ENTER to continue.)')
elif question_1 == 'a' or 'b' or 'c':
    input('INCORRECT! The correct answer is choice d). (Press ENTER to continue.)')
else:
    input("ERROR! Please enter a valid entry. (Press ENTER to reset.)")


question_2 = input('\n Modus Ponens is:'
                   '\n'
                   '\na) p -> q, p, ergo: q'
                    '\nb) p -> q, -p, ergo: -q'
                   '\nc) a -> b, b -> c, ergo: a -> c'
                   '\nd) p -> q, -q, ergo: -p'
                    '\n'
                    '\nENTER ANSWER HERE: ')
if question_2 == 'a':
    input('CORRECT! (Press ENTER to continue.)')
elif question_2 == 'b' or 'c' or 'd':
    input('INCORRECT! The correct answer is choice d). (Press ENTER to continue.)')
else:
    input("ERROR! Please enter a valid entry. (Press ENTER to reset.)")


question_3 = input('\nComplete the following according to the correct valid form:'
                   '\n1. If Mike wakes up at 9:30, then he missed his first class of the day which starts at 8:15 am.'
                   '\n2.____.'
                   '\n ∴ It\'s not the case that Mike woke up at 9:30.'
                   '\na) Mike woke up at 9:30'
                   '\nb) It\'s not the case that Mike woke up at 9:30'
                   '\nc) Mike did not missed his first class of the day which starts at 8:15am.'
                   '\nd) Mike did missed his first class of the day'
                   '\n'
                   '\nENTER ANSWER HERE: ')

if question_3 == 'c':
    input('CORRECT! (Press ENTER to continue.)')
elif question_3 == 'a' or 'b' or 'd':
    input('INCORRECT! The correct answer is choice d). (Press ENTER to continue.)')
else:
    input("ERROR! Please enter a valid entry. (Press ENTER to reset.)")

question_4 = input('\nDisjunctive syllogism is the following form:'
                    '\na) a v b, -b, ∴ a'
                    '\nb) a v b, -a, ∴ -b'
                    '\nc) a v b, -a, ∴ b'
                    '\nd) both a and c'
                    '\n'
                    '\nENTER ANSWER HERE: ')

if question_4 == 'd':
    input('CORRECT! (Press ENTER to continue.)')
elif question_4 == 'a' or 'b' or 'c':
    input('INCORRECT. The correct answer is choice d). (Press ENTER to continue.)')
else:
    input("ERROR! Please enter a valid entry. (Press ENTER to reset.)")

question_5 = input('\nConstructive dilemma is the following:'
                   '\na) a v b, a -> c, b -> d, ∴ c v d'
                   '\nb) a v b, a -> b, b -> d, ∴ b v d'
                   '\nc) a v b, a -> c, b -> d, ∴ c -> d\nd) a v b, a -> c, b -> d, ∴ a v d'
                   '\n'
                   '\nENTER ANSWER HERE: ')

if question_5 == 'a':
    input('CORRECT! (Press ENTER to continue.)')
elif question_5 == 'b' or 'c' or 'd':
    input('INCORRECT. The correct answer is choice d). (Press ENTER to continue.)')
else:
    input("ERROR! Please enter a valid entry. (Press ENTER to reset.)")

input('Now the true or false questions section. (Press ENTER to continue.)')

question_6 = input('\n (T) TRUE or (F) False?'
                   '\n Valdity is defined as follows:'
                   '\n If the premises are true, then the conclusion necessarily follows.'
                   '\n(Enter either t or f.)'
                   '\n'
                   '\nANSWER: ')
if question_6 == 't':
    input('CORRECT! (Press ENTER to continue.)')
elif question_6 == 'f':
    input('INCORRECT. The correct answer is TRUE. (Press ENTER to continue.)')
else:
    input("ERROR! Please enter a valid entry. (Press ENTER to reset.)")


question_7 = input('\n (T) TRUE or (F) False?\nThe soundness of an argument is defined as follows:\n The argument is actually true in reality.\n(Enter either t or f.)\n\nANSWER: ')
if question_7 == 't':
    input('CORRECT! (Press ENTER to continue.)')
elif question_7 == 'f':
    input('INCORRECT. The correct answer is TRUE. (Press ENTER to continue.)')
else:
    input("ERROR! Please enter a valid entry. (Press ENTER to reset.)")

question_8 = input('\n8. (T) TRUE or (F) False?'
                   '\nAn argument can be sound, but also not valid.'
                   '\n(Enter either t or f)'
                   '\n'
                   '\nANSWER: ')
if question_8 == 'f':
    input('CORRECT! (Press ENTER to continue.)')
elif question_8 == 't':
    input('INCORRECT. The correct answer is FALSE. (Press ENTER to continue.)')
else:
    input("ERROR! Please enter a valid entry. (Press ENTER to reset.)")

question_9 = input('\n9. (T) TRUE or (F) False?'
                   '\nAn argument can be valid, but not sound.'
                   '\n(Enter either t or f)'
                   '\n'
                   '\nANSWER: ')

if question_9 == 't':
    input('CORRECT! (Press ENTER to continue.)')
elif question_9 == 'f':
    input('INCORRECT. The correct answer is TRUE. (Press ENTER to continue.)')
else:
    input("ERROR! Please enter a valid entry. (Press ENTER to reset.)")

question_10 = input('\n10. (T) TRUE or (F) False?'
                    '\nInvalidity can be defined as follows:'
                    '\n The premises are true, but the conclusion is false'
                    '\n(Enter either t or f)'
                    '\n'
                    '\nANSWER: ')

if question_10 == 't':
    input('CORRECT! (Press ENTER to continue.)')
elif question_10 == 'f':
    input('INCORRECT! The correct is TRUE.')
else:
    input("ERROR! Please enter a valid entry. (Press ENTER to reset.)")


if question_1 == 'd':
    score += 1
else:
    score += 0

if question_2 == 'a':
    score += 1
else:
    score += 0

if question_3 == 'c':
    score += 1
else:
    score += 0

if question_4 == 'd':
    score += 1
else:
    score += 0

if question_5 == 'a':
    score += 1
else:
    score += 0

if question_6 == 't':
    score += 1
else:
    score += 0

if question_7 == 't':
    score += 1
else:
    score += 0

if question_8 == 'f':
    score += 1
else:
    score += 0

if question_9 == 't':
    score += 1
else:
    score += 0

if question_10 == 't':
    score += 1
else:
    score += 0


input('Thank you, ' + user_name + ' for completing our logic survey exam. To see your results please press ENTER.')

print('\nYour score: ' + str(score) + '/' + str(total_number_of_questions) + '.')

if score/total_number_of_questions == 1:
    input('\nCongratulations, you got everything correct!(Press ENTER to continue.)')
else:
    input('\nThank you for taking our logic survey exam. You can retake the exam after 48 hours.(Press ENTER to '
          'continue.)')

print('\nThank you again for taking our logic survey exam. Have a blessed day.')

















