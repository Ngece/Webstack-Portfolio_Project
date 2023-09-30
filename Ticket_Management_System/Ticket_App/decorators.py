from django.contrib.auth.decorators import user_passes_test, login_required

# Verify user types to restrict access to certain pages for different users
def is_dispatcher(user):
    return user.role == 'dispatcher'

def is_technician(user):
    return user.role == 'technician'

def is_company(user):
    return user.role == 'company'

# check if a user is a "technician" or "dispatcher"
is_technician_or_dispatcher = lambda user: user.role in ['technician', 'dispatcher']

dispatcher_required = user_passes_test(is_dispatcher)
technician_required = user_passes_test(is_technician)
company_required = user_passes_test(is_company)
technician_or_dispatcher_required = user_passes_test(is_technician_or_dispatcher)