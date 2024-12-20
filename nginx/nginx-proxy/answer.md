# Ответ
## Config Nginx
```bash
server {
    listen 80;
    server_name _;

    location / {
        root /usr/share/nginx/html/techorda;
        index index.html;
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
## App.py on 9090 port
```bash
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello():
    return "Whatsup!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9090, debug=True)
```

## bash
```bash
$ curl http://localhost/api
Whatsup!
```