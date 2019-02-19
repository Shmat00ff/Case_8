from random import *
from math import *
def difficulty():
    n = int(input("choose difficulty(1-4): "))
    d = {}
    if n == 1:
        d.update({"Corn": 10500})
        d.update({"People": 100})
        d.update({"Territory": 150})
        d.update({"Treasure": 10000})
        d.update({"Army": 50})
        d.update({"Anxiety": 5})
        d.update({"Friends": 0})
        d.update({"Year": 0})
    elif n == 2:
        d.update({"Corn": 9500})
        d.update({"People": 90})
        d.update({"Territory": 120})
        d.update({"Treasure": 8000})
        d.update({"Army": 45})
        d.update({"Anxiety": 10})
        d.update({"Friends": 0})
        d.update({"Year": 0})
    elif n == 3:
        d.update({"Corn": 8000})
        d.update({"People": 75})
        d.update({"Territory": 100})
        d.update({"Treasure": 6000})
        d.update({"Army": 40})
        d.update({"Anxiety": 20})
        d.update({"Friends": 0})
        d.update({"Year": 0})
    elif n == 4:
        d.update({"Corn": 6500})
        d.update({"People": 60})
        d.update({"Territory": 80})
        d.update({"Treasure": 5000})
        d.update({"Army": 30})
        d.update({"Anxiety": 40})
        d.update({"Friends": 0})
        d.update({"Year": 0})
    else:
        print("You write a wrong number,fool.")

    return d

def event(x):
    ev = ["none", "plague", "none", "pests", "none", "elements", "none", "thief"]
    m = choice(ev)
    if m == "plague":
        eve = x.get("People") * 0.85
        x.update({"People": floor(eve)})
    elif m == "pests":
        eve = x.get("Corn") * 0.7
        x.update({"Corn": floor(eve)})
    elif m == "elements":
        eve = x.get("Territory") * 0.8
        x.update({"Territory": floor(eve)})

    print(m)
    return x

def war(x):

    n = str(input("Do you want to start war?(Yes/No)")).lower()
    if n == "yes":
        country1 = randint(10,40)
        country2 = randint(40,60)
        country3 = randint(60,100)
        m = int(input("Which country do you want to fight?(1/2/3)"))
        army = x.get("Army")
        if m == 1:
            enemy = country1
        elif m == 2:
            enemy = country2
        elif m == 3:
            enemy = country3
        else:
            print("You write a wrong number,fool.")

        if army > enemy:
            army *= 0.6
            ter = x.get("Territory")*1.2
            x.update({"Territory": floor(ter)})
            x.update({"Army": floor(army)})
        elif army < enemy:
            army *= 0.3
            ter = x.get("Territory")*0.7
            x.update({"Territory": floor(ter)})
            x.update({"Army": floor(army)})
        else:
            draw = choice(["win", "win", "lose"])
            if draw == "win":
                army *= 0.6
                ter = x.get("Territory") * 1.2
                x.update({"Territory": floor(ter)})
                x.update({"Army": floor(army)})
            elif draw == "lose":
                army *= 0.3
                ter = x.get("Territory") * 0.7
                x.update({"Territory": floor(ter)})
                x.update({"Army": floor(army)})

def prod(d):
    p = randint(20,70)
    pr = int(input('У вас хотят купить пшеницу за'+ p + 'рублей. Сколько продать? '))
    # достать значение из словаря и вычесть пшеницу, добавить деньги
    c = d["Corn"] - pr
    t = d["Treasure"] + (p*pr)
    d.update({"Corn": s})
    d.update({"Treasure": t})

def bye(d):
    p = randint(20, 70)
    pr = int(input('Вам хотят продать пшеницу за' + p + 'рублей. Сколько купить? '))
    # достать значение из словаря и вычесть деньги, добавить пшеницу
    c = d["Corn"] + pr
    t = d["Treasure"] - (p * pr)
    d.update({"Corn": s})
    d.update({"Treasure": t})

def main():
    n = difficulty()
    m = event(n)
    print(m)

def rate():
    rt = (d["Corn"] / 100 + (d["Army"] + d["People"])/ 10 + / d["Terrirory"]/ 10 + d["Treasure"]/ 1000 / d["Anxiety"]) * year * n
    return rt

if __name__ == "__main__":
    main()
