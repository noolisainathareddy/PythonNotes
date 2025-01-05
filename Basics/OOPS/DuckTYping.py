class Mac:

    def execute(self):
        print("This is mac")

class Windows:
    def execute(self):
        print("This is Windows")

class Run:

    def apps(self, laptop):
        laptop.execute()

App = Run()

App.apps(Mac())
App.apps(Windows())