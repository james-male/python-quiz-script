from questions import *


def show_current_scores():
    """

  :rtype : string
  """
    print('------------------------------------')
    print('Your total for incorrect answers:{}'.format(incorrectAnswers))
    print('Your total for correct answers:{}'.format(correctAnswers))
    print('Your current score is {}/20'.format(totalScore))
    print('------------------------------------')


print('')
userName = raw_input('Please enter your name ')
print('')
print(
    'Hello {} and welcome to the general knowledge quiz. To answer a question you must type in either a, b, c or d '
    'and hit enter.').format(userName)
print('There are 20 questions in total. you should aim to get at least 14 of them correct.')
print('You will be given your score after each question as well as at the very end. Good Luck!')
print('')

incorrectAnswers = 0
correctAnswers = 0
totalScore = 0

# #################################### QUESTION 1 ######################################
print('')
print(quizQuestions[0])
print('')
print('A Golf')
print('B Tennis')
print('C Swimming')
print('D Football')
print('')
##################################### QUESTION 1 ######################################

answer1 = raw_input('Please type in A, B, C or D for your answer ').upper()
print('You have chosen ' + answer1 + '. Your answer is...')

if answer1 == 'B':
    print('Correct!')
    totalScore += 1
    correctAnswers += 1
else:
    print('Incorrect!')
    incorrectAnswers += 1
    print('The correct answer was B')

show_current_scores()

##################################### QUESTION 2 ######################################
print('')
print(quizQuestions[1])
print('')
print('A Wodar')
print('B Werkip')
print('C Wasser')
print('D Waski')
print('')
##################################### QUESTION 2 ######################################


answer2 = raw_input('Please type in A, B, C or D for your answer ').upper()
print('You have chosen ' + answer2 + '. Your answer is...')

if answer2 == 'C':
    print('Correct!')
    totalScore += 1
    correctAnswers += 1
else:
    print('Incorrect!')
    incorrectAnswers += 1
    print('The correct answer was C')

show_current_scores()

##################################### QUESTION 3 ######################################
print('')
print(quizQuestions[2])
print('')
print('A Gigabyte')
print('B Byte')
print('C terabyte')
print('D Petabyte')
print('')
##################################### QUESTION 3 ######################################

answer3 = raw_input('Please type in A, B, C or D for your answer ').upper()
print('You have chosen ' + answer3 + '. Your answer is...')

if answer3 == 'B':
    print('Correct!')
    totalScore += 1
    correctAnswers += 1
else:
    print('Incorrect!')
    incorrectAnswers += 1
    print('The correct answer was B')

show_current_scores()

##################################### QUESTION 4 ######################################
print('')
print(quizQuestions[3])
print('')
print('A Rio de Janeiro')
print('B Recife')
print('C Sao Paulo')
print('D Brasilia')
print('')
##################################### QUESTION 4 ######################################

answer4 = raw_input('Please type in A, B, C or D for your answer ').upper()
print('You have chosen ' + answer4 + '. Your answer is...')

if answer4 == 'D':
    print('Correct!')
    totalScore += 1
    correctAnswers += 1
else:
    print('Incorrect!')
    incorrectAnswers += 1
    print('The correct answer was D')

show_current_scores()

##################################### QUESTION 5 ######################################
print('')
print(quizQuestions[4])
print('')
print('A Rubel')
print('B Dollaro')
print('C Euro')
print('D Escudo')
print('')
##################################### QUESTION 5 ######################################

answer5 = raw_input('Please type in A, B, C or D for your answer ').upper()
print('You have chosen ' + answer5 + '. Your answer is...')

if answer5 == 'C':
    print('Correct!')
    totalScore += 1
    correctAnswers += 1
else:
    print('Incorrect!')
    incorrectAnswers += 1
    print('The correct answer was C')

show_current_scores()

##################################### QUESTION 6 ######################################
print('')
print(quizQuestions[5])
print('')
print('A Green')
print('B Blue')
print('C Black')
print('D Brown')
print('')
##################################### QUESTION 6 ######################################

answer6 = raw_input('Please type in A, B, C or D for your answer ').upper()
print('You have chosen ' + answer6 + '. Your answer is...')

if answer6 == 'C':
    print('Correct!')
    totalScore += 1
    correctAnswers += 1
else:
    print('Incorrect!')
    incorrectAnswers += 1
    print('The correct answer was C')

show_current_scores()

##################################### QUESTION 7 ######################################
print('')
print(quizQuestions[6])
print('')
print('A Helium')
print('B Oxygen')
print('C Methane')
print('D Nitrogen')
print('')
##################################### QUESTION 7 ######################################

answer7 = raw_input('Please type in A, B, C or D for your answer ').upper()
print('You have chosen ' + answer7 + '. Your answer is...')

if answer7 == 'D':
    print('Correct!')
    totalScore += 1
    correctAnswers += 1
else:
    print('Incorrect!')
    incorrectAnswers += 1
    print('The correct answer was D')

show_current_scores()

##################################### QUESTION 8 ######################################
print('')
print(quizQuestions[7])
print('')
print('A Ruby')
print('B Sapphire')
print('C Crystal')
print('D Emerald')
print('')
##################################### QUESTION 8 ######################################

answer8 = raw_input('Please type in A, B, C or D for your answer ').upper()
print('You have chosen ' + answer8 + '. Your answer is...')

if answer8 == 'C':
    print('Correct!')
    totalScore += 1
    correctAnswers += 1
else:
    print('Incorrect!')
    incorrectAnswers += 1
    print('The correct answer was C')

show_current_scores()

##################################### QUESTION 9 ######################################
print('')
print(quizQuestions[8])
print('')
print('A Viet Nam War')
print('B Civil War')
print('C Korean War')
print('D World War II')
print('')
##################################### QUESTION 9 ######################################

answer9 = raw_input('Please type in A, B, C or D for your answer ').upper()
print('You have chosen ' + answer9 + '. Your answer is...')

if answer9 == 'A':
    print('Correct!')
    totalScore += 1
    correctAnswers += 1
else:
    print('Incorrect!')
    incorrectAnswers += 1
    print('The correct answer was A')

show_current_scores()

##################################### QUESTION 10 ######################################
print('')
print(quizQuestions[9])
print('')
print('A Throne')
print('B Splash')
print('C Bell')
print('D Blade')
print('')
##################################### QUESTION 10 ######################################

answer10 = raw_input('Please type in A, B, C or D for your answer ').upper()
print('You have chosen ' + answer10 + '. Your answer is...')

if answer10 == 'D':
    print('Correct!')
    totalScore += 1
    correctAnswers += 1
else:
    print('Incorrect!')
    incorrectAnswers += 1
    print('The correct answer was D')

show_current_scores()

##################################### QUESTION 11 ######################################
print('')
print(quizQuestions[10])
print('')
print('A Atlantic')
print('B Indian')
print('C Arctic')
print('D Pacific')
print('')
##################################### QUESTION 11 ######################################

answer11 = raw_input('Please type in A, B, C or D for your answer ').upper()
print('You have chosen ' + answer11 + '. Your answer is...')

if answer11 == 'D':
    print('Correct!')
    totalScore += 1
    correctAnswers += 1
else:
    print('Incorrect!')
    incorrectAnswers += 1
    print('The correct answer was D')

show_current_scores()

##################################### QUESTION 12 ######################################
print('')
print(quizQuestions[11])
print('')
print('A 120')
print('B 217')
print('C 206')
print('D 207')
print('')
##################################### QUESTION 12 ######################################

answer12 = raw_input('Please type in A, B, C or D for your answer ').upper()
print('You have chosen ' + answer12 + '. Your answer is...')

if answer12 == 'C':
    print('Correct!')
    totalScore += 1
    correctAnswers += 1
else:
    print('Incorrect!')
    incorrectAnswers += 1
    print('The correct answer was C')

show_current_scores()

##################################### QUESTION 13 ######################################
print('')
print(quizQuestions[12])
print('')
print('A Panda bear')
print('B Brown bear')
print('C Grizzy bear')
print('D polor bear')
print('')
##################################### QUESTION 13 ######################################

answer13 = raw_input('Please type in A, B, C or D for your answer ').upper()
print('You have chosen ' + answer13 + '. Your answer is...')

if answer13 == 'D':
    print('Correct!')
    totalScore += 1
    correctAnswers += 1
else:
    print('Incorrect!')
    incorrectAnswers += 1
    print('The correct answer was D')

show_current_scores()

##################################### QUESTION 14 ######################################
print('')
print(quizQuestions[13])
print('')
print('A Ear')
print('B Knee')
print('C Foot')
print('D Russian Flag')
print('')
##################################### QUESTION 14 ######################################

answer14 = raw_input('Please type in A, B, C or D for your answer ').upper()
print('You have chosen ' + answer14 + '. Your answer is...')

if answer14 == 'A':
    print('Correct!')
    totalScore += 1
    correctAnswers += 1
else:
    print('Incorrect!')
    incorrectAnswers += 1
    print('The correct answer was A')

show_current_scores()

##################################### QUESTION 15 ######################################
print('')
print(quizQuestions[14])
print('')
print('A Salt')
print('B Water')
print('C Air')
print('D Sugar')
print('')
##################################### QUESTION 15 ######################################

answer15 = raw_input('Please type in A, B, C or D for your answer ').upper()
print('You have chosen ' + answer15 + '. Your answer is...')

if answer15 == 'B':
    print('Correct!')
    totalScore += 1
    correctAnswers += 1
else:
    print('Incorrect!')
    incorrectAnswers += 1
    print('The correct answer was B')

show_current_scores()

##################################### QUESTION 16 ######################################
print('')
print(quizQuestions[15])
print('')
print('A China')
print('B Canada')
print('C Russia')
print('D USA')
print('')
##################################### QUESTION 16 ######################################

answer16 = raw_input('Please type in A, B, C or D for your answer ').upper()
print('You have chosen ' + answer16 + '. Your answer is...')

if answer16 == 'C':
    print('Correct!')
    totalScore += 1
    correctAnswers += 1
else:
    print('Incorrect!')
    incorrectAnswers += 1
    print('The correct answer was C')

show_current_scores()

##################################### QUESTION 17 ######################################
print('')
print(quizQuestions[16])
print('')
print('A Tom Stafford')
print('B Buzz Aldren')
print('C Neil Armstrong')
print('D Bruce McCandless')
print('')
##################################### QUESTION 17 ######################################

answer17 = raw_input('Please type in A, B, C or D for your answer ').upper()
print('You have chosen ' + answer17 + '. Your answer is...')

if answer17 == 'C':
    print('Correct!')
    totalScore += 1
    correctAnswers += 1
else:
    print('Incorrect!')
    incorrectAnswers += 1
    print('The correct answer was C')

show_current_scores()

##################################### QUESTION 18 ######################################
print('')
print(quizQuestions[17])
print('')
print('A Russia')
print('B India')
print('C China')
print('D Canada')
print('')
##################################### QUESTION 18 ######################################

answer18 = raw_input('Please type in A, B, C or D for your answer ').upper()
print('You have chosen ' + answer18 + '. Your answer is...')

if answer18 == 'C':
    print('Correct!')
    totalScore += 1
    correctAnswers += 1
else:
    print('Incorrect!')
    incorrectAnswers += 1
    print('The correct answer was C')

show_current_scores()

##################################### QUESTION 19 ######################################
print('')
print(quizQuestions[18])
print('')
print('A Walking')
print('B Swimming')
print('C Cycling')
print('D Sex')
print('')
##################################### QUESTION 19 ######################################

answer19 = raw_input('Please type in A, B, C or D for your answer ').upper()
print('You have chosen ' + answer19 + '. Your answer is...')

if answer19 == 'D':
    print('Correct!')
    totalScore += 1
    correctAnswers += 1
else:
    print('Incorrect!')
    incorrectAnswers += 1
    print('The correct answer was D')

show_current_scores()

##################################### QUESTION 20 ######################################
print('')
print(quizQuestions[19])
print('')
print('A Bogey')
print('B par')
print('C Wicket')
print('D Epee')
print('')
##################################### QUESTION 20 ######################################

answer20 = raw_input('Please type in A, B, C or D for your answer ').upper()
print('You have chosen ' + answer20 + '. Your answer is...')

if answer20 == 'A':
    print('Correct!')
    totalScore += 1
    correctAnswers += 1
else:
    print('Incorrect!')
    incorrectAnswers += 1
    print('The correct answer was A')

show_current_scores()

if correctAnswers >= 14:
    print('')
    print('Well done {} you answered 14 or more questions correctly. Because of this you have passed the quiz!'.format(userName))
else:
    print('')
    print('You scored under 14. Because of this you have not passed the test. Better luck next time')