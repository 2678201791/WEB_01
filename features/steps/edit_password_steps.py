from behave import given, when, then
from selenium import webdriver
from time import sleep

#('登录账号 {user}和密码 {password}')

@given('登录账号 {user} 和密码 {password} 、新密码{new_password}')    # 对应步骤  Given 关键词 behave， 参数放在{}中
def step_impl(context,user,password,new_password):   # context是上下文对象，有参数的话，加上对应参数
    context.user=user
    context.password=password
    context.new_password = new_password # 将参数绑定上下文对象，以便其他步骤使用


@when('打开通讯录页面(修改密码)')
def step_impl(context):
    context.driver = webdriver.Firefox()  # 同样绑定上下文对象
    context.driver.get('http://localhost:8080/SpringMVCMybatis/loginJsp')
    sleep(0.5)
    context.driver.find_element_by_xpath('/html/body/form/input[1]').send_keys(context.user)
    context.driver.find_element_by_xpath('/html/body/form/input[2]').send_keys(context.password)
    context.driver.find_element_by_xpath('/html/body/form/input[3]').click()

@when('修改密码')
def step_impl(context):
    sleep(0.5)
    context.driver.find_element_by_xpath('//*[@id="indeColuDiv"]/a[2]').click()
    sleep(0.5)
    context.driver.find_element_by_xpath('//*[@id="modiButt"]/input[2]').click()
    sleep(0.5)
    context.driver.find_element_by_xpath('//*[@id="passForm"]/input[1]').send_keys(context.password)
    context.driver.find_element_by_xpath('//*[@id="passForm"]/input[2]').send_keys(context.new_password)
    context.driver.find_element_by_xpath('//*[@id="passForm"]/input[3]').send_keys(context.new_password)
    context.driver.find_element_by_xpath('//*[@id="passForm"]/input[4]').click()
    sleep(0.3)
    context.driver.find_element_by_xpath('//*[@id="indeColuDiv"]/a[3]').click()


@then('尝试用新密码登录页面并验证登录是否成功')
def step_impl(context):
    context.driver.find_element_by_xpath('/html/body/div[1]/a[3]').click()
    sleep(1)
    context.driver.find_element_by_xpath('/html/body/form/input[1]').send_keys(context.user)
    sleep(1)
    context.driver.find_element_by_xpath('/html/body/form/input[2]').send_keys(context.new_password)
    sleep(1)
    context.driver.find_element_by_xpath('/html/body/form/input[3]').click()


@then('还原密码')
def step_impl(context):
    sleep(0.5)
    context.driver.find_element_by_xpath('//*[@id="indeColuDiv"]/a[2]').click()
    sleep(0.5)
    context.driver.find_element_by_xpath('//*[@id="modiButt"]/input[2]').click()
    sleep(0.5)
    context.driver.find_element_by_xpath('//*[@id="passForm"]/input[1]').send_keys(context.new_password)
    context.driver.find_element_by_xpath('//*[@id="passForm"]/input[2]').send_keys(context.password)
    context.driver.find_element_by_xpath('//*[@id="passForm"]/input[3]').send_keys(context.password)
    context.driver.find_element_by_xpath('//*[@id="passForm"]/input[4]').click()
    sleep(0.3)
    context.driver.find_element_by_xpath('//*[@id="indeColuDiv"]/a[3]').click()

@then('关闭网页(修改密码)')
def step_impl(context):
    context.driver.quit()