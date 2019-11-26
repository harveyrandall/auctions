from django.core.management.base import BaseCommand, CommandError
from django.core.mail import send_mass_mail
from bidding.models import Item

class Command(BaseCommand):
    help = "Notifies users about the ending of a poll. Notifies the winner if there are bids and the poster if there are no bids."

    def handle(self, *args, **kwargs):
        not_notified = Item.objects.filter(ended_notification=False)
        messages = list()
        for i in not_notified:
            if i.item_ended:
                bid = i.current_bid
                if bid:
                    user = bid.user
                    messages.append((
                        'You are the winning bidder for "%s"' % i.item_name,
                        'Congratulations you have won the auction for "%s". The winning bid was £%d' % (i.item_name, bid.amount),
                        "ecs639u@gmail.com",
                        [user.email]
                    ))
                    self.stdout.write(self.style.SUCCESS("'%s' notification has been sent to winner." % i.item_name))
                else:
                    user = i.user
                    messages.append((
                        'Your auction has ended',
                        'Unfortunately no bids were made for your item "%s". Try listing it again?' % (i.item_name),
                        "ecs639u@gmail.com",
                        [user.email]
                    ))
                    self.stdout.write(self.style.SUCCESS("'%s' notification has been sent to item owner. No bids made." % i.item_name))
            else:
                self.stdout.write(self.style.WARNING("'%s' has not ended yet. No notification sent." % i.item_name))

        send_mass_mail(tuple(messages), fail_silently=False)
        not_notified.update(ended_notification=True)