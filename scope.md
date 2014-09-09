# Scope

Scope can be thought of as the lifetime of a reference (i.e. variables, objects, and methods).  Python scope can take some getting used to but here is a quick cheatsheet on what the rules are for looking up a value.  Python uses lexical scoping and binds scope on declaration of a variable/reference (rather than on function execution).  The difference between lexical (static) and dynamic scope is beyond the scope of this course, but the wikipedia page has a concise [explanation][1].

```bash
x=1
function g () { echo $x ; x=2 ; }
function f () { local x=3 ; g ; }
f # does this print 1, or 3?
echo $x # does this print 1, or 2?
```

### Rules

__LEGB Rule__

![scope][2]

__L: Local.__ (Names assigned in any way within a function (def or lambda)), and not declared global in that function.

__E: Enclosing function locals.__ (Name in the local scope of any and all enclosing functions (def or lambda), from inner to outer.

__G: Global (module).__ Names assigned at the top-level of a module file, or declared global in a def within the file.

__B: Built-in (Python).__ Names preassigned in the built-in names module : open,range,SyntaxError,...

Python uses lexical scoping and a variable is __bound__ when it is defined (or assigned to).  When in doubt always jump into a debugger (`ipdb.set_trace()`) at the point of you program in which you are uncertain and inspect the variables.  In Python, the `locals()` method tells you exactly what is in the local scope, and the globals() tells you everything that is in the global scope.

```python
def foo(arg): 
    x = 1
    print locals()

foo(7)
#=> {'arg': 7, 'x': 1}

foo('bar')
#=> {'arg': 'bar', 'x': 1}
```

### Creating Scope

In Python, you can create new scope by defining a function (`def ... or lambda`) or creating a class.  Think of each of these as adding layers to a wonderful scope onion (or maybe Russian dolls are a better analogy).

![matroyska dolls][4]

You can never look down scope but can most always look up (unless you shadow a variable).  For example:

```python
x = "global"

def new_scope(x):
    print x
    y = "I'm just hiding"
    x = "shadow variable"
    return x

print x #=> "global"
new_scope("argument") #=> "argument"

print x #=> "global"

print new_scope("argument") 
    #=> "argument"
    #=> "shadow variable"

print y #=> NameError: name 'y' is not defined
```

### How do I get into the Scope club (with a velvet rope)

#### Pass-by-reference vs. pass-by-value

Most languages are either pass by reference or pass by value.  The difference being in pass-by-reference the argument can be mutated and it effects that variable up scope, whereas in pass-by-value creates a 'copy'.  Unfortunately Python is a mixture of these in something called 'pass-by-object-reference'.  Or rather:

    Object references are passed by value

But that may not make more sense. If you ever have a question, it is often best to try it out in a python interpreter:

```python

x = "global"

def do_nothing(ll):
    print x
    return ll

def return_list(ll):
    ll = ["assign", "a", "list"]
    return ll

def mutate_list(ll):
    ll.append("Messin with my list")
    return ll

new_list = ['foo', 'bar']

print do_nothing(new_list) #=> "global" 
                           #=> ['foo', 'bar']
print return_list(new_list) #=> ["assign", "a", "list"]
print mutate_list(new_list) #=> ['foo', 'bar', "Messin with my list"]
```

I just showed you how to get into the scope club, to get out you can either mutate a object passed in, or the safest option is to return variables.

This is a common source of confusion for people new to Python but the worst offender of breaking some of these conventions is `pandas`.  You should always read the docs of a new library to understand its own semantics and nuances.

__[More info][3]__

### What is that `self` thing you keep using

```python
# from above...
class Animal(object):
    def __init__(self, name, emotion):
        self.name = name
        self.emotion = emotion

    def speak(self):
        print "My name is " + self.name

    # self is replaced by the object
    # the method is called on
    def eat(self, food):
        print "I " + self.emotion + " " + food

frank = Animal("Frank", "adore")
frank.speak() #=> "My name is Frank"

# object is passed as first argument to a method call
frank.eat("bananas") #-> Animal.eat(frank, "bananas")
    #=> "I adore bananas"
```

The object a method is called on is always passed as the first argument (`self`).  In this case, the object `frank` of the class `Animal` is passed as the first argument to the method call `eat(...)`.  This ensures that we always explicitly have access to the object the method belongs to.  When we create a new object instantiation of the class `Animal`, we bind the variable `self` to the object created.  In this case, the call to `Animal("Frank")` binds the variable `self` to the returned object.  This instantialion also runs the code in the class's `__init__()` method implicitly.  `__init()__` is just a function though and we can (though it is very bad practice to) call it once a object has been created.

```python
class Person(object):
    def __init__(self, name):
        self.name = name
        print "I am alive"

jon = Person("Jon") #=> I am alive

jon #=> <__main__.Person instance at 0x105addc20>

jon.name #=> 'Jon'

jon.__init__("Susie") #=> I am alive

jon.name #=> 'Susie'
```

_More info: [http://freepythontips.wordpress.com/2013/08/07/the-self-variable-in-python-explained/](http://freepythontips.wordpress.com/2013/08/07/the-self-variable-in-python-explained/)_

# Appendix

Another handy tool when learning about scope and stacks is the [stack visualization tool](http://pythontutor.com) at pythontutor.com.  Here is a great [tutorial](http://cscircles.cemc.uwaterloo.ca/11b-how-functions-work/) on visually exploring variable scope in Python as you execute a program.  Scope gets more specific as you go down, i.e. the top of the image (`Global Frame`) is the top most scope and `sum_squared_error` is the most specific.  Each box on the left represents a different scope (created when we call a function).  The nested scopes can look up/out but the outer scopes cannot look in.  For example, `sum_squared_error` can access anything defined in any scope above it (unless it is shielded by another function or class) but the global scope cannot peek into the `sum_squared_error` function and its variables.  To move data/values/variables between scope you either pass arguments and return values: __function arguments -> down/into scope :: return values -> up/out scope__

--

Visualized Execution of the example `Variance` class from above: 

![oo](images/oo.png)

#### <a href="http://www.pythontutor.com/visualize.html#code=import+math%0A%0Aclass+Variance(object)%3A%0A++++def+__init__(self,+input_list)%3A%0A++++++++self.data+%3D+input_list%0A++++++++self.total_length+%3D+0%0A++++++++self.difference_sum+%3D+0%0A%0A++++def+mean(self)%3A%0A++++++++total+%3D+0.0%0A++++++++for+num+in+self.data%3A%0A++++++++++++total+%2B%3D+num%0A++++++++++++self.total_length+%2B%3D+1%0A++++++++self.mean+%3D+total/self.total_length%0A%0A++++def+sum_squared_error(self)%3A%0A++++++++for+num+in+self.data%3A%0A++++++++++++self.difference_sum+%2B%3D+math.pow(num+-+self.mean,+2)%0A++++++++self.variance+%3D+self.difference_sum+/+self.total_length%0A%0A++++def+compute_variance(self)%3A%0A++++++++return+self.variance%0A++++%0Avari+%3D+Variance(%5B1.,2.,3.,4.%5D)%0Avari.mean()%0Avari.sum_squared_error()%0Avari.compute_variance()&mode=display&cumulative=false&heapPrimitives=false&drawParentPointers=false&textReferences=false&showOnlyOutputs=false&py=2&curInstr=0">Interactive</a> OO

--

![functional](images/functional.png)
#### <a href="http://www.pythontutor.com/visualize.html#code=import+math%0A%0Adef+mean(data)%3A%0A++++return+reduce(float.__add__,+data)/len(data)%0A%0Adef+sum_squared_error(data,+mean)%3A%0A++++return+reduce(float.__add__,+%5B+math.pow(num+-+mean,+2)+for+num+in+data%5D)/len(data)%0A%0Adef+variance(data)%3A%0A++++return+sum_squared_error(data,+mean(data))%0A%0Avariance(%5B1.,2.,3.,4.%5D)&mode=display&cumulative=false&heapPrimitives=false&drawParentPointers=false&textReferences=false&showOnlyOutputs=false&py=2&curInstr=0">Interactive</a> Functional

<!-- References -->
[1]: http://en.wikipedia.org/wiki/Scope_(computer_science)#Lexical_scoping_vs._dynamic_scoping
[2]: http://developer.nokia.com/community/wiki/images/b/b5/Figure2-1.png?20101129095437
[3]: http://robertheaton.com/2014/02/09/pythons-pass-by-object-reference-as-explained-by-philip-k-dick/
[4]: http://www.sciencephotography.com/xrayfish/xray%20jan24-06/Russian-doll1.jpg

<!-- Easter Eggs -->
[gotchas]: http://docs.python-guide.org/en/latest/writing/gotchas/
