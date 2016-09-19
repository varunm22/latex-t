# Quick Description:

Latex-t takes either pictures of hand drawn equations or data from a Synaptics
touch pad and converts them to Latex! This project was made as part of Hack
MIT 2016. 

# Instructions for use:

Clone the repo and navigate into the repo folder. Then, from the command line,
run:

```
python main.py <image file>
```
For an example image, use 'examples/eq4.jpg'


# Full Description


## Inspiration

When working on problem sets for Mathematics or Computer Science classes, we've all found it's a lot easier to write and think on paper or a white board than it is to think in Latex. The most tedious part of completing these problems always ends up being typing up this inspiration into Latex. 

## What it does

Our project has two parts. The first part takes an image of written equations, then processes the image and splits the work into lines. Using flood fill, our program finds individual characters, then sends these characters to ShapeCatcher.com to map the character to a variety of possible unicode characters. Then our program chooses the most likely match based on a combination of ShapeCatcher's specific score and our prioritizing of common characters. Then, our program utilizes the relative locations of the characters in the initial image to determine if certain numbers are subscript, superscript, and/or fractions. Finally, our program combines the unicode characters and the positional information to generate and email Latex code to the user which can then be added to a Latex document by the user. 

The second part uses the Synaptics Large Touch Sensor to allow the user to draw and input equations into the program. The time based drawing data is then sent to a server running a tool called Seshat, which was written as a PhD project by a computer scientist a couple years ago which interprets single line equations into Latex code.

## How we built it

The first part of our program runs entirely in Python. We use a variety of algorithms to complete the tasks listed above. 

For the second part, we used Python to interpret touch data from the Synaptics large touch sensor and parse it into a format that Seshat could interpret. Then, we used a post request to send this to Seshat so we could return the response as a Latex equation. 

## Challenges we ran into

One of the challenges we ran into was the fact that a lot of character recognition systems utilize time based data in addition to the picture. Because of this, we had to either find a way to get time based data or find a character recognition that didn't need it. Shape catcher was our first approach. Our main difficulty with using Shape Catcher was the fact that it didn't have any sort of API, so we had to manually figure out what post request to send to get back a response. In addition, we had to learn how to parse the HTML response. 

With time based data, we utilized the Synaptics touchpad to draw equations. Then, we could send this data to Seshat server to find the equation. The biggest challenges here were getting the touchpad data to be collected efficiently with a high frame rate, getting the data into the right format, and properly getting data back from the Seshat server. 

## Accomplishments that we're proud of

We were most proud of the fact that we were able to individually implement all of these algorithms for OCR on our own and get them to work together through a variety of files written by a variety of people. We definitely struggled with having clear code with clear specs that people could read and understand to work together with. 

For the second part of the project, we're most proud of the fact that we were able to properly work with the Synaptics touch sense to the extent where we could get data and properly interpret and format it. 

## What we learned

We learned about utilizing get and post requests! Also, we learned a ton about image processing with all of our work with the original image. Also, we learned a lot about using external sensors through our experiments with the Synaptics Touch Sensor. 

## What's next for Latex-t

Right now, Latex-t unfortunately can't hit a lot of specialized mathematical symbols and expressions like integrals and sums. Our goal is next to expand the scope of what Latex-t can accomplish. Then, our plan would be to incorporate both sides of our project into an iPad app. The iPad gives us the interfaces both of a large touchscreen for drawing equations and a camera for taking static pictures of written equations. 


# Imports: 

Python Image Library package
http://www.pythonware.com/products/pil/
I downloaded version 1.1.7 for python 2.7 for Windows only


Numpy
www.numpy.org
always do "import numpy as np" in your program - this is standard

Requests
http://docs.python-requests.org/en/master/
V 2.11.1 for Python 2.7 for Windows


