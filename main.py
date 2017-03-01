#! python3
# 50StatesQuizCreator.py - Creates quizzes with questions and answers in random order, along with the answer key.

import random,sys

capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 
'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 
'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

for quizNum in range(int(sys.argv[1])):

  quiz = open('Quiz' + str(quizNum+1) + '.txt', 'w')
  ans = open('Ans' + str(quizNum+1) +' .txt', 'w')

  quiz.write('State Capitals Quiz No.' + str(quizNum+1) + "\n\n")
  quiz.write("Name:\n\nClass:\n\nAge:\n\n")

  states = list(capitals.keys())
  random.shuffle(states)

  for i in range(len(capitals)):

    correctAns = capitals[states[i]]
    wrongAns = list(capitals.values())

    del wrongAns[wrongAns.index(correctAns)]
    wrongAns = random.sample(wrongAns, 3)

    options = wrongAns + [correctAns]
    random.shuffle(options)

    quiz.write("Q" + str(i+1) + ". What is the capital of " + states[i] + "?\n\n")

    for a in range(len(options)):

      quiz.write('ABCD'[a] + ". " + options[a] + "\n")

      if(a==len(options) -1):
        quiz.write('ABCD'[a] + ". " + options[a] + "\n\n")

    ans.write("Q" + str(i+1) + ": " + states[i] + "  =>  " + "ABCD"[options.index(correctAns)] + "\n")
  
  quiz.close()
  ans.close()
