from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class ModelSmokeTest(TestCase):
    def test_team_str(self):
        team = Team(name='Test Team', universe='Test')
        self.assertEqual(str(team), 'Test Team')
    def test_user_str(self):
        team = Team(name='Test Team', universe='Test')
        user = User(email='test@example.com', name='Test User', team=team)
        self.assertEqual(str(user), 'Test User')
    def test_activity_str(self):
        team = Team(name='Test Team', universe='Test')
        user = User(email='test@example.com', name='Test User', team=team)
        activity = Activity(user=user, activity_type='Test', duration_minutes=10, date='2025-01-01')
        self.assertIn('Test', str(activity))
    def test_workout_str(self):
        workout = Workout(name='Test Workout', description='desc')
        self.assertEqual(str(workout), 'Test Workout')
    def test_leaderboard_str(self):
        team = Team(name='Test Team', universe='Test')
        leaderboard = Leaderboard(team=team, total_points=10, rank=1)
        self.assertIn('Test Team', str(leaderboard))
