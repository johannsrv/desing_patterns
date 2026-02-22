# Design patterns

There are 3 type of design patterns, which are the following:

    * Creation patterns: These patterns provide object creation mechanisms that increase the flexibility and reuse of existing code

    * Structural patterns: These patterns explain how to assemble objects and classes structures into larger structures, while maintaining the flexibility and efficiency of the structure.

    * behavior patterns: These patterns deal with algorithms and the assignment of responsibilities among objects.

### Creation patterns:
##### Singleton:

The Singleton is a design pattern that ensures a class has only one instance throughout the entire execution of a program and provides a global point of access to it.

* No matter how many times the object is instantiated, the same instance is always returned.

* All variables and modifications affect the same shared object.

🔹 When to use it?

* When you need to control a single resource (for example, a database connection such as SQLite or PostgreSQL).
* When you need a global access point to shared configuration.
* When the object is expensive to create and should not be duplicated.

🔹 Key Idea

There are no multiple synchronized instances.  
There is only one shared instance across the entire system.

🧠 Even Simpler Explanation (for personal notes)

Singleton =
* 1 class
* 1 object
* Global access
* Shared state

##### Factory Method:

The Factory Method is a creational design pattern that defines an interface for creating objects, but allows subclasses to decide which concrete class to instantiate.

* Instead of creating objects directly using a constructor, the creation process is delegated to a special method called the "factory method".

* It makes the code more flexible and loosely coupled, since the creation logic is separated from the object’s usage.

🔹 When to use it?

* When you do not know beforehand which exact class you will need to instantiate.
* When you want to delegate the creation responsibility to subclasses.
* When you want to reduce coupling between client code and concrete classes.
* When you need to extend object creation without modifying existing code (open/closed principle).

🔹 Key Idea

The client does not create objects directly.  
The client uses a method that decides which type of object to create.

🧠 Even Simpler Explanation (for personal notes)

Factory Method =
* Defines a method to create objects
* Subclass decides which object to create
* Decouples creation from usage
* Makes code easier to extend
