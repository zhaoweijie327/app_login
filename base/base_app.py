'''
封装driver基类和常用操作
'''
import base64
import os

from selenium.webdriver.support.wait import WebDriverWait
from utils_app import App_DriverUtils

BAS_URL = os.path.abspath(os.path.dirname(__file__))

class App_DriverBase:

    def __init__(self):
        self.driver = App_DriverUtils.app_open_driver()

        # 封装单个元素定位方法
    def find_element(self, loc, tag=3, waittime=10, sousuotime=1.0):
        if tag == 1:
            '''
            # 封装单个元素定位方法
            :param loc:
            :return:
            '''
            element = self.driver.find_element(*loc)

        elif tag == 2:
            '''
            # 封装一组元素定位方法
            :param loc: 元素
            :return:
            '''
            element = self.driver.find_elements(*loc)

        elif tag == 3:
            '''
            显示等待单个元素方法
            :param loc: 元素
            :param waittime:
            :param sousuotime:
            :return:
            '''
            element = WebDriverWait(self.driver, waittime, sousuotime).until(lambda x: x.find_element(*loc))

        else:
            '''
            # 封装显示等待一组元素定位方法
            :param loc:  元素
            :param waittime:
            :param sousuotime:
            :return:
            '''
            element = WebDriverWait(self.driver, waittime, sousuotime).until(lambda x: x.find_elements(*loc))
        return element


class App_DriverHandles:

    def find_send_keys(self,element,text):
        '''
        输入框输入方法
        :param element:
        :param text:
        :return:
        '''
        element.clear() # 清除内容
        element.send_keys(text) # 输入内容

    def find_click(self,element):
        '''
        点击操作
        :param element:
        :return:
        '''
        element.click()

    def find_text(self,element):
        '''
        获取信息
        :param element:
        :return:
        '''
        return element.text

    def find_install_app(self,driver,apk_name,path='/apk'):
        '''
        安装手机app方法
        :param driver: 驱动
        :param apk_name: apk名称
        :param path: 存放apk文件路径
        :return:
        '''
        apk_path = BAS_URL + path + apk_name
        driver.install_apk(apk_path)

    def find_remove_app(self,driver,apk_name):
        '''
        卸载app操作
        :param driver: 驱动
        :param apk_name: apk名称
        :return:
        '''
        driver.remove_app(apk_name)

    def find_is_app_installed(self,driver,apk_name):
        '''
        判断app是否存在
        :param driver: 驱动
        :param apk_name: apk名称
        :return:
        '''
        return driver.is_app_installed(apk_name)

    def find_push_app(self,driver,data,houzhui=None):
        '''
        上传操作
        :param driver: 驱动
        :param data: 文件
        :param houzhui: 后缀
        :return:
        '''
        data = data
        data_file = str(base64.b64decode(data.encode('utf-8')),'utf-8')
        if houzhui is None:
            driver.push_file("/sdcard/" + data ,data_file)
        else:
            driver.push_file("/sdcard/" + data + houzhui, data_file)

    def find_pull_app(self,driver,path):
        '''
        从手机拉取文件数据
        :param driver: 驱动
        :param path: 路径+文件名
        :return:
        '''
        data = driver.pull_file(path)
        print('数据:',str(base64.b64decode(data.encode(data)),'utf-8'))

    def find_page_source(self,driver):
        '''
        打印手机当前屏幕内的XML元素结构
        :param driver: 驱动
        :return:
        '''
        return driver.page_source

    def find_sliding(self,element1,element2,driver,tag=1,swipe_tag=1,sliding_distance=2000):
        '''
        滑动的三种操作方法
        :param element1: 元素
        :param element2: 元素
        :param driver: 驱动
        :param tag: 默认值为1
        :param swipe_tag: 坐标滑动默认为1
        :param sliding_distance: 滑动距离 适用于第一个判断
        :return:
        '''
        if tag == 1:
            # 分辨率
            size = driver.get_window_size()
            # 宽
            width = size.get("width")
            # 高
            height = size.get("height")
            # 滑动 上下 高80 -高20 宽50   左右 宽80 -宽20 高50
            if swipe_tag == 1:
                # 向上滑动
                driver.swipe(width * 0.5, height * 0.8, width * 0.5, height * 0.2, sliding_distance)
            if swipe_tag == 2:
                # 向下滑动
                driver.swipe(width * 0.5, height * 0.2, width * 0.5, height * 0.8, sliding_distance)
            if swipe_tag == 3:
                # 向左滑动
                driver.swipe(width * 0.8, height * 0.5, width * 0.2, height * 0.5, sliding_distance)
            if swipe_tag == 4:
                # 向右滑动
                driver.swipe(width * 0.2, height * 0.5, width * 0.8, height * 0.5, sliding_distance)
        elif tag == 2:
            '''
            不用坐标，直接用元素滑动
            '''
            save = element1  # 取起点
            bo = element2  # 取终点
            driver.drag_and_drop(save,bo)
        else:
            '''
            不用坐标，直接用元素滑动
            '''
            save = element1  # 取起点
            bo = element2  # 取终点
            driver.scroll(save, bo)

    def find_background(self,driver,min=5):
        '''
        从后台返回到前台操作
        :param driver: 驱动
        :param min: 秒
        :return:
        '''
        driver.background_app(min)




