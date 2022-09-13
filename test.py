from PIL import Image, ImageColor
import os
import numpy

#productimage = Image.open ("products/productimageps.jpg")

#width, height = productimage.size

def find_coeffs(pb, pa):
    matrix = []
    for p1, p2 in zip(pa, pb):
        matrix.append([p1[0], p1[1], 1, 0, 0, 0, -p2[0]*p1[0], -p2[0]*p1[1]])
        matrix.append([0, 0, 0, p1[0], p1[1], 1, -p2[1]*p1[0], -p2[1]*p1[1]])

    A = numpy.matrix(matrix, dtype=float)
    B = numpy.array(pb).reshape(8)

    res = numpy.dot(numpy.linalg.inv(A.T * A) * A.T, B)
    return numpy.array(res).reshape(8)

def skewer (product_filename, mockup_filename, frame_corners):
    mockup = Image.open ("mockups/" + mockup_filename)
    productimage = Image.open ("products/" + product_filename)
    width, height = productimage.size
    coeffs = find_coeffs(
        [(0, 0), (width, 0), (width, height), (0, height)], # pb
        frame_corners # pa
        )

    productimage = productimage.convert('RGBA')
    skewedimage = productimage.transform((4200, 2900), Image.Transform.PERSPECTIVE, coeffs, fillcolor=(255,255,255,0))

    mockup.paste(skewedimage, (0, 0), skewedimage)
    #if (mockup_transparent):
    #    # make new image transparent by pasting clean copy over old copy with product image sandwiched between
    #    mockup2 = Image.open ("mockups/" + mockup_filename)
    #    mockup.paste(mockup2, (0, 0), mockup2)
    rgb_im = mockup.convert('RGB')
    rgb_im.save ("outputs/" + mockup_filename + product_filename)  

#skewer("tulips.jpg", "pmockup5.jpg",[(2001, 582), (2935, 420), (2941, 2024), (2016, 1983)])

products = os.listdir ("products")
for productfilename in products:
    print(productfilename)
    skewer(productfilename, "pmockup5.jpg",[(2001, 582), (2935, 420), (2941, 2024), (2016, 1983)])
    



