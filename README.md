
# :notebook: Desafio Técnico - Fidelity 
Este é um projeto simples desenvolvido como parte de um desafio técnico. A aplicação é um sistema básico de registro e login.

## :bulb: O que a aplicação faz
A aplicação permite que usuários se registrem e façam login em um sistema simples. O fluxo é o seguinte:

1. Cadastro: O usuário pode criar uma conta fornecendo nome, e-mail e senha.
2. Login: Após o registro, o usuário pode fazer login utilizando o e-mail e a senha cadastrados.
3. Página Inicial (Home): Uma vez autenticado, o usuário é redirecionado para a página inicial onde pode ver seu nome.

## :key: Funcionalidades

Cadastro de usuário com validações de dados.
- Sistema de login para usuários cadastrados.
- Envio de e-mail de confirmação após o cadastro.
- Sistema de logout para encerrar a sessão.

## :computer: Tecnologias Utilizadas

- **Django**: Framework web em Python para construir a aplicação.
- **SQLite**: Banco de dados embutido no Django para armazenar os dados dos usuários.
- **HTML/CSS/JavaScript**: Para a construção das interfaces de usuário.
- **SMTP**: Para envio de e-mail de confirmação ao registrar-se na plataforma.

## :runner: Como Rodar a Aplicação
1. **Clonar o Repositório**

Clone o repositório para sua máquina local:
```
git clone https://github.com/seu-usuario/desafio-login.git
cd desafio-login
```

2. **Criar um Ambiente Virtual**
Recomenda-se criar um ambiente virtual para gerenciar as dependências do projeto. Para isso, execute:

```
python -m venv venv
```
Ative o ambiente virtual:

- **No Windows**:

```
venv\Scripts\activate
```

- **No macOS/Linux**:

```
source venv/bin/activate
```

3. **Instalar as Dependências**
Instale as dependências do projeto:

```
pip install django
pip install dotenv
```

4. **Configurar o Django**
Antes de rodar a aplicação, é necessário configurar o banco de dados e as migrações do Django. Execute o seguinte comando:

```
python manage.py migrate
```


5. Criar um Superusuário (Opcional)
Caso queira acessar o painel administrativo do Django, crie um superusuário:

```
python manage.py createsuperuser
```

Siga as instruções para definir nome de usuário, e-mail e senha.

6. **Rodar o Servidor**
Agora, você pode rodar o servidor local do Django:

```
python manage.py runserver
```

A aplicação estará disponível em: http://127.0.0.1:8000

7. **Acessar a Aplicação**

- Acesse a página de registro: /register/ para criar uma nova conta.
- Acesse a página de login: /login/ para fazer login com a conta criada.
- Após o login, você será redirecionado para a página inicial.

## :email: Envio de E-mails

A aplicação utiliza SMTP para enviar um e-mail de confirmação ao usuário após o cadastro. Para que o envio de e-mails funcione corretamente, você precisará criar um arquivo .env na raiz do projeto com as suas credenciais de e-mail.

**Passos para configurar:**

1. **Crie o arquivo** `.env` **na raiz do projeto.**

2. **Adicione as seguintes variáveis no arquivo** `.env`:

```
EMAIL_HOST_USER=seu_email@gmail.com
EMAIL_HOST_PASSWORD=sua_senha_de_app
SECRET_KEY=gerar_uma_chave_secreta_django
```

- `EMAIL_HOST_USER`: O seu e-mail do Gmail (ou outro serviço de e-mail, se preferir).
- `EMAIL_HOST_PASSWORD`: A senha do seu aplicativo, que você pode gerar através das configurações de segurança da sua conta do Gmail (caso utilize o Gmail). Saiba mais sobre senhas de app no Gmail [aqui](https://support.google.com/accounts/answer/185833?hl=pt-BR).
- `SECRET_KEY`: Sua chave secreta do Django, que deve ser mantida privada.

O Django usará essas credenciais para enviar e-mails. Não é necessário modificar o código, pois ele já está configurado para buscar essas variáveis de ambiente no arquivo `.env`.

Nota: Se você estiver utilizando Gmail, pode ser necessário habilitar o acesso de "aplicativos menos seguros" ou criar uma senha de aplicativo específico, caso tenha a autenticação de dois fatores ativada.

## ✨ Contribuindo
Sinta-se à vontade para contribuir com melhorias ou relatar problemas. Para isso, basta realizar um fork deste repositório e enviar um pull request com suas alterações.
