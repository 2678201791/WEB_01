from behave import given, when, then
from selenium import webdriver
from time import sleep


@given('登录账号 {user}和密码 {password}')    # 对应步骤  Given 关键词 behave， 参数放在{}中
def step_impl(context, user,password):   # context是上下文对象，有参数的话，加上对应参数
    context.user = user # 将参数绑定上下文对象，以便其他步骤使用
    context.password = password



@when('打开通讯录页面')
def step_impl(context):
    context.driver = webdriver.Firefox()  # 同样绑定上下文对象
    context.driver.get('http://localhost:8080/SpringMVCMybatis/loginJsp')

@when('输入关键词并登录')
def step_impl(context):
    sleep(0.5)
    context.driver.find_element_by_xpath('/html/body/form/input[1]').send_keys(context.user)
    sleep(0.5)
    context.driver.find_element_by_xpath('/html/body/form/input[2]').send_keys(context.password)
    sleep(0.5)
    context.driver.find_element_by_xpath('/html/body/form/input[3]').click()



@then('页面中应包含关键词')
def step_impl(context):
    context.driver.implicitly_wait(10)
    assert '你好' in context.driver.page_source
    # self.assertIn(context.keyword, self.driver.page_source)
    sleep(2)

@then('关闭网页')
def step_impl(context):
    context.driver.quit()