from django.core.exceptions import ValidationError
from django.test import TestCase
from django.utils import timezone

from .models import Computer

class ComputerModelTest(TestCase):

    def test_all_possible_status(self):

        # First a test to make sure full_clean is properly checking the choices field
        testjsondata = {'computer': 'test', 'status': 'BadInput'}
        testsave = Computer(name=testjsondata['computer'], status=testjsondata['status'], start_time=timezone.now())
        with self.assertRaises(ValidationError):
            testsave.full_clean()

        # Checks that each choice can be saved and loaded
        for choice in Computer.CHOICES:
            testsave = Computer(name=testjsondata['computer'] + choice[1], status=choice[1], start_time=timezone.now())
            testsave.save()
            self.assertIs(Computer.objects.get(name=testjsondata['computer'] + choice[1]).status == choice[1], True)
