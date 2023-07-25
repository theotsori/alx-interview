# UTF-8 Validation Algorithm

This Python module defines a function `validUTF8` that checks the validity of a given data set as a UTF-8 encoding.

![Validutf8](https://www.perl.com/images/building-a-utf8-encoder-in-perl/bart-simpson-utf8.png)

## Usage

To use the `validUTF8` function, import it into your Python script or interactive session and pass the data set as a list of integers. Each integer should represent 1 byte of data. The function returns `True` if the data set is a valid UTF-8 encoding, and `False` otherwise.

```python
from utf8_validation import validUTF8

data = [65]  # Example data set
result = validUTF8(data)
print(result)  # Output: True
```

## Function Signature

```python
def validUTF8(data):
    """
    Check the validity of a UTF-8 data set.
```

## Helper Function

The algorithm includes a helper function `check_following_bytes` that verifies if the subsequent bytes of a multi-byte character are valid.

```python
def check_following_bytes(num_following):
    """
    Check if the subsequent bytes of a multi-byte character are valid.
    """
```

## Algorithm Description

The `validUTF8` function validates the data set based on the following rules:

- A character in UTF-8 can be 1 to 4 bytes long.
- The first byte of a multi-byte character starts with a pattern of "1" followed by the necessary number of "0"s, while the subsequent bytes start with "10".
- If a byte starts with "0", it represents a single-byte character.
- If a byte starts with "11", it represents the first byte of a multi-byte character (2 to 4 bytes).
- If a byte starts with "10", it represents a subsequent byte of a multi-byte character.

The function iterates through the data set and checks each byte against these rules. If any byte is found to be invalid, the function returns `False`. Otherwise, if the entire data set is a valid UTF-8 encoding, it returns `True`.

## Example

Here is an example of how to use the `validUTF8` function:

```python
from utf8_validation import validUTF8

data = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
result = validUTF8(data)
print(result)  # Output: True
```

## Requirements

- Python 3.x

Note: Make sure to adjust the file names and import statements as needed, depending on how you structure your project. Additionally, you should have a separate file named `utf8_validation.py` (or any other appropriate name) that contains the `validUTF8` function and helper function.