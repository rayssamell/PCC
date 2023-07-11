from django.contrib.auth.models import Group
from accounts.models import Usuario


def groups_check(user):
    profissional_group = Group.objects.get(name='Profissional')
    if isinstance(user, Usuario):
        return user.tipoUsuario == 'P' and profissional_group in user.groups.all()
    return False