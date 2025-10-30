class Rider:

    def __init__(self, name):

        self.name=name
        self.ride_history= []
    
    def __str__(self):
        return f"Name: {self.name}\n"
    

first_user= Rider("Amahle Cele")
print(first_user)