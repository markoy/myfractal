class fractal:

   def __init__(self):
       self.matrix = []
       self.result_matrix = []

   def test_fill(self, x, y):
       self.matrix = [[q for q in range(y)] for i in range(x)]

   def test_fill_complex(self, x, y, min, max):
       self.matrix = [[complex(min+(max-min)/x*w, min+(max-min)/y*q) for q in range(y)] for w in range(x)]
       self.result_matrix = [[0+0j for q in range(y)] for i in range(x)]

   def calculate_fractal(self):
       z = 0 + 0j
       for y in range(len(self.result_matrix[0])):
           for x in range(len(self.result_matrix)):
               z = 0 + 0j
               for count in range(10):
                    z = pow(z,2) + self.matrix[x][y]
               self.result_matrix[x][y] = abs(z)

   def show_as_text(self):
       for y in range(len(self.matrix[0])):
            for x in range(len(self.matrix)):
                print (self.matrix[x][y], end=" ")
            print()

   def show_result_as_text(self):
       for y in range(len(self.result_matrix[0])):
            for x in range(len(self.result_matrix)):
                print (self.result_matrix[x][y], end=" ")
            print()

   def start(self):
       self.test_fill_complex(self, 10, 10, -2, 2)


eka = fractal
eka.start(eka)
eka.show_as_text(eka)
eka.calculate_fractal(eka)
eka.show_result_as_text(eka)
