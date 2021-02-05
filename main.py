import random

def rock_paper_scissors():
    user_input = input('Please enter \'rock\', \'paper\' or \'scissors\': ').lower()
    choice_list = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(choice_list)    # I could even do random.choice(['rock', 'paper', 'scissors'])
    # while user_input:
    #     if user_input == 'r' and computer_choice == 'r':
    #         print(f'I choose {computer_choice}. It\'s a draw!')
    #         break
    #     elif user_input == 'r' and computer_choice == 'paper':
    #         print(f'I choose {computer_choice}. I win!')
    #         break
    #     elif user_input == 'r' and computer_choice == 'scissors':
    #         print(f'I choose {computer_choice}. You win!')
    #         break
    #     elif user_input == 'p' and computer_choice == 'paper':
    #         print(f'I choose {computer_choice}. It\'s a draw!')
    #         break
    #     elif user_input == 'p' and computer_choice == 'scissors':
    #         print(f'I choose {computer_choice}. I win!')  
    #         break 
    #     elif user_input == 'p' and computer_choice == 'rock':
    #         print(f'I choose {computer_choice}. You win!') 
    #         break
    #     elif user_input == 's' and computer_choice == 'rock':
    #         print(f'I choose {computer_choice}. I win!')
    #         break  
    #     elif user_input == 's' and computer_choice == 'paper':
    #         print(f'I choose {computer_choice}. You win!')     
    #         break   
    #     elif user_input == 's' and computer_choice == 'scissors':
    #         print(f'I choose {computer_choice}. It\'s a draw!')
    #         break
    # so tha't way too long and I need to find a shorter way to do it:

    def is_win(user, machine):
        # rock>scissors, scissors>paper, paper>rock
        # return true if player wins
        if (user == 'rock' and machine == 'scissors') or (user == 'scissors' and machine == 'paper') or (user == 'paper' and machine == 'rock'):
            return True
        else:
            return False

    if user_input == computer_choice:
        print('-> Oh dang it... it\'s a tie!')
    while user_input != computer_choice:
        if is_win(user_input, computer_choice):   # if the function is true: then print and break
            print(f'-> My choice is {computer_choice}. You win!')
            break
        else:
            print(f'-> My choice is {computer_choice}. You lost!')
            break

    play_again = input('Wanna play again? (Yes/No): ').lower()
    if play_again == 'yes':
        return rock_paper_scissors()
    else:
        print('Exiting...')

rock_paper_scissors()

    






