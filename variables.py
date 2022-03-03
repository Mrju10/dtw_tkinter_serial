
class COM:
    #creating a class variable and making it a variable
    global Rate, serial_port
    Rate = 11500
    serial_port= 'COM6'
    
    print("BautRate:", Rate)
    print("Puerto  Seleccionado:", serial_port)
    def __init__(self, Rate, serial_port):
        self.Rate = Rate
        self.serial_port = serial_port
        def display_Rate():
            print("Speed of the Tesla is:", Rate)
 

