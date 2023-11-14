## Desgin patter rule
Many design patterns are based on rule
- favour composition over inheritance but why?

## Inheritance - why?
- create a code with higher cohesion
- instead of putting everything in one single big class create a class hierarchy of classes and subclasses, where you put separate things in subclass so they are separated

## Composition - what?
- use separate classes to represent separate things in app and each of these classes use each other in some meaningful way

Diference between **Inheritance** and **Composition**
- diference between (inheritance) **is a realtionship** and **has a relationship** (composition)

Inheritance allows you to separate the responsibility:
- you need to watch out with **inheritance** because that introduce strongest possible **coupling** in object oriented programming
- let's explore why, so this will answer

## Why composition is better than inheritance

This repository contains the code for the Composition vs Inheritance video on the ArjanCodes channel (watch the video [here](https://youtu.be/0mcP8ZpUR38)).

## No inheritance with low cohesion
The example is about different employee types and reward structures.
In the first version (`before.py`), there is no inheritance, just three classes (= three employee types) with low cohesion (lots of responsibilities per class), and code duplication.

## With inheritance
Then there is a version that tries to solve those issues with inheritance (`with_inheritance.py`),

- no duplication of common attributes
- interface grouping

## With composition
and another version that uses composition (`with_composition.py`).

Use inheritance manily with `abstract` classes.
So it is mechanism to separate out different parts of the app and batch them up.

Most of design patterns has single layer of inheritance, except decorator which has recursive component.

- Use `abstractbase` classes to define the interfaces and then
- define subclasses for specific version of that and batch them up
- with abstract base classes you reduce coupling

- Inheritance if you are not using abstractbase classes is a mechanism that adds coupling 

- If you want to reduce coupling inheritance thakes you in opposite direction, where abstractbase classes reduce coupling 

## Task 1
Recall the example from last session on `SOLID` topic.
We have the `PaymentProcessor` and `PaymentProcessorSMS`.
Instead of using **inheritance** introduce `Authorizer` **composition** in classes
`DebitPaymentProcessor` and `PayPallPaymentProcessor`.

Introduce composition in the example.

# Task 2 Install mypy and fix issues.