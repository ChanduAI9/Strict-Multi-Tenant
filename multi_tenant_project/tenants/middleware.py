from django_tenants.middleware import TenantMiddleware

class CustomTenantMiddleware(TenantMiddleware):
    def get_tenant(self, model, hostname, request):
        return super().get_tenant(model, hostname, request)
