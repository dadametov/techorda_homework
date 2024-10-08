# useradd-middle

### Полезное

- Команда `su` для того, чтобы зайти как другой пользователь. Обычно используют с флагом `-l`.
- [Про команду "su"](https://www.tecmint.com/difference-between-su-and-su-commands-in-linux/)

### Задание

1. Создать учетную запись с именем пользователя `murat` и полным именем `Murat Serik`.
2. Установите оболочку по умолчанию (англ. "default shell", см. `флаг -s`) - `/bin/sh`.
3. Установите пользователю домашний каталог (см. `флаг -m`).
4. Установить основную группу (см. `флаг -g`) `bin`.
5. Установить пароль пользователю `murat` - `H3l70!vv0r7d`.
6. Зайдите в систему как пользователь `murat` и создайте в домашнем каталоге файл `config.txt` с содержимым:

```
success: true
```

---

### Ответ

sudo useradd -m -s /bin/sh -g bin -c "Murat Serik" murat
echo "murat:H3l70!vv0r7d" | sudo chpasswd
su - murat
echo "success: true" > ~/config.txt
