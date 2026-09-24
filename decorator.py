def changecase(fun):
    def void():
        return fun()
    return void
@changecase
def greet():
    return "Hello World"
print(greet())


