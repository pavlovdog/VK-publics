# VK-publics
Скрипт поможет вам раскрутить свой паблик ВК. 
Умеет автоматом собирать картиночки с постов разных групп ВК и постить их на вашу страницу.

ОПИСАНИЕ

1) main.py

Логика приложения, авторизация, постинг, запросы к VK API, обновление comm.txt.

2) Parse.py

Единственная функция, которая парсит пост ВК, работает только с постами, которые состоят из одной едиственной картинки,
на всё остальное возвращает None.

3) comm.txt

Каждая строка состоит из имени паблика и числа постов, которые на нём есть в данный момент. Когда разница между нынешним числом
постов и тем, что записаны в comm.txt составят 30 или больше, эта разница обрабатывается. Потом в comm.txt обновляется число постов.