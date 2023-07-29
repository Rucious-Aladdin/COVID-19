class Myerror(Exception): #내장클래스인 Exception을 상속한 것
    def __str__(self):
        return "닉을 그렇게 부르면 안됩니다!"

def say_nick(nick):
    if nick == "바보":
        raise Myerror()
    print(nick)

try:
    say_nick("천사")
    say_nick("바보")
except Myerror as e:
    print(e)
