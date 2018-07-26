# Y2 2018 Summer: Routing Lab

Welcome to the routing lab! Please read all the instructions so you don't
get lost halfway through, but definitely feel free to ask for help if you
get stuck. Good luck, and have fun!

## Lecture Exercises

### Part 0: Setup

Before you start coding, make sure you clone the repository for this lab:
```
cd ~/Desktop
git clone https://github.com/meet-projects/y2s18-routing.git
cd y2s18-routing
subl lab &
```

### Part 1: Basic routing

In `app.py`, change the route for `/` to display the `home.html`
template. You can open `home.html` in Sublime to see what the template
looks like. Remember that templates are in the `templates` folder!

*Hint*: Remember functions you've learned in earlier lectures, like
`render_template`.

You can go back to the command line now and start the server, using
`python app.py`. In Chrome, go to `http://127.0.0.1:5000` to see what
it looks like so far.

### Part 2: Variable Routes

In `app.py`, add a route and call the function for this route
`display_student(student_id)`. When you navigate to
`http://127.0.0.1:5000/student/4` you see the `student.html` template
where `student_id` is 4.

*Hint*: The variable `student_id` should have type `int`.

### Part 3: URL Building

In `student.html`, add a link to the home page.

*Hint*: Remember how to use `url_for()`.

## Independent Lab

1. In `app.py`, in `display_student(student_id)`, assign a variable
called `student` to the `Student` object whose `id` is `student_id`.
*Hint*: In `databases.py`, there is a function called `query_by_id(id)` that
returns the Student object with the given `id`, which is an `int`.

2. In `student.html`, add some text and the templating elements `{{ name }}`,
`{{ year }}`, and `{{ finished_lab }}`.

3. Back to `display_student(student_id)` in `app.py`. Edit the return
statement to give the template all the information it needs.
*Hint*: `student.name` should give you the `name` attribute of the
`Student` object called `student`.

4. Refresh your webpage on Chrome to make sure everything works as expected.
If there are errors and the server goes down, you can restart the server
from the command line with `python app.py` again.

----------------------

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
