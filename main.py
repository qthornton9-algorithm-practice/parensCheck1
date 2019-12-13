# def parens(str):
#   one = 0
#   two = 0
#   for i in range(len(str)):
#     print(i)
#     print(str[i])
#     if str[i] != "(" and str[i] != ")":
#       print("skip")
#       continue
#     elif str[i]==")" and i == 0:
#       print("False:1")
#       return False
#     elif str[len(str)-1] == "(":
#       print(len(str)-1,"False:2")
#       return str[len(str)-1]
#     if str[i] == "(":
#       one += 1
#       print(f"one={one}")
#     elif str[i] == ")":
#       two += 1
#       print(f"two={two}")
#   if one == two:
#     print(one, two)
#     print("True")
#     return True
#   else:
#     print(one,",", two)
#     print("False:last")
#     return False
# parens("(hdf(hdg))hgf(")

def balancedParens(str):
  one = 0
  two = 0
  for i in range (len(str)):
    if str[i] != "(" and str[i] !=")":
      continue
    elif str[i] == ")" and i == 0:
      return False
    elif str[len(str)-1] == "(":
      return False
    if str[i] == "(":
      one += 1
    elif str[i] == ")":
      two += 1
  if one == two:
    print("True")
    return True
  else:
    print("False")
    return False
balancedParens("(q(ian)a(R)thor(nton)")