#26.	 Crie um programa que receba duas datas: D1/M1/A1 e D2/M2/A2, efetue a comparação e apresente-as em ordem crescente.

d1= int(input("\nPrimeira Data:\nDigite o dia: "))
m1= int(input("Digite o mês: "))
a1= int(input("Digite o ano: "))

d2= int(input("\nSegunda Data:\nDigite o dia: "))
m2= int(input("Digite o mês: "))
a2= int(input("Digite o ano: "))

if a1==a2 and m1==m2 and d1==d2:
    print("\nDatas iguais, por favor insira datas diferentes!")

if a1>a2:
    print("\nDatas em ordem crescente:", d2,"/",m2,"/",a2,"||",d1,"/",m1,"/",a1)
else:
    print("\nDatas em ordem crescente:", d1, "/", m1, "/", a1, "||", d2, "/", m2, "/", a2)

if a1==a2:
    if m1 > m2:
        print("\nDatas em ordem crescente:", d1, "/", m1, "/", a1, "||", d2, "/", m2, "/", a2)
    else:
        print("\nDatas em ordem crescente:", d2, "/", m2, "/", a2, "||", d1, "/", m1, "/", a1)

    if m1==m2:
        if d1 > d2:
            print("\nDatas em ordem crescente:", d2, "/", m2, "/", a2, "||", d1, "/", m1, "/", a1)
        else:
            print("\nDatas em ordem crescente:", d1, "/", m1, "/", a1, "||", d2, "/", m2, "/", a2)