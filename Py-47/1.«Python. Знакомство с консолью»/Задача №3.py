salary_per_month = int(input("Введите заработную плату в месяц:"))
perc_for_hypothec = int(input("Введите, какой процент(%) уходит на ипотеку:"))
perc_for_life = int(input("Введите, какой процент(%) уходит на жизнь:"))

print("На ипотеку было потрачено:" , salary_per_month * perc_for_hypothec / 100 *12 , "рублей")
#print("Было накоплено:" , salary_per_month * (100 - perc_for_hypothec - perc_for_life) / 100 *12 , "рублей" )
print(f"Было накоплено: {salary_per_month * (100 - perc_for_hypothec - perc_for_life) / 100 *12} рублей")