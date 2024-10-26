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
}
```

## bash
```bash
$ curl --user marketing:marketingP@ssword http://example.com:8080/gifs/
<html>
<head><title>Index of /gifs/</title></head>
<body>
<h1>Index of /gifs/</h1><hr><pre><a href="../">../</a>
<a href="__MACOSX/">__MACOSX/</a>                                          24-Oct-2024 13:09                   -
<a href="dancing.gif">dancing.gif</a>                                        24-Oct-2024 13:09              253794
<a href="jam.gif">jam.gif</a>                                            24-Oct-2024 13:09              471720
<a href="sad.gif">sad.gif</a>                                            24-Oct-2024 13:09             3605836
</pre><hr></body>
</html>
```