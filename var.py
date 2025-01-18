import smtplib
import os
from dotenv import dotenv_values
auth = dotenv_values()

friend= 'Иван'
my_name= 'Кудратилла'
website= 'dvmn.org'
mail_from= 'devmanorg@yandex.ru'
mail_to= 'ken.mcc@yandex.ru'

letter= """\
From: {3}
To: {4}
Subject: Приглашение!
Content-Type: text/plain; charset="UTF-8";

Привет, {0}! {1} приглашает тебя на сайт {2}!

{2} — это новая версия онлайн-курса по программированию. 
Изучаем Python и не только. Решаем задачи. Получаем ревью от преподавателя. 

Как будет проходить ваше обучение на {2}? 

→ Попрактикуешься на реальных кейсах. 
Задачи от тимлидов со стажем от 10 лет в программировании.
→ Будешь учиться без стресса и бессонных ночей. 
Задачи не «сгорят» и не уйдут к другому. Занимайся в удобное время и ровно столько, сколько можешь.
→ Подготовишь крепкое резюме.
Все проекты — они же решение наших задачек — можно разместить на твоём GitHub. Работодатели такое оценят. 

Регистрируйся → {2}  
На курсы, которые еще не вышли, можно подписаться и получить уведомление о релизе сразу на имейл.""".format(friend, my_name, website, mail_from, mail_to)

letter = letter.encode("UTF-8")

server = smtplib.SMTP_SSL('smtp.yandex.ru:465')
server.login(auth['LOGIN'], auth['PASS'])
server.sendmail(mail_from, mail_to, letter)
server.quit()
