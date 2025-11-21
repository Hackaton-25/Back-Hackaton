# core/views/user/login_hack.py
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from core.models.user import User
import json

@csrf_exempt
def login_view(request):
    print("REQUEST METHOD:", request.method)
    print("RAW BODY:", request.body)
    print("CONTENT TYPE:", request.content_type)

    if request.method != "POST":
        return JsonResponse({"error": "POST necessário"}, status=405)

    try:
        data = json.loads(request.body)
    except Exception as e:
        print("JSON ERROR:", e)
        return JsonResponse({"error": f"JSON inválido: {e}"}, status=400)

    print("PARSED DATA:", data)

    # ⚡ Apenas email e password
    email = data.get("email")
    password = data.get("password")

    if not email or not password:
        return JsonResponse({"error": "Email e senha obrigatórios"}, status=400)

    try:
        # Tenta buscar usuário existente
        user = User.objects.get(email=email)
        if user.check_password(password):
            print("Usuário existente logado")
        else:
            return JsonResponse({"error": "Senha inválida"}, status=400)
    except User.DoesNotExist:
        # Cria usuário automático com email como nome padrão
        user = User.objects.create_user(
            name=email.split("@")[0],  # pega parte antes do @ como default
            email=email,
            password=password,
            perfil="aluno"
        )
        print("Usuário criado automaticamente:", user.email)

    return JsonResponse({
        "id": user.id,
        "name": user.name,
        "email": user.email,
        "perfil": user.perfil,
        "escola": user.escola,
        "turma": user.turma,
    })
