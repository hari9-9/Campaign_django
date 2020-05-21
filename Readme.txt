The idea is to build a simple competition webpage that
encourages people to spread the news about a new product. Users arrive at the page and
sign up a form. After a successful sign up, they get one entry for the competition. At that
point, they also have an option to share the sign up link. Every successful sign up referred
via the link will give extra competition entries to the original link poster. There is no limit to
the number of entries that a person can have. So the idea is: The more entries you have, the
higher your chance to win the prize.






Development/Target evironment:
    Windows 10
    Python 3.8.2
    Django 3.0.5
    django-crispy-forms 1.9.0


To run the project please double click "run" file  wait until the browser opens automatically if not loaded please refresh the browser


Login Credentials:
Superuser account :
    username: hari
    password: hari

all other accounts such as testuser,testuser2,......testuser10 have common password 123test123

Testing:
    -login using username: hari, password :hari
    -navigate to the user profile to find the unique URL and copy it
    -now log out and open a new tab and paste the unique URL
    -you will be redirected to the register page, sign up with a new user after successfully signing 
     up log in with new user to see base score set to 1
    -now log out and proceed to login with username: hari, password :hari (the user who had shared the link) 
    -navigate to profile to notice score has been incremented by 1
    -also, view leader board to check out where you stand


