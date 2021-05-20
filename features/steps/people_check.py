from behave import given, when, then
from selenium import webdriver
from time import sleep


@given('登录账号 {user_people}、密码 {password_people} 和联系人姓名 {name} 和备注{annotation}')    # 对应步骤  Given 关键词 behave， 参数放在{}中
def step_impl(context, user_people,password_people,name,annotation):   # context是上下文对象，有参数的话，加上对应参数
    context.user = user_people # 将参数绑定上下文对象，以便其他步骤使用
    context.password = password_people
    context.name=name
    context.annotation=annotation


@when('进入我的所有联系人页面')
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


@then('添加一个联系人')
def step_impl(context):
    context.driver.find_element_by_xpath('/html/body/a').click()
    context.driver.find_element_by_xpath('/html/body/form/input[1]').send_keys(context.name)
    context.driver.find_element_by_xpath('/html/body/form/input[2]').send_keys(context.annotation)
    sleep(0.5)
    context.driver.find_element_by_xpath('/html/body/input').click()





@then('检查页面是否真的添加了该联系人')
def step_impl(context):
    sleep(0.5)
    context.driver.find_element_by_xpath('//*[@id="indeColuDiv"]/a[4]').click()
    assert context.name in context.driver.page_source


@then('删除该联系人')
def step_impl(context):
    sleep(0.5)
    context.driver.find_element_by_xpath('/html/body/table/tbody/tr[2]/td[4]/a').click()


@then('关闭网页（联系人）')
def step_impl(context):
    context.driver.quit()