import sys
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Dashboard(QMainWindow):
    def __init__(self, ponds=None):
        super().__init__()
        self.ponds = ponds
        self.__init_ui()

    def __init_ui(self):
        self.setFixedSize(1440, 900)
        self.setStyleSheet('background-color: white;')
        self.setWindowTitle('Dashboard')

        # Font
        FONT_BOLD_24 = QFont('Poppins')
        FONT_BOLD_24.setPixelSize(24)
        FONT_BOLD_24.setBold(True)

        FONT_REG_14 = QFont('Poppins')
        FONT_REG_14.setPixelSize(14)

        self.stackedWidget = QStackedWidget(self)
        self.stackedWidget.setGeometry(QRect(30, 30, 1381, 841))

        self.doo_pond_dashboard = DooPondDashboard(
            self, FONT_BOLD_24, FONT_REG_14)
        self.stackedWidget.addWidget(self.doo_pond_dashboard)

        self.show()


class DooPondDashboard(QWidget):
    def __init__(self, parent: QWidget = None, FONT_BOLD_24=None, FONT_REG_14=None):
        QWidget.__init__(self, parent)

        self.current_population = CurrentPopulation(
            self, FONT_BOLD_24, FONT_REG_14)
        self.current_population.setGeometry(QRect(0, 60, 201, 111))

        self.dead_fishes = DeadFishes(self, FONT_BOLD_24, FONT_REG_14)
        self.dead_fishes.setGeometry(QRect(230, 60, 201, 111))

        self.male_fishes = MaleFishes(self, FONT_BOLD_24, FONT_REG_14)
        self.male_fishes.setGeometry(QRect(460, 60, 201, 111))

        self.female_fishes = FemaleFishes(self, FONT_BOLD_24, FONT_REG_14)
        self.female_fishes.setGeometry(QRect(690, 60, 201, 111))

        self.population_trend = PopulationTrend(
            self, FONT_BOLD_24, FONT_REG_14)
        self.population_trend.setGeometry(QRect(0, 200, 891, 361))

        self.genesis = Genesis(self, FONT_BOLD_24, FONT_REG_14)
        self.genesis.setGeometry(QRect(0, 590, 431, 251))

        self.move_stress = MoveStress(self, FONT_BOLD_24, FONT_REG_14)
        self.move_stress.setGeometry(QRect(460, 590, 201, 111))

        self.move_instinct = MoveInstinct(self, FONT_BOLD_24, FONT_REG_14)
        self.move_instinct.setGeometry(QRect(690, 590, 201, 111))

        self.death_god = DeathGod(self, FONT_BOLD_24, FONT_REG_14)
        self.death_god.setGeometry(QRect(460, 730, 201, 111))

        self.death_disaster = DeathDisaster(self, FONT_BOLD_24, FONT_REG_14)
        self.death_disaster.setGeometry(QRect(690, 730, 201, 111))


class CurrentPopulation(QFrame):
    def __init__(self, parent: QFrame = None, FONT_BOLD_24=None, FONT_REG_14=None):
        QFrame.__init__(self, parent)

        self.setStyleSheet(
            "background-color: #FFF7F0; border-radius:10;")
        self.setObjectName("current_population")

        self.curr_pop_title = QLabel("Current Population", self)
        self.curr_pop_title.setObjectName("curr_pop_title")
        self.curr_pop_title.setGeometry(QRect(30, 30, 141, 20))
        self.curr_pop_title.setFont(FONT_REG_14)
        self.curr_pop_title.setStyleSheet("color: black;")
        self.curr_pop_title.setAlignment(Qt.AlignLeft)

        self.curr_pop_number = QLabel("0", self)
        self.curr_pop_number.setObjectName("curr_pop_number")
        self.curr_pop_number.setGeometry(QRect(30, 60, 91, 31))
        self.curr_pop_number.setFont(FONT_BOLD_24)
        self.curr_pop_number.setStyleSheet("color: black;")
        self.curr_pop_number.setAlignment(Qt.AlignLeft)

        self.curr_pop_rate = QLabel("0", self)
        self.curr_pop_rate.setObjectName("curr_pop_rate")
        self.curr_pop_rate.setGeometry(QRect(130, 67, 41, 16))
        self.curr_pop_rate.setFont(FONT_REG_14)
        self.curr_pop_rate.setStyleSheet("color: black;")
        self.curr_pop_rate.setAlignment(Qt.AlignRight)


class DeadFishes(QFrame):
    def __init__(self, parent: QFrame, FONT_BOLD_24=None, FONT_REG_14=None) -> None:
        QFrame.__init__(self, parent)

        self.setStyleSheet(
            "background-color: #EEF1FF; border-radius:10;")
        self.setObjectName("dead_fishes")

        self.dead_fishes_title = QLabel("Dead Fishes", self)
        self.dead_fishes_title.setObjectName("dead_fishes_title")
        self.dead_fishes_title.setGeometry(QRect(30, 30, 141, 20))
        self.dead_fishes_title.setFont(FONT_REG_14)
        self.dead_fishes_title.setStyleSheet("color: black;")
        self.dead_fishes_title.setAlignment(Qt.AlignLeft)

        self.dead_fishes_number = QLabel("0", self)
        self.dead_fishes_number.setObjectName("dead_fishes_number")
        self.dead_fishes_number.setGeometry(QRect(30, 60, 91, 31))
        self.dead_fishes_number.setFont(FONT_BOLD_24)
        self.dead_fishes_number.setStyleSheet("color: black;")
        self.dead_fishes_number.setAlignment(Qt.AlignLeft)

        self.dead_fishes_rate = QLabel("0", self)
        self.dead_fishes_rate.setObjectName("dead_fishes_rate")
        self.dead_fishes_rate.setGeometry(QRect(130, 67, 41, 16))
        self.dead_fishes_rate.setFont(FONT_REG_14)
        self.dead_fishes_rate.setStyleSheet("color: black;")
        self.dead_fishes_rate.setAlignment(Qt.AlignRight)


class MaleFishes(QFrame):
    def __init__(self, parent: QFrame, FONT_BOLD_24=None, FONT_REG_14=None) -> None:
        QFrame.__init__(self, parent)

        self.setStyleSheet(
            "background-color: #F0FAFF; border-radius:10;")
        self.setObjectName("male_fishes")

        self.male_fishes_title = QLabel("Male Fishes", self)
        self.male_fishes_title.setObjectName("male_fishes_title")
        self.male_fishes_title.setGeometry(QRect(30, 30, 141, 20))
        self.male_fishes_title.setFont(FONT_REG_14)
        self.male_fishes_title.setStyleSheet("color: black;")
        self.male_fishes_title.setAlignment(Qt.AlignLeft)

        self.male_fishes_number = QLabel("0", self)
        self.male_fishes_number.setObjectName("male_fishes_number")
        self.male_fishes_number.setGeometry(QRect(30, 60, 91, 31))
        self.male_fishes_number.setFont(FONT_BOLD_24)
        self.male_fishes_number.setStyleSheet("color: black;")
        self.male_fishes_number.setAlignment(Qt.AlignLeft)

        self.male_fishes_rate = QLabel("0", self)
        self.male_fishes_rate.setObjectName("male_fishes_rate")
        self.male_fishes_rate.setGeometry(QRect(130, 67, 41, 16))
        self.male_fishes_rate.setFont(FONT_REG_14)
        self.male_fishes_rate.setStyleSheet("color: black;")
        self.male_fishes_rate.setAlignment(Qt.AlignRight)


class FemaleFishes(QFrame):
    def __init__(self, parent: QFrame, FONT_BOLD_24=None, FONT_REG_14=None) -> None:
        QFrame.__init__(self, parent)

        self.setStyleSheet(
            "background-color: #FFF7F0; border-radius:10;")
        self.setObjectName("female_fishes")

        self.female_fishes_title = QLabel("Female Fishes", self)
        self.female_fishes_title.setObjectName("female_fishes_title")
        self.female_fishes_title.setGeometry(QRect(30, 30, 141, 20))
        self.female_fishes_title.setFont(FONT_REG_14)
        self.female_fishes_title.setStyleSheet("color: black;")
        self.female_fishes_title.setAlignment(Qt.AlignLeft)

        self.female_fishes_number = QLabel("0", self)
        self.female_fishes_number.setObjectName("female_fishes_number")
        self.female_fishes_number.setGeometry(QRect(30, 60, 91, 31))
        self.female_fishes_number.setFont(FONT_BOLD_24)
        self.female_fishes_number.setStyleSheet("color: black;")
        self.female_fishes_number.setAlignment(Qt.AlignLeft)

        self.female_fishes_rate = QLabel("0", self)
        self.female_fishes_rate.setObjectName("female_fishes_rate")
        self.female_fishes_rate.setGeometry(QRect(130, 67, 41, 16))
        self.female_fishes_rate.setFont(FONT_REG_14)
        self.female_fishes_rate.setStyleSheet("color: black;")
        self.female_fishes_rate.setAlignment(Qt.AlignRight)


class PopulationTrend(QFrame):
    def __init__(self, parent: QFrame, FONT_BOLD_24=None, FONT_REG_14=None) -> None:
        QFrame.__init__(self, parent)

        self.setStyleSheet(
            "border:2px solid; border-color: #F7F9FB; border-radius:10;")
        self.setObjectName("population_trend")


class Genesis(QFrame):
    def __init__(self, parent: QFrame, FONT_BOLD_24=None, FONT_REG_14=None) -> None:
        QFrame.__init__(self, parent)

        self.setStyleSheet(
            "border:2px solid; border-color: #F7F9FB; border-radius:10;")
        self.setObjectName("genesis")


class MoveStress(QFrame):
    def __init__(self, parent: QFrame, FONT_BOLD_24=None, FONT_REG_14=None) -> None:
        QFrame.__init__(self, parent)

        self.setStyleSheet(
            "background-color: #FFF7F0; border-radius:10;")
        self.setObjectName("move_stress")

        self.move_stress_title = QLabel("Move Stress", self)
        self.move_stress_title.setObjectName("move_stress_title")
        self.move_stress_title.setGeometry(QRect(30, 30, 141, 20))
        self.move_stress_title.setFont(FONT_REG_14)
        self.move_stress_title.setStyleSheet("color: black;")
        self.move_stress_title.setAlignment(Qt.AlignLeft)

        self.move_stress_number = QLabel("0", self)
        self.move_stress_number.setObjectName("move_stress_number")
        self.move_stress_number.setGeometry(QRect(30, 60, 91, 31))
        self.move_stress_number.setFont(FONT_BOLD_24)
        self.move_stress_number.setStyleSheet("color: black;")
        self.move_stress_number.setAlignment(Qt.AlignLeft)

        self.move_stress_rate = QLabel("0", self)
        self.move_stress_rate.setObjectName("move_stress_rate")
        self.move_stress_rate.setGeometry(QRect(130, 67, 41, 16))
        self.move_stress_rate.setFont(FONT_REG_14)
        self.move_stress_rate.setStyleSheet("color: black;")
        self.move_stress_rate.setAlignment(Qt.AlignRight)


class MoveInstinct(QFrame):
    def __init__(self, parent: QFrame, FONT_BOLD_24=None, FONT_REG_14=None) -> None:
        QFrame.__init__(self, parent)

        self.setStyleSheet(
            "background-color: #EEF1FF; border-radius:10;")
        self.setObjectName("move_instinct")

        self.move_instinct_title = QLabel("Move Instinct", self)
        self.move_instinct_title.setObjectName("move_instinct_title")
        self.move_instinct_title.setGeometry(QRect(30, 30, 141, 20))
        self.move_instinct_title.setFont(FONT_REG_14)
        self.move_instinct_title.setStyleSheet("color: black;")
        self.move_instinct_title.setAlignment(Qt.AlignLeft)

        self.move_instinct_number = QLabel("0", self)
        self.move_instinct_number.setObjectName("move_instinct_number")
        self.move_instinct_number.setGeometry(QRect(30, 60, 91, 31))
        self.move_instinct_number.setFont(FONT_BOLD_24)
        self.move_instinct_number.setStyleSheet("color: black;")
        self.move_instinct_number.setAlignment(Qt.AlignLeft)

        self.move_instinct_rate = QLabel("0", self)
        self.move_instinct_rate.setObjectName("move_instinct_rate")
        self.move_instinct_rate.setGeometry(QRect(130, 67, 41, 16))
        self.move_instinct_rate.setFont(FONT_REG_14)
        self.move_instinct_rate.setStyleSheet("color: black;")
        self.move_instinct_rate.setAlignment(Qt.AlignRight)


class DeathGod(QFrame):
    def __init__(self, parent: QFrame, FONT_BOLD_24=None, FONT_REG_14=None) -> None:
        QFrame.__init__(self, parent)

        self.setStyleSheet(
            "background-color: #F0FAFF; border-radius:10;")
        self.setObjectName("death_god")

        self.death_god_title = QLabel("Death God", self)
        self.death_god_title.setObjectName("death_god_title")
        self.death_god_title.setGeometry(QRect(30, 30, 141, 20))
        self.death_god_title.setFont(FONT_REG_14)
        self.death_god_title.setStyleSheet("color: black;")

        self.death_god_number = QLabel("0", self)
        self.death_god_number.setObjectName("death_god_number")
        self.death_god_number.setGeometry(QRect(30, 60, 91, 31))
        self.death_god_number.setFont(FONT_BOLD_24)
        self.death_god_number.setStyleSheet("color: black;")
        self.death_god_number.setAlignment(Qt.AlignLeft)

        self.death_god_rate = QLabel("0", self)
        self.death_god_rate.setObjectName("death_god_rate")
        self.death_god_rate.setGeometry(QRect(130, 67, 41, 16))
        self.death_god_rate.setFont(FONT_REG_14)
        self.death_god_rate.setStyleSheet("color: black;")
        self.death_god_rate.setAlignment(Qt.AlignRight)


class DeathDisaster(QFrame):
    def __init__(self, parent: QFrame, FONT_BOLD_24=None, FONT_REG_14=None) -> None:
        QFrame.__init__(self, parent)

        self.setStyleSheet(
            "background-color: #FFF3F1; border-radius:10;")
        self.setObjectName("death_disaster")

        self.death_disaster_title = QLabel("Death Disaster", self)
        self.death_disaster_title.setObjectName("death_disaster_title")
        self.death_disaster_title.setGeometry(QRect(30, 30, 141, 20))
        self.death_disaster_title.setFont(FONT_REG_14)
        self.death_disaster_title.setStyleSheet("color: black;")
        self.death_disaster_title.setAlignment(Qt.AlignLeft)

        self.death_disaster_number = QLabel("0", self)
        self.death_disaster_number.setObjectName("death_disaster_number")
        self.death_disaster_number.setGeometry(QRect(30, 60, 91, 31))
        self.death_disaster_number.setFont(FONT_BOLD_24)
        self.death_disaster_number.setStyleSheet("color: black;")
        self.death_disaster_number.setAlignment(Qt.AlignLeft)

        self.death_disaster_rate = QLabel("0", self)
        self.death_disaster_rate.setObjectName("death_disaster_rate")
        self.death_disaster_rate.setGeometry(QRect(130, 67, 41, 16))
        self.death_disaster_rate.setFont(FONT_REG_14)
        self.death_disaster_rate.setStyleSheet("color: black;")
        self.death_disaster_rate.setAlignment(Qt.AlignRight)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    d = Dashboard()
    app.exec_()
