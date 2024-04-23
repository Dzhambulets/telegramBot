import telebot
import my_bot

bot= telebot.Telebot(config.TOKEN)

@bot.message.handler(content_types=['text'])
del repeat_all_messages(message):
	bot.send_message(message.chat.id.message.text)

bot.polling(none_stop=True)