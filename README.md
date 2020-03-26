# DatingSite-Plus-Digit-Recognition-with-KNN
Learning Applied Machine learning from Book 'Machine learning in Action'

Improving matches from a dating site with kNN:
My friend Hellen has been using some online dating sites to find different people to
go out with. She realized that despite the site’s recommendations, she didn’t like
everyone she was matched with. After some introspection, she realized there were
three types of people she went out with:



  ■ People she didn’t like
  
  ■ People she liked in small doses
  
  ■ People she liked in large doses
  

After discovering this, Hellen couldn’t figure out what made a person fit into any of
these categories. They all were recommended to her by the dating site. The people
whom she liked in small doses were good to see Monday through Friday, but on the
weekend she’d rather spend time with the people she liked in large doses. Hellen has
asked us to help her filter future matches to categorize them. In addition, Hellen has
collected some data that isn’t recorded by the dating site, but she feels it’s useful in
selecting people to go out with.


The data Hellen collected is in a text file called dataset.txt.
Hellen has been collecting this data for a while and has 1,000 entries. A new sample is on each line, and
Hellen has recorded the following features:

  ■ Number of frequent flyer miles earned per year
  
  ■ Percentage of time spent playing video games
  
  ■ Liters of ice cream consumed per week

Using this information and dataset, suitable match is get throgh KNN, which I implemented from sctrach.


A handwriting recognition system using kNN:

We’re going to work through an example of handwriting recognition with our kNN
classifier. We’ll be working only with the digits 0–9. 
These digits were processed through image-processing software to make them
all the same size and color.1
They’re all 32x32 black and white. The binary images
were converted to text format to make this example easier, although it isn’t the most
efficient use of memory. 
We’ll use the trainingDigits directory to train our classifier and testDigits to

test it. There’ll be no overlap between the two groups. Feel free to take a look at the
files in those folders.

We’d like to use the same classifier that we used in the previous two examples, so
we’re going to need to reformat the images to a single vector. We’ll take the 32x32
matrix that is each binary image and make it a 1x1024 vector. After we do this, we can
apply it to our existing classifier.

The following code is a small function called img2vector, which converts the
image to a vector. The function creates a 1x1024 NumPy array, then opens the given
file, loops over the first 32 lines in the file, and stores the integer value of the first 32
characters on each line in the NumPy array. This array is finally returned


