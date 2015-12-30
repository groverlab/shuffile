import random, os, sys

if len(sys.argv) != 2:
    print """
    USAGE:
        python shuffile.py directory_name
    where 'directory_name' is the full path of the directory containing files to be shuffled.
    """
else:
    dirname = sys.argv[1]
    files = os.listdir(dirname)
    random.shuffle(files)
    counter = 0
    for filename in files:
        if not filename.startswith("."):
            print counter, filename
            os.rename(os.path.join(dirname,filename), os.path.join(dirname,str(counter).zfill(2)+filename))
            counter += 1



