#importing needed libraries
from pyrogram import Client
from pyrogram.types import Message

#initialization of API
api_id = Your_api_id
api_hash = Your_api_hash
bot_token = Your_bot_token

bot = Client(session_name='session', bot_token=bot_token,
             api_id=api_id, api_hash=api_hash)

#Starting the bot
#for all chat id's, write the id you want to message to
bot.start()
bot.send_message(chat_id='Milad_Nooraiy', text='Hi,welcome to Cbot.\U0001F600 \n'
                 'Here you can find how to use this bot \U0001F601 \n\n'
                 '/show : it will show you all the contacts including name,lastname,their adress and their job.\n\n'
                 '/show_people : it will show only the names and family name.\n\n'
                 '/add : it will let you to add someone to contacts. to use it you should do the following way:\n'
                 'add \nname \nlastname \nadress \njob\n\n'
                 '/find : it will help you to find someone based on their familyname. to use it:\n'
                 'find\nfamilyname\n\n'
                 '/remove : it will help you to remove a contact. to use it:\n'
                 'remove\nname\nlastname\n\n'
                 '/change : it will let you to change details. to use it:\n'
                 'change\nname\nlastname\naddress\njob\nnew name\nnew lastname\nnew address\nnew job\n\n'
                 '/save : it will help you to save the contacts in a text file.\n\n'
                 '/delete_all : it will clear the text file.\n\n'
                 '/sort_by_lastname : it will sort the contacts by their family name and then it will show it.\n\n'
                 '/sort_by_job : it will sort the contacts by their  job and then it will show it to you.\n\n'
                 'hope you enjoy!\U0001F605')
bot.send_message(chat_id='Milad_Nooraiy',
                 text='Now,How can i help you?!\U0001F607')
bot.stop()

#some examples
contacts = [['ali', 'karimi', 'tehran', 'player', '+981111111111'], ['sara', 'monjezi', 'mashhad', 'dentist', '+982222222222'],
            ['mina', 'akbari', 'shiraz', 'teacher', '+983333333333'], ['alireza', 'samimi', 'esfehan', 'student', '+984444444444']]


#showing all contacts with their information
def show():
    lis = contacts.copy()
    for i in range(len(lis)):
        lis[i] = ','.join(lis[i])
    for i in lis:
        bot.send_message(chat_id='Milad_Nooraiy', text=i)


#showing name and last name of contacts
def show_people():
    lis = contacts.copy()
    lst = []
    for i in range(len(lis)):
        lst += [lis[i][0:2]]
    for i in range(len(lst)):
        lst[i] = ','.join(lst[i])
    for i in lst:
        bot.send_message(chat_id='Milad_Nooraiy', text=i)

#adding a new contact
def add(a):
    del a[0]
    global contacts
    contacts += [a]

#finding a contact based on last name
def find(a):
    b = a[1]
    lis = contacts.copy()
    for i in range(len(lis)):
        if lis[i][1] == b:
            lis[i] = ','.join(lis[i])
            bot.send_message(chat_id='Milad_Nooraiy', text=lis[i])

#removing a contact based on first and last name
def remove(a):
    b = a[1]
    c = a[2]
    global contacts
    for i in range(len(contacts)):
        if (contacts[i][0] == b) and (contacts[i][1] == c):
            del contacts[i]
            break

#changing information of contact
def change(a):
    lis1 = a[1:5]
    lis2 = a[5:9]
    global contacts
    for i in range(len(contacts)):
        if contacts[i] == lis1:
            del contacts[i]
            break
    contacts += [lis2]

#saving all contacts in a text file
def save():
    global contacts
    f = open('phone_book_text.txt', 'a')
    for i in range(len(contacts)):
        a = ','.join(contacts[i])
        f.write(a+'\n')
    f.close


#clearing the file
def delete_all():
    f = open('phone_book_text.txt', 'w')
    f.close()


#sorting contacts based on last name
def sort_by_lastname():
    global contacts
    lis2, lis3 = [], []
    for i in range(len(contacts)):
        lis2 += [contacts[i][1]]
    lis2 = list(set(lis2))
    lis2.sort()
    n = 0
    while n != len(lis2):
        for i in range(len(contacts)):
            if contacts[i][1] == lis2[n]:
                lis3 += [contacts[i]]
        n += 1
    contacts = lis3
    show()


#sorting contacts based on job
def sort_by_job():
    global contacts
    lis2, lis3 = [], []
    for i in range(len(contacts)):
        lis2 += [contacts[i][3]]
    lis2 = list(set(lis2))
    lis2.sort()
    n = 0
    while n != len(lis2):
        for i in range(len(contacts)):
            if contacts[i][3] == lis2[n]:
                lis3 += [contacts[i]]
        n += 1
    contacts = lis3
    show()


#actions based on input
@bot.on_message()
def fun(app: Client, message: Message):
    if message.text == '/show':
        app.send_message(chat_id=message.chat.id,
                         text='These are your contacts!')
        show()
    elif message.text == '/show_people':
        app.send_message(chat_id=message.chat.id, text='Here you go:')
        show_people()
    elif message.text[0:4] == '/add':
        a = message.text.split('\n')
        app.send_message(chat_id=message.chat.id,
                         text='The contact has been added')
        add(a)
    elif message.text[0:5] == '/find':
        a = message.text.split('\n')
        find(a)
    elif message.text[0:7] == '/remove':
        a = message.text.split('\n')
        app.send_message(chat_id=message.chat.id,
                         text='The contact has been removed')
        remove(a)
    elif message.text[0:7] == '/change':
        a = message.text.split('\n')
        change(a)
        app.send_message(chat_id=message.chat.id,
                         text='The contact has been changed')
    elif message.text == '/save':
        app.send_message(chat_id=message.chat.id,
                         text='The text file is ready')
        save()
    elif message.text == '/delete_all':
        app.send_message(chat_id=message.chat.id,
                         text='The text file is empty now')
        delete_all()
    elif message.text == '/sort_by_lastname':
        app.send_message(chat_id=message.chat.id,
                         text='Here\'s the sorted list:')
        sort_by_lastname()
    elif message.text == '/sort_by_job':
        app.send_message(chat_id=message.chat.id,
                         text='Here\'s the sorted list:')
        sort_by_job()
    else:
        app.send_message(chat_id=message.chat.id,
                         text='sorry,there is no command like this!\U0001F642')


bot.run()
