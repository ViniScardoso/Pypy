var nomes = ['Alice', 'Laura', 'Beatriz', 'Manuela', 'Helena', 'Maria', 'Isabela', 'Valentina', 'Júlia', 'Sophia', 'Artur', 'Matheus', 'Bernardo', 
'Miguel', 'Davi', 'Gael', 'Gabriel', 'Rafael', 'Lucas', 'Theo', 'Alexandre', 'Eduardo', 'Henrique', 'Murilo', 'Theo', 'André', 'Enrico', 'Henry', 'Nathan', 
'Thiago', 'Antônio', 'Enzo', 'Ian', 'Otávio', 'Thomas', 'Augusto', 'Erick', 'Isaac', 'Pietro', 'Vicente', 'Breno', 'Felipe', 'João', 'Rafael', 
'Vinícius', 'Bruno', 'Fernando', 'Kaique', 'Raul', 'Vitor', 'Caio', 'Francisco', 'Leonardo', 'Rian', 'Yago', 'Cauã', 'Frederico', 'Luan', 'Ricardo', 
'Ygor', 'Daniel', 'Guilherme', 'Lucas', 'Rodrigo', 'Yuri', 'Danilo', 'Gustavo', 'Mathias', 'Samuel', 'Agatha', 'Camila', 'Esther', 'Isis', 'Maitê',
'Natália', 'Alícia', 'Carolina', 'Fernanda', 'Joana', 'Malu', 'Nicole', 'Amanda', 'Catarina', 'Gabriela', 'Laís', 'Maria', 'Olívia', 'Ana', 'Cecília', 
'Gabrielle', 'Lara', 'Mariah', 'Pietra', 'Antonela', 'Clara', 'Giovanna', 'Larissa', 'Mariana', 'Rafaela', 'Aurora', 'Clarice', 'Giulia', 'Lavínia', 'Marina', 
'Rebeca', 'Bárbara', 'Eduarda', 'Heloísa', 'Letícia', 'Maya', 'Sara', 'Beatriz', 'Elisa', 'Isabel', 'Liz', 'Melissa', 'Sophie', 'Bianca', 'Emanuelly',
'Isabelly', 'Lorena', 'Milena', 'Stella', 'Bruna', 'Emilly', 'Isadora', 'Luana', 'Mirella', 'Vitória', 'Yasmin'];

var sobrenomes = ['Altoe', 'Sossai', 'Agrizzi', 'Angeli', 'Ferreira', 'Braga', 'Silva', 'Zampirolli', 'Della Coletta', 'Fernandes',
'Alves', 'Costalonga', 'Botteon', 'Caliman', 'Zanette', 'Oliveira', 'Salvador', 'Silva', 'Zandonadi', 'Pesca', 'Falqueto', 'Tosi', 'Costa', 
'Souza', 'Gomes', 'Calmon', 'Pereira', 'Sossai detto', 'Almeida', 'Moreira', 'Jesus', 'Martins', 'Balarini', 'Rodrigues', 'Gonçalves', 
'Pizzol', 'Vieira', 'Breda', 'Bazoni', 'Corrêa', 'Filete', 'Oliveira', 'Venturim', 'Almeida', 'dos Santos', 'Falchetto', 'Barbosa', 'Scaramussa',
'Partelli', 'Barros'];

for(i = 0; i < 130; i++){
    a = String(Math.floor(Math.random() * (205 - 145 + 1) + 145));
    a = parseFloat(a[0]+"."+a[1]+a[2]);

    p = String(Math.floor(Math.random() * (120000 - 50000 + 1) + 50000));
    if(p[0] == 1){
        p = parseFloat(String(p[0]) + String(p[1]) + String(p[2]) + '.' + String(p[3]) + String(p[4]) + String(p[5]));
    }else{
        p = parseFloat(String(p[0]) + String(p[1]) + '.' + String(p[2]) + String(p[3]) + String(p[4]) + String(p[5]));
    }

    imc = p / a**2
    nome1 = nomes[Math.floor(Math.random() * (129 - 0 + 1) - 0)];
    sobrenome = sobrenomes[Math.floor(Math.random() * (49 - 0 + 1) + 0)];
    nome = nome1 + " " + sobrenome;
    username = nome1.toLowerCase()+sobrenome.toLowerCase()+i;
    date = `${Math.floor(Math.random() * (2020 - 1950 + 1) + 1950)}-${Math.floor(Math.random() * (12 - 1 + 1) + 1)}-${Math.floor(Math.random() * (28 - 1 + 1) + 1)}`;

    retorno.innerHTML += `<br>INSERT INTO usuario VALUES (NULL, '${nome}', '${username}', MD5('123'), '${date}');`;
    retorno.innerHTML += `<br>INSERT INTO registro VALUES (NULL, ${p}, ${a}, ${imc.toFixed(2)}, NOW(), ${i+1});<br>`;
}