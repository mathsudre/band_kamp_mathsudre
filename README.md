# BandKamp Generic View - REST API - criação de playlist de músicas.

### 📑 Sobre o projeto

Esse projeto foi desenvolvido durante o 
módulo 5 do curso de Desenvolvimento Web FullStack da Kenzie Academy Brasil, teve como desafio refatora-lo, em primeiro momento tive que migrar os serializers para utilizar os campos da model (ModelSerializer) e migrar o banco de dados de sqlite para o postgres, em seguida refatorar as views para utilizar as generics views fornecidas pelo [DRF](www.django-rest-framework.org/) onde se pode abstrair bastante trabalho para se construir views.

A API tbm possui uma documentação feita pelo [Swagger-UI](https://band-kamp-mathsudre.onrender.com/api/docs/swagger-ui/) e [Redoc](https://band-kamp-mathsudre.onrender.com/api/docs/redoc/), nesses links você pode verificar os endpoints que a API possui.

## Tecnologias utilizadas:
* [Django](https://www.djangoproject.com/): O framework web para perfeccionistas com prazos (o Django constrói aplicativos web com menos código).
* [DRF](www.django-rest-framework.org/): Um kit de ferramentas poderoso e flexível para criar APIs da Web.

## Instalação dos pacotes de teste

- Verifique se os pacotes `pytest` e/ou `pytest-testdox` estão instalados globalmente em seu sistema:
```shell
pip list
```
- Caso seja listado o `pytest` e/ou `pytest-testdox` e/ou `pytest-django` em seu ambiente global, utilize os seguintes comando para desinstalá-los globalmente:
```shell
pip uninstall pytest
```

```shell
pip uninstall pytest-testdox
```

```shell
pip uninstall pytest-django
```

A partir disso, prossiga com os passos:

1. Crie seu ambiente virtual:
```bash
python -m venv venv
```

2. Ative seu venv:
```bash
# linux:
source venv/bin/activate

# windows:
.\venv\Scripts\activate
```

3. Instale o pacote `pytest-testdox`:
```shell
pip install pytest-testdox pytest-django
```


4. Agora é só rodar os testes no diretório principal do projeto:
```shell
pytest --testdox -vvs
```

5. Caso queira um log mais resumido, basta executar com os testes sem as flags **verbose**:
```shell
pytest --testdox
```

## Rodando os testes por partes

Caso você tenha interesse em rodar apenas um diretório de testes específico, pode utilizar o comando:

- Rodando testes de users:
```python
pytest --testdox -vvs tests/users/
```

- Rodando testes de albums:
```python
pytest --testdox -vvs tests/albums/
```

- Rodando testes de songs:
```python
pytest --testdox -vvs tests/songs/
```
