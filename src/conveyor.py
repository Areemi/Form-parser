class Conveyor:
    """Class to manage a set of tasks to be executed in sequence."""
    def __init__(self):
        """Initialize an empty list of tasks."""
        self.tasks = []
        self.q = {}

    def add_task(self, task):
        """Add a task to the conveyor."""
        self.q.append(task)

    def empty(self):
        if self.q:
            return True
        else:
            return False

    def run(self):
        """Execute all tasks in the conveyor."""
        """for task in self.tasks:
            task()"""
        pass
        #while not self.q.empty():
            #task, args = q.get()
            #if task not in utils:
                #raise ValueError('No such util for task %r' % (task))

            #utils[task].execute(*args)

"""class Conveyor:
    
    DOCUMENTME
    

    def __init__(self):
        self.q = []
    
    def run(self):
        # TODO: ImplementMe
        # while(!q.empty()):
        #    task, args = q.get()
        #    if task not in utils:
        #        raise ValueError('No such util for task %r' % (task))
        #
        #    utils[task].execute(*args)
        pass"""
