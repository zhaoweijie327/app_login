import json
import os
import time

import allure
import yaml

from appium import webdriver
from selenium.webdriver.common.by import By

'''
常用工具类
'''

BAS_URL = os.path.abspath(os.path.dirname(__file__))

class App_DriverUtils:

    __driver = None

    @classmethod
    def app_open_driver(cls,platformname=None,platformversion='',devicename=None,apppackage=None,appactivity=None):
        '''
        打开驱动
        :param platformname: 测试平台名字
        :param platformversion: 测试平台对应版本,可以为空
        :param devicename: 设备名字，允许随便写
        :param apppackage: 测试app包
        :param appactivity: 测试app启动名
        :return:
        '''
        # driver为空时
        if cls.__driver == None:
            app_data = {
                # 测试平台名字
                'platformName': platformname,
                # 测试平台对应版本,可以为空
                'platformVersion': platformversion,
                # 设备名字，允许随便写
                'deviceName': devicename,
                # 测试app包
                'appPackage':apppackage,
                # 测试app启动名
                'appActivity':appactivity
            }
            url = "http://127.0.0.1:4723/wd/hub"
            cls.__driver = webdriver.Remote(url,app_data)
            return cls.__driver
        else:
            cls.__driver = None

    @classmethod
    def app_close_driver(cls):
        '''
        关闭驱动
        :return:
        '''
        if cls.__driver is not None:
            cls.app_open_driver().quit()
            cls.__driver = None

# 数据驱动
class DataDriven:

    def data_driver(self,folder='/data',data_num=1):
        # 读取文件
        with open(BAS_URL + folder ,'r',encoding='utf-8') as file:
            if data_num == 1:
                # 转化json格式
                data_json = json.load(file)
            else:
                # 转换yaml格式
                data_json = yaml.safe_load(file)
            return data_json

    def create_dict(self,path='/data',data_num=1):
        '''
        通过字典形式获取   {
                                "xxx":{

                                            }
                                }
        :return:
        '''
        # 创建列表
        data_dict = []
        # 获取json数据
        data = self.data_driver(path,data_num)
        for i in data.values():
            # 把值保存到列表
            data_dict.append(list(i.values()))
        # 返回列表
        return data_dict

    def create_list(self,path='/data',data_num=1):
        '''
                通过字典形式获取   [
                                          {
                                            "xxx": "xxx",
                                            "xxx": {
                                              "xxx": "xxx",
                                            }
                                        ]
                :return:
                '''
        # 创建列表
        data_list = []
        # 获取json数据
        data = self.data_driver(path,data_num)
        for i in data:
            # 把值保存到列表
            data_list.append(list(i.values()))
        # 返回列表
        return data_list

    def create_values(self,values,path='/data',data_num=1):
        '''
                获取单个键里面的值   {
                                "xxx":{

                                            }
                                }
                :return:
                '''
        data_list = []
        # 获取json数据
        data = self.data_driver(path,data_num)
        # 获取值
        data_values = data.get(values)
        # 值保存在列表
        data_list.append(list(data_values.values()))
        # 返回列表
        return data_list

def get_toast(self, mess):
    """
    获取taost提示消息
    :param mess: toast的xpath拼接文本
    :return:
    """
    """注意： 当前appium1.17.1版本可以直接获取toast消息，之前版本不可以 需要Uiautomator2参数"""
    toast_xpath = (By.XPATH, "//*[contains(@text,'%s')]" % mess)
    # 定位toast
    return self.search_ele(toast_xpath, timeout=3, poll_frequency=0.3).text

def screen_image(self, name="截图"):
    """
    截图
    :param name: 报告中图片名字
    :return:
    """
    # 图片名字
    png_name = BAS_URL + "./Image/%d.png" % int(time.time())

    self.driver.get_screenshot_as_file(png_name)

    with open(png_name, "rb") as f:
        allure.attach(f.read(), name, attachment_type=allure.attachment_type.PNG)

class num :

    def num1(self,tag=1,x=5):
        if tag == 1:
            y = x + 3
        elif tag == 2:
            y = 5 + 4
        else:
            y = 1 + 5
        return y
    def num2(self):
        return self.num1(tag=2)

n = num()
print(n.num2())