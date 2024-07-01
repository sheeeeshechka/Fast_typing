import time
from random import *
from math import *
def russian_language():
    def training_r(n): #функция тренировки
        global prog
        if n==1: #выбор фунуции
            s=r1
        elif n==2: 
            s=r2
        elif n==3:
            s=r3
        print('Сейчас вы должны будете как можно быстрее и правильнее ввести с клавиатуры 10 слов')
        time.sleep(2) 
        begin=input('для начала тренировки нажмите клавишу Enter')
        for q in range(1, 4): #обратный отсчет
            print(q)
            time.sleep(1)
        sabina=time.time()
        wrong=0
        for start in range(10):
            ann=choice(s)
            print(ann)
            ann1=input()
            if ann1=='':
                wrong+=10
            else:
                if len(ann)!=len(ann1):
                    wrong+=len(max(ann, ann1))-len(min(ann, ann1))
                for l in range(min(len(ann), len(ann1))):
                    if ann[l]!=ann1[l]:
                        wrong+=3
            del s[s.index(ann)]
        sabinina_mama=time.time()
        cross=(sabinina_mama-sabina)//1
        minus=cross-40
        if wrong==0:
            if cross<=40:
                print('ваш результат 100%!!! поздравляем') 
                prog=100
            elif cross>40:
                print('ваш результат', 100-minus)
                prog=100-minus
        else:
            if minus>=0:
                print('ваш результат', 100-(minus+wrong))
                prog=100-(minus+wrong)
            else:
                print('ваш результат', 100-wrong)
                prog=100-wrong
        if prog<=0:
            print('')

    def saves_r(n):
        global sss
        sss=n*100+prog
        save=open(r"saves.txt", 'a', encoding='utf-8')
        save.write('Русиш треня'+str(sss)+'\n')
        save.close()    
        print('Ваш результат сохранен')

    input('Нажмите Enter')
#списки русского языка
    r1=['двенадцать', 'библиотекарша', 'Родина', 'облако', 'агроном', 'коридор', 'прекрасный', 'вокзал', 'путешествие', 'директор', 'путешественник', 'участвовать', 'товарищ', 'саквояж', 'пассажир', 'багаж', 'облако', 'до свидания', 'пассажирский', 'квитанция','растение','приветливо','винегрет','троллейбус','комбайн','аккуратно','одуванчик','воскресенье','сирень','футбол']
    r2=['расчетливый','рассчитать','расчет','спартакиада','поразительный','из-под','подлежащее','словосочетание','до свидания','бинокль','преодолеть','примирять','колоссальный','алюминиевый','профессионализм','претворить','исполинский','корреспондент','экскаватор','палисадник','эскалатор','искусный','экскаватор','путешественник','президент','искусство','председатель','искусственный','салют','аннотация']
    r3=['мало-помалу','вследствие того что','оттого что','затем чтобы','впоследствии','семафор','недосягаемый','для того чтобы','комендант','как будто','привилегия','беллетристика','апофеоз','декларация','продюсер','пьедестал','делегат','амбразура','кандидат','постамент','антагонизм','консолидация','беспрекословный','дезинфицировать','дирижировать','подлинник','электрификация','кардинальный','идеология','панорама','колоннада','дифирамб','апелляция','на износ','аккордеон','артикуляция','эвфемизм','апартаменты','асимметрия','генеалогия']

    print('Выберите уровень сложности от 1 до 3')
    choi_r=int(input())
    training_r(choi_r)
    saves_r(choi_r)
    games()
def english_language():
    def training_e(n): #функция тренировки
        global prog
        if n==1: #выбор фунуции
            s=e1
        elif n==2: 
            s=e2
        elif n==3:
            s=e3
        print('Сейчас вы должны будете как можно быстрее и правильнее ввести с клавиатуры 10 слов')
        time.sleep(2) 
        begin=input('для начала тренировки нажмите клавишу Enter')
        for q in range(1, 4): #обратный отсчет
            print(q)
            time.sleep(1)
        sabina=time.time()
        wrong=0
        for start in range(10):
            ann=choice(s)
            print(ann)
            ann1=input()
            if ann1=='':
                wrong+=10
            else:
                if len(ann)!=len(ann1):
                    wrong+=len(max(ann, ann1))-len(min(ann, ann1))
                for l in range(min(len(ann), len(ann1))):
                    if ann[l]!=ann1[l]:
                        wrong+=3
            del s[s.index(ann)]
        sabinina_mama=time.time()
        cross=(sabinina_mama-sabina)//1
        minus=cross-40
        if wrong==0:
            if cross<=40:
                print('ваш результат 100%!!! поздравляем') 
                prog=100
            elif cross>40:
                print('ваш результат', 100-minus)
                prog=100-minus
        else:
            if minus>=0:
                print('ваш результат', 100-(minus+wrong))
                prog=100-(minus+wrong)
            else:
                print('ваш результат', 100-wrong)
                prog=100-wrong
        if prog<=0:
            print('')

    def saves_e(n):
        global sss
        sss=n*100+prog
        save=open(r"saves.txt", 'a', encoding='utf-8')
        save.write('инглиш треня'+str(sss)+'\n')
        save.close()    
        print('Ваш результат сохранен')
    input('Нажмите Enter')
    e1=['abate','abjure','augury','boor','cardinal','colander','dangle','dearth','docile','doleful','dormant','drought','extant','feckless','froward','glib','incise','inveigle','maudlin','minatory','moralistic','ossified','perch','pervade','petulant','pillage','plumb','prevail','probity','prodigy','prolific','provident','proximity','prudent','rarefy','repine','runic','supine','vestige','vilify',]
    e2=['aphoristic','avaricious','canonical','culpability','deference','deliberate','delineate','dexterity','diligent','disparage','dispatch','encomium','extirpate','halcyon','impugned','meretricious','ostracism','pejorative','penchant','philistine','ponderous','postulate','precursor','prodigious','proprietary','raconteur','refulgent','stipulate','subliminal','venerate','vigilance','vitriolic',]
    e3=['ambidextrous','blandishment','commensurate','cumbersome','derogatory','diaphanous','discernment','epistemology','equivocation','imperturbability','parsimonious','philanthropy','precipitous','presumptuous','proliferate','quintessential','solicitous','throwback','untoward','vehemence','verisimilar','verisimilitude','vindicate','visionary','vituperate','volatile','voluptuous','whittle']
    print('Выберите уровень сложности от 1 до 3')
    choi_e=int(input())
    training_e(choi_e)
    saves_e(choi_e)
    games()
def math_math():
    def inside_math(n):
        if n==1:
            con=0
            for i in range(10):
                a=randint(1, 10)
                b=randint(1, 10)
                print(a, '*', b, '=')
                c=int(input())
                if c==a*b:
                    con+=1
            print('Ваш результат', con, '\10')
            save=open(r"saves.txt", 'a', encoding='utf-8')
            save.write('матеша внедренная'+str(con)+'\n')
            save.close()
            print('Ваш результат сохранен')
            print('Вы хотите поиграть в устный счет еще раз?')
            print('1) Да')
            print('2) Нет')
            print('Введите 1 или 2')
            rep=int(input())
            if rep==1:
                math_math()
            else:
                games()
        elif n==2:
            con=0
            for i in range(10):
                a=randint(1, 100)
                b=randint(1, 100)
                print(a, '+', b, '=')
                c=int(input())
                if c==a+b:
                    con+=1
            print('Ваш результат', con, '\10')
            save=open(r"saves.txt", 'a', encoding='utf-8')
            save.write('матеша внедренная'+str(con)+'\n')
            save.close()
            print('Ваш результат сохранен')
            print('Вы хотите поиграть в устный счет еще раз?')
            print('1) Да')
            print('2) Нет')
            print('Введите 1 или 2')
            rep=int(input())
            if rep==1:
                math_math()
            else:
                games()
        elif n==3:
            con=0
            for i in range(10):
                a=randint(1, 100)
                b=randint(1, a+1)
                print(a, '-', b, '=')
                c=int(input())
                if c==a-b:
                    con+=1
            print('Ваш результат', con, '\10')
            save=open(r"saves.txt", 'a', encoding='utf-8')
            save.write('матеша внедренная'+str(con)+'\n')
            save.close()
            print('Ваш результат сохранен')
            print('Вы хотите поиграть в устный счет еще раз?')
            print('1) Да')
            print('2) Нет')
            print('Введите 1 или 2')
            rep=int(input())
            if rep==1:
                math_math()
            else:
                games()
        elif n==4:
            con=0
            for i in range(10):
                a=randint(1, 1000)
                b=randint(1, 1000)
                print(a, '+', b, '=')
                c=int(input())
                if c==a+b:
                    con+=1
            print('Ваш результат', con, '\10')
            save=open(r"saves.txt", 'a', encoding='utf-8')
            save.write('матеша внедренная'+str(con)+'\n')
            save.close()
            print('Ваш результат сохранен')
            print('Вы хотите поиграть в устный счет еще раз?')
            print('1) Да')
            print('2) Нет')
            print('Введите 1 или 2')
            rep=int(input())
            if rep==1:
                math_math()
            else:
                games()
        elif n==5:
            con=0
            for i in range(10):
                a=randint(1, 1000)
                b=randint(1, a+1)
                print(a, '-', b, '=')
                c=int(input())
                if c==a-b:
                    con+=1
            print('Ваш результат', con, '\10')
            save=open(r"saves.txt", 'a', encoding='utf-8')
            save.write('матеша внедренная'+str(con)+'\n')
            save.close()
            print('Ваш результат сохранен')
            print('Вы хотите поиграть в устный счет еще раз?')
            print('1) Да')
            print('2) Нет')
            print('Введите 1 или 2')
            rep=int(input())
            if rep==1:
                math_math()
            else:
                games()
        elif n==6:
            con=0
            for i in range(10):
                a=randint(1, 100)
                b=randint(1, 100)
                print(a, '*', b, '=')
                c=int(input())
                if c==a*b:
                    con+=1
            print('Ваш результат', con, '\10')
            save=open(r"saves.txt", 'a', encoding='utf-8')
            save.write('матеша внедренная'+str(con)+'\n')
            save.close()
            print('Ваш результат сохранен')
            print('Вы хотите поиграть в устный счет еще раз?')
            print('1) Да')
            print('2) Нет')
            print('Введите 1 или 2')
            rep=int(input())
            if rep==1:
                math_math()
            else:
                games()
    def person_math():
        print('Тренировку на какую операцию вы хотите провести?')
        print('1) Сложение')
        print('2) Вычитание')
        print('3) Умножение')
        print('Введите число от 1 до 3')
        operation=int(input())
        print('Введите самое большое и самое маленькое число, которое будет появляться в вашей тренировке')
        print('Самое маленькое число')
        aaa=int(input())
        print('Самое большое число')
        bbb=int(input())
        print('Введите количество примеров, которое будет в вашей тренировке')
        colvo=int(input())
        print('Удачной тренировки')
        time.sleep(1)
        print(1)
        time.sleep(1)
        print(2)
        time.sleep(1)
        print(3)
        time.sleep(1)
        if operation==1:
            con=0
            for i in range(colvo):
                a1=randint(aaa, bbb)
                b1=randint(aaa, bbb)
                print(a1, '+', b1, '=')
                c=int(input())
                if c==a1+b1:
                    con+=1
            print('Ваш результат', con, 'из', colvo)
        elif operation==2:
            con=0
            for i in range(colvo):
                a1=randint(aaa, bbb)
                b1=randint(aaa, a1+1)
                print(a1, '-', b1, '=')
                c=int(input())
                if c==a1-b1:
                    con+=1
            print('Ваш результат', con, 'из', colvo)
        elif operation==3:
            con=0
            for i in range(colvo):
                a1=randint(aaa, bbb)
                b1=randint(aaa, bbb)
                print(a1, '*', b1, '=')
                c=int(input())
                if c==a1*b1:
                    con+=1
            print('Ваш результат', con, 'из', colvo)
        save=open(r"saves.txt", 'a', encoding='utf-8')
        save.write('Настраиваемая матеша'+str(con)+'/'+colvo+'\n')
        save.close()
        print('Ваш результат сохранен')
        print('Вы хотите поиграть в устный счет еще раз?')
        print('1) Да')
        print('2) Нет')
        print('Введите 1 или 2')
        rep=int(input())
        if rep==1:
            math_math()
        else:
            games()
    print('Вы можете настроить свою собственную сложность, либо же играть на одной из предложенных игрой.')
    time.sleep(2)
    print('1) Настроить самому')
    print('2) выбрать сложность')
    print('введите 1 или 2')
    variant=int(input())
    if variant==1:
        person_math()
    elif variant==2:
        print('Выберите один из предложенных режимов')
        print('1) Табличное умножение')
        print('2) Сложение чисел от 1 до 100')
        print('3) Вычитание чисел от 1 до 100')
        print('4) Сложение чисел от 1 до 1000')
        print('5) Вычитание чисел от 1 до 1000')
        print('6) Умножение чисел от 1 до 100')
        print('Введите число от 1 до 6')
        inside_hard=int(input())
        print(1)
        time.sleep(1)
        print(2)
        time.sleep(1)
        print(3)
        time.sleep(1)
        inside_math(inside_hard)
print('Здравствуйте, приветствую вас в своей первой программе, чем-то на подобии игры.')
time.sleep(2)
print('После прохождения вы сможете оставить отзыв об этой игре, каждый из которых я обязательно прочту!')
time.sleep(2)
print('Для начала игры нажмите Enter')
count_games=0
start_game=input()
def choose_hard():
    print('Выберите режим игры')
    print('1) слепая печать на русском языке')
    print('2) слепая печать на английском языке')
    print('3) устный скоростной счет')
    print('Введите число от 1 до 3')
    choose_game=int(input())
    if choose_game==1:
        russian_language()
    elif choose_game==2:
        english_language()
    elif choose_game==3:
        math_math()
def games():
    global count_games
    if count_games==0:
        count_games+=1
        choose_hard()
    else:
        print('Вы хотите изменить режим игры и поиграть еще раз?')
        print('1) Да')
        print('2) Нет')
        print('Введите 1 или 2')
        choose_repeat=int(input())
        if choose_repeat==1:
            choose_hard()
        else:
            print('Напишите, пожалуйста, отзыв о вашем опыте игры')
            time.sleep(1)
            print('Если вы не хотите ничего писать, просто нажмите Enter')
            otzyv=input()
            save=open("saves.txt", 'a', encoding='utf-8')
            save.write('отзыв '+otzyv+'\n')
            save.close()
            print('Спасибо за оставленый отзыв!!!')
games()