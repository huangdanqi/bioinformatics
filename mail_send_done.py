#reference
'''
https://www.jb51.net/article/140553.htm
https://zhuanlan.zhihu.com/p/24180606
https://www.runoob.com/python/python-email.html
https://blog.csdn.net/qq_40419501/article/details/116939177
https://www.cnblogs.com/languid/p/10732479.html
https://blog.csdn.net/zeeeitch/article/details/7256736
'''

import os
from smtplib import SMTP_SSL 
from email.mime.text import MIMEText 
from email.header import Header 
import time
import smtplib
#设置服务器所需信息
#163邮箱服务器地址
mail_host = 'smtp.qq.com'  
#163用户名
mail_user = 'xxxx@qq.com'  
#密码(部分邮箱为授权码) 
mail_pass = 'xxxxxxxxxxx'   
#邮件发送方邮箱地址
sender = 'xxxx@qq.com'  
#邮件接受方邮箱地址，注意需要[]包裹，这意味着你可以写多个邮件地址群发
receivers = ['danqi_28@outlook.com']  

#judge=os.system('ps -ef|grep gse_gsm_new_bern_unique_4.py | grep -v grep |wc -l' ) 
ps_string = os.popen('ps -ax | grep '+'gse_gsm_new_bern_unique_4.py'+'|grep -v grep  ','r').read()
ps_strings = ps_string.strip().split('\n')
bern_run=os.popen('wc -l gse_gsm_new_bern_unique_v4_log_time').read()
bern_run_num=bern_run.strip().split('\n')
if len(ps_strings[0]) > 0:
    #设置email信息
    #邮件内容设置'
    text='BNER DOES WELL!!!'+'\n'+str(bern_run_num[0])
    message = MIMEText(text,'plain','utf-8')
    #邮件主题       
    message['Subject'] = 'BERN GOOD NEWS!!!' 
    #发送方信息
    message['From'] = sender 
    #接受方信息     
    message['To'] = receivers[0]  
    #登录并发送邮件
    try:
        smtpObj = smtplib.SMTP() 
        #连接到服务器
        smtpObj.connect(mail_host,25)
        #登录到服务器
        smtpObj.login(mail_user,mail_pass) 
        #发送
        #smtpObj.sendmail(
            #sender,receivers,message.as_string()) 
        smtpObj.sendmail(sender, receivers, message.as_string()) 
        #退出
        smtpObj.quit() 
        print('success')
    except smtplib.SMTPException as e:
        print('error',e) #打印错误   

def spy():
    while True:
        #judge=os.system('ps -ef|grep gse_gsm_new_bern_unique_4.py | grep -v grep |wc -l' ) 
        ps_string = os.popen('ps -ax | grep '+'gse_gsm_new_bern_unique_4.py'+'|grep -v grep  ','r').read()
        ps_strings = ps_string.strip().split('\n')
        time.sleep(10)
        if len(ps_strings[0]) > 0:
            pass
        else:
            #设置email信息
            #邮件内容设置
            bern_run=os.popen('wc -l gse_gsm_new_bern_unique_v4_log_time').read()
            bern_run_num=bern_run.strip().split('\n')
            text_2='BERN DOES BREAKDOWN!!!'+'\n'+str(bern_run_num[0])
            message = MIMEText(text_2,'plain','utf-8')
            #邮件主题       
            message['Subject'] = 'BAD NEWS!!!' 
            #发送方信息
            message['From'] = sender 
            #接受方信息     
            message['To'] = receivers[0]  
            #登录并发送邮件
            try:
                smtpObj = smtplib.SMTP() 
                #连接到服务器
                smtpObj.connect(mail_host,25)
                #登录到服务器
                smtpObj.login(mail_user,mail_pass) 
                #发送
                #smtpObj.sendmail(
                    #sender,receivers,message.as_string()) 
                smtpObj.sendmail(sender, receivers, message.as_string()) 
                #退出
                smtpObj.quit() 
                print('success')
            except smtplib.SMTPException as e:
                print('error',e) #打印错误      
            break
if __name__=='__main__':
    spy()


