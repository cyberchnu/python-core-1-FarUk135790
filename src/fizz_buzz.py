def fizz_buzz(param):
  #Type your code here
  result = ""
  if param %3==0:
    result+="Fizz"
  if param %5==0:
    result+="Buzz"
  if not result:
    result=str(param)
  return result

print(fizz_buzz(3))
print(fizz_buzz(5))
print(fizz_buzz(30))
print(fizz_buzz(991))
