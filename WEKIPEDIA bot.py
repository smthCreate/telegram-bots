import telebot, wikipedia, re

bot = telebot.TeleBot("5451433300:AAENDqQbDjiD2UD34Cm4HD-IA_erIj8PPoY")

wikipedia.set_lang("ru")

def getwiki(s):
    try:
        ny=wikipedia.page(s)
        wikitext = ny.content[:1000]
        wikimas=wikitext.split('.')
        wikimas = wikimas[:-1]
        wikitext2 = ''
        for x in wikimas:
            if not('==' in x):
                if(len((x.strip()))>3):
                    wikitext2 = wikitext2+x+'.'
            else:
                break

        wikitext2=re.sub('\([^()]*\'', '',wikitext2)
        wikitext2 = re.sub('\([^()]*\'', '', wikitext2)
        wikitext2 = re.sub('\([^()]*\'', '', wikitext2)
        return wikitext2
    except Exception as e:
        return "По вашему запросу нет статьи на Wiki"

@bot.message_handler(commands=["start"])
def start(m,res=False):
    bot.send_message(m.chat.id,"Что поискать?")

@bot.message_handler(content_types=["text"])
def handle_text(message):
    answer = "Вот что я нашёл: "+getwiki(message.text)
    bot.send_message(message.chat.id,answer)

bot.polling(none_stop=True, interval=0)