# Composition over Inheritance

Many design patterns are based on this principle.

# Code with higer cohesion 
# Inheritance is a relationship
Instaed of creating one big class
you would create a class hierarchy.
Separate from main classs by subcalsses.

# Cohesion has a relationship

Use separate classes to represent separate things in your application. 
Each of these classes use each other in some menigful way.

Both allows you to separate the responisbilities.


Watch out with inheritance, that introduces the strongest possible coupling in programming. 

# BEFORE

The problems are the following:

- code duplication, classes deals for similar data

- compute pay mixed with employee data

# Solution inheritance
Extract the same thing.
`Employee` class.

Next, class do a lot.
Separate the pay method
to `SalariedEmployee` class.
1. With inheritance we did not solve the `code duplication` issue. 

2. With every variation we add, we will get `explosion` of classes.

Inheritance to separate the responisbility, `duplicate code` and `introduce coupling`.

We have 
`Employee` with employee data.

We have `Payment structure`, hourly, salary, freelancer.

We have `comission` based on the number of contracts.

Instead of doing `inheritance`

You can do `separate` class hierarchies for each concept and combine later on.


# Solution composition 

Separate concepts
and combine them in menagiful way. 

class for `Commision`
class for `Contract`

class for `Contract`
class for `Employee`

`Employee` has `Contract` and optional `Commision` (relationship in pay method)
- `Dependency Inversion` 

# Advantage of using composition instead of inheritance

Avoid code duplication.
No explosion of classes in inheritance.
Easy to extend with other `contracts` and `commsions`.

Few limitaions:
employee has a lot of responisbilities. 

Separate `PersonData`
`dataclasses` - with regular classes need to add initializer

`PyDentic` offers validation

# Summary 
Use `abstarct base` classes to define `interaces`
and then define `subclasses` for
versions of that and patch them up at the end.

Look at it in terms of coupling:
- what you do with an abstract base class that you are reducing coupling between parts of app
bc you are allowing one class to depends on the interface instead
of direct instance
(thats why reduce coupling)

`Inheritance` in general
if you are not usign `abstract base` classes is a mechanism that adds coupling.
By creating subclass it depends on super class. Thats why composition with abstract subclasses is a nice way to decople the app.
# SUGGESTIONS

`make a draft`
`diagnose the code`
for
`coupling`
`composition` better than `inheritance`
`dependency injection` -> `dependency inversion`
`data class`
`property`
`abstractmethod`

`composition`
concepts
1. create Netbox object
2. get Netbox object
3. save Netbox object
4. update Netbox object
5. Use PyDENTIC