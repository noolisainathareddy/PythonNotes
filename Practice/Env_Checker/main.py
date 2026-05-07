import sys, os

def margin():
    for i in range(50):
        print("=", end="", sep='\n',)

margin()
print( f"\n{ 'Environment variable Checker' :^80}" )
margin()

print()
variables = os.environ.items()






