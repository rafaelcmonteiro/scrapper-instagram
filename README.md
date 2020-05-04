# Scrapper Instagram

### Sobre a aplicação.
Este scrapper faz a retirada de dados da galeria de fotos de uma conta do instagram usando selenium.

### Dados retirados.
   * Id - Número atribuido a cada um dos dados retirados.
   * Date - Data de postagem da imagem.
   * Likes - Quantidade de likes da imagem.
   * Description  - Descrição da imagem, caso a imagem não tenha descrição ela é substituida por "Não há descrição"

### Adendo sobre a quantidade de likes.

O instagram, por padrão, retira -1 da quantidade de likes da tag \<span> e coloca o nome de usuário da pessoa dentro da tag \<a>\</a> como no exemplo abaixo.

    Curtido por 
    <a class="FPmhX notranslate cqXBL" title="random_user" href="/random_user/">random_user</a>
    e 

A aplicação retira a quantidade de likes de dentro da tag \<span>2\</span> e 
    
    <button class="sqdOP yWX7d _8A5w5" type="button">outras<span>2</span> pessoas</button>

### Configurando o Environment

##### Build environment:
    distmod: ubuntu1804
    distarch: x86_64
    target_arch: x86_64
    
##### Configurando o environment:

Após clonar o repositório na sua maquina, siga o passo a passo:
* Crie o virtual environment.
* Entre no site e baixar o driver mais recente geckodriver-v0.26.0-linux64.tar.gz
* https://github.com/mozilla/geckodriver/releases
* Descompactar e copiar o arquivo para a pasta bin no root.

É possível copiar o arquivo através do comando linux.
    
    sudo cp geckodriver /usr/local/bin

E por fim rode o código abaixo com o virtual environment ativado.
    
    pip install -r requirements.txt
    
Nota: A aplicação usa o firefox para rodar, então é importante que o browser e o geckodriver estejam instalados corretamente no environment linux.

##### Configurando a aplicação para o seu instagram:

Procure o código abaixo dentro de scrapper_insta.py.
    
    def enter_into_account():
    login('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input', 'login')
    login('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input', 'password')
    
Troque login e password para os seus.