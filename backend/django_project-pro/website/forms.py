from django import forms

class SigninForm(forms.Form):
    username = forms.CharField(label='username', max_length=100)
    password = forms.CharField(label='password', max_length=100)

class accountForm(forms.Form):
    userRole = forms.IntegerField()
    username = forms.CharField(label='username', max_length=100)
    password = forms.CharField(label='password', max_length=100)
    firstname = forms.CharField(label='firstname', max_length=100)
    lastname = forms.CharField(label='lastname', max_length=100)
    address = forms.CharField(label='address', max_length=100)
    balance = forms.DecimalField(decimal_places=2, max_digits = 10)
    payment_method = forms.CharField(label='payment_method', max_length=100)

class deleteAccountForm(forms.Form):
    username = forms.CharField(label='username', max_length=100)
    password = forms.CharField(label='password', max_length=100)

class updateAccountForm(forms.Form):
    token = forms.CharField(label='username', max_length=100)
    payment_method = forms.CharField(label='payment_method', max_length=100)
    address = forms.CharField(label='address', max_length=100)

class AddProductForm(forms.Form):
    category = forms.CharField(max_length=255)
    name = forms.CharField(max_length=255)
    price = forms.DecimalField()
    seller = forms.IntegerField()
    image_id = forms.CharField(max_length=255)
    num_sales = forms.IntegerField()
    inventory = forms.IntegerField()
    approval_status = forms.IntegerField()
    description = forms.CharField(max_length=255)

######################################################################################
class RemoveProductForm(forms.Form):
    product_id = forms.IntegerField()

class ShoppingCartForm(forms.Form):
    token = forms.CharField(max_length=255)

class AddToCartForm(forms.Form):
    item_id = forms.IntegerField()

class RemoveFromCartForm(forms.Form):
    item_id = forms.IntegerField()
