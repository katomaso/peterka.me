Title: Go - arrays versus slices
Summary: A small experiment with mutability of items in arrays and slices.
Category: Coding
Date: 2020-04-30
Author: Tomas Peterka

Let's dive in the beautiful Go syntax and let's see what happens when you modify items in arrays and slices.

We will work on array/slices of simple structure. Why? Because we can.
```go
type X struct {
  Id int
  Str string
}
```

And now the differences between constructing an array and a slice
```go
xa := [...]X {{1, "a"}, {2, "b"}}
```
Array construction contains those `...` as a placeholder for a number yet unknown but known to-be-inserted by the compiler (so we don't need to because we are lazy). Following by typed `X{}` inside which are only `{}` without type specification.

```go
xs := []X {X{1, "a"}, X{2, "b"}}
```
Contrary to that, slices have clean `[]X` type followed by list of constructors. I find it elegant.

Let's apply functions that take array/slice by value and than modify them.
```go
func modXa(xa [2]X) { xa[1].Id = 3 }
func modXs(xs []X)   { xs[1].Id = 3 }
```

Now the grand final
```go
modXa(xa)
modXs(xs)
fmt.Printf("modified array: X[1].id = %d\n", xa[1].Id)
fmt.Printf("modified slice: X[1].id = %d\n", xs[1].Id)
```

As you can already guess - the output will be 
```go
"modified array: X[1].id = 2"
"modified slice: X[1].id = 3"
```

Arrays are copied in full when passed by value! Therefore the original content was left unmodified. However slices, when passed by value, will get modified. That's because they hold a pointer to an array internally. This is actually obvious from [effective go](https://golang.org/doc/effective_go.html#allocation_make) part where they have a code sample
```go
var p *[]int = new([]int) // allocates slice structure; *p == nil; rarely useful
```
that states that a slice is nothing but a pointer to an array.