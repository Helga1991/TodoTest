from selene import browser, have



class TodoMVC:
    def __init__(self):
        self.todo_list = browser.all('todo-list>li')

    def open(self):
        browser.open('https://todomvc4tasj.herokuapp.com/')
        app_loaded = "return $._data($('#clear-completed')[0], 'events')"\
                     ".hasOwnProperty('click')"
        browser.should(have.js_returned(True, app_loaded))
        return self

    def add(self, *todos: str):
        for todo in todos:
            browser.element('#new-todo').type(todo).press_enter()
        return self

    def given_opened(self, *todos: str):
        self.open()
        self.add(*todos)

    def should_be(self, *todos: str):
        self.todo_list.should(have.exact_texts(*todos))
        return self



