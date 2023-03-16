import os
import pathlib
import csv

pwd = str(pathlib.Path(__file__).parent.resolve())
path = pwd + "\\arkhamicons"

with open('data.csv', mode='w', newline='') as data_file:
    data_writer = csv.writer(data_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    data_writer.writerow(["set","encounter","left_image","right_image"])



    complete_files = []
    for root, dir_names, file_names in os.walk(path):
        for f in file_names:
            # This os.path.join() is the most crucial line of all.
            # This line internally implements something DFS style.
            if f != "_set.png" and f != "_investigator.png":
                set = str(root).replace(path,"").split("\\")[1]
                encounter = f.split(".")[0]
                left_image = os.path.join(str(root).replace(path,""),f)
                right_image = os.path.join("\\",set,"_set.png")
                data_writer.writerow([set,encounter,left_image,right_image])        
       
