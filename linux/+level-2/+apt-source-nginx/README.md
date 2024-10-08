# apt-source-nginx

В этом уроке установим nginx из официального репозитория разработчика.

### Полезное

- [официальный nginx инструкция](https://docs.nginx.com/nginx/admin-guide/installing-nginx/installing-nginx-open-source/#installing-a-prebuilt-debian-package-from-the-official-nginx-repository)

### Задание

1. Обновите (англ. "update") базу пакетов.
2. Установить (англ. "install") nginx из официального репозитория.

Подсказки:

1. Чтобы узнать `CODENAME`

```bash
cat /etc/os-release
```

---

### Ответ
sudo apt update

sudo echo > /etc/yum.repos.d/nginx.repo <<EOF
[nginx]
name=nginx repo
baseurl=http://nginx.org/packages/centos/\$releasever/\$basearch/
gpgcheck=1
enabled=1
gpgkey=http://nginx.org/keys/nginx_signing.key
EOF

sudo apt install nginx -y

