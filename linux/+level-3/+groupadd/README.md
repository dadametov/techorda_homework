# groupadd

Суперпользователь может создавать группы из командной строки с помощью команды `groupadd`.

### Полезное

- Введите команду `groupadd` в терминале для получения списка всех флагов

### Задание

1. Создайте группу `kings`.
2. Создать учетную запись `john` c полным именем `John Cena`, с домашней директорией `/home/john` и паролем `myTimeIsNoW!`.
3. Установить основную группу (см. `флаг --user-group`) `john`.
4. Добавьте `john` в дополнительную группу `kings`.
5. Зайдите в систему как пользователь `john`.
6. Создайте в домашнем каталоге файл `config-john.txt` с содержимым `success: true`.
7. Временно назначьте группу `kings` как основную.
8. Создайте в домашнем каталоге файл `config-kings.txt` с содержимым `success: true`.

---

### Ответ

sudo groupadd kings
sudo useradd -m -d /home/john -c "John Cena" -s /bin/bash --user-group john
echo "john:myTimeIsNoW!" | sudo chpasswd
sudo usermod -aG kings john
su - john
echo "success: true" > ~/config-john.txt
newgrp kings
echo "success: true" > ~/config-kings.txt
