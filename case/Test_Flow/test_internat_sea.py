'''
国际海运流程测试
'''

import pytest,allure


@allure.feature('国际海运')
class TestInternatSea:

    @allure.story('遍历贸易术语')
    def test_(self):

        with allure.step('保存'):
            allure.attach('')