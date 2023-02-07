## Projeto AUTO
##### (desenvolvido por **Júlio Cascalles**)


---
Algumas classes que compõe o ciclo de automação:

* Conda - Responsável por criar o ambiente virtual para rodar a aplicação;
* Git - Controla o status do repositório, baixando ou subindo o código fonte;
* Jira - Atualiza o quadro de tarefas, atribuindo usuário e movendo de status ("To Do", "In Progress", "Done");
* Issue - É uma das tarefas do Jira e carrega atributos como resumo, prioridade, comentários, nome do projeto e quantos votos recebeu para aprovação (Também é possível votar numa tarefa).

---
Uma das formas de controlar a _ordem_ da execução com essas classes é usar o **pipeline**
> Para usar como linha de comando do terminal, as seguintes opções estão disponíveis:
* -p = Nome do do projeto;
* -e = Nome do ambiente do Conda (se omitido, assume o nome do projeto);
* -f = Flag que indica início ou término de uma tarefa:
    - "start" para quando você começar uma tarefa;
    - "end" para quando terminar.


---
Sequência de execução:
Ao rodar a função **execute** da pipeline, acontecem as seguintes coisas:

* É feita uma pesquisa no Jira com base em 
    - dados de acesso (usuário e token) armazenados nas _variáveis de ambiente_;
* Das tarefas retornadas é selecionada uma com a função passada no parâmetro **select** da função _execute_;
* O ambiente é montado ou criado;
* O repositório é baixado ou atualizado;
* A tarefa é atualizada;
* No caso da flag "end" é feito o commit e o ambiente de desenvolvimento é desmontado.

---
Como rodar:

Na pasta que contém `/Auto` digite o seguinte comando no terminal:
```
>> python3 Auto  -p <project> [-e <env>] [-f start|end]
```
> Lembre-se que as seguintes variáveis de ambiente devem estar configuradas:
* JIRA_URL - Exemplo: https://fulano.atlasian.net
* JIRA_USER - Exemplo: fulano@empresa.com
* JIRA_TOKEN  (chave de acesso fornecida pelo Jira);
* COMPANY_NAME: Nome da empresa usado no endereço para o **_Github_** (ver linha 4 de git.py)


---
## Observação final
O próprio projeto AUTO foi desenvolvido/testado com ajuda dele mesmo! 
