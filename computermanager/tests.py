from django.test import TestCase
from django.utils import timezone

# Create your tests here.

from .models import Computer

class ComputerModelTest(TestCase):

    def test_all_possible_status(self):

        testjsondata = {'computer': 'test', 'status': 'Waiting'}
        for choice in Computer.CHOICES:
            testsave = Computer(name=testjsondata['computer'] + choice[1], status=choice[1], start_time=timezone.now())
            testsave.save()
            testload = Computer.objects.get(name=testjsondata['computer'] + choice[1])
