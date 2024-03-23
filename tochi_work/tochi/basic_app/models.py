from django.db import models
from django.contrib.auth.models import User

class UploadedImage(models.Model):
    username = models.CharField(max_length=100)
    image = models.ImageField(upload_to='profile_pics/')

class UploadKYC(models.Model):
    card = models.ImageField(upload_to="profile_pics")
    imagePassport = models.ImageField(upload_to="profile_pics")

class AccountBalance(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    acc_balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    deposit_profit = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    total_investment = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    total_active = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    total_deposit = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    total_withdraw = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    gift =  models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    referral =  models.DecimalField(max_digits=10, decimal_places=2, default=0.0)


    pr_balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    pr_plan1 = models.CharField(max_length=20, blank=True, default="")
    pr_plan2 = models.CharField(max_length=20, blank=True, default="")
    pr_plan3 = models.CharField(max_length=20, blank=True, default="")
    pr_plan4 = models.CharField(max_length=20, blank=True, default="")
    pr_plan5 = models.CharField(max_length=20, blank=True, default="")
    pr_plan6 = models.CharField(max_length=20, blank=True, default="")
    pr_plan7 = models.CharField(max_length=20, blank=True, default="")
    pr_plan8 = models.CharField(max_length=20, blank=True, default="")
    pr_plan9 = models.CharField(max_length=20, blank=True, default="")
    pr_plan10 = models.CharField(max_length=20, blank=True, default="")
    pr_plan11 = models.CharField(max_length=20, blank=True, default="")
    pr_plan12 = models.CharField(max_length=20, blank=True, default="")
    
    pr_amount1 = models.CharField(max_length=20, blank=True, default="")
    pr_amount2 = models.CharField(max_length=20, blank=True, default="")
    pr_amount3 = models.CharField(max_length=20, blank=True, default="")
    pr_amount4 = models.CharField(max_length=20, blank=True, default="")
    pr_amount5 = models.CharField(max_length=20, blank=True, default="")
    pr_amount6 = models.CharField(max_length=20, blank=True, default="")
    pr_amount7 = models.CharField(max_length=20, blank=True, default="")
    pr_amount8 = models.CharField(max_length=20, blank=True, default="")
    pr_amount9 = models.CharField(max_length=20, blank=True, default="")
    pr_amount10 = models.CharField(max_length=20, blank=True, default="")
    pr_amount11 = models.CharField(max_length=20, blank=True, default="")
    pr_amount12 = models.CharField(max_length=20, blank=True, default="")
   
    pr_profit1 = models.CharField(max_length=20, blank=True, default="")
    pr_profit2 = models.CharField(max_length=20, blank=True, default="")
    pr_profit3 = models.CharField(max_length=20, blank=True, default="")
    pr_profit4 = models.CharField(max_length=20, blank=True, default="")
    pr_profit5 = models.CharField(max_length=20, blank=True, default="")
    pr_profit6 = models.CharField(max_length=20, blank=True, default="")
    pr_profit7 = models.CharField(max_length=20, blank=True, default="")
    pr_profit8 = models.CharField(max_length=20, blank=True, default="")
    pr_profit9 = models.CharField(max_length=20, blank=True, default="")
    pr_profit10 = models.CharField(max_length=20, blank=True, default="")
    pr_profit11 = models.CharField(max_length=20, blank=True, default="")
    pr_profit12 = models.CharField(max_length=20, blank=True, default="")
   

    pr_date1 = models.CharField(max_length=20, blank=True, default="")
    pr_date2 = models.CharField(max_length=20, blank=True, default="")
    pr_date3 = models.CharField(max_length=20, blank=True, default="")
    pr_date4 = models.CharField(max_length=20, blank=True, default="")
    pr_date5 = models.CharField(max_length=20, blank=True, default="")
    pr_date6 = models.CharField(max_length=20, blank=True, default="")
    pr_date7 = models.CharField(max_length=20, blank=True, default="")
    pr_date8 = models.CharField(max_length=20, blank=True, default="")
    pr_date9 = models.CharField(max_length=20, blank=True, default="")
    pr_date10 = models.CharField(max_length=20, blank=True, default="")
    pr_date11 = models.CharField(max_length=20, blank=True, default="")
    pr_date12 = models.CharField(max_length=20, blank=True, default="")
    



    tr_deposit = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    tr_withdraw = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    tr_balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    tr_others = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

    tr_amount1 = models.CharField(max_length=20, blank=True, default="")
    tr_amount2 = models.CharField(max_length=20, blank=True, default="")
    tr_amount3 = models.CharField(max_length=20, blank=True, default="")
    tr_amount4 = models.CharField(max_length=20, blank=True, default="")
    tr_amount5 = models.CharField(max_length=20, blank=True, default="")
    tr_amount6 = models.CharField(max_length=20, blank=True, default="")
    tr_amount7 = models.CharField(max_length=20, blank=True, default="")
    tr_amount8 = models.CharField(max_length=20, blank=True, default="")
    tr_amount9 = models.CharField(max_length=20, blank=True, default="")
    tr_amount10 = models.CharField(max_length=20, blank=True, default="")
    tr_amount11 = models.CharField(max_length=20, blank=True, default="")
    tr_amount12 = models.CharField(max_length=20, blank=True, default="")


    tr_paymentmode1 = models.CharField(max_length=20,  blank=True, default="")
    tr_paymentmode2 = models.CharField(max_length=20,  blank=True, default="")
    tr_paymentmode3 = models.CharField(max_length=20,  blank=True, default="")
    tr_paymentmode4 = models.CharField(max_length=20,  blank=True, default="")
    tr_paymentmode5 = models.CharField(max_length=20,  blank=True, default="")
    tr_paymentmode6 = models.CharField(max_length=20,  blank=True, default="")
    tr_paymentmode7 = models.CharField(max_length=20,  blank=True, default="")
    tr_paymentmode8 = models.CharField(max_length=20,  blank=True, default="")
    tr_paymentmode9 = models.CharField(max_length=20,  blank=True, default="")
    tr_paymentmode10 = models.CharField(max_length=20,  blank=True, default="")
    tr_paymentmode11 = models.CharField(max_length=20,  blank=True, default="")
    tr_paymentmode12 = models.CharField(max_length=20,  blank=True, default="")


    tr_status1 = models.CharField(max_length=20,  blank=True, default="")
    tr_status2 = models.CharField(max_length=20,  blank=True, default="")
    tr_status3 = models.CharField(max_length=20,  blank=True, default="")
    tr_status4 = models.CharField(max_length=20,  blank=True, default="")
    tr_status5 = models.CharField(max_length=20,  blank=True, default="")
    tr_status6 = models.CharField(max_length=20,  blank=True, default="")
    tr_status7 = models.CharField(max_length=20,  blank=True, default="")
    tr_status8 = models.CharField(max_length=20,  blank=True, default="")
    tr_status9 = models.CharField(max_length=20,  blank=True, default="")
    tr_status10 = models.CharField(max_length=20,  blank=True, default="")
    tr_status11 = models.CharField(max_length=20,  blank=True, default="")
    tr_status12 = models.CharField(max_length=20,  blank=True, default="")

    tr_date1 = models.CharField(max_length=20,  blank=True, default="")
    tr_date2 = models.CharField(max_length=20,  blank=True, default="")
    tr_date3 = models.CharField(max_length=20,  blank=True, default="")
    tr_date4 = models.CharField(max_length=20,  blank=True, default="")
    tr_date5 = models.CharField(max_length=20,  blank=True, default="")
    tr_date6 = models.CharField(max_length=20,  blank=True, default="")
    tr_date7 = models.CharField(max_length=20,  blank=True, default="")
    tr_date8 = models.CharField(max_length=20,  blank=True, default="")
    tr_date9 = models.CharField(max_length=20,  blank=True, default="")
    tr_date10 = models.CharField(max_length=20,  blank=True, default="")
    tr_date11 = models.CharField(max_length=20,  blank=True, default="")
    tr_date12 = models.CharField(max_length=20,  blank=True, default="")

   

    def __str__(self):
        return f"Account Balance for {self.user.username}"