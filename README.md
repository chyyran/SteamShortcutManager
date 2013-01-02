##Description
The purpose of this project is to allow easy modification of Steam's 
"Non-Steam Games" list with normal python code. This list is stored in a file
called 'shortcuts.vdf', which uses a format I have never seen before. The main
two parts of this project are a Parser and a Generator, to allow conversion 
between shortcuts.vdf to python objects and python objects to shortcuts.vdf.
Also included is an API to (hopefully) abstract away the Parser/Generator, 
although you are free to use them directly.

##TODO

- Standardize the test vdf files (as opposed to current vdfs that I haphazardly threw together)
- Create more vdfs with different scenarios (such as tags, which seems to be an
  array, but I can't get Steam to let me add more than 1. Look into that)
  
##License
All of my code is licensed under the MIT License.