# missing-line

### Задание

1. В корневой директории `/home/box` создать папку `sandbox` и в ней создать файл `jusan`.
2. В файл `jusan` записать слово `singularity` без новой линии в конце.

Пример для проверки:

```bash
box@dec74273716e: ~ $ cat jusan | wc -l
     0
```

---

### Ответ

Ошибка в примере. Если записать хоть что нибудь в файле то результат не может быть 0.

mkdir /home/box/sandbox
touch /home/box/sandbox/jusan
echo "singularity" > /home/box/sandbox/jusan