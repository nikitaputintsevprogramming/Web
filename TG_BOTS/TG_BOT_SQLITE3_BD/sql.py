import sqlite3
import re

# Для добавления товара через /add прямо через бота
async def add(item):
    connect = sqlite3.connect('db.db')
    # Устанавливаем курсор
    cursor = connect.cursor()
    # Добавляем item в список
    m = []
    m.append(item)
    # Отправка запроса, чтобы вставить значение item в таблицу shop -> m попадает вместо '?'
    cursor.execute('INSERT INTO shop VALUES(?)', m)
    connect.commit()
    # Закрываем наш курсор
    cursor.close()

# Список (отображение в стоблике при покупке для выбора)
async def buy():
    connect = sqlite3.connect('db.db')
    cursor = connect.cursor()
    # * означает, что мы вытаскиваем все(каждый товар) из таблицы
    query = 'SELECT * FROM shop'
    cursor.execute(query)
    # Сохраняем вытащенные товары в переменной data
    data = cursor.fetchall()
    m = []

    # Каждый товар сохраняем в список через цикл
    for i in data:
        m.append(i)

    l = len(data)
    g = []

    # Чтобы каждый товар не выглядел, как текст мы также проходимся по ним и изменяем каждый элемент
    for i in range(l):
        a = re.sub('|\(|\'|\,|\)', '', str(m[i]))
        g.append(a)
    c = []

    # и сохраняем все проформатированное в новом списке под названием 'g' 
    for i in g:
        # Каждый из товаров высвечиваем нановой строке
        q = i + '\n'
        # и добавляем все в новый список 'c'
        c.append(q)

    v = '\n'.join(c)
    return v