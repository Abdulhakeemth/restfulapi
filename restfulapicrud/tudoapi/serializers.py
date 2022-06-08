from rest_framework import serializers
from .models import User,Commodity

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
        'firstName',
        'lastName',
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
        'updated',
        )
        



class CommoditySerializer(serializers.ModelSerializer):
    class Meta:
        model = Commodity
        fields = (
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
            'updated'
        )                