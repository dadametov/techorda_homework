curl --output jusan-dockerfile.conf https://stepik.org/media/attachments/lesson/686238/jusan-dockerfile.conf
curl --output jusan-dockerfile.zip https://stepik.org/media/attachments/lesson/686238/jusan-dockerfile.zip
unzip jusan-dockerfile.zip
docker build -t nginx:jusan-dockerfile .
docker images|grep jusan-dockerfile