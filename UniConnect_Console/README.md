 <center><h1>UniConnect - The Console</h1></center>

This directory contains the initial implementation of the UniConnect project, designed to manage academic data for a university department. This version includes a console interface that allows users to manage various entities within the system, such as students, lecturers, courses, and more. The console supports commands to create, update, delete, and view records, with persistent storage using JSON serialization/deserialization.

---

<center><h3>Repository Contents by Project Task</h3></center>

| Tasks | Files | Description |
| ----- | ----- | ----------- |
| 0: Authors/README File | [AUTHORS](https://github.com/mosignorjude/UniConnect/blob/main/AUTHORS) | Project authors |
| 1: Pep8 | N/A | All code adheres to PEP8 standards |
| 2: Unit Testing | [/tests](https://github.com/mosignorjude/UniConnect/tree/main/tests) | Unit tests for all core modules |
| 3. BaseModel Implementation | [/models/base_model.py](https://github.com/mosignorjude/UniConnect/blob/main/models/base_model.py) | Defines the parent class for all models |
| 4. BaseModel with kwargs | [/models/base_model.py](https://github.com/mosignorjude/UniConnect/blob/main/models/base_model.py) | Enhances BaseModel to support dictionary-based instantiation |
| 5. FileStorage Class | [/models/engine/file_storage.py](https://github.com/mosignorjude/UniConnect/blob/main/models/engine/file_storage.py) [/models/__init__.py](https://github.com/yourusername/UniConnect/blob/main/models/__init__.py) [/models/base_model.py](https://github.com/yourusername/UniConnect/blob/main/models/base_model.py) | Manages persistent file storage using JSON |
| 6. Console 0.0.1 | [console.py](https://github.com/mosignorjude/UniConnect/blob/mosignor/UniConnect_v0/console.py | Initial console implementation with basic command handling |
| 7. Console 0.1 | [console.py](https://github.com/mosignorjude/UniConnect/blob/mosignor/UniConnect_v0/console.py) | Expanded console functionality for managing records |
| 8. User Class | [console.py](https://github.com/mosignorjude/UniConnect/blob/mosignor/UniConnect_v0/console.py) [/models/engine/file_storage.py](https://github.com/mosignorjude/UniConnect/blob/mosignor/UniConnect_v0/models/engine/file_storage.py) [/models/user.py](https://github.com/yourusername/UniConnect/blob/main/models/user.py) | Implements the User class with dynamic features |
| 9. Additional Classes | [/models/user.py](https://github.com/mosignorjude/UniConnect/blob/main/models/user.py) [/models/course.py](https://github.com/yourusername/UniConnect/blob/main/models/course.py) [/models/lecturer.py](https://github.com/yourusername/UniConnect/blob/main/models/lecturer.py) | Adds more classes for the application |
| 10. Console 1.0 | [console.py](https://github.com/mosignorjude/UniConnect/blob/main/console.py) [/models/engine/file_storage.py](https://github.com/yourusername/UniConnect/blob/main/models/engine/file_storage.py) | Finalizes console and file storage integration |

<br>
<br>
<center><h2>General Use</h2></center>

1. Clone this repository using the following command:

    ```bash
    git clone https://github.com/mosignorjude/UniConnect.git
    ```

2. Navigate to the project directory:

    ```bash
    cd UniConnect
    ```

3. Locate the `console.py` file and run it:

    ```bash
    python console.py
    ```

4. The following prompt will appear:

    ```bash
    (uniconnect)
    ```

5. This prompt indicates that you are in the UniConnect console, where you can use various commands to manage the system.

##### Commands

- `create` - Creates a new instance of the specified class
- `destroy` - Deletes an existing object by class and ID
- `show` - Displays details of an object by class and ID
- `all` - Lists all objects or all objects of a specified class
- `update` - Updates attributes of an existing object by class and ID
- `quit` - Exits the console (EOF will also terminate the session)

##### Alternative Syntax

Advanced syntax for commands allows more flexible interactions:

    Usage: <class_name>.<command>([<id>[name_arg value_arg]|[kwargs]])

Advanced command examples:

- `all` - Lists all objects or all objects of a given class
- `count` - Returns the number of instances of a class
- `show` - Displays an object based on class and ID
- `destroy` - Deletes an object based on class and ID
- `update` - Updates attributes of an object by class and ID

<br>
<br>
<center><h2>Examples</h2></center>

<h3>Primary Command Syntax</h3>

###### Example 0: Create an object
Usage: `create <class_name>`

    ```bash
    (uniconnect) create User
    ```

    ```bash
    (uniconnect) create User
    3aa5babc-efb6-4041-bfe9-3cc9727588f8
    ```

###### Example 1: Show an object
Usage: `show <class_name> <id>`

    ```bash
    (uniconnect) show User 3aa5babc-efb6-4041-bfe9-3cc9727588f8
    [User] (3aa5babc-efb6-4041-bfe9-3cc9727588f8) {'id': '3aa5babc-efb6-4041-bfe9-3cc9727588f8', 'created_at': datetime.datetime(2024, 8, 27, 14, 21, 12, 96959), 'updated_at': datetime.datetime(2024, 8, 27, 14, 21, 12, 96971)}
    ```

###### Example 2: Destroy an object
Usage: `destroy <class_name> <id>`

    ```bash
    (uniconnect) destroy User 3aa5babc-efb6-4041-bfe9-3cc9727588f8
    (uniconnect) show User 3aa5babc-efb6-4041-bfe9-3cc9727588f8
    ** no instance found **
    ```

###### Example 3: Update an object
Usage: `update <class_name> <id> <attribute_name> <attribute_value>`

    ```bash
    (uniconnect) update User 3aa5babc-efb6-4041-bfe9-3cc9727588f8 first_name "John"
    (uniconnect) show User 3aa5babc-efb6-4041-bfe9-3cc9727588f8
    [User] (3aa5babc-efb6-4041-bfe9-3cc9727588f8) {'id': '3aa5babc-efb6-4041-bfe9-3cc9727588f8', 'created_at': datetime.datetime(2024, 8, 27, 14, 21, 12, 96959), 'updated_at': datetime.datetime(2024, 8, 27, 14, 21, 12, 96971), 'first_name': 'John'}
    ```

<h3>Alternative Syntax</h3>

###### Example 0: Show all User objects
Usage: `User.all()`

    ```bash
    (uniconnect) User.all()
    ["[User] (99f45908-1d17-46d1-9dd2-b7571128115b) {'updated_at': datetime.datetime(2024, 8, 27, 14, 21, 12, 96959), 'id': '99f45908-1d17-46d1-9dd2-b7571128115b', 'created_at': datetime.datetime(2024, 8, 27, 14, 21, 12, 96959)}"]
    ```

###### Example 1: Destroy a User
Usage: `User.destroy(<id>)`

    ```bash
    (uniconnect) User.destroy("99f45908-1d17-46d1-9dd2-b7571128115b")
    (uniconnect) User.all()
    ```

###### Example 2: Update User (by attribute)
Usage: `User.update(<id>, <attribute_name>, <attribute_value>)`

    ```bash
    (uniconnect) User.update("98bea5de-9cb0-4d78-8a9d-c4de03521c30", "name", "Alice")
    (uniconnect) User.all()
    ```

###### Example 3: Update User (by dictionary)
Usage: `User.update(<id>, <dictionary>)`

    ```bash
    (uniconnect) User.update("98bea5de-9cb0-4d78-8a9d-c4de03521c30", {'name': 'Bob', 'age': 25})

