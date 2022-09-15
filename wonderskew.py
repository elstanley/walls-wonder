from PIL import Image, ImageColor
import os
import numpy

mockup_filenames = ["mockup9.jpg","pmockup2.jpg","pmockup3.jpg","pmockup4.jpg","pmockup5.jpg","pmockup6.jpg","pmockup7.jpg","pmockup8.jpg"]
frame_corners = [
    [(985,1547), (2827,1550), (2849,2861), (961,2861)], # mockup9
    [(1783,725), (3616,726), (3616,3323),(1782,3322)], #pmockup2
    [(1555,603), (2402,564), (2555,1717), (1703,1842)], #pmockup3
    [(1722,542), (2523,544), (2523,1610), (1722,1610)], #pmockup4
    [(2001, 582), (2935, 420), (2941, 2024), (2016, 1983)], # pmockup5
    [(1125,1678), (1899,1685), (1991,2753), (1175,2795)], #pmockup6
    [(1728,1363), (2390,1361), (2401,2254), (1716,2255)], #pmockup7
    [(1796,874), (2639, 875), (2660,2028), (1784,2028)],  #pmockup8
]

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
    w,h = mockup.size
    coeffs = find_coeffs(
        [(0, 0), (width, 0), (width, height), (0, height)], # pb
        frame_corners # pa
        )

    productimage = productimage.convert('RGBA')
    skewedimage = productimage.transform((w, h), Image.Transform.PERSPECTIVE, coeffs, fillcolor=(255,255,255,0))

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
    for i in range(len(mockup_filenames)):
        skewer (productfilename, mockup_filenames[i], frame_corners[i])
    



