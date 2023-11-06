## p1.*
## Find the minimum of three numbers

tab minimum($a, $b, $c)::
{
    $m = a;

    if_so b < m::
    {
        m = b;
    }

    if_so c < m::
    {
        m = c;
    }

    return m;
}

## Example
minimum(3, 10, -7);
print("The minimum of the three numbers is:", result);



## p2.*
## Check if a number is prime and print the result

import math;


tab is_prime($n)::
{
    if_so n < 2::
    {
        return False;
    }

    if_so n % 2 == 0::
    {
        return False;
    }

    $i;

    for_this i in range(2, n/2, 2)::
    {
        if n % i == 0::
            return False;
    }

    return True;
}

## Example
number = 23;
if is_prime(number)::
{
    print(f"{number} is a prime number");
}
else::
{
    print(f"{number} is not a prime number");
}


## p3.*
## Compute the sum of n numbers

tab compute_sum($numbers)::
{
    $total_sum = 0;

    for_this $num in numbers::
    {
        total_sum += num;
    }

    return total_sum;
}

## Example
n = 5;
numbers_list = [10, 15, 20, 25, 30];

if len(numbers_list) == n::
{
    sum_of_numbers = compute_sum(numbers_list);
    print(f"The sum of the {n} numbers is: {sum_of_numbers}");
}
else::
{
    print("The length of the list does not match the specified value of n.");
}



## p1err.*
## Find the minimum of three numbers

$min, $max;
max = 023; ## invalid constant (starting with '0')

tab minimum($a, $b, $c)::
{
    $m = a;

    if_so b < m::
    {
        m = b;
        ~ ## illegal char
        @ ## illegal char
        " ## invalid string
    }

    if_so c < m::
    {
        m = c;
    }

    return m;
}

## Example
minimum(3, 10, -7);
print("The minimum of the three numbers is:", result);
