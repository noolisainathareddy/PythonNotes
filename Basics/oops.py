class Hello:
    def greet(self):
        print("Welcome Sai!")


comp1 = Hello()
comp2 = Hello()


comp1.greet()
comp2.greet()

Hello.greet(comp1)
Hello.greet(comp2)