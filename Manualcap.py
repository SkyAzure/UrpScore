import csv
from io import BytesIO

import requests
from PIL import Image


def get_row(i):
    with open("/Users/sky/code/python/tust/16012new.csv", encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for h, rows in enumerate(reader):
            if h == i:
                stu_data = rows
    print(stu_data)
    return stu_data


def get_html(stu_data):
    number = stu_data['number']
    password = stu_data['Password']

    # cap_url用于获取验证码, login_url是登陆请求的URL, cj_url成绩
    login_url = "http://jwxtxs.tust.edu.cn:46110/j_spring_security_check"
    cap_url = 'http://jwxtxs.tust.edu.cn:46110/img/captcha.jpg'
    Allscore_url = 'http://jwxtxs.tust.edu.cn:46110/student/integratedQuery/scoreQuery/allTermScores/data'
    score_url = 'http://jwxtxs.tust.edu.cn:46110/student/integratedQuery/scoreQuery/thisTermScores/data'
    # User-Agent信息
    user_agent = r'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.94 Safari/537.36'
    # Headers信息
    head = {'User-Agnet': user_agent, 'Connection': 'keep-alive'}

    session = requests.Session()

    image = session.get(cap_url, headers=head).content
    bytes_io_obj = BytesIO()
    bytes_io_obj.write(image)
    img = Image.open(bytes_io_obj)
    img.show()
    captcha = input("请手动输入验证码:")

    # 登陆Form_Data信息
    post_data = {
        'j_username': number,
        'j_password': password,
        'j_captcha': captcha}
    time_data = {
        'zxjxjhh': '2018-2019-1-1',
        'kch': '',
        'kcm': '',
        'pageNum': '1',
        'pageSize': '30'
    }
    session.post(
        login_url,
        data=post_data,
        headers=head)

    score = session.post(
        Allscore_url,
        data=time_data,
        headers=head)
    if score.status_code == 200:
        return score.json()
    else:
        print(number + "error")


def parse_json(jsonq, stu_data):
    courseName = []
    if jsonq:
        items = jsonq.get('list').get('records')
        for item in items:
            courseName.append(item[11])
        print(courseName)

        # 获取本学期
        # for dirl in jsonq:
        #     items = dirl.get('list')
        # for item in items:
        #     if item.get('courseScore') == '':
        #         continue
        #     student = {'Name': stu_data['Name'],
        #                'number': stu_data['number'],
        #                'courseName': item.get('courseName'),
        #                'courseScore': item.get('courseScore'),
        #                'credit': item.get('credit')}
        #     print(student)


def main():
    for i in range(0, 5):
        stu_data = get_row(i)
        jsonb = get_html(stu_data)
        # print(json)
        parse_json(jsonb, stu_data)


if __name__ == "__main__":
    main()
