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
- Em produção, configure um serviço de armazenamento (S3, etc.) e cuide das permissões.
- Para remover uma foto, clique em "Excluir" na listagem (é solicitado confirmação).


Deploy no Render (resumo)
1. Crie um novo Web Service no Render e conecte ao repositório.
2. Configure as variáveis de ambiente em Settings → Environment (pelo menos `SECRET_KEY`, `ALLOWED_HOSTS` e `DEBUG`).
   - Se for usar Postgres no Render, defina `DATABASE_URL` com a URL fornecida.
3. Build command: `pip install -r requirements.txt`
4. Start command: o `Procfile` já contém `web: gunicorn drive_project.wsgi --log-file -` (Render usa isso automaticamente).
6. O Render por padrão executa `collectstatic` ao fazer deploy; não altere isso a menos que você saiba o que está fazendo. Se quiser pular `collectstatic`, defina `DISABLE_COLLECTSTATIC=True` nas variáveis de ambiente.

Dicas e avisos importantes
- **Arquivos de mídia (`MEDIA`) não são persistentes em instâncias Render**: se precisar de persistência, use S3 (ou outro serviço de armazenamento) e configure `DEFAULT_FILE_STORAGE` com `django-storages` e `boto3`.
- **SECRET_KEY**: defina `SECRET_KEY` nas variáveis de ambiente do serviço no painel do Render (não commitá-la no repositório).
- **Banco de dados**: prefira PostgreSQL (Render oferece Add-ons). Defina `DATABASE_URL` com a URL fornecida.

Arquivos criados/alterados para deploy
- `Procfile` — comando de start (`gunicorn`)
- `runtime.txt` — versão do Python
- `render.yaml` — arquivo de configuração exemplo para deploy no Render
- `.env.example` — variáveis de exemplo para desenvolvimento/local

Se quiser, eu posso adicionar suporte direto ao S3 (armazenamento de mídia) e gerar um `render.yaml` mais completo com Add-on Postgres configurado automaticamente.