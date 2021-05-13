from django import forms
from crispy_forms.bootstrap import Tab, TabHolder
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout
from .models import Customers


class CustomerTabs(forms.ModelForm):
    class Meta:
        model = Customers
        fields = ['email','first_name','last_name','phone_number','address','city','state',
            'policy','deductible','claim_num','pid_num','ref_num','loss_date',
            'ticket_num','ticket_date','vin','license',
            'invoice_cost','schedule_date','timeframe_start','timeframe_end'
            ]
        labels = {'email':'Email','first_name':'First Name','last_name':'Last Name','phone_number':'Phone Number',
            'address':'Address','city':'City','state':'State',
            'policy':'Policy','deductible':'Deductible','claim_num':'Claim Number','pid_num':'PID Number','ref_num':'Referral Number','loss_date':'Loss Date',
            'ticket_num':'Ticket Number','ticket_date':'Ticket Date','vin':'Vin Number','license':'License',
            'invoice_cost':'Invoice Cost','schedule_date':'Schedule Date','timeframe_start':'Start Time','timeframe_end':'End Time'
            }
    
    def __init__(self,*args,**kwargs):
        super(CustomerTabs, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            TabHolder(
                Tab('Customer Information',
                    'first_name',
                    'last_name',
                    'phone_number',
                    'address',
                    'city',
                    'state',
                    ),
                Tab('   Billing',
                    'policy',
                    'deductible',
                    'claim_num',
                    'pid_num',
                    'ref_num',
                    'loss_date',
                ),
                Tab('   Vehicle',
                    'ticket_num',
                    '''wo_num','''
                    'ticket_date',
                    'vin',
                    'license',
                ),
                Tab('   Schedule',
                    'invoice_cost',
                    'schedule_date',
                    'timeframe_start',
                    'timeframe_end',
                ),
            )
        )
        self.helper.layout.append(Submit('submit', 'Submit'))