from django.test import TestCase
from django.contrib.auth.models import User
from .models import Team, Activity, Leaderboard, Workout

class ModelTests(TestCase):
    def test_team_creation(self):
        team = Team.objects.create(name='Test Team')
        self.assertEqual(team.name, 'Test Team')

    def test_activity_creation(self):
        activity = Activity.objects.create(user='testuser', type='run', duration=10, team='Test Team')
        self.assertEqual(activity.type, 'run')

    def test_leaderboard_creation(self):
        lb = Leaderboard.objects.create(team='Test Team', points=100)
        self.assertEqual(lb.points, 100)

    def test_workout_creation(self):
        workout = Workout.objects.create(name='Test Workout', description='desc', difficulty='Easy')
        self.assertEqual(workout.difficulty, 'Easy')

    def test_user_creation(self):
        user = User.objects.create_user(username='testuser', email='test@example.com', password='pass')
        self.assertEqual(user.username, 'testuser')
