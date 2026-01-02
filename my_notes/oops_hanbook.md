## Key Difference Between Class (static) & Instance Variables
| Feature                      | **Class Variable (static)** | **Instance Variable**      | 
| ---------------------------- |-----------------------------| -------------------------- |
| Official Python Term         | Class variable              | Instance variable          | 
| Defined Where                | Inside class body           | Inside methods using `self` | 
| Belongs To                   | Class                       | Object (instance)          | 
| Memory Allocation            | One shared copy             | Separate copy per object   | 
| Shared Between Objects       | ✅ Yes                       | ❌ No                       | 
| Access Using                 | `Class.var` / `obj.var`     | `obj.var`                  | 
| Modified Correctly Using     | Class name / class method   | Object                     | 
| Instance Modification Effect | Creates instance variable   | Changes that object only   | 
| Lifetime                     | Entire program              | Until object exists        | 
| Java/C++ Equivalent          | `static` variable           | Non-static variable        |
| Typical Use Case             | Common/shared data          | Object-specific data       |


## Key Difference Between Instance, Static, Class Methods
| Feature                       | **Instance Method**      | **Static Method**                 | **Class Method**                  |
| ----------------------------- | ------------------------ | --------------------------------- | --------------------------------- |
| Method Type                   | Object-level method      | Utility / helper method           | Class-level method                |
| Decorator Used                | ❌ No decorator           | `@staticmethod`                   | `@classmethod`                    |
| First Parameter               | `self`                   | ❌ None                            | `cls`                             |
| Bound To                      | Object (instance)        | ❌ Not bound                       | Class                             |
| Can Access Instance Variables | ✅ Yes                    | ❌ No                              | ❌ No                              |
| Can Access Class Variables    | ✅ Yes                    | ❌ No (only via class name)        | ✅ Yes                             |
| Can Modify Instance State     | ✅ Yes                    | ❌ No                              | ❌ No                              |
| Can Modify Class State        | ⚠️ Yes (not recommended) | ❌ No                              | ✅ Yes                             |
| Automatic Argument Passed     | Object reference         | ❌ None                            | Class reference                   |
| Invocation Style              | `obj.method()`           | `Class.method()` / `obj.method()` | `Class.method()` / `obj.method()` |
| Internal Call Form            | `Class.method(obj)`      | `method()`                        | `Class.method(cls)`               |
| Inheritance Friendly          | ✅ Yes                    | ⚠️ Limited                        | ✅ Best                            |
| Typical Use Case              | Object behavior          | Validation / utility logic        | Factory methods, class config     |
| Memory Binding                | Bound method             | Plain function                    | Bound to class                    |
