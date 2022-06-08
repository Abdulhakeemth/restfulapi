from django.contrib import admin

# Register your models here.
from django.contrib import admin
from tudoapi.models import *
from .models import User,Commodity


class UserAdmin(admin.ModelAdmin):
    list_display = ('firstName','lastName',
        'address',
        'city',
        'country',
        'pin',
        'icon',
        'emailId',
        'primaryContactNumber',
        'isMailVerified',
        'isPhoneVerified',
        'emailKey',
        'password',
        'otp',
        'otpGenTime',
        'isRegisteredByGoogle',
        'isRegisteredByFacebook',
        'isRegisteredByApple',
        'djangoUser',
        'isActive',
        'isDeleted',
        'created',
        'updated')
admin.site.register(User,UserAdmin)

class CommodityAdmin(admin.ModelAdmin):
    list_display = (
         'name',
            'description',
            'minimum_order_quantity',
            'todays_price',
            'offer_price',
            'measuring_unit',
            'discounted_price',
            'bulk_price',
            'bulk_qty',
            'available_quantity',
            'min_available_qty',
            'max_available_qty',
            'max_qty_allowed_per_order',
            'gst',
            'isActive',
            'quantityPerCrate',
            'delivery_charge',
            'packingByCrateOrBag',
            'created',
            'updated')
admin.site.register(Commodity,CommodityAdmin)            
