# Выберите веб-сайт с табличными данными, который вас интересует (https://finance.yahoo.com/markets/stocks/trending/)
# Напишите код Python, использующий библиотеку requests для отправки HTTP GET-запроса на сайт и получения HTML-содержимого страницы.
# Выполните парсинг содержимого HTML с помощью библиотеки lxml, чтобы извлечь данные из таблицы.
# Сохраните извлеченные данные в CSV-файл с помощью модуля csv.

# Ваш код должен включать следующее:

# Строку агента пользователя в заголовке HTTP-запроса, чтобы имитировать веб-браузер и избежать блокировки сервером.
# Выражения XPath для выбора элементов данных таблицы и извлечения их содержимого.
# Обработка ошибок для случаев, когда данные не имеют ожидаемого формата.
# Комментарии для объяснения цели и логики кода.

# Импорт необходимых библиотек
import requests
from lxml import html
import pandas as pd
import csv


# Определение целевого URL(куда обращаемся)
url = "https://finance.yahoo.com/quote/%5EDJI/history/"

# Отправка HTTP GET запроса на целевой URL с пользовательским заголовком User-Agent
response = requests.get(url, headers = {
   'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'})


# Парсинг HTML-содержимого ответа с помощью библиотеки lxml
tree = html.fromstring(response.content)

# Использование выражения XPath для выбора всех строк таблицы в пределах таблицы 
table_rows = tree.xpath("//table[@class='table yf-ewueuo noDl']/thead/tr")


# # Использование выражения XPath для выбора всего текстового содержимого элементов 'th' в первой строке таблицы
# columns = table_rows[0].xpath(".//th/text()")

# Создадим список
list_data = []

# найдем в строке текст
for row in table_rows:
   columns = row.xpath(".//th/text()")
   
   # Записываем спарсенные данные в список через словарь
   list_data.append({
      'Date': columns[0].strip(),
      'Open': columns[1].strip(),
      'High': columns[2].strip(),
      'Low': columns[3].strip(),
      'Close': columns[4].strip(),
      'Adj Close': columns[5].strip(),
      'Volume': columns[6].strip()
   })


# Все уберем в pandas
df = pd.DataFrame(list_data)
print(df)

# Сохранение данные в CSV
with open('data.csv', 'w', newline='', encoding='utf-8') as csvfile:
   csvwriter = csv.writer(csvfile)
   csvwriter.writerow(["Data", "Open", "High", "Low", "Close", "Adj Close", "Volume"])  # Заголовки столбцов
   csvwriter.writerows(list_data)



