#Readme

##Description
The purpose of this project is to allow easy modification of Steam's 
"Non-Steam Games" list with normal python code. This list is stored in a file
called 'shortcuts.vdf', which uses a format I have never seen before. The main
two parts of this project are a Parser and a Generator, to allow conversion 
between shortcuts.vdf to python objects and python objects to shortcuts.vdf.
Also included is an API to (hopefully) abstract away the Parser/Generator, 
although you are free to use them directly.

##TODO

- Create actual unit tests to replace the manual testing I have set up currently
- Standardize the test vdf files (as opposed to current vdfs that I haphazardly threw together)
- Create more vdfs with different scenarios (such as tags, which seems to be an
  array, but I can't get Steam to let me add more than 1. Look into that)
- Implement the parser (I am holding off on that until I am more confident in
  the output of the generator and that it is correct for most situations)