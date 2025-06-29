#Find sum of thye series n - n2/3 + n4/5 - n8/7 .... m terms (1<=n<=4 and 2<=m<=10)

n = int(input('Enter N (term) value: '))
m = int(input('Enter number of terms: '))

sum_of_series = 0
sign = -1
for i in range(m):
    numerator    = n ** 2 ** i
    dinominator  = 2 * i + 1
    sign         = -1 * sign
    term_        = numerator / dinominator * sign
    sum_of_series = sum_of_series + term_
print(sum_of_series)  
