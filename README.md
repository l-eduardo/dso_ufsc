# Gerenciamento interno de ativos e inventário de TI

Este projeto consiste em um sistema OOP para gerenciamento interno de ativos e inventário de TI com todos os tipos de associação. O sistema é composto pelas seguintes classes:

## Classes

### ITAsset

Esta classe representa um ativo de TI e contém propriedades como ID do ativo, tipo de ativo, fabricante, modelo, número de série, data de compra, data de expiração da garantia e localização.

### Inventário

Esta classe representa um inventário de ativos de TI e contém propriedades como ID do inventário, nome, descrição e uma lista de objetos ITAsset.

### Departamento

Esta classe representa um departamento dentro da organização e contém propriedades como ID do departamento, nome, localização e uma lista de objetos ITAsset.

### Funcionário

Esta classe representa um funcionário responsável pelo gerenciamento de ativos de TI e contém propriedades como ID do funcionário, nome, e-mail, número de telefone e uma lista de objetos ITAsset.

## Associações

O sistema utiliza os seguintes tipos de associação entre as classes:

### Composição

A classe Inventário é composta de objetos ITAsset, o que significa que um inventário pode ter vários ativos de TI.

### Agregação

A classe Departamento tem uma associação de agregação com a classe ITAsset, o que significa que um departamento pode ter vários ativos de TI.

### Herança

A classe Funcionário pode herdar de uma classe base Funcionário, que contém propriedades comuns a todos os funcionários.

### Associação

A classe ITAsset tem uma associação com a classe Departamento, o que significa que um ativo de TI pode ser atribuído a um departamento específico para fins de gerenciamento. A classe ITAsset também tem uma associação com a classe Funcionário, o que significa que um ativo de TI pode ser atribuído a um funcionário específico dentro de um departamento para fins de gerenciamento
