def plusOne(digits):
    """
    :type digits: List[int]
    :rtype: List[int]
    """
    i = len(digits) - 1
    while i >= 0:
        digits[i] += 1
        if digits[i] %10 !=0:
            return digits
        else:
            digits[i] = digits[i] % 10
        i -=1
    # digits = new
    # int[digits.length + 1];
    # digits[0] = 1;
    # return digits;

# print(plusOne([1,2,3]))
print(plusOne([1,2,9,9]))