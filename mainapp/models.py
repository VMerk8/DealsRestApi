from django.db import models
from django.db.models import Sum


class UserQuerySet(models.QuerySet):
    def most_spends(self):
        most_spends_users = User.objects.annotate(total_sum=Sum('deals__total')).order_by('-total_sum')
        return most_spends_users


class User(models.Model):
    objects = UserQuerySet.as_manager()
    username = models.CharField(max_length=30)


class Gem(models.Model):
    title = models.CharField(max_length=30)


class Deal(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='deals')
    item = models.ForeignKey(Gem, on_delete=models.CASCADE, related_name='deals')
    total = models.PositiveIntegerField()
    quantity = models.PositiveSmallIntegerField()
    date = models.DateTimeField()
