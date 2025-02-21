from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from moesifapi.moesif_api_client import *
from django.conf import settings
# Initialize API Client
api_client = MoesifAPIClient(settings.MOESIF_MIDDLEWARE['APPLICATION_ID']).api

@csrf_exempt
@require_http_methods(["POST"])
def users(request, user_id):
    user = {
        'user_id': user_id,
        'company_id': '67890',  # If set, associate user with a company object
        'campaign': {
            'utm_source': 'google',
            'utm_medium': 'cpc',
            'utm_campaign': 'adwords',
            'utm_term': 'api+tooling',
            'utm_content': 'landing'
        },
        'metadata': {
            'email': 'john@acmeinc.com',
            'first_name': 'John',
            'last_name': 'Doe',
            'title': 'Software Engineer',
            'sales_info': {
                'stage': 'Customer',
                'lifetime_value': 24000,
                'account_owner': 'mary@contoso.com'
            },
        }
    }

    api_client.update_user(user)
    return JsonResponse(status=201, data={'user_id': user_id, 'update_users': 'success'},
                        content_type='application/json')


@csrf_exempt
@require_http_methods(["POST"])
def companies(request, company_id):
    company = {
        'company_id': company_id,
        'company_domain': 'acmeinc.com',  # If domain is set, Moesif will enrich your profiles with publicly available info
        'campaign': {
            'utm_source': 'google',
            'utm_medium': 'cpc',
            'utm_campaign': 'adwords',
            'utm_term': 'api+tooling',
            'utm_content': 'landing'
        },
        'metadata': {
            'org_name': 'Acme, Inc',
            'plan_name': 'Free',
            'deal_stage': 'Lead',
            'mrr': 24000,
            'demographics': {
                'alexa_ranking': 500000,
                'employee_count': 47
            },
        }
    }
    api_client.update_company(company)
    return JsonResponse(status=201, data={'company_id': company_id, 'update_companies': 'success'},
                        content_type='application/json')
