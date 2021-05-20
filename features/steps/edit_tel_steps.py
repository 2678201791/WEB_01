from behave import given, when, then
from selenium import webdriver
from time import sleep


@given('（我的所有联系）登录账号 {user}、密码 {password} 和联系方法 {method}、备注{beizhu}')    # 对应步骤  Given 关键词 behave， 参数放在{}中
def step_impl(context, user,password,method,beizhu):   # context是上下文对象，有参数的话，加上对应参数
    context.user = user # 将参数绑定上下文对象，以便其他步骤使用
    context.password = password
    context.method=method
    context.beizhu=beizhu


@when('（我的所有联系）我的所有联系人界面，点击Test联系人')
def step_impl(context):
    context.driver = webdriver.Firefox()  # 同样绑定上下文对象
    context.driver.get('http://localhost:8080/SpringMVCMybatis/loginJsp')
    sleep(0.5)
    context.driver.find_element_by_xpath('/html/body/form/input[1]').send_keys(context.user)
    context.driver.find_element_by_xpath('/html/body/form/input[2]').send_keys(context.password)
    sleep(0.5)
    context.driver.find_element_by_xpath('/html/body/form/input[3]').click()
    sleep(0.5)
    context.driver.find_element_by_xpath('//*[@id="indeColuDiv"]/a[4]').click()
    context.driver.find_element_by_xpath('/html/body/table/tbody/tr[2]/td[1]/a').click()
    sleep(0.5)



@then('（我的所有联系）添加联系方式')
def step_impl(context):
    context.driver.find_element_by_xpath('/html/body/a[3]').click()
    context.driver.find_element_by_xpath('/html/body/form/input[2]').send_keys(context.method)
    context.driver.find_element_by_xpath('/html/body/form/input[3]').send_keys(context.beizhu)
    context.driver.find_element_by_xpath('/html/body/input').click()






@then('（我的所有联系）检查账号是否真的修改')
def step_impl(context):
    assert '联系方法增加成功' in context.driver.page_source


@then('（我的所有联系）删除联系方式')
def step_impl(context):
    sleep(0.5)
    context.driver.find_element_by_xpath('//*[@id="indeColuDiv"]/a[5]').click()
    context.driver.find_element_by_xpath('/html/body/table/tbody/tr[2]/td[6]/form/input[2]').click()
    sleep(0.5)


@then('（我的所有联系）关闭网页')
def step_impl(context):
    context.driver.quit()