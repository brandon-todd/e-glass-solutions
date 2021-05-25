from django import forms
from crispy_forms.bootstrap import Tab, TabHolder
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout
from .models import Customers
from django.template.loader import render_to_string

class CustomerTabs(forms.Form):
    email = forms.EmailField(max_length = 50)
    first_name = forms.CharField(max_length = 50)
    last_name = forms.CharField(max_length = 50)
    phone_number = forms.CharField(validators=[Customers.phone_regex], max_length=17)
    address = forms.CharField(max_length = 200)
    city = forms.CharField(max_length = 50)
    state = Customers.state
    policy = forms.CharField(max_length = 50)
    deductible = forms.CharField(max_length = 50)
    claim_num = forms.IntegerField()
    pid = forms.IntegerField()
    ref_num = forms.IntegerField()
    loss_date = forms.DateField()
    ticket_num = forms.IntegerField()
    wo_num = Customers.wo_num
    ticket_date = forms.DateField()
    vin = forms.CharField(max_length = 30)
    license = forms.CharField(max_length=20)
    invoice_cost = forms.IntegerField()
    schedule_date = forms.DateField()
    timeframe_start = forms.TimeField()
    timeframe_end = forms.TimeField()
    TEMPLATE_PACK = 'bootstrap4'
    css_class = 'tab-pane'
    def render_link(self, template_pack=TEMPLATE_PACK, **kwargs):
        """
        Render the link for the tab-pane. It must be called after render so css_class is updated
        with active if needed.
        """
        link_template = self.link_template % template_pack
        return render_to_string(link_template, {'link': self})

    labels = {'email':'Email','first_name':'First Name','last_name':'Last Name','phone_number':'Phone Number',
        'address':'Address','city':'City','state':'State',
        'policy':'Policy','deductible':'Deductible','claim_num':'Claim Number','pid_num':'PID Number','ref_num':'Referral Number','loss_date':'Loss Date',
        'ticket_num':'Ticket Number','ticket_date':'Ticket Date','vin':'Vin Number','license':'License',
        'invoice_cost':'Invoice Cost','schedule_date':'Schedule Date','timeframe_start':'Start Time','timeframe_end':'End Time',
    }
    
    def __init__(self,*args,**kwargs):
        super(CustomerTabs, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = True
        self.helper.render_unmentioned_fields = False
        self.helper.include_media = True
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
                Tab('Billing',
                    'policy',
                    'deductible',
                    'claim_num',
                    'pid_num',
                    'ref_num',
                    'loss_date',
                ),
                Tab('Vehicle',
                    'ticket_num',
                    'wo_num',
                    'ticket_date',
                    'vin',
                    'license',
                ),
                Tab('Schedule',
                    'invoice_cost',
                    'schedule_date',
                    'timeframe_start',
                    'timeframe_end',
                ),
            )
        )
        self.helper.layout.append(Submit('submit', 'Submit'))