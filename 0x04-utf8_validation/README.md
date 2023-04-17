# 0x04. UTF-8 Validation

This Python script checks if a given data set represents valid UTF-8 encoding.

## How to Use

The script has a function called validUTF8 which takes a list of integers as input. This list of integers should represent a data set. To use the function, simply import the script and call the validUTF8 function, passing the data set as a parameter.

## Here's an example:

```python

validUTF8 = __import__('0-validate_utf8').validUTF8

data_set = [197, 130, 1]
is_valid = validUTF8(data_set)
print(is_valid)  

True
```
If the data set is a valid UTF-8 encoding, the function will return True. Otherwise, it will return False.

## Note

This script assumes that the input data set contains only integers. If there are other data types in the list, the function will return False.
