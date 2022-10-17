class Pet:
    def __init__(self, owner, name):
        self.owner = owner
        self.name = name

    def __str__(self):
        return f'{self.name} is owned by {self.owner}'

    def walk(self):
        print('walka walka')


# henrietta = Pet('Weston', 'Henrietta')

# print(henrietta)
# my_str_return = henrietta.__str__()
# print(my_str_return)
# henrietta.walk()

class Dog(Pet):
    def __init__(self, owner, name, price = 20):
        super().__init__(owner, name)
        self.price = price
        
    def __str__(self):
        return f'{super().__str__()} and costed {self.price} monies'

    def bark(self):
        print('bark')

    def chase_tail(self):
        print('oh boy oh boy oh boy')

    def get_price(self):
        return self.price

dog = Dog('Michelle', 'Sir Nutter Butters', 'priceless')

print(dog)
dog.bark()
dog.chase_tail()
dog.walk()
print(dog.get_price())

class Cat(Pet):
    def __init__(self, owner, name, price = 10):
        super().__init__(owner, name)
        self.price = price

    def __str__(self):
        return f'{super().__str__()} and costed {self.price} dollars'

    def purr(self):
        print('purrrrrrrr')

    def clean(self):
        print('cleaning!')

    def get_price(self):
        return self.price

    # override parent method
    def walk(self):
        print('strut strut')
    
cat = Cat('Stephen', 'Sake', 'can\'t put a price on you Sake!')

print(cat)
cat.purr()
cat.clean()
print(cat.get_price())
cat.walk()

dog.price = dog.price + ' 🖤🖤🖤🖤🖤🖤🖤'
cat.price = cat.price + '🐈'

print(dog, cat)