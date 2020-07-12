### RangeDict 
Ranges are omnipresent in our lives - we are talking about durations, lengths or intervals. 
Unfortunately they are hard to model in code using standard data structures built in mainstream languages.


This library offers you fast `range dict` implementation, built on top of Python's standard dictionary.  

#### Example usage

```python
>>> holidays = RangeDict()

>>> holidays[date(2020, 7, 1), date(2020, 7, 14)] = "John's holidays"

>>> holidays[date(2020, 7, 10)]
"John's holidays"

>>> holidays[date(2020, 7, 10), date(2020, 7, 20)] = "Mary's holidays"

>>> holidays[date(2020, 7, 12)]
["John's holidays", "Mary's holidays"]
```

#### Supported data types
Range can be expressed using:
 - int
 - float
 - date
 - datetime

#### Standard behavior
Because `RangeDict` extends Python's standard dictionary,
it is capable of accepting single value as a key:

```python
>>> holidays[date(2020, 7, 12)] = "Piotr's (one day) holiday"
```
