import prompt


def ask_and_check_answer(game, user_name):

    for i in range(3):
        (question, correct_answer) = game()

        print('Question:', question)
        answer = prompt.string('Your answer: ')

        if answer == correct_answer:
            print("Correct!")
        else:
            print(f''''"{answer}" is wrong answer ;(.
Correct answer was "{correct_answer}"''')
            print(f"Let's try again, {user_name}!")
            break

    if i == 3:
        print(f'Congratulations, {user_name}!')
