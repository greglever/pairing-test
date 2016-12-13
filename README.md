# pairing-test
## An idea for a simple pair programming test
Please add your own ideas and make suggestions to this repo in the form of a PR as you see fit


Run the following in the head of the repository after cloning it to your local machine:

```
python3 -m venv .env
source ./.env/bin/activate
pip install -r requirements.txt
```


Run the application locally: 

```
PYTHONPATH=. python3 ./application.py
```

and have a browser window opened pointed to:

```
http://localhost:5000
```


###Get simple API output to work:
1. returning a user's name based on sending userId with the URL
How do we get *everything* from the `users` table for a given `id`
Given this result is an object, how do we access the name attribute ?
How would we add this userId to the URL ?
What could we do instead of `SELECT *` based on what we use for the output ?" 
Add this in and send it back (problem !)
Fix the problem and get the API working
Would you do any refactoring of this code, put anything into functions or move anything around ? Why ?


### Create a simple analytics API endpoint: 
1. that accepts a userId and returns the mean and standard deviation of the yAxisValues and xAxisValues it gets from do_some_simple_analytics and also the gradient of the points plotted on a graph.
Have you used numpy before ? 
Have you used scipy before ?
See if they open iPython and import do_some_simple_analytics. 
Run the function with a user Id and inspect the output.

### Additional questions

3. Should we be using analytics functions in SQL or using numpy/scipy instead ? Advantages or disadvantages ?

4. How would you write a list comprehension in Python ?

5. How about a dictionary comprehension ?

6. Give them someone else's algorithm and see if they can implement it OK

All the while you can see how familiar they are with the particular editor being used.