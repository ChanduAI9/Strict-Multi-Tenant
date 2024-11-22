from django.db import models
from django_tenants.models import TenantMixin, DomainMixin

class Client(TenantMixin):
    name = models.CharField(max_length=100)
    paid_until = models.DateField()
    on_trial = models.BooleanField(default=True)
    schema_name = models.CharField(max_length=100, unique=True)
    
    auto_create_schema = True  



    def __str__(self):
        return self.name

class Domain(DomainMixin):
    domain=models.CharField(max_length=255,unique=True)
    is_primary=models.BooleanField(default=True)
    tenant=models.ForeignKey(Client,related_name='domain',on_delete=models.CASCADE)



    def __str__(self):
        return self.domain
    
