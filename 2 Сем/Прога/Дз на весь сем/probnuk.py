import tkinter as tk

class TruckDataGUI:
    def __init__(self, truck_data):
        self.truck_data = truck_data
        
        # Create the main window
        self.window = tk.Tk()
        self.window.title('Truck Data')
        
        # Create a label for each piece of data
        name_label = tk.Label(self.window, text='Name: ' + truck_data['name'])
        payload_label = tk.Label(self.window, text='Payload: ' + str(truck_data['payload']))
        length_label = tk.Label(self.window, text='Length: ' + str(truck_data['length']))
        width_label = tk.Label(self.window, text='Width: ' + str(truck_data['width']))
        depth_label = tk.Label(self.window, text='Depth: ' + str(truck_data['depth']))
        
        # Pack the labels into the window
        name_label.pack()
        payload_label.pack()
        length_label.pack()
        width_label.pack()
        depth_label.pack()
        
        # Start the tkinter event loop
        self.window.mainloop()

# Define some example truck data
truck_data_1 = {'name': 'Big Truck', 'payload': 10000, 'length': 10, 'width': 2, 'depth': 3}
truck_data_2 = {'name': 'Medium Truck', 'payload': 5000, 'length': 8, 'width': 2, 'depth': 2.5}
truck_data_3 = {'name': 'Small Truck', 'payload': 2000, 'length': 6, 'width': 1.5, 'depth': 2}

# Create a new instance of the GUI with each truck data set
gui_1 = TruckDataGUI(truck_data_1)
gui_2 = TruckDataGUI(truck_data_2)
gui_3 = TruckDataGUI(truck_data_3)
