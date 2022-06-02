import validators

isValid = validators.url("enter input")

if isValid == True:
    print("Valid url")
else:
    print("invalid url")