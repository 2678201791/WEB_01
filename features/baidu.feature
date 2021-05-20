Feature: 通讯录
  Scenario Outline: 登录用例
    Given 登录账号 <user>和密码 <password>
    When 打开通讯录页面
    When 输入关键词并登录
    Then 页面中应包含关键词
    Then 关闭网页

    Examples:登录用账号密码
    |   user             |      password     |
    |   People001        |      123          |
    |   People002        |      123          |
    |   People003        |      123          |
    |   People004        |      123          |
    |   People005        |      123          |


  Scenario Outline: 修改密码
    Given 登录账号 People001 和密码 123 、新密码<new_password>
    When 打开通讯录页面(修改密码)
    And  修改密码
    Then 尝试用新密码登录页面并验证登录是否成功
    Then 还原密码
    Then 关闭网页(修改密码)

    Examples:修改密码
    |   new_password     |
    |   456              |

  Scenario Outline: 我的所有联系人
    Given 登录账号 People001、密码 123 和联系人姓名 <name> 和备注<annotation>
    When 进入我的所有联系人页面
    Then 添加一个联系人
    Then 检查页面是否真的添加了该联系人
    Then 删除该联系人
    Then 关闭网页（联系人）

    Examples:联系人资料
    |   name             |      annotation   |
    |   People001        |      test001      |

  Scenario Outline: 修改用户名
    Given （修改用户名）登录账号 People001、密码 123 和新名字 <new_name>
    When （修改用户名）进入我的用户信息界面
    Then （修改用户名）修改用户名
    Then （修改用户名）检查用户名是否真的修改
    Then （修改用户名）关闭网页

    Examples:修改用户名
    |   new_name         |
    |   new_People001    |

  Scenario Outline: 修改账号
    Given （修改账号）登录账号 <user>、密码 123 和新账号 <new_user>
    When （修改账号）进入我的用户信息界面
    Then （修改账号）修改账号
    Then （修改账号）检查账号是否真的修改
    Then （修改账号）关闭网页

    Examples:修改账号
    |   new_user         |   user           |
    |   new_People001    |   People001      |
    |   People001        |   new_People001  |

  Scenario Outline: 我的所有联系
    Given （我的所有联系）登录账号 People001、密码 123 和联系方法 <method>、备注<beizhu>
    When （我的所有联系）我的所有联系人界面，点击Test联系人
    Then （我的所有联系）添加联系方式
    Then （我的所有联系）检查账号是否真的修改
    Then （我的所有联系）删除联系方式
    Then （我的所有联系）关闭网页

    Examples:修改账号
    |   method           |   beizhu         |
    |   110              |   Police         |



