import datetime
from celery import shared_task
from .models import Loan
from django.core.mail import send_mail
from django.conf import settings
from library_system.celery import app

@shared_task
def send_loan_notification(loan_id):
    try:
        loan = Loan.objects.get(id=loan_id)
        member_email = loan.member.user.email
        book_title = loan.book.title
        send_mail(
            subject='Book Loaned Successfully',
            message=f'Hello {loan.member.user.username},\n\nYou have successfully loaned "{book_title}".\nPlease return it by the due date.',
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[member_email],
            fail_silently=False,
        )
    except Loan.DoesNotExist:
        pass

@app.task
def check_overdue_loans():
    overdue_loans = Loan.objects.filter(is_returned=False, due_date__lt=datetime.date.today())

    for loan in overdue_loans:

        try:
            member_email = loan.member.user.email
            book_title = loan.book.title
            send_mail(
                subject='Book Overdue Reminder',
                message=f'Hello {loan.member.user.username},\n\nYour loan of "{book_title}" is overdue.\nPlease return as soon as you can. Thanks.',
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[member_email],
                fail_silently=False,
            )
        except:
            pass

