def names_write(names):
    file = open("Files/names.txt", "w")
    file.write("<p style='color: red'>Імена: </p>\n")
    for item in names:
        file.write(item + "\n")
    file.close()


def dates_write(dates):
    file = open("Files/dates.txt", "w")
    file.write("<p style='color: red'>Дати: </p>\n")
    for item in dates:
        file.write(item + "\n")
    file.close()


def mails_write(mails):
    file = open("Files/mails.txt", "w")
    file.write("<p style='color: red'>Поштові скриньки:</p>\n")
    for item in mails:
        file.write(item + "\n")
    file.close()


def phone_write(phones):
    file = open("Files/phones.txt", "w")
    file.write("<p style='color: red'>Телефони: </p>\n")
    for item in phones:
        file.write(item + "\n")
    file.close()
