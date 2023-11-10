# Just for fun!
Простой эхо бот, для демонстрации возможностей деплоя не сервер


## Как сделать запуск бота в виде сервиса в Ubuntu
### 1 ШАГ
nano /lib/systemd/system/just4funbot.service

### 2 ШАГ
```
[Unit]
Description=Just for fun bot
After=network.target

[Service]
EnvironmentFile=/etc/environment
ExecStart=/root/just_for_fun_bot/venv/bin/python app.py
ExecReload=/root/just_for_fun_bot/venv/bin/python app.py
WorkingDirectory=/root/just_for_fun_bot
KillMode=process
Restart=always
RestartSec=5

[Install]
WantedBy=multi-user.target
```
### 3 ШАГ
```
$ systemctl enable just4funbot
$ systemctl start just4funbot
```
