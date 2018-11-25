Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 26 2018, 23:26:24)
[Clang 6.0 (clang-600.0.57)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> s1 = "spam"
>>> s2 = "ni"
>>> "The Knights who say, " +s2
'The Knights who say, ni'

>>> 3 * s1 + 2 * s2
'spamspamspamnini'

>>> s1[1]
'p'

>>> s1[1:3]
'pa'

>>> s1[2] + s2[:2]
'ani'


>>> s2.upper().ljust(4) * 3
'NI  NI  NI  '

>>> [s1, s2[:-1]]
['spam', 'n']

>>> for ch in "aardvark":
	print(ch)

a
a
r
d
v
a
r
k


>>> for w in "Now is the winter of our discontent...".split():
	print(w)


Now
is
the
winter
of
our
discontent...

>>> for w in "Mississippi".split("i"):
	print(w, end=" ")
M ss ss pp


>>> msg = ""
>>> for s in "secret".split("e")

>>> for s in "secret".split("e"):
	msg = msg + chr(ord(ch)+1)
print(msg)
SyntaxError: invalid syntax
>>>
>>> "Looks like {1} and {0} for breakfast".format("eggs", "spam")
'Looks like spam and eggs for breakfast'
>>>
>>> "Hello {0}".format("Susan", "Computewell")
'Hello Susan'
>>> "{0:0.2f} {0:0.2f}".format(2.3, 2.3458)
'2.30 2.30'
>>> "{7.5f} {7.5f}".format(2.3, 2.3468)
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    "{7.5f} {7.5f}".format(2.3, 2.3468)
IndexError: tuple index out of range
>>> "Time left {0:02}:{1:05.2f}".format(1,37.374)
'Time left 01:37.37'
>>> "{1:3}".format("14")
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    "{1:3}".format("14")
IndexError: tuple index out of range
>>>
