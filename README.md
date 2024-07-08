# Como criar um ambiente virtual ?
python -m venv venv

# Ativar View no Windows

# Acessar a pasta da venv
cd .\venv\Scripts

# Ativá-la
.\activate

# Como baixar as dependencias ?
pip install -r requirements.txt

# Como rodar?
python manage.py runserver


# Banco de Dados
Atualmente está utilizando SQLite, caso seja queira alterar, no arquivo 
settings.py, no pacote de NAES2024, deverá ser alterado o acesso ao banco.

Consumir a view do modules.

http://localhost:8000/api/v1

Já está recebendo método GET, POST, PUT, DELETE.
Porém será necessário alterá-lo.

# Gerar e rodar migrations
python manage.py migrate

python manage.py makemigrations