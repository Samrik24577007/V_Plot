The mapped.bed.gz file contains the starting and ending positions of the long about 1000bp DNA in 2nd and 3rd column and the starting and ending position of the smaller fragment binding to it in column 8 and 9, also its length in column 11

First we created a anonymous dictonary under which created another and set initial value to zero.
Use stdin to read the file line by line, split line separated by tab and store each element in a list.
"a" is the distance between the middle point of large DNA and fragment DNA.
"b" is half length of the larger DNA
Distance between the middle points and length of DNA fragments are normalised with respect to half length as 500 bp.
I stored distance and different lengths under that in the dictonary. 
I counted the number of occurance of each length under each distance and stored in dictionary.
I calculated the total number of lengths and wrt that calculated normalised frequency of each length
I got output as three columns, in 1st column the distance of fragment from the larger DNA, in 2nd column lengths of fragments having that distance and in 3rd column frequency of that length.

I plotted the output data using matplotlib.pyplot where distance as X-axis and length as Y-axis with frequencies as colour gradient,colourbar is used to understand relation between colour density and frequency. 
