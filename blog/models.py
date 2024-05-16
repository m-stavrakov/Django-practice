from django.db import models
from django.utils import timezone
# this is from the authentication which is in /admin; it is build in
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
# no need to create id as django handles that by himself, can see in the models folder
# every time you make any changes run commands:
# $ python manage.py makemigrations
# $ python manage.py migrate
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    # if the user is deleted all the posts by him will be deleted as well
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    # so when we create a new post (with the view class) the user will be redirected 
    def get_absolute_url(self):
        # with reverse we can find an url by a name, and will bring us the url for to the according pk
        return reverse('post-detail', kwargs={'pk': self.pk})

# command $python manage.py sqlmigrate {name of project (blog)} 0001
# this will migrate to sql; To view the SQL that will be created from the class Post in models.py 
# BEGIN;
# --
# -- Create model Posts
# --
# CREATE TABLE "blog_posts" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "title" varchar(100) NOT NULL, "content" text NOT NULL, "date_posted" datetime NOT NULL, "author_id" integer NOT NULL REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED);
# CREATE INDEX "blog_posts_author_id_6f561d00" ON "blog_posts" ("author_id");
# COMMIT;