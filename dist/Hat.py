import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QLCDNumber, QLabel, QLineEdit, QPushButton, QInputDialog
from PyQt5.QtGui import QPixmap
import random

cnt = 0
dif = 0
words = []
names = []
dict = []
words1 = []
score = []
tries = 0
k = 1
t = 0


class MyWidget(QMainWindow):
    def __init__(self):
        global cnt, dif
        super().__init__()
        uic.loadUi('window.ui', self)

        self.label_players_cnt.setVisible(False)
        self.pushButton_accept_cnt.setVisible(False)
        self.words_common.setVisible(False)
        self.words_dict.setVisible(False)
        self.words_common_and_dict.setVisible(False)
        self.Players_cnt_2.setVisible(False)
        self.Players_cnt_3.setVisible(False)
        self.Players_cnt_4.setVisible(False)
        self.Players_cnt_5.setVisible(False)
        self.Players_cnt_6.setVisible(False)
        self.Players_cnt_7.setVisible(False)
        self.Players_cnt_8.setVisible(False)
        self.Difficulty_easy.setVisible(False)
        self.Difficulty_normal.setVisible(False)
        self.Difficulty_hard.setVisible(False)
        self.Difficulty_hardcore.setVisible(False)

        self.Players_cnt_2.clicked.connect(self.cnt_choose_2)
        self.Players_cnt_3.clicked.connect(self.cnt_choose_3)
        self.Players_cnt_4.clicked.connect(self.cnt_choose_4)
        self.Players_cnt_5.clicked.connect(self.cnt_choose_5)
        self.Players_cnt_6.clicked.connect(self.cnt_choose_6)
        self.Players_cnt_7.clicked.connect(self.cnt_choose_7)
        self.Players_cnt_8.clicked.connect(self.cnt_choose_8)
        self.Difficulty_easy.clicked.connect(self.dif_choose_1)
        self.Difficulty_normal.clicked.connect(self.dif_choose_2)
        self.Difficulty_hard.clicked.connect(self.dif_choose_3)
        self.Difficulty_hardcore.clicked.connect(self.dif_choose_4)
        self.pushButton_Dictionary.clicked.connect(self.dict_words)

        self.guide_label = QLabel(self)
        self.guide_label.setVisible(False)
        self.guide_label.setText('Играют от 2 до 8 игроков. \n \
В свою очередь один игрок объясняет другому \n \
слово на экране, а тот пытается его угадать. \n \
За оба вида деятельности игроки получают по 1 очку.\n \n \
Нельзя во время объяснения: \n \
- Употреблять однокоренные слова \n \
- Показывать слово жестами \n \
- Показывать слово на экране угадывающему')
        self.guide_label.adjustSize()
        self.guide_label.move(20, 50)

        self.error_label = QLabel(self)
        self.error_label.setText('Не отмечено количество игроков/сложность')
        self.error_label.move(50, 100)
        self.error_label.setVisible(False)
        self.error_label.adjustSize()

        self.pushButton_Back = QPushButton('Назад', self)
        self.pushButton_Back.resize(self.pushButton_Back.sizeHint())
        self.pushButton_Back.move(120, 220)
        self.pushButton_Back.setVisible(False)

        self.pushButton_Back_from_dictionary = QPushButton('Назад', self)
        self.pushButton_Back_from_dictionary.resize(self.pushButton_Back_from_dictionary.sizeHint())
        self.pushButton_Back_from_dictionary.move(120, 220)
        self.pushButton_Back_from_dictionary.setVisible(False)

        self.pushButton_add_dictionary = QPushButton('Добавить', self)
        self.pushButton_add_dictionary.resize(self.pushButton_add_dictionary.sizeHint())
        self.pushButton_add_dictionary.move(45, 180)
        self.pushButton_add_dictionary.setVisible(False)

        self.pushButton_del_dictionary = QPushButton('Удалить', self)
        self.pushButton_del_dictionary.resize(self.pushButton_del_dictionary.sizeHint())
        self.pushButton_del_dictionary.move(120, 180)
        self.pushButton_del_dictionary.setVisible(False)

        self.pushButton_clear_dictionary = QPushButton('Очистить', self)
        self.pushButton_clear_dictionary.resize(self.pushButton_clear_dictionary.sizeHint())
        self.pushButton_clear_dictionary.move(195, 180)
        self.pushButton_clear_dictionary.setVisible(False)

        self.dict_label = QLabel(self)
        self.dict_label.setVisible(False)
        self.dict_label.move(20, 30)

        self.pushButton_Back1 = QPushButton('Назад', self)
        self.pushButton_Back1.resize(self.pushButton_Back1.sizeHint())
        self.pushButton_Back1.move(120, 220)
        self.pushButton_Back1.setVisible(False)
        self.pushButton_Back1.clicked.connect(self.step1)

        self.pushButton_Play.clicked.connect(self.settings)
        self.pushButton_Guide.clicked.connect(self.guide)
        self.pushButton_Exit.clicked.connect(self.out)

    def dict_words(self):
        global dict
        self.pushButton_Play.setVisible(False)
        self.pushButton_Guide.setVisible(False)
        self.pushButton_Exit.setVisible(False)
        self.pushButton_Dictionary.setVisible(False)
        self.pushButton_add_dictionary.setVisible(True)
        self.pushButton_del_dictionary.setVisible(True)
        self.pushButton_clear_dictionary.setVisible(True)
        self.dict_label.setVisible(True)

        dict = sorted(dict)
        s = ""
        for i in range(len(dict)):
            s += dict[i] + ' '
            if i != 0 and i % 6 == 0:
                s += "\n"
        self.dict_label.setText(s)
        self.dict_label.adjustSize()
        self.dict_label.setVisible(True)

        self.pushButton_Back_from_dictionary.setVisible(True)
        self.pushButton_Back_from_dictionary.clicked.connect(self.menu_1)
        self.pushButton_add_dictionary.setVisible(True)
        self.pushButton_add_dictionary.clicked.connect(self.add_word)
        self.pushButton_del_dictionary.setVisible(True)
        self.pushButton_del_dictionary.clicked.connect(self.delete_word)
        self.pushButton_clear_dictionary.setVisible(True)
        self.pushButton_clear_dictionary.clicked.connect(self.clear_dict)

    def add_word(self):
        global dict
        word, okBtnPressed = QInputDialog.getText(self, "Введите слово ", "Какое слово вы хотите добавить?")
        if okBtnPressed and not word in dict:
            dict.append(word)
            dict = sorted(dict)
            s = ""
            for i in range(len(dict)):
                s += dict[i] + ' '
                if i != 0 and i % 6 == 0:
                    s += "\n"
            self.dict_label.setText(s)
            self.dict_label.adjustSize()

    def delete_word(self):
        global dict
        word, okBtnPressed = QInputDialog.getText(self, "Введите слово ", "Какое слово вы хотите удалить?")
        if okBtnPressed and word in dict:
            del (dict[dict.index(word)])
            s = ""
            for i in range(len(dict)):
                s += dict[i] + ' '
                if i != 0 and i % 6 == 0:
                    s += "\n"
            self.dict_label.setText(s)
            self.dict_label.adjustSize()

    def clear_dict(self):
        global dict
        dict = []
        self.dict_label.setText("")
        self.dict_label.adjustSize()

    def menu_1(self):
        self.pushButton_Play.setVisible(True)
        self.pushButton_Guide.setVisible(True)
        self.pushButton_Exit.setVisible(True)
        self.pushButton_Dictionary.setVisible(True)

        self.pushButton_add_dictionary.setVisible(False)
        self.pushButton_del_dictionary.setVisible(False)
        self.pushButton_clear_dictionary.setVisible(False)
        self.dict_label.setVisible(False)
        self.pushButton_Back_from_dictionary.setVisible(False)

    def settings(self):
        self.pushButton_Back1.setVisible(False)
        self.error_label.setVisible(False)
        self.pushButton_Play.setVisible(False)
        self.pushButton_Guide.setVisible(False)
        self.pushButton_Exit.setVisible(False)
        self.pushButton_Dictionary.setVisible(False)

        self.label_players_cnt.setVisible(True)
        self.pushButton_accept_cnt.setVisible(True)
        self.Players_cnt_2.setVisible(True)
        self.Players_cnt_3.setVisible(True)
        self.Players_cnt_4.setVisible(True)
        self.Players_cnt_5.setVisible(True)
        self.Players_cnt_6.setVisible(True)
        self.Players_cnt_7.setVisible(True)
        self.Players_cnt_8.setVisible(True)
        self.Difficulty_easy.setVisible(True)
        self.Difficulty_normal.setVisible(True)
        self.Difficulty_hard.setVisible(True)
        self.Difficulty_hardcore.setVisible(True)

        self.pushButton_accept_cnt.clicked.connect(self.players)

    def cnt_choose_2(self):
        global cnt, dif
        cnt = 2

    def cnt_choose_3(self):
        global cnt, dif
        cnt = 3

    def cnt_choose_4(self):
        global cnt, dif
        cnt = 4

    def cnt_choose_5(self):
        global cnt, dif
        cnt = 5

    def cnt_choose_6(self):
        global cnt, dif
        cnt = 6

    def cnt_choose_7(self):
        global cnt, dif
        cnt = 7

    def cnt_choose_8(self):
        global cnt, dif
        cnt = 8

    def dif_choose_1(self):
        global cnt, dif
        dif = 1

    def dif_choose_2(self):
        global cnt, dif
        dif = 2

    def dif_choose_3(self):
        global cnt, dif
        dif = 3

    def dif_choose_4(self):
        global cnt, dif
        dif = 4

    def step1(self):
        self.error_label.setVisible(False)
        self.pushButton_Back1.setVisible(False)
        self.label_players_cnt.setVisible(True)
        self.Players_cnt_2.setVisible(True)
        self.Players_cnt_3.setVisible(True)
        self.Players_cnt_4.setVisible(True)
        self.Players_cnt_5.setVisible(True)
        self.Players_cnt_6.setVisible(True)
        self.Players_cnt_7.setVisible(True)
        self.Players_cnt_8.setVisible(True)
        self.Difficulty_easy.setVisible(True)
        self.Difficulty_normal.setVisible(True)
        self.Difficulty_hard.setVisible(True)
        self.Difficulty_hardcore.setVisible(True)
        self.pushButton_accept_cnt.setVisible(True)
        self.pushButton_Back1.setVisible(False)

    def players(self):
        global cnt, dif, words, names, score
        self.label_players_cnt.setVisible(False)
        self.Players_cnt_2.setVisible(False)
        self.Players_cnt_3.setVisible(False)
        self.Players_cnt_4.setVisible(False)
        self.Players_cnt_5.setVisible(False)
        self.Players_cnt_6.setVisible(False)
        self.Players_cnt_7.setVisible(False)
        self.Players_cnt_8.setVisible(False)
        self.Difficulty_easy.setVisible(False)
        self.Difficulty_normal.setVisible(False)
        self.Difficulty_hard.setVisible(False)
        self.Difficulty_hardcore.setVisible(False)
        self.pushButton_accept_cnt.setVisible(False)

        self.pushButton_accept_names = QPushButton('Принять', self)
        self.pushButton_accept_names.resize(self.pushButton_accept_names.sizeHint())
        self.pushButton_accept_names.move(120, 240)
        self.pushButton_accept_names.clicked.connect(self.words_choose)
        self.pushButton_accept_names.setVisible(False)

        if cnt == 0 or dif == 0:
            self.error_label.setVisible(True)
            self.pushButton_Back1.setVisible(True)
        else:
            if dif == 1:
                words = ['царство', 'гранит', 'номер', 'фиалка', 'резинка', 'победа', 'сказка', 'ар', \
                         'тапок', 'лента', 'килт', 'родина', 'стопка', 'козерог', 'университет', 'дно', \
                         'парк', 'фен', 'постер', 'док', 'запой', 'плётка', 'верблюдица', 'специя', 'география', \
                         'шип', 'симптом', 'бижутерия', 'болото', 'журнал', 'лапша', 'многоугольник', 'развод', \
                         'чердак', 'засада', 'освобождение', 'шорты', 'гантель', 'писатель', 'заявка', 'маятник', \
                         'осьминог', 'галоп', 'лепесток', 'экономика', 'шампур', 'земляника', 'заика', 'лентяй', \
                         'экскурсия', 'завтрак', 'акула', 'танец', 'селезень', 'стручок', 'избыток', 'образование', \
                         'жидкость', 'кандалы', 'фильтр', 'электрик', 'очередь', 'лосось', 'декорация', 'зевок',
                         'музыка', \
                         'гроссмейстер', 'достоинство', 'дуга', 'зефир', 'метла', 'выпуск', 'оклад', 'интуиция',
                         'таблица', \
                         'морж', 'камера', 'кочка', 'сосед', 'мотоциклист', 'месть', 'суп', 'центр', 'зола']

            elif dif == 2:
                words = ['напильник', 'авторитет', 'модник', 'чадо', 'психотерапевт', 'оздоровление', 'шатёр', \
                         'реставрация', 'коммерсант', 'абсурд', 'техосмотр', 'бдительность', 'местность', \
                         'удивление', 'поверье', 'акация', 'приклад', 'склонность', 'электорат', 'отступ', \
                         'радиопередача', 'шкет', 'поставщик', 'терновник', 'неугомонность', 'микрон', \
                         'неповиновение', 'женоубийца', 'ректорат', 'выкидыш', 'кровопийца', 'серость', \
                         'стенокардия', 'крысоловка', 'устройство', 'тесть', 'ребус', 'универсам', 'верование', \
                         'переполох', 'беспредел', 'аномалия', 'полемика', 'экскремент', 'свод', 'фаворит', \
                         'объяснение', 'заграждение', 'хряк', 'метрика', 'крепление', 'пируэт', 'экстремист', \
                         'мусульманин', 'предместье', 'пожертвование', 'панорама', 'непристойность', 'хитин', \
                         'неряха', 'чувственность', 'жестикуляция', 'фурнитура', 'освещение', 'стрекотня', \
                         'сверхсрочник', 'рубрикатор', 'правопорядок', 'предосторожность', 'кириллица', \
                         'комбикорм', 'шкатулка', 'пихта', 'заглавие', 'многолетие', 'вирусолог', 'примитивность', \
                         'разъезд', 'чужестранец', 'горнолыжник', 'выродок', 'изъяснение', 'злословие', 'усыпальница']

            elif dif == 3 or dif == 4:
                words = ['подстрочник', 'плеяда', 'адепт', 'выскабливание', 'щегольство', 'деменция', 'босячество', \
                         'будёновец', 'цеховщина', 'юморина', 'перитонит', 'парадигма', 'благодать', 'механизатор', \
                         'можжевельник', 'литургия', 'чалма', 'бестиарий', 'сёгун', 'урбанист', 'редукция', 'мойва', \
                         'корневище', 'фунгицид', 'междуречье', 'словоупотребление', 'железобетон', 'канцелярщина', \
                         'подобострастие', 'мормышка', 'конспирация', 'круча', 'политеизм', 'коврижка', 'брандмауэр', \
                         'алебастр', 'анчар', 'лорнет', 'короста', 'эполет', 'головешка', 'цвергшнауцер', 'геральдика', \
                         'пигалица', 'болотина', 'армяк', 'синеклиза', 'архивист', 'лучина', 'церемониймейстер',
                         'куница', \
                         'хитросплетение', 'оползень', 'эскадра', 'воркотня', 'сюръективность', 'ридикюль', 'вурдалак', \
                         'биополе', 'ротозей', 'вооружённость', 'монетаризм', 'ординар', 'пигмей', 'синереза',
                         'псаломщик', \
                         'альтерация', 'текстолог', 'обыватель', 'эрзац', 'бронетранспортёр', 'саксаул', 'образина', \
                         'мокрица', 'штакетник', 'генералитет', 'хохмач', 'вельможа', 'лейкоз', 'нигилизм',
                         'сколопендра', \
                         'апокриф', 'хохотун', 'волокита']

            names = []

            def set_names(i, s="имя:"):
                global cnt
                if i == cnt:
                    return
                name, okBtnPressed = QInputDialog.getText(self, "Введите имя " + str(i + 1) + " игрока", s)
                if okBtnPressed and not name in names and name != '' and len(name) != name.count(' '):
                    names.append(name)
                    score.append(0)
                    set_names(i + 1)
                else:
                    s = "имя:(введённое ранее имя уже используется другим игроком)"
                    set_names(i, s)

            set_names(0)
            self.pushButton_accept_names.setVisible(True)

    def words_choose(self):
        self.pushButton_accept_names.setVisible(False)

        self.words_common.setVisible(True)
        self.words_dict.setVisible(True)
        self.words_common_and_dict.setVisible(True)

        self.word_choose_label = QLabel(self)
        self.word_choose_label.setVisible(True)
        self.word_choose_label.setText("Выберите запас слов")
        self.word_choose_label.adjustSize()
        self.word_choose_label.move(160 - len("Выберите запас слов") // 2 * 6, 50)

        self.words_dict.clicked.connect(self.words_dict_2)
        self.words_common_and_dict.clicked.connect(self.words_dict_3)

        self.pushButton_accept_words = QPushButton('Принять', self)
        self.pushButton_accept_words.resize(self.pushButton_accept_words.sizeHint())
        self.pushButton_accept_words.move(120, 240)
        self.pushButton_accept_words.clicked.connect(self.run)
        self.pushButton_accept_words.setVisible(True)

    def words_dict_2(self):
        global words, dict, words1
        words1 = dict[:]

    def words_dict_3(self):
        global words, dict, words1
        words1 = dict + words

    def run(self):
        global tries
        global cnt, dif, words, names, words1
        words = words1[:]
        self.pushButton_accept_words.setVisible(False)
        self.words_common.setVisible(False)
        self.words_dict.setVisible(False)
        self.words_common_and_dict.setVisible(False)
        self.word_choose_label.setVisible(False)

        tries = 10
        if dif == 2:
            tries = 7
        elif dif == 3:
            tries = 5
        elif dif == 4:
            tries = 3

        self.turn_label = QLabel(self)
        self.turn_label.setVisible(True)
        self.turn_label.setText(names[0] + " объясняет " + names[1])
        self.turn_label.adjustSize()
        self.turn_label.move(160 - len(names[0] + " объясняет " + names[1]) // 2 * 6, 50)

        self.pushButton_success = QPushButton('Угадано', self)
        self.pushButton_success.resize(self.pushButton_success.sizeHint())
        self.pushButton_success.move(45, 220)
        self.pushButton_success.clicked.connect(self.run_success)
        self.pushButton_success.setVisible(True)

        self.pushButton_error = QPushButton('Ошибка', self)
        self.pushButton_error.resize(self.pushButton_error.sizeHint())
        self.pushButton_error.move(120, 220)
        self.pushButton_error.clicked.connect(self.run_error)
        self.pushButton_error.setVisible(True)

        self.word_label = QLabel(self)
        self.word_label.setVisible(True)
        self.word_label.setText("Нажмите \"Угадано\", чтобы начать")
        self.word_label.adjustSize()
        self.word_label.move(60, 100)

        self.tries_label = QLabel(self)
        self.tries_label.setVisible(True)
        self.tries_label.setText("Осталось " + str(tries) + " попыток")
        self.tries_label.adjustSize()
        self.tries_label.move(160 - len("Осталось " + str(tries) + " попыток") // 2 * 6, 150)

        self.pushButton_main_menu = QPushButton('Меню', self)
        self.pushButton_main_menu.resize(self.pushButton_main_menu.sizeHint())
        self.pushButton_main_menu.move(195, 220)
        self.pushButton_main_menu.clicked.connect(self.main_menu)
        self.pushButton_main_menu.setVisible(True)

    def run_success(self):
        global tries, words, score, t, k
        if self.word_label.text() != "Нажмите \"Угадано\", чтобы начать":
            score[t] += 1
            score[(t + k) % cnt] += 1
        if dif == 2:
            tries = min(7, tries + 3)
        elif dif == 3:
            tries = min(5, tries + 2)
        elif dif == 4:
            tries = min(3, tries + 1)
        else:
            tries = min(10, tries + 5)
        self.tries_label.setText("Осталось " + str(tries) + " попыток")
        self.tries_label.adjustSize()
        self.tries_label.move(160 - len("Осталось " + str(tries) + " попыток") // 2 * 6, 150)
        if len(words) > 0:
            word_current = words[random.randint(0, len(words) - 1)]
            self.word_label.setText(word_current)
            self.word_label.move(160 - len(word_current) // 2 * 6, 100)
            del (words[words.index(word_current)])
        else:
            self.turn_label.setVisible(False)
            self.pushButton_success.setVisible(False)
            self.pushButton_error.setVisible(False)
            self.pushButton_main_menu.setVisible(False)
            self.word_label.setVisible(False)
            self.tries_label.setVisible(False)

            self.pushButton_score = QPushButton('Счёт', self)
            self.pushButton_score.resize(self.pushButton_score.sizeHint())
            self.pushButton_score.move(140, 160)
            self.pushButton_score.clicked.connect(self.score_show)
            self.pushButton_score.setVisible(True)

    def run_error(self):
        global tries, t, k, cnt, words
        if self.word_label.text() != "Нажмите \"Угадано\", чтобы начать":
            tries -= 1
            self.tries_label.setText("Осталось " + str(tries) + " попыток")
            self.tries_label.adjustSize()
            self.tries_label.move(160 - len("Осталось " + str(tries) + " попыток") // 2 * 6, 150)
            if tries == 0:
                self.pushButton_success.setVisible(False)
                self.pushButton_error.setVisible(False)
                self.pushButton_main_menu.setVisible(False)
                self.word_label.setVisible(False)
                words.append(self.word_label.text())
                word_current = words[random.randint(0, len(words) - 1)]
                self.word_label.setText(word_current)
                self.word_label.move(160 - len(word_current) // 2 * 6, 100)
                del (words[words.index(word_current)])

                t = (t + 1) % cnt
                if t == 0:
                    k = (k + 1) % cnt

                if k == 0:
                    k = 1

                self.turn_label.setText(names[t] + " объясняет " + names[(t + k) % cnt])
                self.turn_label.adjustSize()
                self.turn_label.move(160 - len(names[0] + " объясняет " + names[1]) // 2 * 6, 50)

                self.pushButton_continue = QPushButton('Следующая пара игроков', self)
                self.pushButton_continue.resize(self.pushButton_continue.sizeHint())
                self.pushButton_continue.move(90, 220)
                self.pushButton_continue.clicked.connect(self.continue_game)
                self.pushButton_continue.setVisible(True)

    def continue_game(self):
        global dif, tries

        self.pushButton_success.setVisible(True)
        self.pushButton_error.setVisible(True)
        self.pushButton_main_menu.setVisible(True)
        self.word_label.setVisible(True)
        self.pushButton_continue.setVisible(False)

        tries = 10
        if dif == 2:
            tries = 7
        elif dif == 3:
            tries = 5
        elif dif == 4:
            tries = 3

        self.tries_label.setText("Осталось " + str(tries) + " попыток")
        self.tries_label.adjustSize()

        self.tries_label.move(160 - len("Осталось " + str(tries) + " попыток") // 2 * 6, 150)

    def score_show(self):
        global score, names, cnt
        self.pushButton_score.setVisible(False)

        self.score_player_1 = QLabel(self)
        self.score_player_1.setText(names[0] + '     ' + str(score[0]))
        self.score_player_1.adjustSize()
        self.score_player_1.move(20, 36)
        self.score_player_1.setVisible(True)

        self.score_player_2 = QLabel(self)
        self.score_player_2.setText(names[1] + '     ' + str(score[1]))
        self.score_player_2.adjustSize()
        self.score_player_2.move(20, 36 * 2)
        self.score_player_2.setVisible(True)

        if cnt > 2:
            self.score_player_3 = QLabel(self)
            self.score_player_3.setText(names[2] + '     ' + str(score[2]))
            self.score_player_3.adjustSize()
            self.score_player_3.move(20, 36 * 3)
            self.score_player_3.setVisible(True)

        if cnt > 3:
            self.score_player_4 = QLabel(self)
            self.score_player_4.setText(names[3] + '     ' + str(score[3]))
            self.score_player_4.adjustSize()
            self.score_player_4.move(20, 36 * 4)
            self.score_player_4.setVisible(True)

        if cnt > 4:
            self.score_player_5 = QLabel(self)
            self.score_player_5.setText(names[4] + '     ' + str(score[4]))
            self.score_player_5.adjustSize()
            self.score_player_5.move(20, 36 * 5)
            self.score_player_5.setVisible(True)

        if cnt > 5:
            self.score_player_6 = QLabel(self)
            self.score_player_6.setText(names[5] + '     ' + str(score[5]))
            self.score_player_6.adjustSize()
            self.score_player_6.move(20, 36 * 6)
            self.score_player_6.setVisible(True)

        if cnt > 6:
            self.score_player_7 = QLabel(self)
            self.score_player_7.setText(names[6] + '     ' + str(score[6]))
            self.score_player_7.adjustSize()
            self.score_player_7.move(20, 36 * 7)
            self.score_player_7.setVisible(True)

        if cnt > 7:
            self.score_player_8 = QLabel(self)
            self.score_player_8.setText(names[7] + '     ' + str(score[7]))
            self.score_player_8.adjustSize()
            self.score_player_8.move(20, 36 * 8)
            self.score_player_8.setVisible(True)

        self.pushButton_main_menu_1 = QPushButton('Меню', self)
        self.pushButton_main_menu_1.resize(self.pushButton_main_menu_1.sizeHint())
        self.pushButton_main_menu_1.move(195, 220)
        self.pushButton_main_menu_1.clicked.connect(self.main_menu_1)
        self.pushButton_main_menu_1.setVisible(True)

    def main_menu(self):
        global names, cnt, dif, words, k, score, t
        self.turn_label.setVisible(False)
        self.pushButton_success.setVisible(False)
        self.pushButton_error.setVisible(False)
        self.pushButton_main_menu.setVisible(False)
        self.word_label.setVisible(False)
        self.tries_label.setVisible(False)

        self.pushButton_Play.setVisible(True)
        self.pushButton_Guide.setVisible(True)
        self.pushButton_Exit.setVisible(True)
        self.pushButton_Dictionary.setVisible(True)

        words1 = []
        names = []
        cnt = 0
        dif = 0
        words = []
        score = []
        k = 1
        t = 0

    def main_menu_1(self):
        global names, cnt, dif, words, k, score, t
        self.pushButton_error.setVisible(False)
        self.pushButton_main_menu_1.setVisible(False)

        self.score_player_1.setVisible(False)
        self.score_player_2.setVisible(False)
        if cnt > 2:
            self.score_player_3.setVisible(False)
        if cnt > 3:
            self.score_player_4.setVisible(False)
        if cnt > 4:
            self.score_player_5.setVisible(False)
        if cnt > 5:
            self.score_player_6.setVisible(False)
        if cnt > 6:
            self.score_player_7.setVisible(False)
        if cnt > 7:
            self.score_player_8.setVisible(False)

        self.pushButton_Play.setVisible(True)
        self.pushButton_Guide.setVisible(True)
        self.pushButton_Exit.setVisible(True)
        self.pushButton_Dictionary.setVisible(True)

        words1 = []
        names = []
        cnt = 0
        dif = 0
        words = []
        score = []
        k = 1
        t = 0

    def guide(self):
        self.pushButton_Play.setVisible(False)
        self.pushButton_Guide.setVisible(False)
        self.pushButton_Exit.setVisible(False)
        self.pushButton_Dictionary.setVisible(False)

        self.guide_label.setVisible(True)
        self.pushButton_Back.setVisible(True)

        self.pushButton_Back.clicked.connect(self.menu)

    def menu(self):
        self.pushButton_Play.setVisible(True)
        self.pushButton_Guide.setVisible(True)
        self.pushButton_Exit.setVisible(True)
        self.pushButton_Dictionary.setVisible(True)

        self.guide_label.setVisible(False)
        self.pushButton_Back.setVisible(False)

    def out(self):
        exit()


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())
