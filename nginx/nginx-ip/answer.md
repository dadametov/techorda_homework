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

```

## bash
```bash
$ curl -H "Host: example.com" -i http://localhost:8080/secret_word
HTTP/1.1 404 Not Found
Server: nginx/1.20.1
Date: Thu, 24 Oct 2024 16:30:51 GMT
Content-Type: text/html
Content-Length: 153
Connection: keep-alive

<html>
<head><title>404 Not Found</title></head>
<body>
<center><h1>404 Not Found</h1></center>
<hr><center>nginx/1.20.1</center>
</body>
</html>

```