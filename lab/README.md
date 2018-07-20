## Y2 2018 Summer: Routing Lab

Welcome to the routing lab! Please read all the instructions so you don't
get lost halfway through, but definitely feel free to ask for help if you
get stuck. Good luck, and have fun!

### Part 0: Setup

1. Before you start coding, make sure you clone the repository for this lab:
```
cd ~/Desktop
git clone https://github.com/meet-projects/y2s18-routing.git
cd y2s18-routing
subl lab &
```

2. From the databases lab yesterday, copy over all the code in
`knowledge_databases.py` and `knowledge_model.py`.

3. Double-check that everything still works like it did before.
In this lab, we're going to be connecting routing with databases,
so it's important to have a working database! If the database lab
was not finished or if the code doesn't work, you can also just
use the example code, but let a TA know first!

### Part 1: Basic routing

1. Now for the fun stuff! In `app.py`, change the route for `/` to the
`home.html` template. You can open `home.html` in Sublime to see what the
template looks like. Remember that templates are in the `templates` folder!

2. You can go back to the command line now and start the server, using 
`python app.py`. In Chrome, you can go to `http://127.0.0.1:5000`,
and make sure that you see the template you are expecting to see.

3. Back to coding now! In `app.py`, add a route so that when you navigate to
`http://127.0.0.1:5000/article/4` you see the `article.html` template where
`article_id` is 4.

### Part 2: Displaying an article

1. Add templating elements to `article.html` so that it can display
article information, not just the `article_id`.

2. Edit the route you just added in `app.py` to give the
template all the information it needs. *Hint*: You'll need to access the
database for this! Take a look at your `knowledge_databases.py` for some
functions to use.

3. In `article.html` add a link to the home page. *Hint*: You may want to
use `url_for()`.

4. Refresh your webpage on Chrome to make sure everything works as expected.
If there are errors and the server goes down, you can restart the server
from the command line with `python app.py` again.

### Part 3: Displaying feature articles

1. Pick a few articles in your database to be feature articles, and remember
their `article_id`s. In `home.html`, add templating code to display the
topics of all the feature articles using `{% for %}` and `{% endfor %}`.
You may want to look at older slides for review on how to use them.

2. Edit the route to the home page to give `home.html` all the information it
needs to display the feature articles. *Hint*: You'll need to query the
database for each article you want to feature.

3. In the `home.html` template, add a link in the same `for` loop which will
bring you to the page for each feature article.

4. Again, check that everything works on Chrome. Refresh your server if it
goes down with `python app.py`.

### Part 4. Making it colorful

1. Congratulations! You're done with the routing part of the lab.

2. Make your new website prettier by adding your own CSS and additional
templating like you've learned in the past few days!
