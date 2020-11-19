from django.db import models


class Seller(models.Model):
    account = models.CharField(max_length=45)
    password = models.CharField(max_length=200)
    seller_property = models.ForeignKey('SellerProperty', on_delete=models.CASCADE)
    brand_name_korean = models.CharField(max_length=45)
    brand_name_english = models.CharField(max_length=45)
    brand_crm_number = models.CharField(max_length=45)
    is_master = models.BooleanField(default=False)
    is_delete = models.BooleanField(default=False)
    image = models.CharField(max_length=200, null=True)
    seller_status = models.ForeignKey('SellerStatus', on_delete=models.CASCADE, default=1)
    background_image = models.CharField(max_length=200, null=True)
    simple_introduce = models.CharField(max_length=45, null=True)
    detail_introduce = models.CharField(max_length=45, null=True)
    brand_crm_open = models.CharField(max_length=15, null=True)
    brand_crm_end = models.CharField(max_length=15, null=True)
    is_brand_crm_holiday = models.BooleanField(default=False)
    zip_code = models.IntegerField(null=True)
    address = models.CharField(max_length=45, null=True)
    detail_address = models.CharField(max_length=45, null=True)
    delivery_information = models.CharField(max_length=45, null=True)
    refund_exchange_information = models.CharField(max_length=45, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.account

    class Meta:
        db_table = 'sellers'


class SellerProperty(models.Model):
    name = models.CharField(max_length=45)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'seller_properties'


class SellerStatus(models.Model):
    name = models.CharField(max_length=45)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'seller_status'


class SellerStatusHistory(models.Model):
    update_time = models.DateTimeField(auto_now_add=True)
    seller_status = models.ForeignKey('SellerStatus', on_delete=models.CASCADE)
    seller = models.ForeignKey('Seller', on_delete=models.CASCADE)

    def __str__(self):
        return self.seller.account

    class Meta:
        db_table = 'seller_status_histories'


class ManagerInformation(models.Model):
    name = models.CharField(max_length=45, null=True)
    phone_number = models.CharField(max_length=45, null=True)
    email = models.CharField(max_length=45, null=True)
    seller = models.ForeignKey('Seller', on_delete=models.CASCADE)
    ordering = models.IntegerField(null=True)

    def __str__(self):
        return self.seller.account

    class Meta:
        db_table = 'manager_information'
