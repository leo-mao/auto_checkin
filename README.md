# 无忧行自动签到获取无忧币

今日签到![无忧行自动签到](https://github.com/leo-mao/auto_checkin/workflows/%E6%97%A0%E5%BF%A7%E8%A1%8C%E7%AD%BE%E5%88%B0/badge.svg)

---
### 使用方法
1. 利用`stream app`通过mitm在`无忧行`手机客户端抓包，获取payload中的userid
2. clone本项目
3. 在项目的`Settings` -> `Environment` 中新建一个环境`autocheckin-py3.9`, 并在其中的`Environment Secrets`中新建一个名为`USERID`的环境变量，并填入获取到`的userid`，每天北京时间`00:05`会自动签到获取无忧币



> 手动测试本workflow可以通过 `Actions`->左侧标签栏中`autocheckin` -> 右侧窗口中`run wokrflow` -> `run workflow`，脚步运行的输出会显示在`build`->`jegotrip 无忧行签到`一栏中，来测试是否正确部署，目前还不支持推送运行结果至外部
 
参考:   
https://gist.github.com/isombyt/6570c116416654cf905b72c75c59c9b7  
https://github.com/fengjueming/jegotrip_autosign  
https://ooxx.be/js/jegotrip.js  
