# Drive Simples (Django)

Mini app Django para enviar, listar e excluir fotos (comportamento similar a um Drive simples).

Requisitos
- Python 3.10+ (ou compatível)

Instalação (Windows PowerShell)

1. Criar e ativar ambiente virtual

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

2. Aplicar migrations

```powershell
.\.venv\Scripts\python manage.py migrate
```

3. Criar superusuário (opcional)

```powershell
.\.venv\Scripts\python manage.py createsuperuser
```

4. Rodar o servidor de desenvolvimento

```powershell
.\.venv\Scripts\python manage.py runserver
```

Acesse: http://127.0.0.1:8000/ para enviar e ver fotos. Arquivos enviados ficam em `media/photos/...`.

Notas
- Em produção, configure um serviço de armazenamento (S3, etc.) e cuidado com permissões.
- Para remover uma foto, clique em "Excluir" na listagem (é solicitado confirmação).