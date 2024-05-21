from django.core.management.base import BaseCommand
from django.utils import timezone
from books.models import BookCheckout


class Command(BaseCommand):
    help = 'Removes expired book reservations'

    def handle(self, *args, **options):
        # Get all book checkouts where the return_date is null (not returned yet)
        unreturned_checkouts = BookCheckout.objects.filter(return_date__isnull=True)

        # Loop through each unreturned checkout
        for checkout in unreturned_checkouts:
            # Checked if the checkout date is more than 1 day ago
            if checkout.checkout_date < timezone.now().date() - timezone.timedelta(days=1):
                # If it is, delete the checkout (remove the reservation)
                checkout.delete()
                self.stdout.write(
                    self.style.SUCCESS(f'Removed reservation for {checkout.book.title} by {checkout.user.username}'))
