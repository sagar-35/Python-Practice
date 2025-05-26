import camelcase

c = camelcase.CamelCase()

txt = "hello world! how are you?"

print(c.hump(txt))
#This method capitalizes the first letter of each word.
