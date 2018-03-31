#20.	Receba a hora de início do turno de trabalho e exiba na tela se é turno manhã, tarde ou noite. Considera:
#• Manhã – 5hs às 12,59hs;
#• Tarde – 13hs às 20,59;
#• Noite – 21hs às 4,59hs;

hr_inicio = float(input("\nDigite a hora de ínicio do turno: "))

if hr_inicio >=5 and hr_inicio <=12.59:
    print("\nTurno da Manhã")

elif hr_inicio >=13 and hr_inicio <=20.59:
    print("\nTurno da Tarde")

else:
    print("\nTurno da Noite")


