To run tests:
```bash
python3 -m pytest .
```

Challenge comes from: https://adventofcode.com/2018/day/1

Starting with a frequency of zero, what is the resulting frequency after all of the changes in frequency have been applied?

For example, if the device displays frequency changes of +1, -2, +3, +1, then starting from a frequency of zero, the following changes would occur:

Current frequency  0, change of +1; resulting frequency  1.
Current frequency  1, change of -2; resulting frequency -1.
Current frequency -1, change of +3; resulting frequency  2.
Current frequency  2, change of +1; resulting frequency  3.
In this example, the resulting frequency is 3.
