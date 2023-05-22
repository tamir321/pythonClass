class Parent:
    parm = 7
    def __init__(self,name):
        self.name = name
        self.parent_attribute = 'I am a parent'

    def parent_method(self):
        print('Back in my day...')



# Create a child class that inherits from Parent
class Child(Parent):
    parm = 9
    def __init__(self):
        super().__init__(2)
        self.child_attribute = 'I am a child'

    def parent_method(self):
        print('over load Back in my day...')

# Create a child class that inherits from Parent
class Second_Child(Parent):
    def __init__(self):
        Parent.__init__(self ,2) # notice the (self , )
        self.child_attribute = 'I am a second child'


# Create instance of child
child = Child()
second_Child= Second_Child()

# Show attributes and methods of child class
print(child.child_attribute)
print(child.parent_attribute)
print("child.parm",child.parm)
child.parent_method()

print("~*"*20)


print(second_Child.child_attribute)
print(second_Child.parent_attribute)
print("second_Child.parm",second_Child.parm)
second_Child.parent_method()

print(isinstance(child,Parent))
print(isinstance(child,Child))
print(isinstance(child,Second_Child))