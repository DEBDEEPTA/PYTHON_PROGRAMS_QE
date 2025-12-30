# seek() & tail()
## _1.What is the File Pointer (Cursor)?_
    When a file is opened, Python maintains an internal pointer (also called a cursor).
    👉 This pointer: Marks the current position in the file
                     Moves automatically when you read or write
                     Determines where the next read/write happens


## _2. tell() vs Seek()_
    🔑 Facats
         -> tell() returns current cursor position
         -> seek() moves the file pointer
         -> Text mode has restricted seek
         -> Binary mode offers full pointer control
| Function     | Purpose                            |
| ------------ |------------------------------------|
| `tell()`     | Get current position               |
| `seek()`     | Move pointer                       |
| `seek(0)`    | Reset pointer                      |
| `seek(0, 2)` | Go to EOF (check binary file size) |

## _3.tell()_
```
    with open("data.txt", "r") as f:
    print(f.tell())     # 0
    f.read(5)           # pointer moves to read next 5 characters
    print(f.tell())     # 5
```
    🔍 Explanation
       File opens → pointer at 0
       read(5) reads 5 characters → pointer moves to 5

## _4.seek()_
```
    file.seek(offset, whence=0)
```
| Parameter | Meaning                    |
| --------- | -------------------------- |
| `offset`  | Number of bytes/characters |
| `whence`  | Reference point            |

| whence value | Meaning                     |
|--------------| --------------------------- |
| `0`          | Beginning of file (default) |
| `1`          | Current position            |
| `2`          | End of file                 |

| Text Mode Limitation                                                                                                   | Binary Mode(full Control)                                                           |
|------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------|
| 1. seek() only reliable with whence=0<br>2. Offset counts characters, not raw bytes<br>3. Negative offsets not allowed | 1. Offset counts bytes<br>2. All whence values allowed<br>3. Negative seeks allowed |




