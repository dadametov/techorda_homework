docker run -d --name jusan-docker-bind -p 7777:80 -v ./nginx.conf:/etc/nginx/nginx.conf nginx:mainline
chmod +x tester-docker-bind.sh
bash ./tester-docker-bind.sh