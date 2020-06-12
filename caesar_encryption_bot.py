pip install pytelegrambotapi

# Подключаем модуль случайных чисел // Connect the random number module
import random

# Подключаем модуль для Телеграма // Connect the module for Telegram
import telebot

# Токен // Token 
bot = telebot.TeleBot('@YOUR_TOKEN@')

# Алфавит // Alphabet
alphabet_e = 'abcdefghijklmnopqrstuvwxyz'
alphabet_r = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
# Ключ(число, на которое символ будет смещаться) // Key (number by which the symbol will be shifted) 
k = 14 

# Метод, который получает сообщения и обрабатывает их // A method that receives messages and processes them
@bot.message_handler(content_types=['text']) 

def caezzar(message):
  #Переход в режим шифрования // Release to encryption mode 
  if message.text.lower() == 'enc':
    bot.send_message(message.from_user.id, "Encription mod on") 
    global k
    k *= 1
  #Переход в режим дешифрования // Release to decryption mode 
  if message.text.lower() == 'dec':
    bot.send_message(message.from_user.id, "Decription mod on")
    k *= -1

  if message.text.lower() != 'dec' and message.text.lower() != 'enc':
    msg = message.text.lower()

    # Зашифрованное/расшифрованное сообщение // Encrypted/Decrypted message
    output = ''

    for let in msg:

      if let in alphabet_e: 
        t = alphabet_e.find(let)
       # upd_let - смещенный символ // offset character
        upd_let = (t + k) % len(alphabet_e)
        output += alphabet_e[upd_let]

      if let in alphabet_r:
        t = alphabet_r.find(let)
       # upd_let - смещенный символ // offset character
        upd_let = (t + k) % len(alphabet_r)
        output += alphabet_r[upd_let]
     
      else:
        output += let 
    # Отправляем зашифрованное/расшифрованное сообщение пользователю // Send an encrypted/decrypted message to the user
    bot.send_message(message.from_user.id, output)    

# Запускаем постоянную работу бота в Телеграме // Launching a permanent bot job in Telegram
bot.polling(none_stop=True, interval=0)

