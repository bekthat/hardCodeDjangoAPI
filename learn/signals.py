from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models import Count
from django.utils import timezone
from .models import Access, Group, Product, User


@receiver(post_save, sender=Access)
def handle_new_access(sender, instance, created, **kwargs):
    if created:

        if instance.product.start_date > timezone.now():

            distribute_or_redistribute(instance)
        else:

            print("Продукт уже начался, доступ не предоставляется")
            instance.delete()


def distribute_or_redistribute(access):
    product = access.product
    user = access.user
    if product.start_date <= timezone.now():
        return
    if not distribute_user(user, product):
        if product.start_date > timezone.now():
            perform_redistribution(product)
            distribute_user(user, product)


def distribute_user(user, product):
    groups = Group.objects.filter(product=product).annotate(user_count=Count('users')).order_by('user_count')
    for group in groups:
        if group.users.count() < group.max_users:
            group.users.add(user)
            return True
    return False


def perform_redistribution(product):
    users = User.objects.filter(access__product=product).distinct()

    groups = Group.objects.filter(product=product)

    total_users = users.count()
    num_groups = groups.count()

    optimal_users_per_group, remainder = divmod(total_users, num_groups)

    for group in groups:
        group.users.clear()

    user_index = 0
    users_list = list(users)

    for group in groups:

        for _ in range(optimal_users_per_group + (1 if remainder > 0 else 0)):
            if user_index < total_users:
                group.users.add(users_list[user_index])
                user_index += 1
        if remainder > 0:
            remainder -= 1
