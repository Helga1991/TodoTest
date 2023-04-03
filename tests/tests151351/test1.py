from time import sleep
from selene import have
from selene.support.shared import browser

def test_e2e(todos=None):
    todos.given_opened('a', 'b', 'c')
    todos.should_be('a', 'b', 'c')

class TodoMVC:
   
browser.config.hold_browser_open = True
# GIVEN
browser.open('http://todomvc.com/examples/emberjs')
# WHEN
browser.element('#new-todo').type('a').press_enter()
browser.element('#new-todo').type('b').press_enter()
browser.element('#new-todo').type('c').press_enter()
# THEN
browser.all('#todo-list>li').should(have.exact_texts('a', 'b', 'c'))
sleep(2)


# WHEN
browser.all('#todo-list>li').element_by(have.exact_text('b')).element('.toggle').click()
sleep(2)
browser.element('#clear-completed').click()
# THEN
browser.all('#todo-list>li').should(have.exact_texts('a', 'c'))

sleep(2)
