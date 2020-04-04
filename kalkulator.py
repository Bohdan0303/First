a=float(input())
b=float(input())
c=input("+ - * / mod pow div")
if c == "+" :
    print(float(a) + float(b))
elif c == "-" :
    print(float(a) - float(b))
elif c == "*" :
    print(float(a) * float(b))
elif c == "/" :
    print(float(a) / float(b))
    if b == 0:
        print("Деление на 0!")
elif c == "mod" :
    print(float(a) % float(b))
    if b == 0 :
        print("Деление на 0!")
elif c == "pow":
    print(float(a) ** float(b))
elif c == "div":
    print(float(a) // float(b))
    if b == 0:
        print("Деление на 0!")

