"""Case-study #7 Генерация предложений
Разработчики:
Bayanova A. 60%, Shmatov D. 80%
"""


from random import *
from math import *
def difficulty(n):

    d = {}
    if n == 1:
        d.update({"Corn": 10500})
        d.update({"People": 100})
        d.update({"Territory": 150})
        d.update({"Treasure": 10000})
        d.update({"Army": 50})
        d.update({"Anxiety": 5})
        d.update({"Year": 0})
    elif n == 2:
        d.update({"Corn": 9500})
        d.update({"People": 90})
        d.update({"Territory": 120})
        d.update({"Treasure": 8000})
        d.update({"Army": 45})
        d.update({"Anxiety": 10})
        d.update({"Year": 0})
    elif n == 3:
        d.update({"Corn": 8000})
        d.update({"People": 75})
        d.update({"Territory": 100})
        d.update({"Treasure": 6000})
        d.update({"Army": 40})
        d.update({"Anxiety": 20})
        d.update({"Year": 0})
    elif n == 4:
        d.update({"Corn": 6500})
        d.update({"People": 60})
        d.update({"Territory": 80})
        d.update({"Treasure": 5000})
        d.update({"Army": 30})
        d.update({"Anxiety": 40})
        d.update({"Year": 0})
    else:
        print("You write a wrong number,fool.")

    return d

def event(x):
    ev = ["none", "plague", "none", "pests", "none", "elements", "none", "thieves", "born", "die", "die"]
    m = choice(ev)
    if m == "plague":
        eve = x.get("People") * 0.85
        x.update({"People": floor(eve)})
        print("Your country was beaten by", m, "and 15% of people was died.")
    elif m == "pests":
        eve = x.get("Corn") * 0.7
        x.update({"Corn": floor(eve)})
        print("Your country was beaten by", m, "and You lost 30% of corn")
    elif m == "elements":
        eve = x.get("Territory") * 0.8
        x.update({"Territory": floor(eve)})
        print("Your country was beaten by", m, "and You lost 20% of territory.")
    elif m == "thieves":
        eve = x.get("Treasure") * 0.6
        x.update({"Treasure": floor(eve)})
        print("Your country was beaten by", m, "and You lost 40% of gold")
    elif m == "born":
        o = randint(10,20)
        eve = x.get("People") + o
        x.update({"People": eve})
        print("In your country was born", o, "people")
    elif m == "born":
        o = randint(10,20)
        eve = x.get("People") - o
        x.update({"People": eve})
        print("In your country was died", o, "people")
    else:
        print("The sun shines over your kingdom")

    return x

def war(x):

    n = str(input("Do you want to start war?(Yes/No)")).lower()
    if n == "yes":
        country1 = randint(20,50)
        country2 = randint(50,70)
        country3 = randint(70,100)
        m = int(input("Which country do you want to fight: Dementevo, Bufetovo or Minakovo."
                      " Write only the number of the kingdom(1/2/3)"))
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
            anx = x.get("Anxiety")*1.25
            x.update({"Territory": floor(ter)})
            x.update({"Army": floor(army)})
            x.update({"Anxiety": anx})
            print("You win the war")
        elif army < enemy:
            army *= 0.3
            ter = x.get("Territory")*0.7
            anx = x.get("Anxiety") * 1.5
            x.update({"Territory": floor(ter)})
            x.update({"Army": floor(army)})
            x.update({"Anxiety": anx})
            print("You lost the war")
        else:
            draw = choice(["win", "lose"])
            if draw == "win":
                army *= 0.6
                ter = x.get("Territory") * 1.2
                anx = x.get("Anxiety") * 1.25
                x.update({"Territory": floor(ter)})
                x.update({"Army": floor(army)})
                x.update({"Anxiety" : anx})
                print("You win the war")
            elif draw == "lose":
                army *= 0.3
                anx = x.get("Anxiety") * 1.5
                ter = x.get("Territory") * 0.7
                x.update({"Territory": floor(ter)})
                x.update({"Army": floor(army)})
                x.update({"Anxiety": anx})
                print("You win the war")
    else:
        q = x.get("Anxiety")*0.75
        if x.get("Anxiety") < 1:
            q = 0
        x.update({"Anxiety" : q})

        print("Your Anxiety decreased by 25%.")

    return x

def food(x):
    n = randint(10,25)
    p = x.get("People") * n
    q = x.get("Corn") - p
    x.update({"Corn": q})
    print("People have eaten", p, "corn in a year." )
    return x




def prod(d):
    k = choice([1, 2, 2])
    if k == 1:
        p = randint(2,5)
        pr = int(input('Somebody wants to buy your corn for {} gold. How many do you want to sell? '.format(p)))
        # достать значение из словаря и вычесть пшеницу, добавить деньги
        s = d["Corn"] - pr
        t = d["Treasure"] + (p*pr)
        d.update({"Corn": s})
        d.update({"Treasure": t})
        return d

    if k == 2:
        p = randint(4, 7)
        pr = int(input('Somebody wants to sell your corn for {} gold. How many do you want to buy?  '.format(p)))
        # достать значение из словаря и вычесть деньги, добавить пшеницу
        s = d["Corn"] + pr
        t = d["Treasure"] - (p * pr)
        d.update({"Corn": s})
        d.update({"Treasure": t})
        return d

def exarmy(x):
    n = str(input("Do you want to extend yor army? 10 people to 5 soldiers.(yes/no)").lower())
    if n == "yes":
        q = x.get("People") - 10
        w = x.get("Army") + 5
        x.update({"People" : q})
        x.update({"Army" : w})

    return x

def rate(m):
    rt = (m["Corn"] / 100 + (m["Army"] + m["People"])/ 10 +  m["Territory"]/ 10 + m["Treasure"]/ 1000 / m["Anxiety"]) * m["Year"]
    return rt

def gamelost(x):
    if x.get("People") < 1:
        print("There are nobody in your kingdom. You lose. Try again Later.")
        accept = "no"
        print("You lived", x.get("Year"), "years. Thanks for game.")
        return accept
    elif x.get("Territory") < 1:
        print("There are no place to live. You lose. Try again Later.")
        accept = "no"
        print("You lived", x.get("Year"), "years. Thanks for game.")
        return accept
    elif x.get("Anxiety") >= 100:
        print("Your kingdom is in chaos. You lose. Try again Later.")
        accept = "no"
        print("You lived", x.get("Year"), "years. Thanks for game.")
        return accept
    elif x.get("Corn") < 1:
        p = randint(600,900)
        q = str(input("There are no food in your kingdom. Do you want to buy Corn? Price is {}.(Yes/No)".format(p)).lower())
        if q != "yes":
            print("Your kingdom died of starvation. You lose. Try again Later.")
            accept = "no"
            print("You lived", x.get("Year"), "years. Thanks for game.")
            return accept
        elif q == "yes":
            pr = int(input('How many do you want to buy?'))
            s = x["Corn"] + pr
            t = x["Treasure"] - p
            x.update({"Corn": s})
            x.update({"Treasure": t})
            if x.get("Corn") < 1:
                print("Your kingdom died of starvation. You lose. Try again Later.")
                accept = "no"
                year = x.get("Year")
                print("You lived", year, "years")
                return accept
            return x
    else:
        accept = str(input("Do you want to continue the game?(Yes/No)").lower())
        if accept == "no":
            print("You lived", x.get("Year"), "years. Thanks for game.")
        else:
            x.update({"Year": x.get("Year") + 1})
        return accept

def r(e):
    name = input('Введите имя пользователя на англ: ')
    f = open('rate.txt', 'w')
    res = rate(e) #тут значение должно быть
    f.write(str(res) + ' ')
    f.write(name + '\n')
    f.close()

def main():
    n = int(input("Choose difficulty(1-4): "))
    print("Your difficulty is", n, "and status of your kingdom is: ")
    q = difficulty(n)
    print(q)
    accept = "yes"
    while accept == "yes":
        m = event(q)
        t = exarmy(m)
        w = war(t)
        e = prod(w)
        sts = food(e)
        print("Your score is", rate(sts) * n)
        print("Status of your kingdom is:")
        print(sts)
        accept = gamelost(sts)
    r(sts)


if __name__ == "__main__":
    main()
