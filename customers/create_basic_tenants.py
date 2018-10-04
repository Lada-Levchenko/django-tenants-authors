from customers.models import Client, Domain


def create_tenants():

    tenant = Client(schema_name='public', name='Public')
    tenant.save()

    domain = Domain()
    domain.domain = 'authors.com'
    domain.tenant = tenant
    domain.is_primary = True
    domain.save()

    tenant = Client(schema_name='author1', name='Author 1')
    tenant.save()

    domain = Domain()
    domain.domain = 'author1.authors.com'
    domain.tenant = tenant
    domain.is_primary = True
    domain.save()

    tenant = Client(schema_name='author2', name='Author 2')
    tenant.save()

    domain = Domain()
    domain.domain = 'author2.authors.com'
    domain.tenant = tenant
    domain.is_primary = True
    domain.save()
