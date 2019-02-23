import os
import json

def create_registration():

    print('-----------------------------')
    print('Register to enter the contest')
    print('-----------------------------')
    name = input('Name: ')
    tesla_id = input('Tesla ID: ')
    reg_num = input('Registration Number: ')
    dept = input('Department and Section: ')
    year = input('Year: ')

    details = {
    'name': name,
    'id': tesla_id,
    'reg_num': reg_num,
    'dept': dept,
    'year': year
    }

    with open('metadata.json', 'w') as file:
        json.dump(details, file, indent=2)



if __name__ == '__main__':

    ascii_art = \
    """
$$$$$$$$\ $$$$$$$$\  $$$$$$\  $$\        $$$$$$\  
\__$$  __|$$  _____|$$  __$$\ $$ |      $$  __$$\ 
   $$ |   $$ |      $$ /  \__|$$ |      $$ /  $$ |
   $$ |   $$$$$\    \$$$$$$\  $$ |      $$$$$$$$ |
   $$ |   $$  __|    \____$$\ $$ |      $$  __$$ |
   $$ |   $$ |      $$\   $$ |$$ |      $$ |  $$ |
   $$ |   $$$$$$$$\ \$$$$$$  |$$$$$$$$\ $$ |  $$ |
   \__|   \________| \______/ \________|\__|  \__|
                                                                                                    
    """

    print(ascii_art)
    print('Welcome to the Tesla Image Processing and Computer Vision contest!')

    if not os.path.exists(os.path.join(os.getcwd(), 'metadata.json')):
        create_registration()
    else:
        print('--------------------------------')
        print('You are currently registered as:')
        print('--------------------------------')

        with open('metadata.json', 'r') as file:
            data = json.load(file)

        print('Name:', data['name'])
        print('Tesla ID:', data['id'])
        print('Registration Number:', data['reg_num'])
        print('Department and Section:', data['dept'])
        print('Year:', data['year'])
        print('--------------------------------')

        print('Not you? Delete "metadata.json" in this folder and run this program again.')
