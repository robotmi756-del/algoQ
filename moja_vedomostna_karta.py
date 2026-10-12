#vytvor program vedomostných kariet
#pripoj knižnice
#pripoj knižnice
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget,  QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QMessageBox, QRadioButton,QGroupBox,QButtonGroup

class Question:
    def __init__(self, question, right_ans, wrong1, wrong2, wrong3):
        self.question = question
        self.right_ans = right_ans
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

question_list = []
question_list.append(Question(""))
question_list.append(Question(""))
question_list.append(Question(""))
app = QApplication([])





app = QApplication([])

window = QWidget()
window.setWindowTitle("Vedemostna karta")
window.move(100, 100)
window.resize(400, 200)


otazka = QLabel("Kotra z narodnosti neexistuje?")
button = QPushButton("Vyhodnotit")


RadioGroupBox = QGroupBox("Odpovede")
btn_answer1 = QRadioButton("Slovenska")
btn_answer2 = QRadioButton("Ceskoslovenska")
btn_answer3 = QRadioButton("Ceska")
btn_answer4 = QRadioButton("Madarska")


btn_group = QButtonGroup()
btn_group.addButton(btn_answer1)
btn_group.addButton(btn_answer2)
btn_group.addButton(btn_answer3)
btn_group.addButton(btn_answer4)

layout_answer = QHBoxLayout()
layout_answerV1 = QVBoxLayout()
layout_answerV2 = QVBoxLayout()


layout_answerV1.addWidget(btn_answer1)
layout_answerV1.addWidget(btn_answer2)

layout_answerV2.addWidget(btn_answer3)
layout_answerV2.addWidget(btn_answer4)


layout_answer.addLayout(layout_answerV1)
layout_answer.addLayout(layout_answerV2)

RadioGroupBox.setLayout(layout_answer)


#okno s vysledkami

AnswerGroupBox = QGroupBox("Vysdledky")
vysledok = QLabel("Spravne/Nespravne")
spravna_odpoved = QLabel("spravna odpoved")

layout_vysledok = QVBoxLayout()

layout_vysledok.addWidget(vysledok, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_vysledok.addWidget(spravna_odpoved, alignment=Qt.AlignCenter, stretch=2)

AnswerGroupBox.setLayout(layout_vysledok)

layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()


layout_line1.addWidget(otazka, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))

layout_line2.addWidget(RadioGroupBox)
layout_line2.addWidget(AnswerGroupBox)
AnswerGroupBox.hide()

layout_line3.addStretch(1)
layout_line3.addWidget(button, stretch=2)
layout_line3.addStretch(1)

layout_main = QVBoxLayout()

layout_main.addLayout(layout_line1, stretch=2)
layout_main.addLayout(layout_line2, stretch=8)
layout_main.addStretch(1)
layout_main.addLayout(layout_line3, stretch=1)
layout_main.addStretch(1)
layout_main.setSpacing(5)

def show_result():
    RadioGroupBox.hide()
    AnswerGroupBox.show()
    button.setText("Dialsia Otazka")

def show_question():
    RadioGroupBox.show()
    AnswerGroupBox.hide()
    button.setText("Vyhodnotit")


btn_group.setExclusive(False)
btn_answer1.setChecked(False)
btn_answer2.setChecked(False)
btn_answer3.setChecked(False)
btn_answer4.setChecked(False)
btn_group.setExclusive(True)


def test():
    if "vyhodnotit" == button.text():
        show_result()
    else:
        show_question()

button.clicked.connect(test)



window.setLayout(layout_main)
window.show()
app.exec()

















