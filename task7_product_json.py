#Parase a JSON file representing product details (name, price, quantity) and display the details in tabular format
import json
data=[]
n=int(input("\nEnter number of products"))

for i in range (n):
     name=str(input(f"Enter name of product {i+1}:"))
     price=int(input(f"Enter price of product {i+1}:"))
     quantity=int(input(f"Enter quantity of product {i+1}:"))

     product={
          "name" : name,
          "price" : price,
          "quantity" : quantity
     }

     data.append(product)

with open ("products.json",'w') as file:
    products=json.dump(data, file, indent=4)

print("Data written successfully\n")

with open ("products.json", 'r') as file:
     products=json.load(file)

print("{:<15} {:<10} {:<10}".format("Product Name", "Price", "Quantity"))
print("-" * 40)

for product in products:
     print("{:<15} {:<10} {:<10}".format(product['name'], product['price'], product['quantity']))   
