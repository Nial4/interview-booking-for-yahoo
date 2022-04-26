# This is a sample Python script.

import os
import time
import pickle
from time import sleep
from selenium import webdriver
import datetime
import smtplib
from email.mime.text import MIMEText
from email.utils import formatdate

# home page
damai_url = "https://www.saiyo-dr.jp/yj/MyPage/new_mypage.do"
# login page
login_url = "https://www.saiyo-dr.jp/yj/MyPage/new_mypage.do"
# check page
target_url = 'Is your booking page, have some 【満席】'



class Concert:
    def __init__(self):
        self.status = 0  # status
        self.login_method = 1  # {0:simulate login,1:Cookie login}
        self.driver = webdriver.Chrome(executable_path='/usr/lib/chromium-browser/chromedriver')

    def set_cookie(self):
        self.driver.get(damai_url)
        print("###Please click to log in###")
        while self.driver.current_url != 'https://www.saiyo-dr.jp/yj/MyPage/new_mypage.do?action=init':
            sleep(3)
        print("###success###")
        pickle.dump(self.driver.get_cookies(), open("cookies.pkl", "wb"))
        print("###Cookie saved!###")
        self.driver.get(target_url)

    # def get_cookie(self):
    #     try:
    #         cookies = pickle.load(open("cookies.pkl", "rb"))  # 载入cookie
    #         for cookie in cookies:
    #             cookie_dict = {
    #                 'domain': '.saiyo-dr.jp',
    #                 'name': cookie.get('name'),
    #                 'value': cookie.get('value')
    #             }
    #             self.driver.add_cookie(cookie_dict)
    #         print('###载入Cookie###')
    #     except Exception as e:
    #         print(e)

    def login(self):
        if self.login_method == 0:
            self.driver.get(login_url)
            # 载入登录界面
            print('###start logging in###')

        elif self.login_method == 1:
            # if not os.path.exists('cookies.pkl'):
            #     # 如果不存在cookie.pkl,就获取一下 If cookie.pkl does not exist, get it
            #     self.set_cookie()
            # else:
            #     self.driver.get(target_url)
            #     self.get_cookie()
            self.set_cookie()

    def enter_concert(self):
        """Open browser"""
        print('###Open browser，Enter###')
        # self.driver.maximize_window()           # 最大化窗口
        # 调用登陆
        self.login()  # Login function
        self.driver.refresh()  # refresh function
        self.status = 2  # Login success status
        print("###登录成功###")

    def choose_ticket(self):
        last = 65
        if self.status == 2:  # Login successful entry
            while True:
                print("=" * 30)
                print("###Start testing for reservations###")
                textA_1 = self.driver.find_elements_by_css_selector("form[name='listBody'] tr") 
                if len(textA_1) == last:
                    print("No appointment time yet, go to sleep:"+ str(last) +"  ## "+ str(datetime.datetime.today()))
                elif len(textA_1) < last:
                    last = len(textA_1)
                    print("It seems to be reduced, but there is no appointment time yet, go to sleep:"+ str(last) +"  ## "+ str(datetime.datetime.today()))
                else:
                    print("time available, Chance!!")
                    print(len(textA_1))
                    break
                sleep(300)
                self.driver.refresh()

    def finish(self):
        self.driver.quit()

    def mail_me(self):
        print("make a mail or TG message")
        sendAddress = 'xxxxxx@gmail.com'
        password = 'xxxxxx'

        subject = '[test]time available!!!'
        bodyText = 'test text'
        fromAddress = 'xxxxxx@gmail.com'
        toAddress = ["xxxxxx@gmail.com", "xxxxxx@outlook.com"]

        # SMTPサーバに接続
        smtpobj = smtplib.SMTP('smtp.gmail.com', 587)
        smtpobj.starttls()
        smtpobj.login(sendAddress, password)

        # メール作成
        msg = MIMEText(bodyText)
        msg['Subject'] = subject
        msg['From'] = fromAddress
        msg['Date'] = formatdate()

        # 作成したメールを送信
        smtpobj.sendmail(fromAddress, toAddress, msg.as_string())
        smtpobj.close()


if __name__ == '__main__':
    try:
        con = Concert()
        con.enter_concert()  # Open browser
        con.choose_ticket()  # start checking
        con.mail_me()        # make some message to u

    except Exception as e:
        print(e)
        con.finish()
