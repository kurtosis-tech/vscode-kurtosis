# This file was generated by `make builtins` based on the spec at:
# https://raw.githubusercontent.com/google/starlark-go/master/doc/spec.md

def abs(x):
  """`abs(x)` returns the absolute value of its argument `x`, which must be an int or float. The result has the same type as `x`."""
  pass

def any(x) -> bool:
  """`any(x)` returns `True` if any element of the iterable sequence x has a truth value of true. If the iterable is empty, it returns `False`."""
  pass

def all(x) -> bool:
  """`all(x)` returns `False` if any element of the iterable sequence x has a truth value of false. If the iterable is empty, it returns `True`."""
  pass

def bool(x) -> bool:
  """`bool(x)` interprets `x` as a Boolean value---`True` or `False`. With no argument, `bool()` returns `False`."""
  pass

def chr(i):
  """`chr(i)` returns a string that encodes the single Unicode code point whose value is specified by the integer `i`. `chr` fails unless 0 ≤ `i` ≤ 0x10FFFF."""
  pass

def dict() -> Dict:
  """`dict` creates a dictionary.  It accepts up to one positional argument, which is interpreted as an iterable of two-element sequences (pairs), each specifying a key/value pair in the resulting dictionary."""
  pass

def dir(x) -> List[String]:
  """`dir(x)` returns a new sorted list of the names of the attributes (fields and methods) of its operand. The attributes of a value `x` are the names `f` such that `x.f` is a valid expression."""
  pass

def enumerate(x) -> List[Tuple[int, any]]:
  """`enumerate(x)` returns a list of (index, value) pairs, each containing successive values of the iterable sequence xand the index of the value within the sequence."""
  pass

def fail(*args, sep=" "):
  """The `fail(*args, sep=" ")` function causes execution to fail with the specified error message. Like `print`, arguments are formatted as if by `str(x)` and separated by a space, unless an alternative separator is specified by a `sep` named argument."""
  pass

def float(x) -> float:
  """`float(x)` interprets its argument as a floating-point number."""
  pass

def getattr(x, name):
  """`getattr(x, name)` returns the value of the attribute (field or method) of x named `name`. It is a dynamic error if x has no such attribute."""
  pass

def hasattr(x, name) -> bool:
  """`hasattr(x, name)` reports whether x has an attribute (field or method) named `name`."""
  pass

def hash(x) -> int:
  """`hash(x)` returns an integer hash of a string x such that two equal strings have the same hash. In other words `x == y` implies `hash(x) == hash(y)`."""
  pass

def int(x) -> int:
  """`int(x[, base])` interprets its argument as an integer."""
  pass

def len(p) -> int:
  """`len(p)` returns the number of elements in its argument."""
  pass

def list() -> List:
  """`list` constructs a list."""
  pass

def max(x):
  """`max(x)` returns the greatest element in the iterable sequence x."""
  pass

def min(x):
  """`min(x)` returns the least element in the iterable sequence x."""
  pass

def ord(s):
  """`ord(s)` returns the integer value of the sole Unicode code point encoded by the string `s`."""
  pass

def print(*args, sep=" "):
  """`print(*args, sep=" ")` prints its arguments, followed by a newline. Arguments are formatted as if by `str(x)` and separated with a space, unless an alternative separator is specified by a `sep` named argument."""
  pass

def range() -> List[int]:
  """`range` returns an immutable sequence of integers defined by the specified interval and stride."""
  pass

def repr(x) -> String:
  """`repr(x)` formats its argument as a string."""
  pass

def reversed(x) -> List:
  """`reversed(x)` returns a new list containing the elements of the iterable sequence x in reverse order."""
  pass

def set(x):
  """`set(x)` returns a new set containing the elements of the iterable x. With no argument, `set()` returns a new empty set."""
  pass

def sorted(x) -> List:
  """`sorted(x)` returns a new list containing the elements of the iterable sequence x, in sorted order.  The sort algorithm is stable."""
  pass

def str(x) -> String:
  """`str(x)` formats its argument as a string."""
  pass

def tuple(x):
  """`tuple(x)` returns a tuple containing the elements of the iterable x."""
  pass

def type(x) -> String:
  """type(x) returns a string describing the type of its operand."""
  pass

def zip() -> List:
  """`zip()` returns a new list of n-tuples formed from corresponding elements of each of the n iterable sequences provided as arguments to `zip`.  That is, the first tuple contains the first element of each of the sequences, the second tuple contains the second element of each of the sequences, and so on.  The result list is only as long as the shortest of the input sequences."""
  pass

class Dict:
  def clear(self):
    """`D.clear()` removes all the entries of dictionary D and returns `None`. It fails if the dictionary is frozen or if there are active iterators."""
    pass

  def get(self, key):
    """`D.get(key[, default])` returns the dictionary value corresponding to the given key. If the dictionary contains no such value, `get` returns `None`, or the value of the optional `default` parameter if present."""
    pass

  def items(self) -> List:
    """`D.items()` returns a new list of key/value pairs, one per element in dictionary D, in the same order as they would be returned by a `for` loop."""
    pass

  def keys(self) -> List:
    """`D.keys()` returns a new list containing the keys of dictionary D, in the same order as they would be returned by a `for` loop."""
    pass

  def pop(self, key):
    """`D.pop(key[, default])` returns the value corresponding to the specified key, and removes it from the dictionary.  If the dictionary contains no such value, and the optional `default` parameter is present, `pop` returns that value; otherwise, it fails."""
    pass

  def popitem(self):
    """`D.popitem()` returns the first key/value pair, removing it from the dictionary."""
    pass

  def setdefault(self, key):
    """`D.setdefault(key[, default])` returns the dictionary value corresponding to the given key. If the dictionary contains no such value, `setdefault`, like `get`, returns `None` or the value of the optional `default` parameter if present; `setdefault` additionally inserts the new key/value entry into the dictionary."""
    pass

  def update(self) -> None:
    """`D.update([pairs][, name=value[, ...])` makes a sequence of key/value insertions into dictionary D, then returns `None.`"""
    pass

  def values(self) -> List:
    """`D.values()` returns a new list containing the dictionary's values, in the same order as they would be returned by a `for` loop over the dictionary."""
    pass

class List:
  def append(self, x) -> None:
    """`L.append(x)` appends `x` to the list L, and returns `None`."""
    pass

  def clear(self) -> None:
    """`L.clear()` removes all the elements of the list L and returns `None`. It fails if the list is frozen or if there are active iterators."""
    pass

  def extend(self, x) -> None:
    """`L.extend(x)` appends the elements of `x`, which must be iterable, to the list L, and returns `None`."""
    pass

  def index(self, x) -> int:
    """`L.index(x[, start[, end]])` finds `x` within the list L and returns its index."""
    pass

  def insert(self, i, x) -> None:
    """`L.insert(i, x)` inserts the value `x` in the list L at index `i`, moving higher-numbered elements along by one.  It returns `None`."""
    pass

  def pop(self):
    """`L.pop([index])` removes and returns the last element of the list L, or, if the optional index is provided, at that index."""
    pass

  def remove(self, x) -> None:
    """`L.remove(x)` removes the first occurrence of the value `x` from the list L, and returns `None`."""
    pass

class Set:
  def union(self, iterable):
    """`S.union(iterable)` returns a new set into which have been inserted all the elements of set S and all the elements of the argument, which must be iterable."""
    pass

class String:
  def elem_ords(self):
    """`S.elem_ords()` returns an iterable value containing the sequence of numeric bytes values in the string S."""
    pass

  def capitalize(self) -> String:
    """`S.capitalize()` returns a copy of string S with its first code point changed to its title case and all subsequent letters changed to their lower case."""
    pass

  def codepoint_ords(self):
    """`S.codepoint_ords()` returns an iterable value containing the sequence of integer Unicode code points encoded by the string S. Each invalid code within the string is treated as if it encodes the Unicode replacement character, U+FFFD."""
    pass

  def count(self, sub) -> int:
    """`S.count(sub[, start[, end]])` returns the number of occcurences of `sub` within the string S, or, if the optional substring indices `start` and `end` are provided, within the designated substring of S. They are interpreted according to Starlark's [indexing conventions](#indexing)."""
    pass

  def endswith(self, suffix) -> bool:
    """`S.endswith(suffix[, start[, end]])` reports whether the string `S[start:end]` has the specified suffix."""
    pass

  def find(self, sub) -> int:
    """`S.find(sub[, start[, end]])` returns the index of the first occurrence of the substring `sub` within S."""
    pass

  def format(self, *args, **kwargs) -> String:
    """`S.format(*args, **kwargs)` returns a version of the format string S in which bracketed portions `{...}` are replaced by arguments from `args` and `kwargs`."""
    pass

  def index(self, sub) -> int:
    """`S.index(sub[, start[, end]])` returns the index of the first occurrence of the substring `sub` within S, like `S.find`, except that if the substring is not found, the operation fails."""
    pass

  def isalnum(self) -> bool:
    """`S.isalnum()` reports whether the string S is non-empty and consists only Unicode letters and digits."""
    pass

  def isalpha(self) -> bool:
    """`S.isalpha()` reports whether the string S is non-empty and consists only of Unicode letters."""
    pass

  def isdigit(self) -> bool:
    """`S.isdigit()` reports whether the string S is non-empty and consists only of Unicode digits."""
    pass

  def islower(self) -> bool:
    """`S.islower()` reports whether the string S contains at least one cased Unicode letter, and all such letters are lowercase."""
    pass

  def isspace(self) -> bool:
    """`S.isspace()` reports whether the string S is non-empty and consists only of Unicode spaces."""
    pass

  def istitle(self) -> bool:
    """`S.istitle()` reports whether the string S contains at least one cased Unicode letter, and all such letters that begin a word are in title case."""
    pass

  def isupper(self) -> bool:
    """`S.isupper()` reports whether the string S contains at least one cased Unicode letter, and all such letters are uppercase."""
    pass

  def join(self, iterable) -> String:
    """`S.join(iterable)` returns the string formed by concatenating each element of its argument, with a copy of the string S between successive elements. The argument must be an iterable whose elements are strings."""
    pass

  def lower(self) -> String:
    """`S.lower()` returns a copy of the string S with letters converted to lowercase."""
    pass

  def lstrip(self) -> String:
    """`S.lstrip()` returns a copy of the string S with leading whitespace removed."""
    pass

  def partition(self, x):
    """`S.partition(x)` splits string S into three parts and returns them as a tuple: the portion before the first occurrence of string `x`, `x` itself, and the portion following it. If S does not contain `x`, `partition` returns `(S, "", "")`."""
    pass

  def removeprefix(self, x) -> String:
    """`S.removeprefix(prefix)` returns a copy of string S with the prefix `prefix` removed if S starts with `prefix`, otherwise it returns S."""
    pass

  def removesuffix(self, x) -> String:
    """`S.removesuffix(suffix)` returns a copy of string S with the suffix `suffix` removed if S ends with `suffix`, otherwise it returns S."""
    pass

  def replace(self, old, new) -> String:
    """`S.replace(old, new[, count])` returns a copy of string S with all occurrences of substring `old` replaced by `new`. If the optional argument `count`, which must be an `int`, is non-negative, it specifies a maximum number of occurrences to replace."""
    pass

  def rfind(self, sub) -> int:
    """`S.rfind(sub[, start[, end]])` returns the index of the substring `sub` within S, like `S.find`, except that `rfind` returns the index of the substring's _last_ occurrence."""
    pass

  def rindex(self, sub) -> int:
    """`S.rindex(sub[, start[, end]])` returns the index of the substring `sub` within S, like `S.index`, except that `rindex` returns the index of the substring's _last_ occurrence."""
    pass

  def rpartition(self, x):
    """`S.rpartition(x)` is like `partition`, but splits `S` at the last occurrence of `x`."""
    pass

  def rsplit(self) -> List[String]:
    """`S.rsplit([sep[, maxsplit]])` splits a string into substrings like `S.split`, except that when a maximum number of splits is specified, `rsplit` chooses the rightmost splits."""
    pass

  def rstrip(self) -> String:
    """`S.rstrip()` returns a copy of the string S with trailing whitespace removed."""
    pass

  def split(self) -> List[String]:
    """`S.split([sep [, maxsplit]])` returns the list of substrings of S, splitting at occurrences of the delimiter string `sep`."""
    pass

  def elems(self):
    """`S.elems()` returns an iterable value containing successive 1-byte substrings of S. To materialize the entire sequence, apply `list(...)` to the result."""
    pass

  def codepoints(self):
    """`S.codepoints()` returns an iterable value containing the sequence of substrings of S that each encode a single Unicode code point. Each invalid code within the string is treated as if it encodes the Unicode replacement character, U+FFFD."""
    pass

  def splitlines(self) -> List[String]:
    """`S.splitlines([keepends])` returns a list whose elements are the successive lines of S, that is, the strings formed by splitting S at line terminators (currently assumed to be a single newline, `\n`, regardless of platform)."""
    pass

  def startswith(self, prefix) -> bool:
    """`S.startswith(prefix[, start[, end]])` reports whether the string `S[start:end]` has the specified prefix."""
    pass

  def strip(self) -> String:
    """`S.strip()` returns a copy of the string S with leading and trailing whitespace removed."""
    pass

  def title(self) -> String:
    """`S.title()` returns a copy of the string S with letters converted to title case."""
    pass

  def upper(self) -> String:
    """`S.upper()` returns a copy of the string S with letters converted to uppercase."""
    pass

