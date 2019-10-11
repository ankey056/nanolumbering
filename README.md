
# nanolumbering

## Description

Prototype of program that recognizes nanoparticles on scanning
electron microscope images.

License: MIT

## Usage

```./source/perform.py INPUTDIR/ OUTPUTDIR/```

The program handles all images in INPUTDIR directory and collects
results in OUTPUTDIR directory.

The program works only with TIFF image which includes scale metadata.

Collected results constists of files with same name as input image
file:

+ input image file with highlighted areas of recognized objects
+ table with columns:
  * i - object number
  * w, h, s, p - object's horizontal and vertical sizes, area and
    perimeter  on the image, respectively
  * d_l ~= p / pi
  * d_s = 2 * sqrt(s / pi)
  * d = sqrt( w^2 + h^2)
+ object's areas statistics file:
  * mean - arithmetical mean
  * S - total area of recognized objects on the image
  * std - standard deviation

### Learning

Correct operation of the program requires learning procedure that may
be started by `make learning` command. The program learns from each
test image from `learning/tests/` directory that have control file in
`learning/standards/` directory with same name as test file (file's
extension may be different). Control file is grayscale image with
black (#000000) background and white (#FFFFFF) areas which highlights
objects on the test image. Size of test and control images must be
equal.

## Requirements

Software works with python 2 (tested with python 2.7.15), moreover
OpenCV 2 is required (tested with OpenCV 2.4.13.6).
