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
5. Não esqueça de habilitar (ou não) `DISABLE_COLLECTSTATIC` — por padrão o Render executa `collectstatic`, o app está configurado para funcionar com WhiteNoise.

Dicas
- Para armazenar arquivos de mídia em produção, prefira S3 ou outro serviço de armazenamento e configure `DEFAULT_FILE_STORAGE`.
- Consulte a documentação do Render para detalhes de banco de dados e variáveis de ambiente.