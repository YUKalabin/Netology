var_month = (input("Введите месяц:"))
var_date = int(input("Введите число:"))

if var_month = январь or january or Январь or January:
    var_month = 1
elif var_month = февраль or Февраль or February or february:
    var_month = 2
elif var_month = "март" or "Март" or "March" or "March":
    var_month = 3
elif var_month = апрель or Апрель or April or april:
    var_month = 4
elif var_month = май or Май or May or may:
    var_month = 5
elif var_month = июнь or Июнь or June or june:
    var_month = 6
elif var_month = июль or Июль or July or july:
    var_month = 7
elif var_month = август or Август or August or august:
    var_month = 8
elif var_month = сентябрь or Сентябрь or September or semptember:
    var_month = 9
elif var_month = октябрь or Октябрь or October or october:
    var_month = 10
elif var_month = ноябрь or Ноябрь or November or november:
    var_month = 11
elif var_month = декабрь or Декабрь or December or december:
    var_month = 12
else:
    print("Wrong month")

print(var_month)