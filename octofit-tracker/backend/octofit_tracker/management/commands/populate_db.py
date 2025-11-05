from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Clear existing data
        Activity.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()
        Workout.objects.all().delete()
        Leaderboard.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='Team Marvel', universe='Marvel')
        dc = Team.objects.create(name='Team DC', universe='DC')

        # Create users (superheroes)
        users = [
            User.objects.create(email='tony@marvel.com', name='Iron Man', team=marvel),
            User.objects.create(email='steve@marvel.com', name='Captain America', team=marvel),
            User.objects.create(email='bruce@marvel.com', name='Hulk', team=marvel),
            User.objects.create(email='clark@dc.com', name='Superman', team=dc),
            User.objects.create(email='bruce@dc.com', name='Batman', team=dc),
            User.objects.create(email='diana@dc.com', name='Wonder Woman', team=dc),
        ]

        # Create activities
        for user in users:
            Activity.objects.create(user=user, activity_type='Running', duration_minutes=30, date=timezone.now().date())
            Activity.objects.create(user=user, activity_type='Cycling', duration_minutes=45, date=timezone.now().date())

        # Create workouts
        Workout.objects.create(name='Super Strength', description='Strength training for superheroes', suggested_for_team=marvel)
        Workout.objects.create(name='Flight Training', description='Aerobic workout for flying heroes', suggested_for_team=dc)

        # Create leaderboards
        Leaderboard.objects.create(team=marvel, total_points=300, rank=1)
        Leaderboard.objects.create(team=dc, total_points=250, rank=2)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
