from djongo import models
from djongo.models.fields import ObjectIdField

class User(models.Model):
    id = ObjectIdField(primary_key=True)  # Use ObjectIdField for compatibility with ArrayField
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username

class Team(models.Model):
    id = ObjectIdField(primary_key=True)
    name = models.CharField(max_length=100)
    members = models.ArrayField(model_container=User)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Activity(models.Model):
    id = ObjectIdField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    activity_type = models.CharField(max_length=100)
    duration = models.IntegerField()  # in minutes
    calories_burned = models.FloatField()
    date = models.DateField()

    def __str__(self):
        return f"{self.activity_type} by {self.user.username}"

class Leaderboard(models.Model):
    id = ObjectIdField(primary_key=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    points = models.IntegerField()

    def __str__(self):
        return f"{self.team.name} - {self.points} points"

class Workout(models.Model):
    id = ObjectIdField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    duration = models.IntegerField()  # in minutes
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name