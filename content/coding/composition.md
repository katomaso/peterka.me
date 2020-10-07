Title: Composition in Go
Summary: Composition is one of two principles of object oriented programming 
Category: Coding
Date: 2018-06-28

Composition is abbreviated as HAS-A whereas inheritance as IS-A. Example
could be that a class Dog IS-AN animal while HAS-A head, tail, and legs.

Composition is the only object oriented design available in Go programming language.
There is, indeed, an illusion of inheritance. Go propagates methods of inner types
to the outer types. However, attributes are not propagated altogether. Thus a method
relying on re-definition will not work.

I did [a small experiment](https://play.golang.org/p/h8xIszoUjKp) to illustrate my words.

```
package main

import "fmt"

type Dog struct {
  sound string
}

type Chiwawa struct {
  Dog
  sound string
}

func (dog Dog) bark() {
  fmt.Println(dog.sound)
}

func main() {
  var (
    dog = Dog{"whaf"}
    chw = Chiwawa{dog, "squeek"}
  )
  
  dog.bark()
  chw.bark()
}
```

Outputs

```
whaf
whaf
```