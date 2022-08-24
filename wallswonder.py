from PIL import Image
import os

def makemockup (productfinal):
    mockup = Image.open ("mockups/mockup1.jpg")
    product = Image.open ("products/" + productfinal)
    width, height = product.size
    if width <= height:
        print ("skipping portrait image")
        return
    product2 = product.resize ((2536,2024))
    mockup.paste( product2, box=(1228,1414) )
    mockup.save ("outputs/mockup1-" + productfinal)
products = os.listdir ("products")
for i in products:
    print(i)
    makemockup(i)


    



