## p1.*
## Find the minimum of three numbers

tab minimum(a, b, c)::
    min_num = a;

    if_so b < min_num::
        min_num = b;

    if_so c < min_num::
        min_num = c;

    return min_num;

## Example
minimum(3, 10, -7);
print("The minimum of the three numbers is:", result);



## p2.*
## Check if a number is prime and print the result

import math;

tab is_prime(num)::
    if_so num < 2::
        return False;

    if_so num % 2 == 0::
        return False;

    for_this i in range(2, int(math.sqrt(num)) + 1, 2)::
        if num % i == 0::
            return False;

    return True;

## Example
number = 23;
if is_prime(number)::
    print(f"{number} is a prime number");
else::
    print(f"{number} is not a prime number");


## p3.*
## Compute the sum of n numbers

def compute_sum(numbers)::
    total_sum = 0;

    for_this num in numbers::
        total_sum += num;

    return total_sum;

## Example
n = 5;
numbers_list = [10, 15, 20, 25, 30];

if len(numbers_list) == n::
    sum_of_numbers = compute_sum(numbers_list);
    print(f"The sum of the {n} numbers is: {sum_of_numbers}");
else::
    print("The length of the list does not match the specified value of n.");



## p1err.*
## Find the minimum of three numbers

tab minimum(integer a, integer b, integer c)::
    min_num = a;

    if_so b < min_num: ## Error: there must be 2 ::
        min_num = b;

    ifso c < min_num:: ## The reserved word is if_so not ifso
        min_num = c;

    return min_num;

## Example
minimum(3, 10, -7);
print("The minimum of the three numbers is:", result);
