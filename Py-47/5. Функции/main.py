documents = [
      {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
      {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
      {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
    ]

directories = {
        '1': ['2207 876234', '11-2'],
        '2': ['10006'],
        '3': []
      }

# 1) - p – people – команда, которая спросит номер документа и выведет имя человека, которому он принадлежит;

def get_name(doc):
  for docum in doc:
    if command_ == docum['number']:
      # print(docum['name'])
      return docum['name']
    # else:
    #   print(None)  
# get_name(documents)

# 2) - s – shelf – команда, которая спросит номер документа и выведет номер полки, на которой он находится;

def get_shelf(dir, command_doc):
  for _shelf, _doc in dir.items():
    if command_doc in _doc:
      # print(f"Документ находится на полке №{_shelf}")
      return _shelf
    # else:
    #   print('Такого документа нет, введите существующий документ')
  return None


# 3) - l – list – команда, которая выведет список всех документов в формате passport "2207 876234" "Василий Гупкин";

def listing(doc):
  for dict in doc:
    print(f'{dict["type"]} "{dict["number"]}" "{dict["name"]}"')


# 4) - a – add – команда, которая добавит новый документ в каталог и в перечень полок, спросив его номер, тип, имя владельца и номер полки, на котором он будет храниться. Корректно обработайте ситуацию, когда пользователь будет пытаться добавить документ на несуществующую полку.

def add_(doc, dir):
    new_dict = {}
    shelf_ = None
    new_dict['type'] = input('Введите тип документа: ')
    new_dict['number'] = input('Введите номер документа: ')
    new_dict['name'] = input('Введите имя и фамилию: ')
    while shelf_ not in dir.keys():
        shelf_ = input('Введите номер полки от 1 до 3: ')
    doc.append(new_dict)
    dir[shelf_].append(new_dict['number'])

# d – delete – команда, которая спросит номер документа и удалит его из каталога и из перечня полок. Предусмотрите сценарий, когда пользователь вводит несуществующий документ;

def del_(doc, dir):
  doc_number = input("Введите номер документа для его удаления: ")
  for dict_ in doc:
    if doc_number == dict_["number"]:
      doc.remove(dict_)    
  for shelf_, doc_ in dir.items():
    if doc_number in doc_:
      doc_.remove(doc_number)
      break
  else:
    print("Такого документа нет.")
  return doc, dir


  



def main(doc):

  while True:
    print('''
    Список возможных команд:

    p - Имя человека по номеру документа;
    s – Номер полки по номеру документа;
    l – Список всех документов с реквизитами;
    a – Добавление нового документа;
    d - Удаление документа.
    ''')
    command = input('Выберите желаемое действие: ')
    if command == 'p':
      global command_
      command_ = input('Введите номер документа: ')
      print(get_name(documents))
      print()
    elif command == 's':
      global command_doc      
      while True:
        command_doc = input('Введите номер документа: ')
        shelf = get_shelf(directories, command_doc)
        if shelf is not None:
          print()
          print(f"Документ находится на полке №{shelf}")
          break
        elif command_doc == "":
          break
        else:
          print('Такого документа нет.')
          print('Для выхода из цикла нажмите Enter или введите корректный номер документа')
    elif command == 'l':
      listing(documents)
      print()
    elif command == 'a':
      add_(documents, directories)
    elif command == 'd':
      del_(documents, directories)
      print()
    
    elif command == 'q':
      print('Выход из программы')
      break

main(documents)


