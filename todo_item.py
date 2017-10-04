import datetime

class TodoItem():

    title = ''
    deadline = datetime.date(2017, 12, 12)
    is_done = False


    def __init__(self, title, deadline):
        if type(title) != str or type(deadline) != datetime.date:
            raise ValueError

        else:
            self.title = title
            self.deadline = deadline

    def mark(self):
        self.is_done = True
        return self.is_done

    def unmark(self):
        self.is_done = False
        return self.is_done

    def __str__(self):
        mark = "[ ]"
        if self.is_done == True:
            mark = "[x]"
        elif self.is_done == False:
            mark = "[ ]"

        return "{} {}-{} {}".format(mark, self.deadline.day, self.deadline.month, self.title)

# task = TodoItem("Zrob zakupy", datetime.date(2017, 11, 11))
# print(task)
# TodoItem.mark(task)
# print(task)
