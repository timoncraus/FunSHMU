def check(mass):
    bio = 0
    info = 0
    eng = 0
    rus = 0
    mass, dv = mass[:6], mass[-1:-9: -1]
    dv2 = ('работа на секретном объекте', 'работа в лаборатории', 'выпуск актуальных продуктов',
           'общение с большим количеством людей', 'помощь людям', 'изучение планеты',
           'работа с документами', 'разработка игр')

    for j in range(8):
        if dv[j] is True:
            mass.append(dv2[j])

    d = {'bio': ['на природе', 'национальный парк', 'ведёшь себя спокойно', 'человеком практичным',
                 'обучать навыкам работы', 'наблюдение', 'изучение планеты', 'рнабота в лаборатории'],
         'info': ['за компьютером', 'офис крупной IT-компании или какой-нибудь IT-воркшоп',
                  'ведёшь себя спокойно', 'человеком практичным',
                  'давать знания', 'моделирование', 'работа на секретном объекте', 'разработка игр'],
         'rus': ['за чтением книги', 'старинную библиотеку или знаменитый книжный магазин',
                 'проявляешь общительность', 'выдумщиком, романтиком',
                 'учить общению с другими детьми', 'анализ', 'выпуск актуальных продуктов',
                 'работа с документами'],
         'eng': ['общаясь с друзьями', 'любое, где можно пообщаться с местными жителями',
                 'проявляешь общительность', 'выдумщиком, романтиком',
                 'учить общению с другими детьми', 'сравнение', 'общение с большим количеством людей',
                 'помощь людям']} 
    for i in mass:
        if i in d['bio']:
            bio += 1
        if i in d['info']:
            info += 1
        if i in d['rus']:
            rus += 1
        if i in d['eng']:
            eng += 1
    m = [('info', info), ('eng', eng), ('bio', bio), ('rus', rus)]
    m.sort(key=lambda x: x[1])
    return m[-1]
    
    
from flask import Flask
from flask import render_template, redirect, request
from forms.user import Test


app = Flask(__name__)

app.config['SECRET_KEY'] = 'our_key'

@app.route('/')
def index():
    return render_template('main.html')

@app.route('/vozhatie')
def vozhatie():
    return render_template('vozhatie.html')

@app.route('/traditions')
def traditions():
    return render_template('traditions.html')

@app.route('/results_rus')
def rus():
    return render_template('results_rus.html')

@app.route('/results_eng')
def eng():
    return render_template('results_eng.html')

@app.route('/results_info')
def info():
    return render_template('results_info.html')

@app.route('/results_bio')
def bio():
    return render_template('results_bio.html')

@app.route('/memes')
def memes():
    return render_template('memes.html')

@app.route('/test_1', methods=['GET', 'POST'])
def test_1():
    total = 0
    form = Test()
    if form.validate_on_submit():
        user_answers = list(form.data.values())
        user_answers = user_answers[:-2]
        res = check(user_answers)
        if res[0] == 'eng':
            return redirect('/results_eng')
        if res[0] == 'rus':
            return redirect('/results_rus')
        if res[0] == 'info':
            return redirect('/results_info')
        if res[0] == 'bio':
            return redirect('/results_bio')
    return render_template('test_1.html', title='Тест на предмет', form=form)

@app.route('/testing', methods=['POST', 'GET'])
def testing():
    f = open("my.txt", "w")
    f.write("")
    f.close()
    res = render_template('testing.html', link="location.href='/l1';", minLength="-1", confirmed="t")
    return res

def l1():
    if request.method=="POST":
        actList = ""
        f = open("my.txt", "a")
        for i in range(9):
            try:
                f.write(request.form['v' + str(i+1)])
                actList+=request.form['v' + str(i+1)]
            except:
                pass
        f.close()
        return render_template('testing5.html', link="location.href='/l2';", link2="/l1", num="1", maxLength="1", minLength="0",
            text="Если бы вы могли сделать так, чтобы определенной вещи больше не было, то что бы это была за вещь?", confirmed="t", activeButtons=actList, variant1="Насилие", variant2="Сомнения", variant3="Болезни", variant4="Токсичность", variant5="Каподастр", variant6="Ручка", variant7="Алкоголь и сигареты", variant8="Сонный паралич", variant9="Бессмысленные вещи")
    return render_template('testing5.html', link="location.href='/l2';", link2="/l1", num="1", maxLength="1", minLength="0",
        text="Если бы вы могли сделать так, чтобы определенной вещи больше не было, то что бы это была за вещь?", confirmed="f", variant1="Насилие", variant2="Сомнения", variant3="Болезни", variant4="Токсичность", variant5="Каподастр", variant6="Ручка", variant7="Алкоголь и сигареты", variant8="Сонный паралич", variant9="Бессмысленные вещи")
app.add_url_rule('/l1', 'l1', l1, methods=['POST', 'GET'])


def l2():
    if request.method=="POST":
        f = open("my.txt", "a")
        f.write("\n" + request.form['rr'])
        f.close()
        return render_template('testing4.html', link="location.href='/l3';", link2="/l2", num="2",
            text="Если человек вас предал, вы скорее простите его и дадите второй шанс (0%), просто перестанете с ним общаться (50%) или как-либо ему отомстите (100%)?", confirmed="t", activeButtons=request.form['rr'])
    return render_template('testing4.html', link="location.href='/l3';", link2="/l2", num="2",
        text="Если человек вас предал, вы скорее простите его и дадите второй шанс (0%), просто перестанете с ним общаться (50%) или как-либо ему отомстите (100%)?", confirmed="f")
app.add_url_rule('/l2', 'l2', l2, methods=['POST', 'GET'])


def l3():
    if request.method=="POST":
        actList = ""
        f = open("my.txt", "a")
        f.write("\n")
        for i in range(9):
            try:
                f.write(request.form['v' + str(i+1)])
                actList+=request.form['v' + str(i+1)]
            except:
                pass
        f.close()
        return render_template('testing6.html', link="location.href='/l4';", link2="/l3", num="3", maxLength="2", minLength="0",
            text="Если бы вам пришлось каждый день завтракать одним и тем же, то что бы вы выбрали?", confirmed="t", activeButtons=actList, variant1="Жульен", variant2="Вода", variant3="Бутерброд с чаем", variant4="Яичница", variant5="Сырники", variant6="Блины", variant7="Мясо по-французски", variant8="Греческий салат")
    return render_template('testing6.html', link="location.href='/l4';", link2="/l3", num="3", maxLength="2", minLength="0",
        text="Если бы вам пришлось каждый день завтракать одним и тем же, то что бы вы выбрали?", confirmed="f", variant1="Жульен", variant2="Вода", variant3="Бутерброд с чаем", variant4="Яичница", variant5="Сырники", variant6="Блины", variant7="Мясо по-французски", variant8="Греческий салат")
app.add_url_rule('/l3', 'l3', l3, methods=['POST', 'GET'])

def l4():
    if request.method=="POST":
        actList = ""
        f = open("my.txt", "a")
        f.write("\n")
        for i in range(9):
            try:
                f.write(request.form['v' + str(i+1)])
                actList+=request.form['v' + str(i+1)]
            except:
                pass
        f.close()
        return render_template('testing7.html', link="location.href='/l5';", link2="/l4", num="4", maxLength="2", minLength="0",
            text="Если бы вы вели свой личный дневник, ежедневно записывая в него произошедшие события, то какого цвета были бы страницы в нем?", confirmed="t", activeButtons=actList, variant1="Белые", variant2="Желтенькие", variant3="Разноцветные", variant4="Кофейные", variant5="Цвета чернил", variant6="Сиреневые", variant7="Бежевые")
    return render_template('testing7.html', link="location.href='/l5';", link2="/l4", num="4", maxLength="2", minLength="0",
        text="Если бы вы вели свой личный дневник, ежедневно записывая в него произошедшие события, то какого цвета были бы страницы в нем?", confirmed="f", variant1="Белые", variant2="Желтенькие", variant3="Разноцветные", variant4="Кофейные", variant5="Цвета чернил", variant6="Сиреневые", variant7="Бежевые")
app.add_url_rule('/l4', 'l4', l4, methods=['POST', 'GET'])


def l5():
    if request.method=="POST":
        f = open("my.txt", "a")
        f.write("\n" + request.form['rr'])
        f.close()
        return render_template('testing4.html', link="location.href='/l6';", link2="/l5", num="5",
            text="Вам по душе больше работать в одиночестве (0%), урегулировано и чередуясь (50%) или в команде (100%)?", confirmed="t", activeButtons=request.form['rr'])
    return render_template('testing4.html', link="location.href='/l6';", link2="/l5", num="5",
        text="Вам по душе больше работать в одиночестве (0%), урегулировано и чередуясь (50%) или в команде (100%)?", confirmed="f")
app.add_url_rule('/l5', 'l5', l5, methods=['POST', 'GET'])

def l6():
    if request.method=="POST":
        f = open("my.txt", "a")
        f.write("\n" + request.form['v1'])
        f.close()
        return render_template('testing1.html', link="location.href='/l7';", link2="/l6", num="6", maxLength="1", minLength="0",
        text="Считаете ли вы себя азартным человеком?", confirmed="t", activeButtons=request.form['v1'])
    return render_template('testing1.html', link="location.href='/l7';", link2="/l6", num="6", maxLength="1", minLength="0",
        text="Считаете ли вы себя азартным человеком?", confirmed="f")
app.add_url_rule('/l6', 'l6', l6, methods=['POST', 'GET'])

def l7():
    kn = 7
    if request.method=="POST":
        f = open("my.txt", "a")
        f.write("\n" + request.form['rr'])
        f.close()
        return render_template('testing4.html', link="location.href='/l" + str(kn+1) + "';", link2="/l" + str(kn), num=str(kn),
            text="Вам скорее по душе вдумчивое и усидчивое занятие (0%) или частая смена деятельности, в которой важна скорость решений (100%)?", confirmed="t", activeButtons=request.form['rr'])
    return render_template('testing4.html', link="location.href='/l" + str(kn+1) + "';", link2="/l" + str(kn), num=str(kn),
        text="Вам скорее по душе вдумчивое и усидчивое занятие (0%) или частая смена деятельности, в которой важна скорость решений (100%)?", confirmed="f")
app.add_url_rule('/l7', 'l7', l7, methods=['POST', 'GET'])


def l8():
    if request.method=="POST":
        actList = ""
        f = open("my.txt", "a")
        f.write("\n")
        for i in range(9):
            try:
                f.write(request.form['v' + str(i+1)])
                actList+=request.form['v' + str(i+1)]
            except:
                pass
        f.close()
        return render_template('testing5.html', link="location.href='/l9';", link2="/l8", num="8", maxLength="2", minLength="0",
            text="Если бы вам выпал абсолютно свободный день, то каким занятием вы бы больше всего его заполнили?", confirmed="t", activeButtons=actList, variant1="Прогулка с друзьями", variant2="Чтение", variant3="Волейбол", variant4="Рисование", variant5="Сериалы", variant6="Выпечка", variant7="Игра в компьютер", variant8="Танцы", variant9="Прогулка по полю в прохладный осенний день")
    return render_template('testing5.html', link="location.href='/l9';", link2="/l8", num="8", maxLength="2", minLength="0",
        text="Если бы вам выпал абсолютно свободный день, то каким занятием вы бы больше всего его заполнили?", confirmed="f", variant1="Прогулка с друзьями", variant2="Чтение", variant3="Волейбол", variant4="Рисование", variant5="Сериалы", variant6="Выпечка", variant7="Игра в компьютер", variant8="Танцы", variant9="Прогулка по полю в прохладный осенний день")
app.add_url_rule('/l8', 'l8', l8, methods=['POST', 'GET'])

def l9():
    if request.method=="POST":
        f = open("my.txt", "a")
        f.write("\n" + request.form['v1'])
        f.close()
        return render_template('testing1.html', link="location.href='/l10';", link2="/l9", num="9", maxLength="1", minLength="0",
        text="Вы чувствуете себя более заряженным и энергичным после длительного пребывания в одиночестве?", confirmed="t", activeButtons=request.form['v1'])
    return render_template('testing1.html', link="location.href='/l10';", link2="/l9", num="9", maxLength="1", minLength="0",
        text="Вы чувствуете себя более заряженным и энергичным после длительного пребывания в одиночестве?", confirmed="f")
app.add_url_rule('/l9', 'l9', l9, methods=['POST', 'GET'])

def l10():
    if request.method=="POST":
        f = open("my.txt", "a")
        f.write("\n" + request.form['v1'])
        f.close()
        return render_template('testing1.html', link="location.href='/l11';", link2="/l10", num="10", maxLength="1", minLength="0",
        text="Легко ли вас вывести из себя в обычное время?", confirmed="t", activeButtons=request.form['v1'])
    return render_template('testing1.html', link="location.href='/l11';", link2="/l10", num="10", maxLength="1", minLength="0",
        text="Легко ли вас вывести из себя в обычное время?", confirmed="f")
app.add_url_rule('/l10', 'l10', l10, methods=['POST', 'GET'])

def l11():
    kn = 11
    if request.method=="POST":
        f = open("my.txt", "a")
        f.write("\n" + request.form['rr'])
        f.close()
        return render_template('testing4.html', link="location.href='/l" + str(kn+1) + "';", link2="/l" + str(kn), num=str(kn),
            text="Вы считаете, что у вас скорее низкая (0%), умеренная (%) или высокая самооценка (100%)?", confirmed="t", activeButtons=request.form['rr'])
    return render_template('testing4.html', link="location.href='/l" + str(kn+1) + "';", link2="/l" + str(kn), num=str(kn),
        text="Вы считаете, что у вас скорее низкая (0%), умеренная (%) или высокая самооценка (100%)?", confirmed="f")
app.add_url_rule('/l11', 'l11', l11, methods=['POST', 'GET'])

def l12():
    if request.method=="POST":
        f = open("my.txt", "a")
        f.write("\n" + request.form['v1'])
        f.close()
        return render_template('testing1.html', link="location.href='/l13';", link2="/l12", num="12", maxLength="1", minLength="0",
        text="Вы считаете себя впечатлительным человеком?", confirmed="t", activeButtons=request.form['v1'])
    return render_template('testing1.html', link="location.href='/l13';", link2="/l12", num="12", maxLength="1", minLength="0",
        text="Вы считаете себя впечатлительным человеком?", confirmed="f")
app.add_url_rule('/l12', 'l12', l12, methods=['POST', 'GET'])

def l13():
    if request.method=="POST":
        f = open("my.txt", "a")
        f.write("\n" + request.form['v1'])
        f.close()
        return render_template('testing1.html', link="location.href='/l14';", link2="/l13", num="12", maxLength="1", minLength="0",
        text="Свойственна ли вам резкая смена настроения?", confirmed="t", activeButtons=request.form['v1'])
    return render_template('testing1.html', link="location.href='/l14';", link2="/l13", num="12", maxLength="1", minLength="0",
        text="Свойственна ли вам резкая смена настроения?", confirmed="f")
app.add_url_rule('/l13', 'l13', l13, methods=['POST', 'GET'])

def l14():
    if request.method=="POST":
        actList = ""
        f = open("my.txt", "a")
        f.write("\n")
        for i in range(9):
            try:
                f.write(request.form['v' + str(i+1)])
                actList+=request.form['v' + str(i+1)]
            except:
                pass
        f.close()
        return render_template('testing7.html', link="location.href='/l15';", link2="/l14", num="14", maxLength="1", minLength="0",
            text="Если бы у вас была возможность прожить следующие 5 лет в определенной стране, то какую бы выбрали?", confirmed="t", activeButtons=actList, variant1="Франция", variant2="Грузия", variant3="Швейцария", variant4="Италия", variant5="Россия", variant6="Испания", variant7="Швеция")
    return render_template('testing7.html', link="location.href='/l15';", link2="/l14", num="14", maxLength="1", minLength="0",
        text="Если бы у вас была возможность прожить следующие 5 лет в определенной стране, то какую бы выбрали?", confirmed="f", variant1="Франция", variant2="Грузия", variant3="Швейцария", variant4="Италия", variant5="Россия", variant6="Испания", variant7="Швеция")
app.add_url_rule('/l14', 'l14', l14, methods=['POST', 'GET'])

def l15():
    if request.method=="POST":
        actList = ""
        f = open("my.txt", "a")
        f.write("\n")
        for i in range(9):
            try:
                f.write(request.form['v' + str(i+1)])
                actList+=request.form['v' + str(i+1)]
            except:
                pass
        f.close()
        return render_template('testing6.html', link="location.href='/l16';", link2="/l15", num="15", maxLength="2", minLength="0",
            text="Какой запах вам более всего нравится?", confirmed="t", activeButtons=actList, variant1="Корицы", variant2="Книг", variant3="Раннего летнего утра", variant4="Свежей выпечки", variant5="Акации", variant6="После небольшого дождя", variant7="Капучино", variant8="Свежего постельного белья")
    return render_template('testing6.html', link="location.href='/l16';", link2="/l15", num="15", maxLength="2", minLength="0",
        text="Какой запах вам более всего нравится?", confirmed="f", variant1="Корицы", variant2="Книг", variant3="Раннего летнего утра", variant4="Свежей выпечки", variant5="Акации", variant6="После небольшого дождя", variant7="Капучино", variant8="Свежего постельного белья")
app.add_url_rule('/l15', 'l15', l15, methods=['POST', 'GET'])

def l16():
    if request.method=="POST":
        f = open("my.txt", "a")
        f.write("\n" + request.form['v1'])
        f.close()
        return render_template('testing1.html', link="location.href='/testingEnd';", link2="/l16", num="16", maxLength="1", minLength="0",
        text="На вас ездят на рыбалочку?", confirmed="t", activeButtons=request.form['v1'])
    return render_template('testing1.html', link="location.href='/testingEnd';", link2="/l16", num="16", maxLength="1", minLength="0",
        text="На вас ездят на рыбалочку?", confirmed="f")
app.add_url_rule('/l16', 'l16', l16, methods=['POST', 'GET'])

def testingEnd():
    f = open("my.txt", "r")
    answers = f.readlines()
    answers = list(map(lambda x:x.strip(), answers))
    f.close()


    myDict = {"Аня Дуюнова":0, "Саша Маркелова":0, "Максим Минаев":0, "Аделина Аветисян":0, "Матвей Суворин":0, "Ваня Спасёнов":0, "Стёпа Цыганов":0, "Полина Игнатюк":0, "Лера Иванова":0, "Даня Квятосинский":0}
    if answers[0] == "1":
        myDict["Аня Дуюнова"]+=1
        myDict["Саша Маркелова"]+=1
    elif answers[0] == "2":
        myDict["Максим Минаев"]+=1
    elif answers[0] == "3":
        myDict["Аделина Аветисян"]+=1
    elif answers[0] == "4":
        myDict["Матвей Суворин"]+=1
    elif answers[0] == "5":
        myDict["Даня Квятосинский"]+=1
    elif answers[0] == "6":
        myDict["Стёпа Цыганов"]+=1
    elif answers[0] == "7":
        myDict["Полина Игнатюк"]+=1
    elif answers[0] == "8":
        myDict["Лера Иванова"]+=1
    elif answers[0] == "9":
        myDict["Ваня Спасёнов"]+=1

    if int(answers[1]) <= 10:
        myDict["Даня Квятосинский"]+=1
    elif int(answers[1]) > 10 and int(answers[1]) <= 20:
        myDict["Даня Квятосинский"]+=0.5
    elif int(answers[1]) > 20 and int(answers[1]) <= 30:
        myDict["Ваня Спасёнов"]+=0.5
        myDict["Лера Иванова"]+=0.5
    elif int(answers[1]) > 30 and int(answers[1]) <= 40:
        myDict["Ваня Спасёнов"]+=1
        myDict["Лера Иванова"]+=1
        myDict["Аделина Аветисян"]+=0.7
    elif int(answers[1]) > 40 and int(answers[1]) <= 50:
        myDict["Ваня Спасёнов"]+=1
        myDict["Лера Иванова"]+=1
        myDict["Аделина Аветисян"]+=1
        myDict["Аня Дуюнова"]+=1
        myDict["Саша Маркелова"]+=1
        myDict["Максим Минаев"]+=1
        myDict["Матвей Суворин"]+=1
        myDict["Полина Игнатюк"]+=1
    elif int(answers[1]) > 50 and int(answers[1]) <= 60:
        myDict["Ваня Спасёнов"]+=0.5
        myDict["Лера Иванова"]+=0.5
        myDict["Аделина Аветисян"]+=0.7
        myDict["Аня Дуюнова"]+=1
        myDict["Саша Маркелова"]+=1
        myDict["Максим Минаев"]+=1
        myDict["Матвей Суворин"]+=1
        myDict["Полина Игнатюк"]+=1
    elif int(answers[1]) > 60 and int(answers[1]) <= 70:
        myDict["Аня Дуюнова"]+=0.5
        myDict["Саша Маркелова"]+=0.5
        myDict["Максим Минаев"]+=0.5
        myDict["Матвей Суворин"]+=0.5
        myDict["Полина Игнатюк"]+=0.5
    elif int(answers[1]) > 70 and int(answers[1]) <= 80:
        pass
    elif int(answers[1]) > 80 and int(answers[1]) <= 90:
        myDict["Стёпа Цыганов"]+=0.5
    elif int(answers[1]) > 90:
        myDict["Стёпа Цыганов"]+=1

    if answers[2] == "1":
        myDict["Стёпа Цыганов"]+=1
    elif answers[2] == "2":
        myDict["Даня Квятосинский"]+=1
    elif answers[2] == "3":
        myDict["Матвей Суворин"]+=1
    elif answers[2] == "4":
        myDict["Максим Минаев"]+=1
    elif answers[2] == "5":
        myDict["Лера Иванова"]+=1
        myDict["Аня Дуюнова"]+=1
    elif answers[2] == "6":
        myDict["Ваня Спасёнов"]+=1
    elif answers[2] == "7":
        myDict["Аделина Аветисян"]+=1
    elif answers[2] == "8":
        myDict["Полина Игнатюк"]+=1
        myDict["Саша Маркелова"]+=1

    if answers[3].find("1") != -1:
        myDict["Ваня Спасёнов"]+=1
        myDict["Матвей Суворин"]+=1
    elif answers[3].find("2") != -1:
        myDict["Аделина Аветисян"]+=1
    elif answers[3].find("3") != -1:
        myDict["Лера Иванова"]+=1
    elif answers[3].find("4") != -1:
        myDict["Стёпа Цыганов"]+=1
    elif answers[3].find("5") != -1:
        myDict["Даня Квятосинский"]+=1
    elif answers[3].find("6") != -1:
        myDict["Аня Дуюнова"]+=1
        myDict["Полина Игнатюк"]+=1
    elif answers[3].find("7") != -1:
        myDict["Аня Дуюнова"]+=1
        myDict["Саша Маркелова"]+=1

    if int(answers[4]) <= 10:
        myDict["Даня Квятосинский"]+=0.7
        myDict["Аделина Аветисян"]+=0.8
        myDict["Саша Маркелова"]+=1
    elif int(answers[4]) > 10 and int(answers[4]) <= 20:
        myDict["Даня Квятосинский"]+=0.3
        myDict["Аделина Аветисян"]+=0.4
        myDict["Саша Маркелова"]+=0.5
    elif int(answers[4]) > 30 and int(answers[4]) <= 40:
        myDict["Даня Квятосинский"]+=0.3
        myDict["Стёпа Цыганов"]+=0.5
        myDict["Ваня Спасёнов"]+=0.5
        myDict["Аня Дуюнова"]+=0.5
    elif int(answers[4]) > 40 and int(answers[4]) <= 50:
        myDict["Даня Квятосинский"]+=0.7
        myDict["Стёпа Цыганов"]+=1
        myDict["Ваня Спасёнов"]+=1
        myDict["Аня Дуюнова"]+=1
    elif int(answers[4]) > 50 and int(answers[4]) <= 60:
        myDict["Даня Квятосинский"]+=0.7
        myDict["Стёпа Цыганов"]+=1
        myDict["Ваня Спасёнов"]+=1
        myDict["Аня Дуюнова"]+=1
    elif int(answers[4]) > 60 and int(answers[4]) <= 70:
        myDict["Даня Квятосинский"]+=0.3
        myDict["Стёпа Цыганов"]+=0.5
        myDict["Ваня Спасёнов"]+=0.5
        myDict["Аня Дуюнова"]+=0.5
        myDict["Максим Минаев"]+=0.5
        myDict["Матвей Суворин"]+=0.5
        myDict["Лера Иванова"]+=0.5
    elif int(answers[4]) > 70 and int(answers[4]) <= 80:
        myDict["Максим Минаев"]+=1
        myDict["Матвей Суворин"]+=1
        myDict["Лера Иванова"]+=1
    elif int(answers[4]) > 80 and int(answers[4]) <= 90:
        myDict["Максим Минаев"]+=0.5
        myDict["Матвей Суворин"]+=0.5
        myDict["Лера Иванова"]+=0.5
        myDict["Даня Квятосинский"]+=0.3
        myDict["Полина Игнатюк"]+=0.5
        myDict["Аделина Аветисян"]+=0.4
    elif int(answers[4]) > 90:
        myDict["Даня Квятосинский"]+=0.7
        myDict["Полина Игнатюк"]+=1
        myDict["Аделина Аветисян"]+=0.8

    if answers[5] == "1":
        myDict["Саша Маркелова"]+=1
        myDict["Ваня Спасёнов"]+=1
        myDict["Стёпа Цыганов"]+=1
    elif answers[5] == "-1":
        myDict["Аня Дуюнова"]+=1
        myDict["Максим Минаев"]+=1
        myDict["Аделина Аветисян"]+=1
        myDict["Матвей Суворин"]+=1
        myDict["Полина Игнатюк"]+=1
        myDict["Лера Иванова"]+=1
        myDict["Даня Квятосинский"]+=1

    if int(answers[6]) <= 10:
        myDict["Даня Квятосинский"]+=0.7
        myDict["Аделина Аветисян"]+=1
        myDict["Саша Маркелова"]+=1
        myDict["Полина Игнатюк"]+=1
    elif int(answers[6]) > 10 and int(answers[6]) <= 20:
        myDict["Даня Квятосинский"]+=0.3
        myDict["Аделина Аветисян"]+=0.5
        myDict["Саша Маркелова"]+=0.5
        myDict["Полина Игнатюк"]+=0.5
    elif int(answers[6]) > 30 and int(answers[6]) <= 40:
        myDict["Ваня Спасёнов"]+=0.5
    elif int(answers[6]) > 40 and int(answers[6]) <= 50:
        myDict["Ваня Спасёнов"]+=1
        myDict["Максим Минаев"]+=0.6
    elif int(answers[6]) > 50 and int(answers[6]) <= 60:
        myDict["Ваня Спасёнов"]+=1
        myDict["Максим Минаев"]+=1
        
    elif int(answers[6]) > 60 and int(answers[6]) <= 70:
        myDict["Ваня Спасёнов"]+=0.5
        myDict["Максим Минаев"]+=0.6
        myDict["Лера Иванова"]+=0.5
        myDict["Матвей Суворин"]+=0.5
        myDict["Аня Дуюнова"]+=0.5
    elif int(answers[6]) > 70 and int(answers[6]) <= 80:
        myDict["Лера Иванова"]+=1
        myDict["Матвей Суворин"]+=1
        myDict["Аня Дуюнова"]+=1
    elif int(answers[6]) > 80 and int(answers[6]) <= 90:
        myDict["Лера Иванова"]+=0.5
        myDict["Матвей Суворин"]+=0.5
        myDict["Аня Дуюнова"]+=0.5
        myDict["Стёпа Цыганов"]+=0.5
        myDict["Даня Квятосинский"]+=0.3
    elif int(answers[6]) > 90:
        myDict["Даня Квятосинский"]+=0.7
        myDict["Стёпа Цыганов"]+=1

    if answers[7].find("1") != -1:
        myDict["Матвей Суворин"]+=1
        myDict["Стёпа Цыганов"]+=1
        myDict["Даня Квятосинский"]+=1
    elif answers[7].find("2") != -1:
        myDict["Максим Минаев"]+=0.3
        myDict["Аделина Аветисян"]+=1
    elif answers[7].find("3") != -1:
        myDict["Ваня Спасёнов"]+=1
    elif answers[7].find("4") != -1:
        myDict["Саша Маркелова"]+=1
    elif answers[7].find("5") != -1:
        myDict["Максим Минаев"]+=0.3
        myDict["Аня Дуюнова"]+=1
    elif answers[7].find("6") != -1:
        myDict["Полина Игнатюк"]+=1
    elif answers[7].find("7") != -1:
        myDict["Максим Минаев"]+=0.3
        myDict["Ваня Спасёнов"]+=1
    elif answers[7].find("8") != -1:
        myDict["Аня Дуюнова"]+=1
    elif answers[7].find("9") != -1:
        myDict["Максим Минаев"]+=0.3
        myDict["Лера Иванова"]+=1

    if answers[8] == "1":
        myDict["Саша Маркелова"]+=1
        myDict["Стёпа Цыганов"]+=1
        myDict["Максим Минаев"]+=1
        myDict["Аделина Аветисян"]+=1
        myDict["Матвей Суворин"]+=1
        myDict["Даня Квятосинский"]+=0.4
    elif answers[8] == "-1":
        myDict["Аня Дуюнова"]+=1
        myDict["Ваня Спасёнов"]+=1
        myDict["Полина Игнатюк"]+=1
        myDict["Лера Иванова"]+=1
        myDict["Даня Квятосинский"]+=0.4

    if answers[9] == "1":
        myDict["Максим Минаев"]+=1
        myDict["Аделина Аветисян"]+=1
        myDict["Полина Игнатюк"]+=1
    elif answers[9] == "-1":
        myDict["Даня Квятосинский"]+=1
        myDict["Стёпа Цыганов"]+=1
        myDict["Матвей Суворин"]+=1
        myDict["Саша Маркелова"]+=1
        myDict["Аня Дуюнова"]+=1
        myDict["Ваня Спасёнов"]+=1
        myDict["Лера Иванова"]+=1

    if int(answers[10]) > 30 and int(answers[10]) <= 40:
        myDict["Ваня Спасёнов"]+=0.5
        myDict["Аделина Аветисян"]+=0.3
        myDict["Стёпа Цыганов"]+=0.3
        myDict["Полина Игнатюк"]+=0.3
        myDict["Лера Иванова"]+=0.3
    elif int(answers[10]) > 40 and int(answers[10]) <= 50:
        myDict["Ваня Спасёнов"]+=1
        myDict["Аделина Аветисян"]+=1
        myDict["Стёпа Цыганов"]+=1
        myDict["Полина Игнатюк"]+=1
        myDict["Лера Иванова"]+=1
        myDict["Аня Дуюнова"]+=0.3
        myDict["Матвей Суворин"]+=0.3
    elif int(answers[10]) > 50 and int(answers[10]) <= 60:
        myDict["Ваня Спасёнов"]+=0.5
        myDict["Аделина Аветисян"]+=1
        myDict["Стёпа Цыганов"]+=1
        myDict["Полина Игнатюк"]+=1
        myDict["Лера Иванова"]+=1
        myDict["Аня Дуюнова"]+=1
        myDict["Матвей Суворин"]+=1
        myDict["Даня Квятосинский"]+=0.3
    elif int(answers[10]) > 60 and int(answers[10]) <= 70:
        myDict["Аделина Аветисян"]+=0.3
        myDict["Стёпа Цыганов"]+=0.3
        myDict["Полина Игнатюк"]+=0.3
        myDict["Лера Иванова"]+=0.3
        myDict["Аня Дуюнова"]+=1
        myDict["Матвей Суворин"]+=1
        myDict["Даня Квятосинский"]+=1
    elif int(answers[10]) > 70 and int(answers[10]) <= 80:
        myDict["Даня Квятосинский"]+=1
        myDict["Максим Минаев"]+=0.5
    elif int(answers[10]) > 80 and int(answers[10]) <= 90:
        myDict["Даня Квятосинский"]+=0.3
        myDict["Максим Минаев"]+=1
        myDict["Саша Маркелова"]+=0.5
    elif int(answers[10]) > 90:
        myDict["Максим Минаев"]+=0.5
        myDict["Саша Маркелова"]+=1

    if answers[11] == "1":
        myDict["Аня Дуюнова"]+=1
        myDict["Саша Маркелова"]+=1
        myDict["Ваня Спасёнов"]+=1
        myDict["Стёпа Цыганов"]+=1
        myDict["Максим Минаев"]+=1
        myDict["Аделина Аветисян"]+=1
        myDict["Полина Игнатюк"]+=1
        myDict["Лера Иванова"]+=1
    elif answers[11] == "-1":
        myDict["Даня Квятосинский"]+=1
        myDict["Матвей Суворин"]+=1

    if answers[12] == "1":
        myDict["Аня Дуюнова"]+=1
        myDict["Саша Маркелова"]+=1
        myDict["Ваня Спасёнов"]+=1
        myDict["Стёпа Цыганов"]+=1
        myDict["Максим Минаев"]+=1
        myDict["Аделина Аветисян"]+=1
        myDict["Полина Игнатюк"]+=1
        myDict["Даня Квятосинский"]+=1
    elif answers[12] == "-1":
        myDict["Матвей Суворин"]+=1
        myDict["Лера Иванова"]+=1
        
    if answers[13].find("1") != -1:
        myDict["Стёпа Цыганов"]+=1
    elif answers[13].find("2") != -1:
        myDict["Саша Маркелова"]+=1
    elif answers[13].find("3") != -1:
        myDict["Матвей Суворин"]+=1
        myDict["Максим Минаев"]+=1
    elif answers[13].find("4") != -1:
        myDict["Полина Игнатюк"]+=1
    elif answers[13].find("5") != -1:
        myDict["Аделина Аветисян"]+=1
        myDict["Ваня Спасёнов"]+=1
    elif answers[13].find("6") != -1:
        myDict["Аня Дуюнова"]+=1
    elif answers[13].find("7") != -1:
        myDict["Лера Иванова"]+=1
    myDict["Даня Квятосинский"]+=0.2

    if answers[14].find("1") != -1:
        myDict["Полина Игнатюк"]+=1
    elif answers[14].find("2") != -1:
        myDict["Ваня Спасёнов"]+=1
    elif answers[14].find("3") != -1:
        myDict["Лера Иванова"]+=1
    elif answers[14].find("4") != -1:
        myDict["Аня Дуюнова"]+=1
    elif answers[14].find("5") != -1:
        myDict["Саша Маркелова"]+=1
    elif answers[14].find("6") != -1:
        myDict["Матвей Суворин"]+=1
    elif answers[14].find("7") != -1:
        myDict["Стёпа Цыганов"]+=1
        myDict["Ваня Спасёнов"]+=1
        myDict["Аделина Аветисян"]+=1
    elif answers[14].find("8") != -1:
        myDict["Максим Минаев"]+=1


    if answers[15] == "1":
        myDict["Саша Маркелова"]+=30

    max_val = max(myDict.values())
    final_dict = {k:v for k, v in myDict.items() if v == max_val}

    return render_template('testingEnd.html', person=str(list(final_dict.keys())[0]), text="Ваши баллы для каждого из вожатых: " + str(myDict))
app.add_url_rule('/testingEnd', 'testingEnd', testingEnd, methods=['POST', 'GET'])


if __name__ == '__main__':
    port = 50
    app.run(host='127.0.0.1', port=port, debug=True)

