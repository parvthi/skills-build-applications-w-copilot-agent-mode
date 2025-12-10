from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status

class APITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.team = Team.objects.create(name='Test Team', universe='Test')
        self.user = User.objects.create(name='Test User', email='test@example.com', team=self.team)
        self.workout = Workout.objects.create(name='Test Workout', description='desc', difficulty='Easy')
        self.activity = Activity.objects.create(user=self.user, activity_type='Test', duration_minutes=10, date='2025-01-01')
        self.leaderboard = Leaderboard.objects.create(team=self.team, total_points=100, rank=1)

    def test_api_root(self):
        response = self.client.get(reverse('api-root'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_list(self):
        response = self.client.get('/api/users/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_team_list(self):
        response = self.client.get('/api/teams/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_activity_list(self):
        response = self.client.get('/api/activities/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_workout_list(self):
        response = self.client.get('/api/workouts/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_leaderboard_list(self):
        response = self.client.get('/api/leaderboards/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
