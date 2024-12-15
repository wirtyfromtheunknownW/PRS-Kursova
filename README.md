# PRS-Kursova

**Документация на курсовата работа**

**I. Задание**

1. Намерете функционалност, свързана с XML, която няма директен аналог в JSON.
   - Избрана функционалност: използване на namespace в XML.

2. Създайте програма, която да обработва XML файла.
3. Реализирайте уеб услуга, която изпраща обработения XML файл след автентикация.

---

**II. Кратко описание на решението и технологиите**

- Проектът се базира на **Python** и **Django**. Django се използва за реализация на уеб услугата с вградена автентикация.

- Библиотеката **lxml** се използва за обработка на XML файла, включително поддръжка на namespace.

---

**III. Описание на проекта**

1. **XML файл**:
   Използва се XML с namespace, за да се отделят различните категории книги. Ексампълно съдържание:

   ```xml
   <?xml version="1.0" encoding="UTF-8"?>
   <library xmlns:fiction="http://example.com/fiction" xmlns:nonfiction="http://example.com/nonfiction">
       <fiction:book>
           <fiction:title>The Great Gatsby</fiction:title>
           <fiction:author>F. Scott Fitzgerald</fiction:author>
           <fiction:year>1925</fiction:year>
       </fiction:book>
       <nonfiction:book>
           <nonfiction:title>Sapiens: A Brief History of Humankind</nonfiction:title>
           <nonfiction:author>Yuval Noah Harari</nonfiction:author>
           <nonfiction:year>2011</nonfiction:year>
       </nonfiction:book>
   </library>
   ```

2. **Python скрипт**:
   - Парсира XML файла.
   - Добавя нова книга към файла.
   - Запазва промените обратно в XML файла.

   Примерен код:
   ```python
   from lxml import etree as ET

   xml_file = "library.xml"
   namespaces = {
       "fiction": "http://example.com/fiction",
       "nonfiction": "http://example.com/nonfiction"
   }

   def parse_xml(file_path):
       tree = ET.parse(file_path)
       root = tree.getroot()
       return tree, root

   def add_book(root, namespace, title, author, year):
       book = ET.Element(f"{{{namespace}}}book")
       ET.SubElement(book, f"{{{namespace}}}title").text = title
       ET.SubElement(book, f"{{{namespace}}}author").text = author
       ET.SubElement(book, f"{{{namespace}}}year").text = year
       root.append(book)

   tree, root = parse_xml(xml_file)
   add_book(root, namespaces["fiction"], "1984", "George Orwell", "1949")
   tree.write(xml_file, pretty_print=True, xml_declaration=True, encoding="UTF-8")
   ```

3. **Django уеб услуга**:
   - Използва се декоратор `@login_required` за защита на услугата.
   - Изпраща обработения XML файл на потребителите след вход в системата.

   Примерен изглед:
   ```python
   from django.http import HttpResponse
   from django.contrib.auth.decorators import login_required
   import os

   @login_required
   def download_xml(request):
       file_path = os.path.join(os.path.dirname(__file__), 'library.xml')
       with open(file_path, 'r', encoding='utf-8') as file:
           response = HttpResponse(file.read(), content_type='application/xml')
           response['Content-Disposition'] = 'attachment; filename="library.xml"'
           return response
   ```

4. **Инструкции за стартиране на проекта на друг компютър**:
   За да направите проекта функционален на друг компютър, следвайте тези стъпки:
   
   - **Клониране на проекта:**
     ```bash
     git clone <URL_на_репозиторито>
     cd <име_на_папката>
     ```

   - **Създаване на виртуална среда:**
     ```bash
     python -m venv venv
     source venv/bin/activate  # За Windows: venv\Scripts\activate
     ```

   - **Инсталиране на зависимостите:**
     ```bash
     pip install -r requirements.txt
     ```

   - **Прилагане на миграциите:**
     ```bash
     python manage.py migrate
     ```

   - **Стартиране на уеб сървъра:**
     ```bash
     python manage.py runserver
     ```

http://127.0.0.1:8000/admin/ - за да стигна до логин страница 
http://127.0.0.1:8000/xml/download - за да сваля файла след автентикация 

---

**IV. Заключение**

Курсовата работа показва успешно реализация на XML обработка и уеб услуга с автентикация. Django позволява бърза имплементация и сигурност при управление на достъпа до услугата, а lxml осигурява гъвкавост при обработка на XML файлове.

