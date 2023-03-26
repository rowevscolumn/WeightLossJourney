# WeightLossJourney

A simple Python script that I use to take my weight loss progress into a csv

Back in about 2013 I was on a weight loss journey and to keep track of my progress, instead of writing it down or using an app, I chose to challenge myself by using MySQL to keep track, because I needed practice with my SQL statements. That table is now well and gone, but it did help me know how well I did. In August of 2022, I wanted to restart my weight loss journey, and wrote a simple Python script to save my progress into a csv file. The reasoning was several fold. I wanted to keep my Python and Pandas up to par, I wanted to play around with widgets, and also I took that csv file and loaded it into Power BI for my first attempt at making a graph.

Have a look for yourself for a quick rewrite of it, to tidy it up a bit. It's still incredibly simple code, but effective. And I plan on adding more stuff including a matplotlib graph as well as other things.

## Steps

1. Open WeightLossJourney.ipynb in Jupyter Notebook
1. Run the first 3 cells to open the data.
1. type your new weight into the Widget textbox
1. Run the next cell to save that number into your csv file. It automatically time stamps into ISO-8601 Format.
