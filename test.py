import math

# Calculating binomial probablity for this
group = 50
thresh = 36
prod = 0.5

sum = 0
for i in range(0, group - thresh + 1):
    denom = math.factorial(i) * math.factorial(group - i)
    sum += 1/denom

print(str(round(sum * math.factorial(group) * math.pow(prod, group) * 100, 2)) + '% chance')