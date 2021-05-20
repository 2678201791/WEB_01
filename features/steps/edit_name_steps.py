from behave import given, when, then
from selenium import webdriver
from time import sleep


@given('（修改用户名）登录账号 {user}、密码 {password} 和新名字 {new_name}')    # 对应步骤  Given 关键词 behave， 参数放在{}中
def step_impl(context, user,password,new_name):   # context是上下文对象，有参数的话，加上对应参数
    context.user = user # 将参数绑定上下文对象，以便其他步骤使用
    context.password = password
    context.new_name=new_name


@when('（修改用户名）进入我的用户信息界面')
def step_impl(context):
    context.driver = webdriver.Firefox()  # 同样绑定上下文对象
    context.driver.get('http://localhost:8080/SpringMVCMybatis/loginJsp')
    sleep(0.5)
    context.driver.find_element_by_xpath('/html/body/form/input[1]').send_keys(context.user)
    context.driver.find_element_by_xpath('/html/body/form/input[2]').send_keys(context.password)
    context.driver.find_element_by_xpath('/html/body/form/input[3]').click()
    sleep(0.5)
    context.driver.find_element_by_xpath('//*[@id="indeColuDiv"]/a[2]').click()
    sleep(0.5)



@then('（修改用户名）修改用户名')
def step_impl(context):
    context.driver.find_element_by_xpath('//*[@id="modiButt"]/input[3]').click()
    sleep(0.5)
    context.driver.find_element_by_xpath('//*[@id="userForm"]/input[1]').clear()
    context.driver.find_element_by_xpath('//*[@id="userForm"]/input[1]').send_keys(context.new_name)
    context.driver.find_element_by_xpath('//*[@id="userForm"]/input[2]').click()
    sleep(1)


@then('（修改用户名）检查用户名是否真的修改')
def step_impl(context):
    name = '名称&nbsp;&nbsp;'+context.new_name
    assert name in context.driver.page_source


@then('（修改用户名）关闭网页')
def step_impl(context):
    context.driver.quit()