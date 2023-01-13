import sys

import PyQt5.Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


EXCHANGE = 7.53450  # Exchange rate for EUR to HRK

# available coins and bills
change = [0.01, 0.02, 0.05, 0.10, 0.20, 0.50, 1.00, 2.00, 5.00, 10.00, 20.00, 50.00, 100.00, 200.00]


def nearest_smaller_value2(total_amnt, lst):
    """
    finds nearest smaller value in a list
    """
    closest = None
    for i in lst:
        if (i <= total_amnt) and (closest is None or i > closest):
            closest = i
    return closest


def count_coins(lst):
    for coin in change:
        count = lst.count(coin)
        if count > 0:
            cent = eval(f"cent_{int(coin*100)}")
            image_object = eval(f"image_object{int(coin*100)}")
            cent.setText(f"{count}")
            image_object.show()
            cent.show()
        else:
            cent = eval(f"cent_{int(coin*100)}")
            image_object = eval(f"image_object{int(coin*100)}")
            image_object.hide()
            cent.hide()


def frame_sentence():
    try:
        to_give_back = []

        price = euro_input.text()  # Saves input to variable from eur_input
        hrk = hrk_input.text()  # Saves input to variable from hrk_input

        # Calculates the amount that need to be returned
        give_back = round((round(float(hrk) / EXCHANGE, 2) - float(price)), 2)
        # Send output of give_back
        displ_total_eur.setText(f"{give_back}")
        while give_back != 0:  # until there is nothing left to return
            coins_and_bills = nearest_smaller_value2(give_back, change)
            to_give_back.append(coins_and_bills)  # adds coins that need to be returned
            give_back = give_back - float(coins_and_bills)
            give_back = round(give_back, 2)
        list_of_coins.setText(f"{to_give_back}")
        count_coins(to_give_back)  # uses count_coins function to hide and show images and sets needed count for each
    except TypeError:
        hrk_input.setText("Low amount")

# All canvases, images, label and positions needed for the app are below


app = QApplication(sys.argv)
window = QWidget()
window.setGeometry(200, 200, 1000, 800)
window.setWindowTitle("When given HRK")
window.setStyleSheet("background-color: #0f4b6e;")

canvas = QLabel(window)
canvas.setStyleSheet("background-color: #0f4b6e; border: 0;")
canvas.setGeometry(0, 0, 1920, 1080)  # original value 700, 120

canvas = QLabel(window)
canvas.setStyleSheet("background-color: #0f4b6e; border: 0;")
canvas.setGeometry(0, 0, 1920, 1080)  # original value 700, 120


image1 = QPixmap('1CENT.png')
image_object1 = QLabel(canvas)
image_object1.setPixmap(image1)
image_object1.setGeometry(1, 130, 88, 89)

image2 = QPixmap('2CENT.png')
image_object2 = QLabel(canvas)
image_object2.setPixmap(image2)
image_object2.setGeometry(95, 130, 100, 101)

image5 = QPixmap('5CENT.png')
image_object5 = QLabel(canvas)
image_object5.setPixmap(image5)
image_object5.setGeometry(200, 130, 113, 112)

image10 = QPixmap('10CENT.png')
image_object10 = QLabel(canvas)
image_object10.setPixmap(image10)
image_object10.setGeometry(320, 130, 107, 105)

image20 = QPixmap('20CENT.png')
image_object20 = QLabel(canvas)
image_object20.setPixmap(image20)
image_object20.setGeometry(435, 130, 119, 117)

image50 = QPixmap('50CENT.png')
image_object50 = QLabel(canvas)
image_object50.setPixmap(image50)
image_object50.setGeometry(560, 130, 130, 128)

image100 = QPixmap('1EURO.png')
image_object100 = QLabel(canvas)
image_object100.setPixmap(image100)
image_object100.setGeometry(695, 130, 124, 124)

image200 = QPixmap('2EURO.png')
image_object200 = QLabel(canvas)
image_object200.setPixmap(image200)
image_object200.setGeometry(825, 130, 136, 136)

image500 = QPixmap('5EURO.png')
image_object500 = QLabel(canvas)
image_object500.setPixmap(image500)
image_object500.setGeometry(1, 330, 160, 77)

image1000 = QPixmap('10EURO.png')
image_object1000 = QLabel(canvas)
image_object1000.setPixmap(image1000)
image_object1000.setGeometry(170, 330, 160, 85)

image2000 = QPixmap('20EURO.png')
image_object2000 = QLabel(canvas)
image_object2000.setPixmap(image2000)
image_object2000.setGeometry(340, 330, 180, 96)

image5000 = QPixmap('50EURO.png')
image_object5000 = QLabel(canvas)
image_object5000.setPixmap(image5000)
image_object5000.setGeometry(530, 330, 192, 101)

image10000 = QPixmap('100EURO.png')
image_object10000 = QLabel(canvas)
image_object10000.setPixmap(image10000)
image_object10000.setGeometry(730, 330, 192, 103)

image20000 = QPixmap('200EURO.png')
image_object20000 = QLabel(canvas)
image_object20000.setPixmap(image20000)
image_object20000.setGeometry(1, 520, 208, 109)


cent_1 = QLineEdit(window)
cent_1.setAlignment(PyQt5.Qt.Qt.AlignCenter)
cent_1.setReadOnly(True)
cent_1.move(25, 280)
cent_1.resize(50, 30)
cent_1.setStyleSheet("background-color: #0f4b6e; color: white; border: 1px solid transparent;")

cent_2 = QLineEdit(window)
cent_2.setAlignment(PyQt5.Qt.Qt.AlignCenter)
cent_2.setReadOnly(True)
cent_2.move(125, 280)
cent_2.resize(50, 30)
cent_2.setStyleSheet("background-color: #0f4b6e; color: white; border: 1px solid transparent;")

cent_5 = QLineEdit(window)
cent_5.setAlignment(PyQt5.Qt.Qt.AlignCenter)
cent_5.setReadOnly(True)
cent_5.move(225, 280)
cent_5.resize(50, 30)
cent_5.setStyleSheet("background-color: #0f4b6e; color: white; border: 1px solid transparent;")

cent_10 = QLineEdit(window)
cent_10.setAlignment(PyQt5.Qt.Qt.AlignCenter)
cent_10.setReadOnly(True)
cent_10.move(345, 280)
cent_10.resize(50, 30)
cent_10.setStyleSheet("background-color: #0f4b6e; color: white; border: 1px solid transparent;")

cent_20 = QLineEdit(window)
cent_20.setAlignment(PyQt5.Qt.Qt.AlignCenter)
cent_20.setReadOnly(True)
cent_20.move(470, 280)
cent_20.resize(50, 30)
cent_20.setStyleSheet("background-color: #0f4b6e; color: white; border: 1px solid transparent;")

cent_50 = QLineEdit(window)
cent_50.setAlignment(PyQt5.Qt.Qt.AlignCenter)
cent_50.setReadOnly(True)
cent_50.move(600, 280)
cent_50.resize(50, 30)
cent_50.setStyleSheet("background-color: #0f4b6e; color: white; border: 1px solid transparent;")

cent_100 = QLineEdit(window)
cent_100.setAlignment(PyQt5.Qt.Qt.AlignCenter)
cent_100.setReadOnly(True)
cent_100.move(730, 280)
cent_100.resize(50, 30)
cent_100.setStyleSheet("background-color: #0f4b6e; color: white; border: 1px solid transparent;")

cent_200 = QLineEdit(window)
cent_200.setAlignment(PyQt5.Qt.Qt.AlignCenter)
cent_200.setReadOnly(True)
cent_200.move(865, 280)
cent_200.resize(50, 30)
cent_200.setStyleSheet("background-color: #0f4b6e; color: white; border: 1px solid transparent;")

cent_500 = QLineEdit(window)
cent_500.setAlignment(PyQt5.Qt.Qt.AlignCenter)
cent_500.setReadOnly(True)
cent_500.move(65, 450)
cent_500.resize(50, 30)
cent_500.setStyleSheet("background-color: #0f4b6e; color: white; border: 1px solid transparent;")

cent_1000 = QLineEdit(window)
cent_1000.setAlignment(PyQt5.Qt.Qt.AlignCenter)
cent_1000.setReadOnly(True)
cent_1000.move(225, 450)
cent_1000.resize(50, 30)
cent_1000.setStyleSheet("background-color: #0f4b6e; color: white; border: 1px solid transparent;")

cent_2000 = QLineEdit(window)
cent_2000.setAlignment(PyQt5.Qt.Qt.AlignCenter)
cent_2000.setReadOnly(True)
cent_2000.move(400, 450)
cent_2000.resize(50, 30)
cent_2000.setStyleSheet("background-color: #0f4b6e; color: white; border: 1px solid transparent;")

cent_5000 = QLineEdit(window)
cent_5000.setAlignment(PyQt5.Qt.Qt.AlignCenter)
cent_5000.setReadOnly(True)
cent_5000.move(600, 450)
cent_5000.resize(50, 30)
cent_5000.setStyleSheet("background-color: #0f4b6e; color: white; border: 1px solid transparent;")


cent_10000 = QLineEdit(window)
cent_10000.setAlignment(PyQt5.Qt.Qt.AlignCenter)
cent_10000.setReadOnly(True)
cent_10000.move(800, 450)
cent_10000.resize(50, 30)
cent_10000.setStyleSheet("background-color: #0f4b6e; color: white; border: 1px solid transparent;")

cent_20000 = QLineEdit(window)
cent_20000.setAlignment(PyQt5.Qt.Qt.AlignCenter)
cent_20000.setReadOnly(True)
cent_20000.move(65, 650)
cent_20000.resize(50, 30)
cent_20000.setStyleSheet("background-color: #0f4b6e; color: white; border: 1px solid transparent;")


displ_total_eur = QLineEdit(window)
displ_total_eur.setReadOnly(True)
displ_total_eur.move(490, 5)
displ_total_eur.resize(100, 30)
displ_total_eur.setStyleSheet("background-color: #0f4b6e; color: white; border: 1px solid transparent;")

list_of_coins = QLineEdit(window)
list_of_coins.setReadOnly(True)
list_of_coins.move(490, 45)
list_of_coins.resize(250, 30)
list_of_coins.setStyleSheet("background-color: #0f4b6e; color: white; border: 1px solid transparent;")

label_1 = QLabel(window)
label_1.setText("What is the cost?")
label_1.move(5, 15)
label_1.setStyleSheet("background-color: #0f4b6e; color: white;")

label_2 = QLabel(window)
label_2.setText("How much HRK did you get?")
label_2.move(5, 55)
label_2.setStyleSheet("background-color: #0f4b6e; color: white;")

label_3 = QLabel(window)
label_3.setText("EUR")
label_3.move(210, 15)
label_3.setStyleSheet("background-color: #0f4b6e; color: white;")

label_4 = QLabel(window)
label_4.setText("HRK")
label_4.move(255, 55)
label_4.setStyleSheet("background-color: #0f4b6e; color: white;")

label_5 = QLabel(window)
label_5.setText("Total to give back (in EUR)->")
label_5.move(350, 15)
label_5.setStyleSheet("background-color: #0f4b6e; color: white;")

label_6 = QLabel(window)
label_6.setText("List of coins and bills (in EUR)->")
label_6.move(338, 55)
label_6.setStyleSheet("background-color: #0f4b6e; color: white;")

euro_input = QLineEdit(window)  # EUR input
euro_input.setFocus()  # This makes it, so it's first thing available for input when program opens
euro_input.move(100, 5)
euro_input.resize(100, 30)
euro_input.setStyleSheet("background-color: #0f4b6e; color: white; border: 1px solid white;")

hrk_input = QLineEdit(window)  # HRK input
hrk_input.move(150, 45)
hrk_input.resize(100, 30)
hrk_input.setStyleSheet("background-color: #0f4b6e; color: white; border: 1px solid white;")

button = QPushButton("Calculate", window)
button.move(5, 85)
button.resize(100, 30)
button.setStyleSheet("background-color: yellow; color: blue;")
button.clicked.connect(frame_sentence)

window.show()
sys.exit(app.exec_())
