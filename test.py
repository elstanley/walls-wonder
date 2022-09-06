from PIL import Image, ImageColor
import os
import numpy

tuli = Image.open ("products/tulips.jpg")

width, height = tuli.size

def find_coeffs(pb, pa):
    matrix = []
    for p1, p2 in zip(pa, pb):
        matrix.append([p1[0], p1[1], 1, 0, 0, 0, -p2[0]*p1[0], -p2[0]*p1[1]])
        matrix.append([0, 0, 0, p1[0], p1[1], 1, -p2[1]*p1[0], -p2[1]*p1[1]])

    A = numpy.matrix(matrix, dtype=float)
    B = numpy.array(pb).reshape(8)

    res = numpy.dot(numpy.linalg.inv(A.T * A) * A.T, B)
    return numpy.array(res).reshape(8)

coeffs = find_coeffs(
        [(0, 0), (width, 0), (width, height), (0, height)], # pb
        [(2001, 582), (2935, 420), (2941, 2024), (2016, 1983)] # pa
        )

tuli = tuli.convert('RGBA')
tuli2 = tuli.transform((4200, 2900), Image.Transform.PERSPECTIVE, coeffs, fillcolor=(255,255,255,0))
tuli2.show ()

tuli2.save ("emma.png")
