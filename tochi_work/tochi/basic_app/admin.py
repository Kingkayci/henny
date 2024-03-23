from django.contrib import admin
from .models import UploadedImage, UploadKYC, AccountBalance

# Register your models here.
admin.site.register(UploadedImage)
admin.site.register(UploadKYC)
admin.site.register(AccountBalance)