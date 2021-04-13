from appium.webdriver.common.touch_action import TouchAction

from utils_app import App_DriverUtils

'''
app模拟手势操作
'''
class TouchAction_App:

    def __init__(self):
        self.driver = App_DriverUtils.app_open_driver()

    def touchaction_app(self):
        '''
        实例化TouchAction
        :return:
        '''
        return TouchAction(self.driver)

    def touch_tap(self,element,tag=1):
        '''
        敲屏幕方法
        :param element: 元素
        :param tag: 默认值1
        :return:
        '''
        if tag == 1:
            # 利用元素定位敲击屏膜
            self.touchaction_app().tap(element).perform()
        else:
            # 利用坐标定位敲击屏膜
            more = element.location
            self.touchaction_app().tap(x=more.get('x'),y=more.get('y')).perform()

    def touch_press(self,element,tag=1):
        '''
        按屏幕
        :param element: 元素
        :param tag: 默认值1
        :return:
        '''
        if tag == 1:
            # 利用元素定位按屏膜
            self.touchaction_app().press(element).release().perform()
        else:
            # 利用坐标定位按屏膜
            more = element.location
            self.touchaction_app().press(x=more.get('x'),y=more.get('y')).release().perform()

    def touch_press_wait(self,element,tag=1,min=2000):
        '''
        按屏幕,等待操作
        :param element: 元素
        :param tag: 默认值1
        :param min: 默认值2000秒
        :return:
        '''
        if tag == 1:
            # 利用元素定位按屏膜
            self.touchaction_app().press(element).wait(min).release().perform()
        else:
            # 利用坐标定位按屏膜
            more = element.location
            self.touchaction_app().press(x=more.get('x'),y=more.get('y')).wait(min).release().perform()

    def touch_long_press(self,element,tag=1,min=2000):
        '''
        手指长按操作
        :param element: 元素
        :param tag: 默认值1
        :param min: 默认值2000秒
        :return:
        '''
        if tag == 1:
            # 利用元素定位按屏膜
            self.touchaction_app().long_press(element,duration=min).release().perform()
        else:
            # 利用坐标定位按屏膜
            more = element.location
            self.touchaction_app().long_press(x=more.get('x'),y=more.get('y'),duration=min).release().perform()

    def touch_move_to(self,element1,element2,tag=1,min=2000,min_min=200):
        if tag == 1:
            # 利用元素定位结合.press滑动操作
            self.touchaction_app().press(element1).wait(min).move_to(element2).release().perform()
        elif tag == 2:
            # 利用坐标定位结合.press滑动操作
            more = element1.location
            bo = element2.location
            self.touchaction_app().press(x=more.get('x'),y=more.get('y')).wait(min).move_to(x=bo.get('x'),y=bo.get('y')).release().perform()
        elif tag == 3:
            # 利用元素定位结合.long_press滑动操作
            self.touchaction_app().long_press(element1).wait(min).move_to(element2).release().perform()
        elif tag == 4:
            # 利用坐标定位结合.long_press滑动操作
            more = element1.location
            bo = element2.location
            self.touchaction_app().long_press(x=more.get('x'), y=more.get('y')).wait(min).move_to(x=bo.get('x'), y=bo.get(
                'y')).release().perform()

    def touch_move_nine(self,x=100,y=100,min_min=200,x1=100,y1=100,
                        x2=100,y2=100,x3=100,y3=100,x4=100,y4=100,x5=100,y5=100,x6=100,y6=100,):
        '''
        画九宫格
        :param x:
        :param y:
        :param min_min:
        :param x1:
        :param y1:
        :param x2:
        :param y2:
        :param x3:
        :param y3:
        :param x4:
        :param y4:
        :param x5:
        :param y5:
        :param x6:
        :param y6:
        :return:
        '''
        # 九宫格画图解锁
        self.touchaction_app().press(x=x, y=y).wait(min_min).move_to(x=x1,y=y1).wait(min_min).move_to(x=x2,y=y2).wait(
            min_min).move_to(x=x3,y=y3).wait(min_min).move_to(x=x4,y=y4).wait(min_min).move_to().wait(min_min)\
            .move_to(x=x5,y=y5).wait(min_min).move_to(x=x6,y=y6).release().perform()

