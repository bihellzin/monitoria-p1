# Lista para a final  

O arquivo alunos_cripto.txt contém os dados dos alunos criptografados. A primeira linha contém o CPF do aluno, a segunda linha contém o nome completo do aluno, a terceira linha contém o semestre que o aluno está cursando, a quarta linha contém o curso que o aluno faz e da quinta linha pra baixo contém as cadeiras que o aluno está cursando.  

***

## Primeira parte

### Exemplo de aluno descriptografado  

12345678900  
Carlos José Alves  
3  
Comportamento organizacional  
Redes de computadores  
Algoritmos e estuturas de dados  
Estatística  
Libras  
  
***

### Exemplo de aluno criptografado  

bdfhjlnpr``  
ÂäØÞæ@Þæǒ@ØìÊæ  
f  
¦ÒæèÊÚÂæ@ÈÊ@ÒÜÌÞäÚÂǎÂÞ  
ÞÚàÞäèÂÚÊÜèÞ@ÞäÎÂÜÒôÂÆÒÞÜÂØ  
¤ÊÈÊæ@ÈÊ@ÆÞÚàêèÂÈÞäÊæ  
ØÎÞäÒèÚÞæ@Ê@ÊæèêèêäÂæ@ÈÊ@ÈÂÈÞæ  
æèÂèǚæèÒÆÂ  
  

Para fazer a decriptografia, voce deverá dividir o ord dos caracteres do arquivo com os dados criptografados por 2 (__divisão inteira__).  

***  

## Segunda parte  

Na segunda parte a sua tarefa e armazenar os dados decriptografados numa lista e cada elemento da lista deve ser um dicionário contendo os dados dos alunos. Os valores das chaves de CPF, nome completo e semestre devem ser armazenados com o tipo string, o valor da chave das cadeiras sendo cursadas deve ser uma tupla contendo as cadeiras. Observe o exemplo de um elemento abaixo.  

```python
{
  'cpf': '12345678900',
  'nome_completo': 'Carlos José Alves',
  'semestre': '3',
  'cadeiras': (
    'Comportamento organizacional',
    'Redes de computadores',
    'Algoritmos e estuturas de dados',
    'Estatística',
    'Libras'
  )
}
```  

***  

## Terceira parte  

Implemente uma busca de alunos utilizando recursão, para isso, crie uma função para buscar um aluno pelo CPF e mostre os dados desse aluno. Dica: uma lista terá que ser usada como argumento e, para evitar problema com lista vazia, crie uma lista auxiliar toda vez que for fazer uma busca.  

Essa atividade contém os assuntos principais da cadeira como laços, estruturas condicionais, listas, dicionários, tuplas, arquivos e funções. Caso tenha alguma dúvida, entrar em contato com algum dos monitores.  

Boa sorte