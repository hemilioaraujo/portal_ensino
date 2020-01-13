PORTAL DE ENSINO
=====================
### PROJETO DE INICIAÇÃO CIENTÍFICA DOS ALUNOS DE CIÊNCIA DA COMPUTAÇÃO DA UNIPAC  
![logo-unipac](https://bitbucket.org/pic_unipac/portal_ensino/raw/2f2393fb69d4d293fa7e6663e149e6525b7081ee/arquivos_readme/logo_unipac.png)

Este projeto está sendo desenvolvido em **[Python]** utilizando o framework web **[Django]**.

#### Requisitos:

* Django==2.2.8
* django-bootstrap-form==3.4
* python-decouple==3.1
* Pillow==6.2.0

#### Para instalar os requisitos, basta executar o comando:  

```shell
pip install -r requirements.txt
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
