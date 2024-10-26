# Ответ
## bash
```bash
[root@centos ~]# ufw allow 80/tcp
Skipping adding existing rule
Skipping adding existing rule (v6)
[root@centos ~]#
[root@centos ~]# ufw allow 443/tcp
Skipping adding existing rule
Rule added (v6)
[root@centos ~]# ufw status
Status: active

To                         Action      From
--                         ------      ----
SSH                        ALLOW       Anywhere
224.0.0.251 mDNS           ALLOW       Anywhere
80/tcp                     ALLOW       Anywhere
443/tcp                    ALLOW       Anywhere
SSH (v6)                   ALLOW       Anywhere (v6)
ff02::fb mDNS              ALLOW       Anywhere (v6)
80/tcp (v6)                ALLOW       Anywhere (v6)
```