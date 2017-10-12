# Python Snippets for Machine Learning Learning

This repository covers some developed/in development snippets used for machine learning in Python, such as: CSV to ARFF, CSV percentage split.

# TECHNOLOGIES & LIBRARIES USED

1) [Python 2.7](https://docs.python.org/2/)

# SNIPPETS

1\. CSV percentage split (supervised learning): insert a CSV file with semicolon delimitators and split proportionally to each true label, exporting two files - one for training (normally 80%) and another for testing (normally 20%).

# HOW TO USE

1\. Set permissions to split-supervised-learning.py to run:

```
$ chmod +x split-supervised-learning.py
```

2\. Insert the CSV file to be splitted inside /data/raw.

3\. Make sure the delimitators for each value is a semicolon and the header titles are between quotes.

4\. Run python script with the true label name, the file name from /data/raw (without .csv extension), the training-rate and the testing rate. Examples:

```
$ ./split-supervised-learning.py lettr letters 80 20
$ ./split-supervised-learning.py quality wine 90 10
```

# REFERENCES

1) [Lichman, M. (2013). UCI Machine Learning Repository. Irvine, CA: University of California, School of Information and Computer Science.](http://archive.ics.uci.edu/ml)

2) [Letter Recognition Data Set.](https://archive.ics.uci.edu/ml/datasets/Letter+Recognition)

3) [P. Cortez, A. Cerdeira, F. Almeida, T. Matos and J. Reis. Modeling wine preferences by data mining from physicochemical properties. In Decision Support Systems, Elsevier, 47(4):547-553, 2009.](https://archive.ics.uci.edu/ml/datasets/wine+quality)

# COLABORATORS

KAWASAKI, Davi // davishinjik [at] gmail.com

FLAUSINO, Matheus // matheus.negocio [at] gmail.com

# CONTACT & FEEDBACKS

Feel free to contact or pull request me to any relevant updates you may enquire:

KAWASAKI, Davi // davishinjik [at] gmail.com
