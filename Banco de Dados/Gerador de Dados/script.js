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

for(i = 0; i < 300; i++){
    a = String(Math.floor(Math.random() * (220 - 145 + 1) + 145));
    a = parseFloat(a[0]+"."+a[1]+a[2]);

    if(Math.floor(Math.random() * (10 - 1 + 1) + 1) <= 3){
        a = String(Math.floor(Math.random() * (140 - 30 + 1) + 30));

        if(a >= 100){
            a = parseFloat(a[0]+"."+a[1]+a[2]);
        }else{
            a = parseFloat(0+"."+a[0]+a[1]);
        }
    }

    if(a <= 0.50){
        ano = 2022;
    }else if(a <= 0.80){
        ano = 2021; 
    }else if(a <= 1.10){
        ano = 2020;
    }else if(a <= 1.30){
        ano = 2019;
    }else if(a <= 1.40){
        ano = Math.floor(Math.random() * (2018 - 2014 + 1) + 2014)
    }else if(a <= 1.50){
        ano = Math.floor(Math.random() * (2014 - 2011 + 1) + 2011)
    }else if(a <= 1.60){
        ano = Math.floor(Math.random() * (2010 - 2008 + 1) + 2008)
    }else if(a <= 1.70){
        ano = Math.floor(Math.random() * (2007 - 2005 + 1) + 2005)
    }else if(a >= 1.90){
        ano = Math.floor(Math.random() * (1960 - 1945 + 1) + 1945)
    }else{
        ano = Math.floor(Math.random() * (2004 - 1960 + 1) + 1960)
    }

    if(a <= 0.40){
        p = String(Math.floor(Math.random() * (2000 + 1500 + 1) + 1500));
    }else if(a <= 0.50){
        p = String(Math.floor(Math.random() * (5000 + 1750 + 1) + 1750));
    }else if(a <= 0.50){
        p = String(Math.floor(Math.random() * (5000 + 2000 + 1) + 2000));
    }else if(a <= 0.80){
        p = String(Math.floor(Math.random() * (11000 + 5000 + 1) + 5000));
    }else if(a <= 1.10){
        p = String(Math.floor(Math.random() * (17000 + 10500 + 1) + 10500));
    }else if(a <= 1.40){
        p = String(Math.floor(Math.random() * (40000 + 20000 + 1) + 20000));
    }else if(a <= 1.60){
        p = String(Math.floor(Math.random() * (85000 + 35000 + 1) + 35000));
    }else{
        p = String(Math.floor(Math.random() * (140000 + 50000) + 50000));
    }

    if(ano <= 1960){
        p = String(Math.floor(Math.random() * (95000 + 40000 + 1) + 40000));
    }

    if(p >= 100000){
        p = parseFloat(String(p[0]) + String(p[1]) + String(p[2]) + '.' + String(p[3]) + String(p[4]) + String(p[5]));
    }else if(p <= 9999){
        p = parseFloat(String(p[0]) + '.' + String(p[1]) + String(p[2]) + String(p[3]));
    }else{
        p = parseFloat(String(p[0]) + String(p[1]) + '.' + String(p[2]) + String(p[3]) + String(p[4]) + String(p[5]));
    }
    
    imc = p / a**2
    nome1 = nomes[Math.floor(Math.random() * (129 - 0 + 1) - 0)];
    sobrenome = sobrenomes[Math.floor(Math.random() * (49 - 0 + 1) + 0)];
    nome = nome1 + " " + sobrenome;
    username = nome1.toLowerCase()+sobrenome.toLowerCase()+i;
    date = `${ano}-${Math.floor(Math.random() * (12 - 1 + 1) + 1)}-${Math.floor(Math.random() * (28 - 1 + 1) + 1)}`;

    retorno.innerHTML += `INSERT INTO usuario VALUES (NULL, '${nome}', '${username}', MD5('123'), '${date}');`;
    retorno.innerHTML += `<br>INSERT INTO registro VALUES (NULL, ${p}, ${a}, ${imc.toFixed(2)}, NOW(), ${i+1});<br><br>`;
}