from random import*
pt=0
while pt<10:
    x=randint(0,10)
    c=randint(0,10)
    print(x,"*",c)
    a=int(input("x*c est égal à "))
    if a==x*c:
        pt=pt+1
        print("bien joué tu as",pt,"points")

    else:
        pt=pt-1
        print("raté, tu as desormais",pt,"points")
        if pt<1:
            print("perdu ! ")
            break
