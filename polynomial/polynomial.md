# A Polynomial Class

This is an optional alternate pair assignment for the OOP day.

## Part 0

A *polynomial* is an expression of a single variable consisting of the sum of one or more terms. Each term is a non-negative integer power of the variable times some coefficient. For example

$$ x^2 - 2x +1 $$

$$ -2x^3 - x $$

We want to write a class that creates polynomial objects. We'll write methods to

 * evaluate the polynomial for a given value of $ x $,
 * add or subtract two polynomials, returning another polynomial,
 * mulitply two polynomials,
 * return a string representation of polynomials, suitble for display with LaTeX,
 * take the derivative or integral of a polynomial.

Your class will need to store the coefficents. Talk with your partner about what sort of object you'll use to do this, and make sure you both understand the objects you'll be creating. 

## Part 1: Starting your class

Create a Polynomial class with two methods: `__init__` and `__repr__`. The first should allow you to initialize a new Polynomial object with a list, so `Polynomial([3,2,1]) creates the equivalent of $ x^2 + 2x + 3 $. The second should convert it to a string that could be used to create that same object, so `Polynomial([3,2,1]).__repr__()` will return the string `"Polynomial([3,2,1])"`.

We've suggested you enter the coefficients with the lowest-exponent terms first. Discuss with your partner whether this is the best choice.

## Part 2: Do some math

Add an `evaluate` method to your class that takes a single variable, so `Polynomial([3,2,1]).evaluate(2)` will return 11.

## Part 3: Create more magic methods

Add methods `__add__`, `__sub__`, and `__neg__`, and a `__mul__` method that will take a number as an argument. Test out that they give you the expected results.

Add an `__eq__` method that returns `True` or `False`. It should return `True` for `Polynomial([1,0]) == Polynomial([1])`.

## Part 4: Make human-readable strings

Add an `__str__` method that returns a human-readable expression of the polynomial. Don't try to do it perfectly right away, but have it return something and gradually improve it. For example, `Polynomial(-3, 1, 0, -2)` should return `"-2x^3 + x - 3"`, but your first attempt might return `"-2x^3 + 0x^2 + x^1 + -3x^0"`.

## Part 5: Do calculus

Add `differentiate` and `integrate` methods that return the derivative and integral of a polynomial.

## Part 6: Add multiplication of polynomials

Change the `__mul__` method to check if the argument is another `Polynomial` object. If it is, multiply them together such that (for example) `Polynomial([1,1]) * Polynomial([1,1]) == Polynomial([1,2,1])`.





