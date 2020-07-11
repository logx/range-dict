### RangeDict 

```python
>>> extraordinary_events = RangeDict()

>>> extraordinary_events[date(2020, 2, 12), date(2020, 6, 1)] = "coronavirus_lockdown"

>>> extraordinary_events[date(2020, 4, 10)]
"coronavirus_lockdown"

>>> extraordinary_events[date(2020, 5, 1), date(2020, 5, 3)] = "may_holidays"

>>> extraordinary_events[date(2020, 5, 1)]
["coronavirus_lockdown", "may_holidays"]
```