import re

print("Вы вышли на улицу. Что вы будете делать?")

while True:
    answer = input().lower()
    if (re.fullmatch(".*откр.*зонт.*", answer)):
        print("Вы забыли зонт дома. Что вы будете делать дальше?")
    elif (re.fullmatch(".*(выйт|верну).*", answer)):
        print("Вы вернулись домой. Досвидания!")
        break

    elif (re.fullmatch(".*пройд\w+", answer)):
        print("Вы прошли по Абрикосовой")
        while True:
            answer = input().lower()
            if (re.fullmatch(".*сверн\w+", answer)):
                print("Вы свернули на Виноградную")
            elif (re.fullmatch(".*посто\w+", answer)):
                print("Вы постояли на Тенистой и попали в Детство давнее")
                print("Что бы Вы хотели взять с собой из него?")
                otvet = input()
                print("Вы взяли с собой", otvet," и увидели киоск Мороженое")
                print("может по мороженке ;) ?  да/нет")
                while True:
                    answer = input().lower()
                    if (re.fullmatch("нет", answer)):
                        print("Крылатые качели вернули Вас к дому!")
# как перейти к началу программы?
                    elif (re.fullmatch("да", answer)):
                        print("Эскимо, Пломбир, Фруктовое, Молочное. Что выбираете?")
                    elif (re.fullmatch(".*выберу\s(\w)+.*", answer.lower())):
                        matchs = re.search(".*выберу\s(\w)+", answer.lower())
                        if not matchs[0]:
                            print("Такого, к сожалению, нет... сделайте выбор еще раз")
                        else:
                            if (matchs[0] == "выберу эскимо"):
                                print("У нас лучшее эскимо!")
                            elif (matchs[0] == "выберу пломбир"):
                                print("вот ваш пломбир, все по ГОСТу!")
                            elif (matchs[0] == "выберу фруктовое"):
                                print("упс... закончилось :(")
                            elif (matchs[0] == "выберу молочное"):
                                print("ммм... вот ваше вкууусное молочное")
                            else:
                                print("К сожалению такого сорта нет в ассортименте")

            else:
                print("не там свернули, не там постояли...")
                break

    elif (re.fullmatch(".*(идт|напр|передв|пой(д|т)).*магазин.*", answer)):
        print("Вы пришли в магазин. Что вы там будете делать?")
        while True:
            answer = input().lower()
            if (re.fullmatch(".*(вернут|улиц|выйти).*", answer)):
                print("Вы снова на улице")
                break
            elif (re.fullmatch(".*(выбир|осматр|подой).*продукт.*", answer)):
                print("Вы видите хлеб, молоко и кофемашину. Мда, не густо....")
            elif (re.fullmatch(".*взять\s(\w)+.*", answer)):
                matchs = re.search("взять\s(\w)+", answer)
                if not matchs[0]:
                    print("Не понятно, что именно вы хотите взять")
                else:
                    if (matchs[0] == "взять хлеб"):
                        print("взятие хлеба произошло успешно")
                    elif (matchs[0] == "взять молоко"):
                        print("пакет оказался порван. вы облились")
                    elif (matchs[0] == "взять кофемашину"):
                        print("она слишком тяжелая")
                    else:
                        print("Я не могу ", matchs[0], " этого нет на полке")
                print("Вы видите хлеб, молоко и кофемашину. Мда, не густо....")
            elif (re.fullmatch(".*взять\s(\w)+.*", answer)):
                matchs = re.search("взять\s(\w)+", answer)
                if not matchs[0]:
                    print("Не понятно, что именно вы хотите взять")
                else:
                    if (matchs[0] == "взять хлеб"):
                        print("взятие хлеба произошло успешно")
                    elif (matchs[0] == "взять молоко"):
                        print("пакет оказался порван. вы облились")
                    elif (matchs[0] == "взять кофемашину"):
                        print("она слишком тяжелая")
                    else:
                        print("Я не могу ", matchs[0], " этого нет на полке")
