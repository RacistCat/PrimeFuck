# PrimeFuck
A even harder language than brainfuck. Not as hard as malbolge tho.
```
prime(x) = xth prime
Instructions:
p - mem[data_ptr] = prime(mem[data_ptr] + 1)
d - mem[data_ptr] //= 2
^ - data_ptr = prime(data_ptr + 1)
v - data_ptr //= 2
. - print(chr(mem[data_ptr]))
, - mem[data_ptr] = prime(get_char())
[ - jump to matching "[" if mem[data_ptr] == 0
] - jump to matching "]" if mem[data_ptr] != 0
Programs:
* helloworld.pf - print "Hello, World!". size: ~3KB

```
