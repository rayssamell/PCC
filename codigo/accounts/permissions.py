from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from .models import Usuario


def set_permission(usuario):
    """
    Função que define as permissões e grupo de usuário com base no tipo de usuário.

    Args:
        usuario (Usuario): objeto do modelo Usuario.

    Returns:
        Usuario: objeto do modelo Usuario atualizado com as permissões e grupo definidos.
    """
    content_type = ContentType.objects.get_for_model(Usuario)

    # Mapeia o tipo de usuário para o codename do grupo correspondente
    tipos_usuario_grupo = {
        'P': 'profissional',
        'F': 'familiar',
    }
    codename_grupo = tipos_usuario_grupo.get(usuario.tipoUsuario, 'default')

    # Recupera ou cria o grupo com base no codename
    grupo, _ = Group.objects.get_or_create(name=codename_grupo)

    # Adiciona o usuário ao grupo
    grupo.user_set.add(usuario)

    # Cria ou recupera a permissão
    permissao_codenome = f'acessar_{codename_grupo}'
    permissao_nome = permissao_codenome.replace("_", " ").title()

    try:
        permission, _ = Permission.objects.get_or_create(
            codename=permissao_codenome,
            name=permissao_nome,
            content_type=content_type
        )
    except Exception as e:
        raise Exception(f"Erro ao criar/recuperar permissão {permissao_nome}: {e}")

    # Adiciona a permissão ao usuário
    try:
        usuario.user_permissions.add(permission)
    except Exception as e:
        raise Exception(f"Erro ao adicionar permissão {permissao_nome} ao usuário {usuario.username}: {e}")

    return usuario
