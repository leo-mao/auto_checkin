import  requests
import pprint

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
        resp = requests.post('http://task.jegotrip.com.cn:8080/app/sign', json={
            'userid':self.user_id,
            'taskid':task_id
        })
        
        data = resp.json()
        # pprint.pprint(data)
        return data['result']
        

if __name__ == '__main__':
    cli = JegoTrip('abcd')
    for task in cli.task().get('日常任务', []):
        if task.get('name') == '每日签到奖励' and task.get('triggerAction') == '签到':
            print('签到', "成功" if cli.sign(task['id']) else "失败！！！")
        