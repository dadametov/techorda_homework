 curl --output jusan-docker-mount.conf https://stepik.org/media/attachments/lesson/686238/jusan-docker-mount.conf
 curl --output jusan-docker-mount.zip https://stepik.org/media/attachments/lesson/686238/jusan-docker-mount.zip
 unzip jusan-docker-mount.zip
 docker run -d --name jusan-docker-mount -p 9999:80 -v ./jusan-docker-mount.conf:/etc/nginx/conf.d/jusan-docker-mount.conf -v ./jusan-docker-mount:/var/www/example nginx:mainline
 bash ./tester-docker-mount.sh
 