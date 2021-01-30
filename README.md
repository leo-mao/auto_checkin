# 无忧行自动签到获取无忧币
今天签到状态![无忧行自动签到](https://github.com/leo-mao/auto_checkin/workflows/autocheckin/badge.svg)

### 使用方法
1. 在利`stream app`通过mitm手机客户端抓包，获取payload中的userid
2. clone本项目
3. 在项目的`settings` -> `Environment` 中新建一个环境`autocheckin-py3.9`, 并在其中的`Environment Secrets`中新建一个名为USERID的环境变量，并填入获取到的userid，每天北京时间00:05会自动签到
