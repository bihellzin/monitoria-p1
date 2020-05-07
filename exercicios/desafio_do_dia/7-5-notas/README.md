Fernando, seu professor de programação 1, decidiu que iria premiar alunos ao longo do curso como forma de incentivo para que todos se esforcem. Para isso, no final do semestre ele parabeniza e dá um chocolate (vegano) para os aluno que obtiveram as maiores pontuações nas listas. Fernando então pede para que você faça um programa que receba um valor <em>n</em>, referente a quantidade de alunos matriculados na cadeira, um valor <em>m</em> referente a quantidade de listas do semestre e o históricos, de cada um dos <em>n</em> alunos, que são inteiros com <em>m</em> digitos. E dá, como saída, a quantidade de alunos que conseguiram as melhores notas nas listas.  

# Exemplo  

Digamos que os alunos são Carlos, João e Pedro. Então vamos utilizar os nomes para o histórico, mas o seu programa não deve criar uma variavel para cada aluno.

Input  
```python
n = 3
m = 3

# historicos

carlos = 223
joao = 232
pedro = 112
```  

Output  
```python
2
```  

Como Carlos foi o que teve melhor nota na lista 1 e 3 e João teve as melhores notas nas listas 1 e 2, então somente 2 alunos receberam o chocolate. E mais de um aluno pode ter as melhor nota da lista.
