PORTAL DE ENSINO
=====================
### PROJETO DE INICIAÇÃO CIENTÍFICA DOS ALUNOS DE CIÊNCIA DA COMPUTAÇÃO DA UNIPAC  

![logo-unipac](https://bitbucket.org/pic_unipac/portal_ensino/raw/2f2393fb69d4d293fa7e6663e149e6525b7081ee/arquivos_readme/logo_unipac.png)

Este projeto está sendo desenvolvido em **[Python]** utilizando o framework web **[Django]**.

## Requisitos:

```Pipfile
appdirs = "==1.4.4"
certifi = "==2020.6.20"
distlib = "==0.3.1"
django-bootstrap-form = "==3.4"
filelock = "==3.0.12"
pipenv = "==2020.6.2"
python-decouple = "==3.1"
pytz = "==2019.1"
six = "==1.15.0"
sqlparse = "==0.3.0"
virtualenv = "==20.0.27"
virtualenv-clone = "==0.5.4"
Django = "==2.2.10"
Pillow = "==6.2.2"
psycopg2-binary = "*"
```

## Preparando o ambiente:
### Instalando pipenv e dependências e gerando o ambiente virtual para o projeto

> **pipenv** é um gerenciador de dependências e ambientes virtuais.

```bash
# INSTALAR PIPENV
pip install pipenv

# CRIAR AMBIENTE E INSTALAR DEPENDÊNCIAS NELE
pipenv install

# ENTRAR NO AMBIENTE VIRTUAL
pipenv shel

# SAIR DO AMBIENTE VIRTUAL
exit
```
> **Obs.:** Estes passos devem ser realizado no local onde estão os arquivos Pipfile e Pipfile.lock


### Criar container Docker para banco de dados PostgreSQL

```docker
docker run -d --name <nome do seu container> -p <porta host>:<porta container> -e POSTGRES_USER=<seu_usuario> -e POSTGRES_PASSWORD=<sua_senha> postgres
```

|Argumento|Descrição|
|:---:|:---:|
|`-d`|Faz com que o container rode como Daemon ou serviço.|
|`--name <nome do seu container>`|Define o nome do seu container.|
|`-p <porta host>:<porta container>`|Faz o bind da porta host com a porta do container.|
|`-e POSTGRES_USER=<seu_usuario>`|Passa o usuário do postgresql como variável de ambiente do container.|
|`-e POSTGRES_PASSWORD=<sua_senha>`|Passa a senha do postgresql como variável de ambiente do container.|
|`postgres`|É a imagem do dockerhub que será usada para criar o container.|

### Configuração do settings.py

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres', # nome do database
        'USER': POSTGRESQL_USER, # seu usuário do container postgres
        'PASSWORD': POSTGRESQL_PWD, # sua senha do container postgres
        'HOST': 'localhost', # endereço do 
        'PORT': '5445', # porta definida para o host na criação do container
    }
}
```

### Aplicar configurações anteriores
`python manage.py makemigrations`

`python manage.py migrate`

### Criar Super Usuário
Basta executar o camando a seguir e preencher as requisições

```bash
python manage.py createsuperuser
```

#### Popular a tabela das aulas:

```shell
python manage.py shell
```

```python
from portal_ensino.aulas.models import Aulas
```

```python
objeto = Aulas()
```
```python
objeto.popular_tabela_aulas()
```

[Python]: https://www.python.org/
[Django]: https://www.djangoproject.com/
