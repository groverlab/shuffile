import random, os

dirname = "/Users/wgrover/Documents/Classes/BIEN 167 UG Medical Diagnostics/2015/Mini-project 2 final slides"
files = os.listdir(dirname)
random.shuffle(files)
counter = 0
for filename in files:
    if not filename.startswith("."):
        print counter, filename
        os.rename(os.path.join(dirname,filename), os.path.join(dirname,str(counter).zfill(2)+filename))
        counter += 1



