## Special / Meta Characters
| Symbol  | Meaning                      |    |
| ------- | ---------------------------- | -- |
| `.`     | Any character except newline |    |
| `^`     | Start of string              |    |
| `$`     | End of string                |    |
| `*`     | 0 or more                    |    |
| `+`     | 1 or more                    |    |
| `?`     | 0 or 1                       |    |
| `{m,n}` | Range repetition             |    |
| `[]`    | Character class              |    |
| `()`    | Group                        |    |
| `       | `                            | OR |
| `\`     | Escape character             |    |
## Predefined Character Sets
| Pattern | Meaning                   |
| ------- | ------------------------- |
| `\d`    | Digit (0–9)               |
| `\D`    | Not digit                 |
| `\w`    | Word char (a-z A-Z 0-9 _) |
| `\W`    | Not word                  |
| `\s`    | Whitespace                |
| `\S`    | Not whitespace            |
| `\b`    | Word boundary             |
| `\B`    | Not word boundary         |
## Quantifiers (Used For Repetition)
| Quantifier | Meaning   |
| ---------- | --------- |
| `*`        | 0 or more |
| `+`        | 1 or more |
| `?`        | 0 or 1    |
| `{n}`      | Exactly n |
| `{n,}`     | n or more |
| `{n,m}`    | n to m    |


## Anchors / Boundaries
| Anchor | Meaning                               |
| ------ |---------------------------------------|
| `^`    | Start of string                       |
| `$`    | End of string                         |
| `\b`   | Word boundary (start/end of the word) |

## Core re Module Functions
    1.re.match()
        # Matches only at start
        re.match("cat", "cat is here")   # match
        re.match("cat", "the cat")       # no match

    2.re.search()
      # Search anywhere
      re.search("cat", "the cat is here") #True
    
    3.re.findall()
      # Returns all matches as list
      re.findall("\d+", "a12 b34 c56") # ['12', '34', '56']

    4. re.split()
       # Split String using regular expression
       re.split("[,; ]+", "apple, banana; mango") 

    5. re.sub()
       # Replace matches
       re.sub("\d", "#", "abc123") # o/p ->  abc###
    
    6.re.compile()
      # pre-compiled regular expression
      # best for repeated use as its reduces performance overload
      pattern = re.compile("\d+")
      pattern.findall("a12 b34")




## Match Objects
    When search() or match() succeeds:
| Method        | Meaning                                                                |
| ------------- |------------------------------------------------------------------------|
| `group()`     | matched text                                                           |
| `groups()`    | tuple of groups                                                        |
| `groupdict()` | Returns dictionary of group<br/>syntax:<br/>{group_name: matched_text}<br/>for mising group value is None 
    |
| `start()`     | start index                                                            |
| `end()`       | end index                                                              |
| `span()`      | (start, end)<br>start -> inclusive<br/>end -> exclusive                |



