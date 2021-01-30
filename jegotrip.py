import  requests
import pprint
import os

class JegoTrip():
    user_id : str

    def __init__(self, user_id):
        self.user_id = user_id
    def task(self):
        resp = requests.get(f'http://task.jegotrip.com.cn:8080/app/tasks?userid={self.user_id}')
        data = resp.json()
        # pprint.pprint(data)
        return data['rtn']['tasks']

    def sign(self, task_id) -> bool:
        resp = requests.post('http://task.jegotrip.com.cn:8080/app/sign', 
        json={
            'userid':self.user_id,
            'taskid':task_id
        },
        headers={'Content-Type':'application/json;charset=utf-8',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 source/jegotrip'
        })
        
        data = resp.json()
        # pprint.pprint(data)
        return data['result']
        

if __name__ == '__main__':
    _user_id = os.environ['USERID']
    cli = JegoTrip(_user_id)
    for task in cli.task().get('日常任务', []):
        if task.get('name') == '每日签到奖励' and task.get('triggerAction') == '签到':
            print('签到', "成功" if cli.sign(task['id']) else "失败！！！")
        