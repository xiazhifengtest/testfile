'''import unittest
import requests
from selenium import webdriver
from time import sleep

class Test_Keys(object):
    def __init__(self,browers_type):
        self


    #def open_brower
#关闭浏览器
def quit(self):
    self.driver.quit()
    #访问url
    def vis(self,url):


    #元素定位
    def locator(self,locator_type,locator):
        if locator_type=='id':
            el=self.driver.find_element_by_id(locator)
        if locator_type=='name':
            el=self.driver.find_element_by_name(locator)
        return el
    #输入

    def input_text(self,locator,text):
        self.locator(locator).send_keys(text)
        #点击
    def click_el(self):
        self.locator(locator).click()
    #等待
    def wait(self,seconds):
        sleep(seconds)


if __name__=='__main__':
    url='htto://www.baidu.com'
    browser='chrome'
    driver=Test_Keys(browser)
    driver.vis
    '''
'''
    #属性：
    driver.current_url #用于获得当前页面的URL
    driver.title #用于获取当前页面的标题
    driver.page_source #用于获取页面html源代码
    driver.port #用于获取浏览器的端口
    driver.capabilities['version']  #打印浏览器version的值

    #浏览器：
    driver.get(url):#浏览器加载url
    driver.back() #浏览器后退
    driver.forward() #浏览器前进
    driver.refresh() #浏览器刷新（点击刷新按钮）
    driver.set_page_load_timeout(5) #设置页面加载时间，如果超时会跑异常
    driver.implicitly_wait(秒) #隐式等待，通过一定的时长等待页面上某一元素加载完成。
    #若提前定位到元素，则继续执行。等待10s若超过时间未加载出，则抛出NoSuchElementException异常。


    #执行js：
    driver.execute_script(js) #调用js
    #窗口：
    driver.current_window_handle  #用于获取当前窗口句柄
    driver.window_handles  #用于获取所有窗口句柄

    driver.maximize_window()  #将浏览器最大化显示
    driver.set_window_size(480, 800)  #设置浏览器宽480、高800显示
    driver.get_window_size()  #获取当前窗口的长和宽
    driver.get_window_position()  #获取当前窗口坐标
    driver.set_window_position(300,200)  #设置当前窗口坐标
    driver.get_screenshot_as_file(filename)  #截取当前窗口
    #实例：driver.get_screenshot_as_file('D:/selenium/image/baidu.jpg')

    driver.close()  #关闭当前窗口，或最后打开的窗口
    driver.quit()  #关闭所有关联窗口，并且安全关闭session

    #窗口切换：
    driver.switch_to_frame(id或name属性值)#切换到新表单(同一窗口)。若无id或属性值，可先通过xpath定位到iframe，再将值传给switch_to_frame()
    driver.switch_to.parent_content()#跳出当前一级表单。该方法默认对应于离它最近的switch_to.frame()方法
    driver.switch_to.default_content() #跳回最外层的页面
    driver.switch_to_window(窗口句柄) #切换到新窗口
    driver.switch_to.window(窗口句柄) #切换到新窗口

    #弹框切换：
    driver.switch_to_alert() #警告框处理。处理JavaScript所生成的alert,confirm,prompt
    driver.switch_to.alert() #警告框处理
    driver.get_cookies()   #获取当前会话所有cookie信息
    driver.get_cookie(cookie_name)  #返回字典的key为“cookie_name”的cookie信息。
    #实例：driver.get_cookie("NET_SessionId")

    driver.add_cookie(cookie_dict)   #添加cookie。“cookie_dict”指字典对象，必须有name和value值
    driver.delete_cookie(name,optionsString)  #删除cookie信息
    driver.delete_all_cookies()  #删除所有cookie信息

   能通过id和name的，尽量不要用xpath和css
       Id定位
       唯一属性定位
       组合定位  
       先找到相邻的元素  
       绝对路径

    diver.find_element("xpath"，".//a//span")  # 利于封装

    driver.find_element_by_id()
    driver.find_element_by_name()
    driver.find_element_by_class_name()
    driver.find_element_by_tag_name()
    driver.find_element_by_link_text()
    driver.find_element_by_partial_link_text()  # 模糊查询
    driver.find_element_by_xpath()
    driver.find_element_by_css_selector()  # css选择定位器
    # 属性：
    element.size  #获取元素的尺寸。
    element.text   #获取元素的文本。
    element.tag_name   #获取标签名称

    element.clear()  #用于清除输入框的默认内容
    element.send_keys("xx")  #用于在一个输入框里输入 xx 内容
    element.click()  #用于单击一个按钮
    element.submit()  #提交表单
    element.size  #返回元素的尺寸
    element.text  #获取元素文本
    element.get_attribute('value')
    #返回元素的属性值，可以是id、name、type或元素拥有的其它任意属性
    #如果是input的，可以通过获取value值获得当前输入的值

    element.is_displayed ()
    #返回元素的结果是否可见，返回结果为True或False

    element.is_enabled()  #判断元素是否可用
    element.is_selected()   #返回单选按钮、复选框元素结果是否被选中（True 或 False）
    element.value_of_css_property(height)  #获取元素css样式属性
    #引入ActionChains类
    from selenium.webdriver.common.action_chains import ActionChains

    mouse =driver.find_element_by_xpath("xx") #定位鼠标元素

    #对定位到的元素执行鼠标操作
    ActionChains(driver).context_click(mouse).perform() #鼠标右键操作
    ActionChains(driver).double_click(mouse).perform() #鼠标双击操作
    ActionChains(driver).move_to_element(mouse).perform() #鼠标移动到上面的操作
    ActionChains(driver).click_and_hold(mouse).perform() #鼠标左键按下的操作
    ActionChains(driver).release(mouse).perform()  #鼠标释放

    #鼠标拖拽
    element = driver.find_element_by_name("xxx")  #定位元素的原位置
    target = driver.find_element_by_name("xxx") #定位元素要移动到的目标位置
    ActionChains(driver).drag_and_drop(element, target).perform() #执行元素的移动操作
、    #引入Keys类包
    from selenium.webdriver.common.keys import Keys

    element.send_keys(Keys.BACK_SPACE)  #删除键（BackSpace）
    element.send_keys(Keys.SPACE)  #空格键(Space)
    element.send_keys(Keys.TAB)  #制表键(Tab)
    element.send_keys(Keys.ESCAPE)  #回退键（Esc）
    element.send_keys(Keys.ENTER)  #回车键（Enter）
    element.send_keys(Keys.CONTROL,'a')  #全选（Ctrl+A）
    element.send_keys(Keys.CONTROL,'c')  #复制（Ctrl+C）
    element.send_keys(Keys.CONTROL,'x')  #剪切（Ctrl+X）
    element.send_keys(Keys.CONTROL,'v')  #粘贴（Ctrl+V）
    element.send_keys(Keys.F12)   #键盘F12

    #输入空格键+“python”
    element.send_keys(Keys.SPACE)
    element.send_keys("python")

    '''
# from selenium import webdriver
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.common.by import By
#
# driver = webdriver.Chrome()
# driver.get("https://www.baidu.com")
# driver.maximize_window()
# driver.find_element_by_id("kw").send_keys(u"软件测试自动化框架")
# driver.find_element_by_id("su").click()
# loctor = (By.XPATH, ("(.//div[@id='content_left']/div/div/h3/a)[1]"))
# WebDriverWait(driver, 10, 1).until(EC.element_to_be_clickable(loctor))
#driver.find_element_by_xpath("(.//div[@id='content_left']/div/div/h3/a)[1]").click()

# coding=utf-8
import unittest
from selenium import webdriver
import time
from ddt import data, unpack, ddt


# 使用ddt在类前
@ddt
class catTest(unittest.TestCase):
    # 类的初始化
    @classmethod
    def setUpClass(cls):
        print('setupclass')

    # 类的释放
    @classmethod
    def tearDownClass(cls):
        print('teardown')

    # 用例的初始化
    def setUp(self):
        self.driver = webdriver.Chrome('C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
        self.driver.maximize_window()
        self.driver.get('http://www.baidu.com')

    # 用例的环境释放
    def tearDown(self):
        self.driver.back()
        time.sleep(5)

        self.driver.quit()

    # ddt的数据添加循环使用
    @data(('软件测试', '自动化框架'), ('设置语言', '测试入门'))
    @unpack
    def test_cs1(self, cc, dd):
        self.driver.find_element_by_id('kw').send_keys(cc, dd)
        self.driver.find_element_by_id('su').click()
        self.driver.find_element_by_id('u').click()
        time.sleep(5)

        # self.driver.titlee
        # return self.driver.title
    # def test_cs2(self, ):
    #     self.driver.find_element_by_id('kw').send_keys('问题')
    #     self.driver.find_element_by_id('su').click()
    #
    # def test_cs3(self, ):
    #     self.driver.find_element_by_id('kw').send_keys('自动化')
    #     self.driver.find_element_by_id('su').click()
    #
    # def test_cs4(self, ):
    #     self.driver.find_element_by_id('kw').send_keys('测试')
    #     self.driver.find_element_by_id('su').click()
    # def test_cs2(self,cc):
    #     print(cc)
    # def test_cs3(self,dd):
    #     print(dd)


if __name__ == "__main__":
    unittest.main(verbosity=2)

