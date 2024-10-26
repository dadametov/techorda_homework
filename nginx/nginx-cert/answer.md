# Ответ
## Config Nginx
```bash
server {
    listen 8080;
    server_name example.com;

    location / {
        root /usr/share/nginx/html/techorda;
        index index.html;
    }

    location /images/ {
        auth_basic "Protected Images";
        auth_basic_user_file /etc/nginx/.htpasswd_desig;
        alias /usr/share/nginx/html/techorda/cats/;
        autoindex on;
    }

    location /gifs/ {
        auth_basic "Protected Gifs";
        auth_basic_user_file /etc/nginx/.htpasswd_marketing;
        alias /usr/share/nginx/html/techorda/gifs/;
        autoindex on;
    }

    location /api {
        rewrite ^/api(.*)$ $1 break;
        proxy_pass http://localhost:9090;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        error_log /var/log/nginx/api_proxy_error.log debug;
    }


    location /secret_word {
        allow 192.0.0.0/20;
        deny 192.0.0.1;
        deny all;
        return 203 'jusan-nginx-ip';
        add_header Content-Type text/plain;
    }

}

################ ssl

server {
    listen 443 ssl;
    server_name jusan.kz;

    ssl_certificate /etc/nginx/ssl/track-devops.crt;       # Укажите путь к сертификату
    ssl_certificate_key /etc/nginx/ssl/track-devops.key;   # Укажите путь к приватному ключу
    ssl_dhparam /etc/nginx/ssl/dhparam.pem;          # Укажите путь к файлу dhparam

    location /secret_word {
        default_type text/plain;
        return 201 'jusan-nginx-cert';
    }
}

```

## bash
```bash
$  curl -H "Host: jusan.kz" -k https://localhost/secret_word
jusan-nginx-cert
```