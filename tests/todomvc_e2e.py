from time import sleep
from selene import have
from selene.support.shared import browser

from todomvc_testing.Model import todos


def test_e2e():
    todos.given_opened('a', 'b', 'c')
    todos.should_be('a', 'b', 'c')
    todos.toggle('b')
    todos.should_becompleted('b')

    browser.all('#todo-list>li').should(have.exact_texts('a', 'b', 'c'))
    sleep(2)

    browser.all('#todo-list>li').element_by(have.exact_text('b')).element('.toggle').click()
    sleep(2)
    browser.element('#clear-completed').click()

    browser.all('#todo-list>li').should(have.exact_texts('a', 'c'))

    sleep(2)




