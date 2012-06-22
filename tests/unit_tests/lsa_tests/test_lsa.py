from unittest import TestCase
from semanticpy.lsa.lsa import LSA
from nose.tools import *
import numpy

class TestLSA(TestCase):
   """ """
   def it_should_do_tfidf_test(self):
     matrix = [[0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0],
               [0.0, 1.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0, 0.0],
               [1.0, 1.0, 0.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0],
               [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]]

     expected = [[ 0.        ,  0.        ,  0.23104906,  0.        ,  0.        , 0.09589402,  0.        ,  0.        ,  0.46209812],
                 [ 0.        ,  0.1732868 ,  0.        ,  0.        ,  0.        , 0.07192052,  0.34657359,  0.34657359,  0.        ],
                 [ 0.27725887,  0.13862944,  0.        ,  0.27725887,  0.27725887, 0.05753641,  0.        ,  0.        ,  0.        ],
                 [ 0.        ,  0.        ,  0.69314718,  0.        ,  0.        , 0.        ,  0.        ,  0.        ,  0.        ]]

     expected = numpy.array(expected)

     lsa = LSA(matrix)
     lsa.tfidfTransform()

     eq_(numpy.intersect1d(lsa.matrix,expected), [0])


   def it_should_do_lsa_test(self):
     matrix = [[0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0],
               [0.0, 1.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0, 0.0],
               [1.0, 1.0, 0.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0],
               [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]]

     expected = [[ 0.02284739,  0.06123732,  1.20175485,  0.02284739,  0.02284739, 0.88232986,  0.03838993,  0.03838993,  0.82109254],
                 [-0.00490259,  0.98685971, -0.04329252, -0.00490259, -0.00490259, 1.02524964,  0.99176229,  0.99176229,  0.03838993],
                 [ 0.99708227,  0.99217968, -0.02576511,  0.99708227,  0.99708227, 1.01502707, -0.00490259, -0.00490259,  0.02284739],
                 [-0.0486125 , -0.13029496,  0.57072519, -0.0486125 , -0.0486125 , 0.25036735, -0.08168246, -0.08168246,  0.3806623 ]]

     expected = numpy.array(expected)
     lsa = LSA(matrix)
     lsa.lsaTransform()

     #eq_(lsa.matrix == expected, [])
     eq_(lsa.matrix, [])

     eq_(numpy.intersect1d(lsa.matrix,expected), numpy.array([]))