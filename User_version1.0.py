from PIL import Image, ImageFilter, ImageEnhance
import  os

#Chaning image codes:
def black_and_white(picture):
    new_image=picture.convert(mode="L")
    new_image.show()
    saving_choice = input("Do you want to save your file? Type Y or N ...")
    while saving_choice.isalpha() is False or saving_choice is None or saving_choice not in ('Y', 'N'):
        saving_choice = input('You need to type Y or N')
    if saving_choice == "Y":
        new_image.save("new_image.jpg")
        new_name = input("Type your new image name ... ")
        os.rename("new_image.jpg","{}.jpg".format(new_name))


def blur(picture):
    blur_degree=int(input("How much you wan to blur picture? The higher the number, the more powerfull blur will be..."))
    new_image=picture.filter(ImageFilter.GaussianBlur(blur_degree))
    new_image.show()

def contrast(picture):
    contrast_power=float(input("How much contrast you want to use? The higher the number the bigger contrast. Default is 1.0"))
    new_image = ImageEnhance.Contrast(picture).enhance(contrast_power)
    new_image.show()

def sharpness(picture):
    sharpness_power=int(input("How much you want to sharpen your image? The higher the number the bigger sharpness..."))
    new_image = ImageEnhance.Sharpness(picture).enhance(sharpness_power)
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
          *   Black'n'white (type BNW)
          *   We can blur it (type BLUR)
          *   Increase contrast (type CONT)
          *   Sharpen Image (type SHARP''')
    file_path = input(f'''Ok {user_name} then you need to give me path to your picture ...
    *Hint! put your image to the same folder as python program and remember about givin file format after 
    "."
    ''')

picture=Image.open(file_path)
picture.show()
function=input('''Wow cool photo!Now type what you wanna do with your photo ...
                You can ask for help to get command ... Type H''')
while function.isalpha() is False or function is None or function not in('H',"BNW","BLUR","CONT","SHARP"):
    function=input('You need to give proper name of function so type H for help or function name. '
                      'Watch for capitalies letters!!!')
while function == 'H':
    function=input('''Read hints and type function you want to use.Watch for capitalies letters!!!:
    *   b'n'w - we make your photo n black and white colors
    *   blur - we will blur your photo''')
if function == "BNW":
    black_and_white(picture)
elif function == "BLUR":
    blur(picture)
elif function =="CONT":
    contrast(picture)
elif function == "SHARP":
    sharpness(picture)






