def abovetwothousand(amt):
    n=2000
    div1=amt//n
    mod1=amt%n
    return (mod1,n,div1)


def twothousand(amt):
    n=500
    div1=amt//n
    mod1=amt%n
    return (mod1,n,div1)


def fivehundred(amt):
    n=200
    div1=amt//n
    mod1=amt%n
    return (mod1,n,div1)


def twohundred(amt):
    n=100
    div1=amt//n
    mod1=amt%n
    return (mod1,n,div1)

def onehundred(amt):
    n=50
    div1=amt//n
    mod1=amt%n
    return (mod1,n,div1)

def fifty(amt):
    n=20
    div1=amt//n
    mod1=amt%n
    return (mod1,n,div1)

def twenty(amt):
    n=10
    div1=amt//n
    mod1=amt%n
    return (mod1,n,div1)    

def ten(amt):
    n=5
    div1=amt//n
    mod1=amt%n
    return (mod1,n,div1)

def five(amt):
    n=2
    div1=amt//n
    mod1=amt%n
    return (mod1,n,div1)

def calculate(amt):

    if amt==1:
        n=div1=1
        mod1=0
        return (mod1,n,div1)

    elif amt >=2 and amt<5:
        mod1,n,div1=five(amt)
        return (mod1,n,div1)

    elif amt >=5 and amt<10:
        mod1,n,div1=ten(amt)
        return (mod1,n,div1)

    elif amt>=10 and amt<20:
        mod1,n,div1=twenty(amt)
        return (mod1,n,div1)

    elif amt>=20 and amt<50:
        mod1,n,div1=fifty(amt)
        return (mod1,n,div1)

    elif amt>=50 and amt<100:
        mod1,n,div1=onehundred(amt)
        return (mod1,n,div1)

    elif amt>=100 and amt<200:
        mod1,n,div1=twohundred(amt)
        return (mod1,n,div1)

    elif amt>=200 and amt<500:
        mod1,n,div1=fivehundred(amt)
        return (mod1,n,div1)

    elif amt>=500 and amt<2000:
        mod1,n,div1=twothousand(amt)
        return (mod1,n,div1)

    elif amt>=2000:
        mod1,n,div1=abovetwothousand(amt)
        return (mod1,n,div1)


def main1():
    amt=int(input("Enter the amount: "))
    mod1,n,div1=calculate(amt)
    print("The change for the amount {} is :\n".format(amt))
    print("{} notes of {} rupees".format(div1,n))
    while mod1!=0:
        amt=mod1
        mod1,n,div1 = calculate(amt)
        if n<=5:
            print("{} coins of {} rupees".format(div1,n))
        else:
            print("{} notes of {} rupees".format(div1,n))

if __name__=="__main__":
    main1()