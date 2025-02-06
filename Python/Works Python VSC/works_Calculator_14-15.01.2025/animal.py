class Animal:
    def __init__(self):
        self.name=""
    
    def echo(self,name):
        self.name=name
        for i in range(3):
            print(self.name)

sharick=Animal()
sharick.echo("Шарик")