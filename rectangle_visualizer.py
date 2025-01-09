class Rectangle:
    def __init__(self,width:int,height:int):
        self.width = width
        self.height = height

    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'
    
    def set_width(self,new_width):
        self.width = new_width
    
    def set_height(self,new_height):
        self.height = new_height
    
    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return self.width * 2 + self.height*2

    def get_diagonal(self):
        return ((self.width**2)+(self.height**2))**0.5

    def get_picture(self):
        output_string = ''
        if self.width > 50:
            return 'Too big for picture.'
        if self.height >50:
            return 'Too big for picture.'
        else:
            for lines in range(self.height):
                output_string += '*'*self.width+'\n'
            return output_string

    def get_amount_inside(self,shape_to_fit):
        quant_fig = 0
        main_area = self.get_area()
        sub_area = shape_to_fit.get_area()
        while main_area >= sub_area:
            main_area = main_area - sub_area
            quant_fig += 1
        return quant_fig 

        



class Square(Rectangle):
    
    def __init__(self,side):
        self.side = side
        self.width = self.side
        self.height = self.side

    def __str__(self):
        return f'Square(side={self.side})'

    def set_side(self,new_side):
        self.side = new_side
        self.width = new_side
        self.height = new_side

    def set_width(self,new_width):
        self.side = new_width 
        self.width = new_width 
        self.height = new_width 

    def set_height(self,new_height):
        self.side = new_height 
        self.width = new_height 
        self.height = new_height 
    
ex1 = Rectangle((20),(10))
ex2 = Rectangle(1,1)
print(ex1.get_area())
print(ex1.get_perimeter())
print(ex1.get_diagonal())
print(ex1.get_picture())
