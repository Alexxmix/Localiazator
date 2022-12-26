# Localiazator
A smol python module for localization
Локализатор - небольшой модуль для Python предназначенный для более удобного внедрения падежных форм в локализацию программы.
Разработано и проверенно на Python 3.9
# Инструкция 
Модуль включает в себя 5 функций:
1. Основная функция wordForm(word:str, wordForm:str)
  word - название объекта или название файла без расширения, в котором храняться формы слова.
  wordForm - кодовое обозначение формы, которую нужно подставить.
  Функция получает из папки wordList из файла <word>.txt нужную форму слова.
  
    import localizator

    localizator.setWorkSpace('rus')
    localizator.setDefaultForm('ИпЕд')

    print('Вы получили {}'.format(localizator.wordForm('Water', 'ВпЕд')))
  
2. Функция createDefaultForm(folderName:str, numOfForms:int)
  folderName - название папки в которой есть папка wordList в которой создастся defaultForm.txt
  numOfForms - количество пустых форм для заполнения. Функция создаёт файл-пример организации форм.
3. Функция createWorkSpace(folderName:str)
  folderName - название папки в которой создастся папка wordList в которой будут храниться формы слов для конкректной локализации. Функция создаёт рабочее пространство   для локализации.
4. Функция setWorkSpace(folderName:str)
  folderName - название папки в которой есть папка wordList
  Задаёт папку в которой хранятся файлы формы слова. Предназначенно для облегчённой работы.
5. Функция setDefaultForm(formName:str)
  formName - кодовое название формы к которой будет обращаться функция wordForm, если в файле с формами слова отсутствует необходимая форма.
