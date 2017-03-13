
# coding: utf-8

# # Assignment for week 2
# 
# Use the following table to provide us with
# 
# |name | exam number|
# |----|----|
# |Thomas Griep| 2001366|
# |other group member's name| exam number|

# In the following cell type in markdown the text with a link and an image that you can find [here](http://janboone.github.io/programming-for-economists/_downloads/markdown_text_programming_for_economists.html).
# 
# Note that we are interested in seeing bold text, italics and math etc. Use your browser to find the image's address.
# 
# After you type your text, press SHIFT-ENTER and check whether the text looks the same as [here](http://janboone.github.io/programming-for-economists/_downloads/markdown_text_programming_for_economists.html).

# # this is a section
# ## this is a subsection
# A bullet list looks *like this*:
# * bullet 1
# * bullet 2
# * **bullet 3**
# we can like to this [ wonderfull page ](http://janboone.github.io/programming-for-economists/index.html)
# 
# ![](http://images2.mtv.com/uri/mgid:file:docroot:mtv.com:/crop-images/2013/11/05/the_who_umg.jpg?enlarge=false&maxdimension=1300&matte=true&matteColor=black&quality=0.85 "the who")
# Let's type some math:
# 
# $\sin(x) + \cos(x) = 2$
# 
# As a rule, I really like this line
# 
# ___________________________________
# 
# We are done.
# 

# Install plotly on your computer using these [instructions to install plotly.](https://plot.ly/python/getting-started/) Note that with anaconda you can use "conda install plotly" instead of "pip install".
# 
# Now let us check whether it works, run the code in the following cell:

# In[4]:

from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
from plotly.graph_objs import Bar, Scatter, Figure, Layout
init_notebook_mode(connected=True)
from numpy import arange
range_x = arange(-2,2.1,0.1)
iplot([{"x": range_x, "y": [x**2 for x in range_x]}])


# Do you see the graph in your notebook? If not, ask us during the tutorial!

# After you have finished, we need to upload this notebook on github. Make sure that you upload the file on the github page of each group member.

# Instructions on how to upload this on github can be found [on this page](http://janboone.github.io/programming-for-economists/github.html). This page has two screencasts: one shows how to drag the notebook onto your github page, the other shows how you can use the command line to upload your notebook.
# 

# Remember to update the README file in your repository to include a link to this notebook on github.

# 
