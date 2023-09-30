
import tkinter
import tkintermapview
import os
from PIL import Image, ImageTk

images = {}

def add_marker(marker_data, map_widget):

     map_markers = []
     for marker in marker_data:
          x, y = tkintermapview.convert_address_to_coordinates(marker["address"])
          map_markers.append(map_widget.set_marker(x, y, text=marker["title"], image=images["cbi.jpeg"]))


def tabbed_window(tab):
     

     script_directory = os.path.dirname(os.path.abspath(__file__))
     database_path = os.path.join(script_directory, "offline_tiles_ca.db")

     map_widget = tkintermapview.TkinterMapView(tab, width=800, height=750, corner_radius=0, database_path=database_path, use_database_only=True)

     map_widget.place(relx=1, rely=0, anchor=tkinter.NE)
     map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=22)
     
     map_widget.set_position(37.77493, -122.41942)  # SF
     map_widget.set_zoom(12)
     marker_data = [{"address" : "755 Ocean Ave, San Francisco, CA","title" : "Car break-in reported" }]

     current_path = os.path.join(os.path.dirname(os.path.abspath(__file__)))
     images["cbi.jpeg"] = ImageTk.PhotoImage(Image.open(os.path.join(current_path, "images", "cbi.jpeg")).resize((50, 50)))

     add_marker(marker_data, map_widget)

def main():
     root_tk = tkinter.Tk()
     root_tk.geometry(f"{1000}x{750}")
     root_tk.title("UCrisis")

     tabbed_window(root_tk)

     root_tk.mainloop()

if __name__ == "__main__":
     main()