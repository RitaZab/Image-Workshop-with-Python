from PIL import Image, ImageFilter

#Chaning image codes:
def black_and_white(picture):
    new_image=picture.convert(mode="L")
    new_image.show()


file_path=1
print('Hello!')
user_name=input('What is your name, friend? ')
hint_choice=input(f'Great {user_name}, what you want to do today?Do you want some help? Type Y or N (use capital letter)...')
while hint_choice.isalpha() is False or hint_choice is None or hint_choice not in('Y','N'):
    hint_choice=input('You need to type Y or N')
if hint_choice=='N':
    file_path=input(f'''Ok {user_name} then you need to give me path to your picture ...
                    *Hint! put your image to the same folder as python program and remember about givin file format after 
                    "."''')
elif hint_choice=='Y':
    print('''Ok, we can make your photo:
          *   Black'n'white
          *   We can blur it''')
picture=Image.open(file_path)
picture.show()
function=input('''Wow cool photo!Now type what you wanna do with your photo ...
                You can ask for help to get command ... Type H''')
while function.isalpha() is False or function is None or function not in('H',"BNW"):
    function=input('You need to give proper name of function so type H for help or function name. '
                      'Watch for capitalies letters!!!')
while function == 'H':
    function=input('''Read hints and type function you want to use.Watch for capitalies letters!!!:
    *   b'n'w - we make your photo n black and white colors
    *   blur - we will blur your photo''')
if function == "BNW":
    black_and_white(picture)





