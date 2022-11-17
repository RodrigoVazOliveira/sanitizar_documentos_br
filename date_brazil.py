from datetime import datetime


class DataBrazil:

    def __init__(self):
        self.moment_registred = datetime.today()

    def getMonth(self):
        month_of_year = [
            "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", 'Julho',
            "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"
        ]
        return month_of_year[self.moment_registred.month - 1]

    def get_day_week(self):
        day_of_week = [
            "Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"
        ]
        return day_of_week[self.moment_registred.weekday()]

    def datetime_formated(self):
        return self.moment_registred.strftime("%d/%m/%Y %H:%M:%S")

    def __str__(self):
        return self.datetime_formated()