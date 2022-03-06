<p align = "center">
<img src = https://holbertonintranet.s3.amazonaws.com/uploads/medias/2018/6/65f4a1dd9c51265f49d0.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOU5BHMTQX4%2F20220303%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20220303T122422Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=8e93fb013130b64f89742abd43888ad97eac0e0bdb922864911bc59ac205063f>
</p>

# Background context
## Welcome to the AirBnB clone project!
### First step: Write a command interpreter to manage your AirBnB objects.

This is the first step towards building our first full web application: the AirBnB clone. This first step is very important because we will use what you build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration…

Each task is linked and will help us to:

- put in place a parent class (called BaseModel) to take care of the initialization, serialization and deserialization of our future instances
- create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
- create all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel
- create the first abstracted storage engine of the project: File storage.
- create all unittests to validate all our classes and storage engine

<p align = "center">
<img src = https://holbertonintranet.s3.amazonaws.com/uploads/medias/2018/6/815046647d23428a14ca.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOU5BHMTQX4%2F20220306%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20220306T170951Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=b6f955ca6e7ed5e76cb68221e3c94e0e6726e5dfbe8036694bbfb2e7d7a2439e>
</p>

## What’s a command interpreter?
Do you remember the Shell? It’s exactly the same but limited to a specific use-case. In our case, we want to be able to manage the objects of our project:

- Create a new object (ex: a new User or a new Place)
- Retrieve an object from a file, a database etc…
- Do operations on objects (count, compute stats, etc…)
- Update attributes of an object
- Destroy an object

# Ressources
**Read or watch:**
- [Python abstract classes](https://intranet.hbtn.io/rltoken/5Dv7z90qa94hYqtPRCe_wA)
- [cmd module](https://intranet.hbtn.io/rltoken/Fx9HXIjmGzbmET4ylYg2Rw)
- [uuid module](https://intranet.hbtn.io/rltoken/eaQ6aELbdqb0WmPddhD00g)
- [datetime](https://intranet.hbtn.io/rltoken/_ySDcgtfrwLkTyQzYHTH0Q)
- [unittest module](https://intranet.hbtn.io/rltoken/QX7d4D__xhOJIGIWZBp39g)
- [args/kwargs](https://intranet.hbtn.io/rltoken/jQd3P_uSO0FeU6jlN-z5mg)
- [Python test cheatsheet](https://intranet.hbtn.io/rltoken/WPlydsqB0PG0uVcixemv9A)

# Learning Objectives
At the end of this project, we are expected to be able to explain to anyone, **without the help of Google**:
## General

- How to create a Python package
- How to create a command interpreter in Python using the cmd module
- What is Unit testing and how to implement it in a large project
- How to serialize and deserialize a Class
- How to write and read a JSON file
- How to manage datetime
- What is an UUID
- What is *args and how to use it
- What is **kwargs and how to use it
- How to handle named arguments in a function

# Requirements
## Python Scripts
- Allowed editors: ```vi```, ```vim```, ```emacs```
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All your files should end with a new line
- The first line of all your files should be exactly ```#!/usr/bin/python3```
- A ```README.md``` file, at the root of the folder of the project, is mandatory
- Your code should use the pycodestyle (version 2.7.*)
- All your files must be executable
- The length of your files will be tested using ```wc```
- All your modules should have a documentation (```python3 -c 'print(__import__("my_module").__doc__)' ```)
- All your classes should have a documentation (```python3 -c 'print(__import__("my_module").MyClass.__doc__)' ```)
- All your functions (inside and outside a class) should have a documentation (```python3 -c 'print(__import__("my_module").my_function.__doc__)' ```and ```python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)' ```)
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)

## Python Unit Tests
- Allowed editors: ```vi```, ```vim```, ```emacs```
- All your files should end with a new line
- All your test files should be inside a folder ```tests```
- You have to use the unittest module
- All your test files should be python files (extension: ```.py```)
- All your test files and folders should start by ```test_```
- Your file organization in the tests folder should be the same as your project
- e.g., For models/base_model.py, unit tests must be in: tests/test_models/test_base_model.py
- e.g., For ```models/user.py```, unit tests must be in: ```tests/test_models/test_user.py```
- All your tests should be executed by using this command: ```python3 -m unittest discover tests```
- You can also test file by file by using this command: ```python3 -m unittest tests/test_models/test_base_model.py```
- All your modules should have a documentation (```python3 -c 'print(__import__("my_module").__doc__)' ```)
- All your classes should have a documentation (``` python3 -c 'print(__import__("my_module").MyClass.__doc__)' ```)
- All your functions (inside and outside a class) should have a documentation (```python3 -c 'print(__import__("my_module").my_function.__doc__)' ``` and ```python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)' ```)
- We strongly encourage you to work together on test cases, so that you don’t miss any edge case


# More Info
## Execution
Our shell should work like this in interactive mode:
```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```

But also in non-interactive mode: (like the Shell project in C)

```$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```

All tests should also pass in non-interactive mode: ```$ echo "python3 -m unittest discover tests" | bash```


## Run commands
To open the console, run:
```
$ ./conole.py
```

We can run different commands in our console:
- ```help``` (+ method): gives informations about methods

```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update

(hbnb)help create
Creates a new instance of BaseModel, saves it and prints the id
        Usage: create <class name> or <class name>.create()
        

```

- ```quit``` & ```EOF```: exits the console

```
(hbnb) quit
$
```

- ```create``` + class name or class name.create(): creates a new instance and prints its id. We can create many objects: ```BaseModel```, ```User```, ```Place```, ```City```, ```Review```, ```Amenity```, ```State```.

```
(hbnb) create BaseModel
f8224de5-af1a-431c-847f-2f4f018abe45
(hbnb) create User
c9500bd3-bedc-4bb1-8ab8-2c5d6744b7dd
(hbnb) create State
7cfb7054-699a-4caa-bd0f-eb777b092edf
(hbnb) create Review
fc512277-5e46-4e55-845d-3bdf91c62e68
(hbnb) create City
a177a9d7-fc3d-4f7f-aed7-a8511f649dc8
(hbnb) create Place
09d73f3d-47be-4c79-806b-db24f09640e6
(hbnb) create Amenity
a60cbb5b-16ae-42c2-a6af-48bf5244f6b2
(hbnb) create
** class name missing **
(hbnb) create Country
** class doesn't exist **
```

- ```show``` + id or class name.show(id): Prints the string representation of an instance based on the class name and id.

```
(hbnb) show
** class name missing **
(hbnb) show f8224de5-af1a-431c-847f-2f4f018abe45
** class doesn't exist **
(hbnb) show User f8224de5-af1a-431c-847f-2f4f018abe45
** no instance found **
(hbnb) show BaseModel f8224de5-af1a-431c-847f-2f4f018abe45
[BaseModel] (f8224de5-af1a-431c-847f-2f4f018abe45) {'id': 'f8224de5-af1a-431c-847f-2f4f018abe45', 'created_at': datetime.datetime(2022, 3, 6, 18, 53, 31, 735220), 'updated_at': datetime.datetime(2022, 3, 6, 18, 53, 31, 735268)}
```

- ```destroy``` + id or class name.destroy(id): Deletes an instance based on the class name and id.

```
(hbnb) destroy
** class name missing **
(hbnb) destroy User f8224de5-af1a-431c-847f-2f4f018abe45
** no instance found **
(hbnb) destroy BaseModel f8224de5-af1a-431c-847f-2f4f018abe45
(hbnb) show BaseModel f8224de5-af1a-431c-847f-2f4f018abe45
** no instance found **
```

- ```all``` or class name.all(): Prints all string representation of all instances based or not on the class name.

```
(hbnb) all
["[User] (c9500bd3-bedc-4bb1-8ab8-2c5d6744b7dd) {'id': 'c9500bd3-bedc-4bb1-8ab8-2c5d6744b7dd', 'created_at': datetime.datetime(2022, 3, 6, 18, 53, 34, 929740), 'updated_at': datetime.datetime(2022, 3, 6, 18, 53, 34, 929784)}", "[State] (7cfb7054-699a-4caa-bd0f-eb777b092edf) {'id': '7cfb7054-699a-4caa-bd0f-eb777b092edf', 'created_at': datetime.datetime(2022, 3, 6, 18, 53, 38, 807636), 'updated_at': datetime.datetime(2022, 3, 6, 18, 53, 38, 807678)}", "[Review] (fc512277-5e46-4e55-845d-3bdf91c62e68) {'id': 'fc512277-5e46-4e55-845d-3bdf91c62e68', 'created_at': datetime.datetime(2022, 3, 6, 18, 53, 42, 826370), 'updated_at': datetime.datetime(2022, 3, 6, 18, 53, 42, 826421)}", "[City] (a177a9d7-fc3d-4f7f-aed7-a8511f649dc8) {'id': 'a177a9d7-fc3d-4f7f-aed7-a8511f649dc8', 'created_at': datetime.datetime(2022, 3, 6, 18, 53, 45, 986319), 'updated_at': datetime.datetime(2022, 3, 6, 18, 53, 45, 986364)}", "[Place] (09d73f3d-47be-4c79-806b-db24f09640e6) {'id': '09d73f3d-47be-4c79-806b-db24f09640e6', 'created_at': datetime.datetime(2022, 3, 6, 18, 54, 2, 608003), 'updated_at': datetime.datetime(2022, 3, 6, 18, 54, 2, 608051)}", "[Amenity] (a60cbb5b-16ae-42c2-a6af-48bf5244f6b2) {'id': 'a60cbb5b-16ae-42c2-a6af-48bf5244f6b2', 'created_at': datetime.datetime(2022, 3, 6, 18, 54, 6, 475410), 'updated_at': datetime.datetime(2022, 3, 6, 18, 54, 6, 475470)}"]
(hbnb) all User
["[User] (c9500bd3-bedc-4bb1-8ab8-2c5d6744b7dd) {'id': 'c9500bd3-bedc-4bb1-8ab8-2c5d6744b7dd', 'created_at': datetime.datetime(2022, 3, 6, 18, 53, 34, 929740), 'updated_at': datetime.datetime(2022, 3, 6, 18, 53, 34, 929784)}"]
(hbnb) all Country
** class doesn't exist **
```

- ```update``` + class name + id + attribute name + attribute value or class name.```update```(id, attribute name, attribute value): Updates an instance based on the class name and id by adding or updating attribute

```
(hbnb) update
** class name missing **
(hbnb) update User
** instance id missing **
(hbnb) update User c9500bd3-bedc-4bb1-8ab8-2c5d6744b7dd
** attribute name missing **
(hbnb) update User c9500bd3-bedc-4bb1-8ab8-2c5d6744b7dd name
** value missing **
(hbnb) update User c9500bd3-bedc-4bb1-8ab8-2c5d6744b7dd name "John"
(hbnb) show User c9500bd3-bedc-4bb1-8ab8-2c5d6744b7dd
[User] (c9500bd3-bedc-4bb1-8ab8-2c5d6744b7dd) {'id': 'c9500bd3-bedc-4bb1-8ab8-2c5d6744b7dd', 'created_at': datetime.datetime(2022, 3, 6, 18, 53, 34, 929740), 'updated_at': datetime.datetime(2022, 3, 6, 19, 0, 52, 347755), 'name': 'John'}
```

- ```count``` + class name or class name.count(): retrieves the number of instances of a class:

```
(hbnb) BaseModel.count()
0
(hbnb) User.count()
1
(hbnb) create User
21cea46d-5b61-430c-ab3c-6ed34536d8f5
(hbnb) User.count()
2
```

## Cloning the repo
To clone this repository, run the command:
```
git clone git@github.com:rmarcais/AirBnB_clone.git
```

## Authors

| Élodie Riou | Rémi Marçais |
|:---:|:---:|
|<a href="https://www.linkedin.com/in/ivan-mickisz-550222222/"> <img alt="Ivan Mickisz Linkedin" width="40px" src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/LinkedIn_logo_initials.png/768px-LinkedIn_logo_initials.png"> <a href="https://github.com/IMickisz"> <img alt="Élodie Riou Github" width="40px" src="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png"> | <a href="https://www.linkedin.com/in/r%C3%A9mi-mar%C3%A7ais-274a4421a/"> <img alt="Rémi Marçais Linkedin" width="40px" src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/LinkedIn_logo_initials.png/768px-LinkedIn_logo_initials.png"> <a href="https://github.com/rmarcais"> <img alt="Elodie RIOU Github" width="40px" src="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png"> |
