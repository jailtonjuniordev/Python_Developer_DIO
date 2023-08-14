# Sistema Bancário v1

Na finalização do módulo "Fundamentos de Pyhthon" na Formação Python Developer da DIO, me foi solicitado que criasse de forma simples um sistema bancário, o qual durante o curso será aprimorado.
## Desafio
Fomos contratados por um grande banco para desenvolver seu novo sistema. Esse banco deseja modernizar suas operações e para isso escolheu a linguagem Python. Para a primeira versão do sistema devemos implementar apenas 3 operações: **Deposito**, **Saques**, **Extratos**, conforme descrito abaixo.

### Requisitos
* Permitir que o usuário realize Saques.
    * O sistema deve permitir realizar 3 saques diários com limite máximo de R$ 500,00 por saque. Caso o usuário não tenha saldo em conta, o sistema deve exibir uma mensagem informando que não será possível sacar o dinheiro por falta de saldo. Todos os saques devem ser armazenados em uma variável e exibidos na operação de extrato.

<br/>

* Permitir que o usuário realize Depositos.
    * Deve ser possível depositar valores positivos para a minha conta bancária. A v1 do projeto trabalha apenas com 1 usuário, dessa forma não precisamos nos preocupar em identificar qual é o número da agência e a conta bancária. Todos os **depósitos** devem ser armazenados em uma variável e exibidos na operação de **extrato**.

<br/>

* Permitir que o usuário visualize o Extrato.
    * Essa operação deve listar todos os depósitos e saques realizados na conta. No fim da listagem deve ser exibido o saldo atual da conta.
    Os valores devem ser exibidos utilizando o formato R$ xxx.xx
    Exemplo: 1500.45 == R$ 1500.45

---