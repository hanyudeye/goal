# 模拟用户登陆163邮箱，作为Python使用Selenium的简单案例介绍

#导入时间库和selenium库
import time
from selenium import webdriver
#加载Chrome
browser = webdriver.Chrome()
#登陆163邮箱
browser.get('https://mail.163.com')
#程序暂停3秒钟，等待页面完全加载
time.sleep(3)
#分别在user和key中输入自己的用户名和邮箱密码
user = 'XXXXXX'
key = 'kkkkkkkk'

browser.switch_to.frame(0)
#模拟在网页上输入用户名
browser.find_element_by_name("email").clear()
browser.find_element_by_name("email").send_keys(user)
#模拟在网页上输入邮箱密码
browser.find_element_by_name("password").clear()
browser.find_element_by_name("password").send_keys(key)
#模拟在网页上点击【登陆】按钮
browser.find_element_by_id("dologin").click()