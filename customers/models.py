from django.db import models
from django.core.validators import RegexValidator
from localflavor.us.models import USStateField
# Create your models here.
class Customers(models.Model):
    email = models.EmailField(max_length = 50,name ='email',default = '',null = False, blank = False)
    first_name = models.CharField(max_length = 50, blank = False,default = '')
    last_name = models.CharField(max_length = 50,blank = False,default = '')
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17,name = 'phone_number')
    address = models.CharField(max_length = 200,blank = False, default = '')
    city = models.CharField(max_length = 50,blank = False,null = False, default = '')
    state = USStateField(null = False,blank = False, default = '')
    policy = models.CharField(max_length = 50, null = True, blank = True,name = 'policy')
    deductible = models.CharField(max_length = 50,null =True,blank = True,name = 'deductible')
    claim_num = models.IntegerField(null = True,blank = True,name ='claim_num')
    pid = models.IntegerField(null=True,blank=True,name = 'pid_num')
    ref_num = models.IntegerField(null=True,blank=True,name='ref_num')
    loss_date = models.DateField(null = True,blank=True,name = 'loss_date')
    ticket_num = models.IntegerField(null =True,blank = True,name = 'ticket_num')
    wo_num = models.AutoField(name ='wo_num',primary_key = True)
    ticket_date = models.DateField(null=True,blank=True,name='ticket_date')
    vin = models.CharField(null = False,blank = False,max_length = 30,default='',name = 'vin')
    license = models.CharField(null=True,blank=True,max_length=20,name = 'license')
    invoice_cost = models.IntegerField(null = False,blank=False,name = 'invoice_cost')
    schedule_date = models.DateField(null = True,blank = True, name = 'schedule_date')
    timeframe_start = models.TimeField(null = True,blank=True,name = 'timeframe_start')
    timeframe_end = models.TimeField(null=True,blank=True,name = 'timeframe_end')
    class Meta:
        managed = True
        db_table = 'customers'