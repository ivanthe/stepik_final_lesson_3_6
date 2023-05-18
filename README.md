# STEPIK_Итоговое задание раздела 3 по курсу Автоматизация тестирования с помощью Selenium и Python.


## :open_book: Задание:

1) Создать GitHub-репозиторий, в котором будут лежать файлы conftest.py и test_items.py.
2) Добавить в файл conftest.py обработчик, который считывает из командной строки параметр language.
3) Реализовать в файле conftest.py логику запуска браузера с указанным языком пользователя. Браузер должен объявляться в фикстуре browser и передаваться в тест как параметр.
4) В файл test_items.py написать тест, который проверяет, что страница товара на сайте содержит кнопку добавления в корзину. Тестовая страница: http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/.
5) Тест должен запускаться с параметром language следующей командой:
       pytest --language=es test_items.py
6) Тест должен проходить успешно. Достаточно, чтобы код работал только для браузера Сhrome.

## :heavy_check_mark: Критерии прохождения задания

1) Тест можно запустить командой задав один из доступных языков, например, pytest --language=es. Тест должен успешно проходить.
2) Проверка работоспособности кода для разных языков. 

    Например, для французкого (параметр для командной строки --language=fr). Проверка не автоматическая, пользователь визуально проверяет, что фраза на кнопке добавления в корзину выглядит так: "Ajouter au panier".
    В тесте должна быть задержка реализованная с помощью команды time.sleep(30) сразу после открытия ссылки. 
    
3) Браузер должен объявляться в фикстуре browser и передаваться в тест как параметр.
4) В тесте проверяется наличие кнопки добавления в корзину. Селектор кнопки является уникальным для проверяемой страницы. Есть assert.
5) Название тестового метода внутри файла test_items.py соответствует задаче. Название test_something не удовлетворяет требованиям.


## :hammer_and_wrench: Технологии и инструменты:

  <div>
  <img src="https://github.com/ElenaAngelcheva/ElenaAngelcheva/blob/main/img/logos/python.svg" title="Python" alt="Python" width="40" height="40"/>&nbsp;   
  <img src="https://github.com/ElenaAngelcheva/ElenaAngelcheva/blob/main/img/logos/pycharm.png" title="Pycharm" alt="Pycharm" width="40" height="40"/>&nbsp; 
  <img src="https://github.com/ElenaAngelcheva/ElenaAngelcheva/blob/main/img/logos/pytest.svg" title="Pytest" alt="Pytest" width="40" height="40"/>&nbsp;   
  <img src="https://github.com/ElenaAngelcheva/ElenaAngelcheva/blob/main/img/logos/selenium.svg" title="Selenium" alt="Selenium" width="40" height="40"/>&nbsp;
 </div>
 
 

## :heavy_check_mark: Результаты

1) Браузер объявляется в фикстуре <b>browser</b>.
2) В фикстуре реализовано возможность выбирать один из доступных языков (ru, en, fr, es, fi, pl и другие)
3) Дополнительно в фикстуре реализована возможность запуска одного из двух браузеров Chrome или FireFox (по умолчанию установлен Chrome)
4) Тест успешно проходит.
5) Тест падает с сообщением AssertMessage если кнопка не найдена (для проверки можно в ручную изменить название локатора). Сообщение NoSuchElementException не появляется.

  
## :computer: Локальный запуск

  1. Склонируйте репозиторий
  2. Запустите тест в командной строке
      - Пример команды запуска (браузер по умолчанию Chrome)    -  выбор языка (--language=<<user_language>>  ,где <b> <<user_language>> </b> может быть ru, en, fr, es, fi, pl и другие)
        ```
        pytest --language=es test_items.py
        ``` 

      - Пример команды запуска с выбором браузера Chrome или FireFox  -  (--browser_name=firefox   или   --browser_name=chrome)
        ```
        pytest --language=fr --browser_name=firefox test_items.py
        ```

 
