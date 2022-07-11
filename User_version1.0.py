from PIL import Image, ImageFilter


print('Hello!')
user_name=input('What is your name, friend? ')
hint_choice=input(f'Great {user_name}, what you want to do today?Do you want some help? Type Y or N (use capital letter)...')
while hint_choice.isalpha() is False or hint_choice is None or hint_choice not in('Y','N'):
    hint_choice=input('You need to type Y or N')
if hint_choice=='N':
    function_choice=input(f'Ok {user_name} then you need to give me path to your picture ...')
elif hint_choice=='Y':
    print('''Ok, we can make your photo:
          *   Black'n'white
          *   We can blur it''')



