#Lambda function to check divisibility by 5

divisible_5 = lambda x: True if x % 5 == 0 else False
print("Is 25 divisible by 5?:", divisible_5(25))