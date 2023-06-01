import telebot, wikipedia, re
# ������� ��������� ����
bot = telebot.TeleBot('6225197499:AAG9qAOpIF7VlrmTPptDAEuPORcnIbv4BrE')
# ������������� ������� ���� � Wikipedia
wikipedia.set_lang("ru")
# ������ ����� ������ � Wikipedia � ������������ ��� ������� ��������
def getwiki(s):
    try:
        ny = wikipedia.page(s)
        # �������� ������ ������ ��������
        wikitext=ny.content[:1000]
        # ��������� �� ������
        wikimas=wikitext.split('.')
        # ����������� ��� ����� ��������� �����
        wikimas = wikimas[:-1]
        # ������� ������ ���������� ��� ������
        wikitext2 = ''
        # ���������� �� �������, ��� ��� ������ ������ (�� ���� ���, ����� ����������)
        for x in wikimas:
            if not('==' in x):
                    # ���� � ������ �������� ������ ���� ��������, ��������� �� � ����� ���������� � ���������� ��������� ��� ���������� ����� ����� �� �����
                if(len((x.strip()))>3):
                   wikitext2=wikitext2+x+'.'
            else:
                break
        # ������ ��� ������ ���������� ��������� ������� ��������
        wikitext2=re.sub('\([^()]*\)', '', wikitext2)
        wikitext2=re.sub('\([^()]*\)', '', wikitext2)
        wikitext2=re.sub('\{[^\{\}]*\}', '', wikitext2)
        # ���������� ��������� ������
        return wikitext2
    # ������������ ����������, ������� ��� ������� ������ wikipedia ��� �������
    except Exception as e:
        return '� ������������ ��� ���������� �� ����'
# �������, �������������� ������� /start
@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, '��������� ��� ����� �����, � � ����� ��� �������� �� Wikipedia')
# ��������� ��������� �� �����
@bot.message_handler(content_types=["text"])
def handle_text(message):
    bot.send_message(message.chat.id, getwiki(message.text))
# ��������� ����
bot.polling(none_stop=True, interval=0)

