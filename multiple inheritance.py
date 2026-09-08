class bharath:
    model="bharath"
class benz:
    name="benz"
class bharathbenz(bharath,benz):
    product="bharath-benz"
s=bharathbenz()
print(s.model)
print(s.name)
print(s.product)
