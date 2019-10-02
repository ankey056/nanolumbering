#!/usr/bin/env python2

from sys import argv

from pathname_utils import get_input_images_list, new_path
from pictures_handling import process_file, init_system

input_dir = argv[1]
output_dir = argv[2]

def main (input_dir, output_dir):
    for x in get_input_images_list(input_dir):
        process_file(x, new_path(x, output_dir))

if __name__ == "__main__":
    init_system()
    main(argv[1], argv[2])
