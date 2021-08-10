from django.test import TestCase

from core.models import TestModel


class BaseModelTest(TestCase):

    def setUp(self) -> None:
        self.m1 = TestModel.objects.create()

    def test1_all_deleted(self):
        self.m1.deleted = True
        self.m1.save()

        self.assertNotIn(self.m1, TestModel.objects.all())

    def test2_filter_deleted(self):
        self.m1.deleted = True
        self.m1.save()

        self.assertNotIn(self.m1, TestModel.objects.filter())

    def test3_get_deleted(self):
        self.m1.deleted = True
        self.m1.save()

        self.assertRaises(Exception, TestModel.objects.get, id=1)

    def test4_archive(self):
        self.m1.deleted = True
        self.m1.save()  # Deleted!!!

        self.assertNotIn(self.m1, TestModel.objects.all())
        self.assertIn(self.m1, TestModel.objects.archive())
