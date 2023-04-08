
class Point2D:
    """2D Point class for OpenGL"""
    
    def __init__(self,  coord, size=4.0, color=[1.0,0.0,0.0]):
        """Initialize size, coordinates and color of point"""
        self.size = size
        self.x = coord[0] # x koordinatı
        self.y = coord[1] # y koordinatı
        self.color = color

    def swap(self):
        """Swap x and y coordinates"""
        temp = self.x
        self.x = self.y
        self.y = temp    

 

    
