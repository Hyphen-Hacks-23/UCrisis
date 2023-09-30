
import tkinter
import tkintermapview
import os
import pandas as pd
from PIL import Image, ImageTk

images = {}
marker_data = []
image_titles = ["car break-in", "arson", "robbery"] 
image_extesnions = [".jpeg", ".jpeg", ".jpeg"]

window = None
info_text = None

def add_marker(marker_data, map_widget):

     map_markers = []
     print(marker_data)

     for j in range(len(marker_data)):
          row = marker_data.iloc[j]
          x, y = tkintermapview.convert_address_to_coordinates(row["address"])

          marker_data.at[j, "latitude"] = x
          marker_data.at[j, "longitude"] = y
          
          for i in range(len(image_titles)):
               if image_titles[i] in row["title"].lower():
                    map_markers.append(map_widget.set_marker(x, y, text=row["title"], image=images[image_titles[i]], command=on_marker_click))
                    break
          else:
               map_markers.append(map_widget.set_marker(x, y, text=row["title"], image=images["robbery"]))


def on_marker_click(marker):
     #find index of marker in marker_data using longitude and latitude
     for i in range(len(marker_data)):
          if marker_data["latitude"][i] == marker.position[0] and marker_data["longitude"][i] == marker.position[1]:
               print(marker_data["address"][i])
               text_label.config(text=marker_data["address"][i])
               

               break


def get_data():
     data = pd.read_csv("final_markers.csv")
     return data

def tabbed_window(tab):
     
     global window
     window = tab

     script_directory = os.path.dirname(os.path.abspath(__file__))
     database_path = os.path.join(script_directory, "offline_tiles_ca.db")

     map_widget = tkintermapview.TkinterMapView(tab, width=800, height=750, corner_radius=0, database_path=database_path, use_database_only=False)

     map_widget.place(relx=1, rely=0, anchor=tkinter.NE)
     map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=22)
     
     map_widget.set_position(37.77493, -122.41942)  # SF
     map_widget.set_zoom(10)

     global marker_data
     marker_data = get_data()
     marker_data["latitude"] = 0
     marker_data["longitude"] = 0

     print(marker_data)

     #marker_data = [{"address" : "755 Ocean Ave, San Francisco, CA","title" : "Car break-in reported" }]

     current_path = os.path.join(os.path.dirname(os.path.abspath(__file__)))

     for i in range(len(image_titles)):
          images[image_titles[i]] = ImageTk.PhotoImage(Image.open(os.path.join(current_path, "images", image_titles[i] + image_extesnions[i])).resize((50, 50)))

     add_marker(marker_data, map_widget)
     global text_label
     text_label = tkinter.Label(window, text="fortnite", anchor="w", wraplength=200)
     text_label.pack(anchor="w", padx=10) 
     map_widget.set_zoom(11)

def main():
     root_tk = tkinter.Tk()
     root_tk.geometry(f"{1000}x{750}")
     root_tk.title("UCrisis")

     tabbed_window(root_tk)

     root_tk.mainloop()

if __name__ == "__main__":
     main()