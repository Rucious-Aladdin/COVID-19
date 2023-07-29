money = True

if money:
    print("택시타요")
else:
    print("걸어가요")

#and, or, not 연산자

money = 2000
card = True

if money >= 3000 or card:
    print("택시를 타고 가라")
else:
    print("걸어가라")

a = 1 in [1, 2 ,3]
b = 1 not in [1, 2, 3]

print(a)
print(b)

pocket = ["paper", "cellphone", "money"]

if "money" in pocket:
    print("택시를 타고 가라")
else:
    print("걸어가라")

if "money" not in pocket:
    pass
else:
    print("카드를 꺼내라")

pocket = ["paper", "cellphone"]
card = False

if ("money" or card) in pocket:
    print("택시를 타고가라")
else:
    print("걸어가라")

score = 70
message = "success" if score >= 60 else "failure"
print(message)