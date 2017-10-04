from todo_item import TodoItem
from operator import attrgetter

class TodoQuarter():

    todo_items = []

    def __init__(self, todo_items):
        self.todo_items = todo_items

    # def sort_items(self):
    #     sorted(todo_items, key=attrgetter("TodoItem.self.deadline.month", "TodoItem.self.deadline.day"))
