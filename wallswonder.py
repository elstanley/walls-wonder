from PIL import Image
import os

mockup_filenames = [   "mockup1.jpg", "mockup2.jpg", "mockup3.jpg", "mockup4.jpg", "mockup5.jpg", "mockup6.jpg", "mockup7.jpg", "mockup8.jpg", "mockup9.jpg", "pmockup1.jpg", "pmockup9.png"]
mockup_sizes = [       (2536,2024),   (2052,1463),   (3010,2150), (2100,1680),     (2106,1694),  (2068,1458),    (2346,1530), (2140,1514),     (1840,1308),   (1062,1508),     (988,1330)]    
mockup_positions = [   (1228,1414),   (1240,788),    (1392,1100), (1296,1170),     (920,1148),    (1572,404),    (758,536),    (2134,1466),    (1006,1548),    (1342,560),      (918, 212)]
mockup_transparents =  [False,         False,          False,      False,           False,        False,          False,        False,           False,        False,            True]


def makemockup (productfinal, mockup_filename, mockup_size, mockup_position, mockup_transparent):
    mockup = Image.open ("mockups/" + mockup_filename)
    product = Image.open ("products/" + productfinal)
    width, height = product.size
    (mockupwidth, mockupheight) = mockup_size
    if (width <= height and mockupwidth > mockupheight) or (height <= width and mockupwidth < mockupheight):
        print ("skipping unmatched image")
        return
    product2 = product.resize(mockup_size)
    mockup.paste(product2, box=mockup_position)
    if (mockup_transparent):
        # make new image transparent by pasting clean copy over old copy with product image sandwiched between
        mockup2 = Image.open ("mockups/" + mockup_filename)
        mockup.paste(mockup2, (0, 0), mockup2)
    rgb_im = mockup.convert('RGB')
    rgb_im.save ("outputs/" + mockup_filename + productfinal)

# loop over each product and mockup
products = os.listdir ("products")
for productfilename in products:
    print(productfilename)
    for i in range(len(mockup_filenames)):
        makemockup(productfilename, mockup_filenames[i], mockup_sizes[i], mockup_positions[i], mockup_transparents[i])
    


    



