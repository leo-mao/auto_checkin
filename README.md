# 无忧行自动签到获取无忧币

今天签到![无忧行自动签到](https://github.com/leo-mao/auto_checkin/workflows/autocheckin/badge.svg)

---
### 使用方法
1. 利用`stream app`通过mitm在`无忧行`手机客户端抓包，获取payload中的userid
2. clone本项目
3. 在项目的`Settings` -> `Environment` 中新建一个环境`autocheckin-py3.9`, 并在其中的`Environment Secrets`中新建一个名为`USERID`的环境变量，并填入获取到`的userid`，每天北京时间`00:05`会自动签到获取无忧币



> 手动测试本workflow可以通过 `Actions`->左侧标签栏中`autocheckin` -> 右侧窗口中`run wokrflow` -> `run workflow`，测试是否正确部署
 
 
 参考: 
 https://github.com/fengjueming/jegotrip_autosign

