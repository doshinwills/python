class Duck:
    def talk(self):
        print("Quack Quack")


class Human:
    def talk(self):
        print("Hello there")



def callTalk(obk):
    obk.talk()

h= Human()
d = Duck()

callTalk(h)
callTalk(d)


