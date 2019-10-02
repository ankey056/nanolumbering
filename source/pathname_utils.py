
import glob
import os.path as path

def get_input_images_list (input_dir): 
    return glob.glob(input_dir + "*.tif")

def new_path (p, dir):
    return path.join(dir, path.basename(p))
    

def filename_with_altext (name, altext, prefix=None):
    filename, file_extension = path.splitext(name)
    if prefix: filename = filename + prefix
    return '.'.join([filename,altext])

def filename_with_prefix (name, prefix):
    filename, file_extension = path.splitext(name)
    return filename + prefix + file_extension
