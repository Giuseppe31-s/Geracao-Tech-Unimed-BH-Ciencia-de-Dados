# Projeto de banco de dados E-commerce

## Diagrama ERR E-commerce

![image](https://raw.githubusercontent.com/Giuseppe31-s/Geracao-Tech-Unimed-BH-Ciencia-de-Dados/main/Banco%20de%20Dados%20SQL%20e%20NoSQL/E-commerce/e-commerce%20simples.png)


Objetivo:

Refinar o diagrama apresentado acrescentando os seguintes pontos:

    Cliente PJ e PF – Uma conta pode ser PJ ou PF, mas não pode ter as duas informações;
    Pagamento – Pode ter cadastrado mais de uma forma de pagamento;
    Entrega – Possui status e código de rastreio;

![image](https://raw.githubusercontent.com/Giuseppe31-s/Geracao-Tech-Unimed-BH-Ciencia-de-Dados/main/Banco%20de%20Dados%20SQL%20e%20NoSQL/E-commerce/E-commerce.png)

## Criação do banco de dados em MySQL

#### Criação de schema

```
CREATE DATABASE if not exist ecommerce;
USE ecommerce;
```

#### Criando  tabela de cliente.

```
CREATE TABLE clients(
        idClient INT AUTO_INCREMENT PRIMARY KEY,
        Fname VARCHAR(20),
        Minit CHAR(3),
        Lname VARCHAR(20),
        CPF CHAR(11) NOT NULL,
        Address VARCHAR(30),
        CONSTRAINT unique_cpf_client UNIQUE(CPF)
);
```
#### Criando  tabela do produto

```
CREATE TABLE products (
        idProduct INT AUTO_INCREMENT PRIMARY KEY,
        Pname VARCHAR(10) NOT NULL,
        Classification_Kids BOOL DEFAULT FALSE,
        Category ENUM('Eletrônico', 'Vestimenta', 'Brinquedos', 'Alimentos', 'Móveis') NOT NULL,
        Avaliação FLOAT DEFAULT 0,
        Size VARCHAR(10)
);

```

#### Criando  tabela Pedido.

```
TABLE orders (
        idOrder INT AUTO_INCREMENT PRIMARY KEY,
        idOrderClient INT,
        OrderStatus ENUM('Cancelado', 'Confirmado', 'Em processamento') DEFAULT 'Em Processamento',
        OrderDescription VARCHAR(255),
        SendValue FLOAT DEFAULT 10,
        PaymentCash BOOL DEFAULT FALSE,
        CONSTRAINT fk_orders_client FOREIGN KEY (idOrderClient)
            REFERENCES clients (idClient)
);
```

#### Criando tabela de estoque

```
CREATE TABLE productstorage (
        idProdStorage INT AUTO_INCREMENT PRIMARY KEY,
        StorageLocation VARCHAR(255),
        Quantity INT DEFAULT 0
);
```

### Criando  tabela de fornecedor 

```
CREATE TABLE supplier (
        idSupplier INT AUTO_INCREMENT PRIMARY KEY,
        SocialName VARCHAR(255) NOT NULL,
        CNPJ CHAR(15) NOT NULL,
        Contact CHAR(11) NOT NULL,
        CONSTRAINT unique_supplier UNIQUE (CNPJ)
);
```

#### Criando tabela vendedor.

```
CREATE TABLE seller (
        idSeller INT AUTO_INCREMENT PRIMARY KEY,
        SocialName VARCHAR(255) NOT NULL,
        AbstName VARCHAR(255),
        CNPJ CHAR(15),
        CPF CHAR(11),
        Location VARCHAR(255),
        Contact CHAR(11) NOT NULL,
        CONSTRAINT unique_cnpj_seller UNIQUE (CNPJ),
        CONSTRAINT unique_cpf_seller UNIQUE (CPF)
);
```

#### Criando tabela produto/vendedor.

```
CREATE TABLE productseller (
        idPseller INT,
        idPproduct INT,
        prodQuantity INT DEFAULT 1,
        PRIMARY KEY (idPseller , idPproduct),
        CONSTRAINT fk_product_seller FOREIGN KEY (idPseller)
            REFERENCES seller (idSeller),
        CONSTRAINT fk_product_product FOREIGN KEY (idPproduct)
            REFERENCES products (idProduct)
);
```
#### Criando tabela produto/pedido.


```
CREATE TABLE productorder (
        idPOproduct INT,
        idPOorder INT,
        PoQuantity INT DEFAULT 1,
        PoStatus ENUM('Disponível', 'Sem estoque') DEFAULT 'Disponível',
        PRIMARY KEY (idPOproduct , idPOorder),
        CONSTRAINT fk_productorder_seller FOREIGN KEY (idPOproduct)
            REFERENCES products (idProduct),
        CONSTRAINT fk_productorder_product FOREIGN KEY (idPOorder)
            REFERENCES orders (idOrder)
);
```

#### Criando tabela estoque/produto.

```
CREATE TABLE storagelocation (
        idLproduct INT,
        idLstorage INT,
        location VARCHAR(255) NOT NULL,
        PRIMARY KEY (idLproduct , idLstorage),
        CONSTRAINT fk_productstorage_seller FOREIGN KEY (idLproduct)
            REFERENCES products (idProduct),
        CONSTRAINT fk_productstorage_product FOREIGN KEY (idLstorage)
            REFERENCES productstorage (idProdStorage)
);
```
#### Criando tabela produto/fornecedor.

```
CREATE TABLE productsupplier (
        idPsSupplier INT,
        idPsProduct INT,
        quantity INT NOT NULL,
        PRIMARY KEY (idPsSupplier , idPsProduct),
        CONSTRAINT fk_product_supplier_supplier FOREIGN KEY (idPsSupplier)
            REFERENCES supplier (idSupplier),
        CONSTRAINT fk_product_supplier_product FOREIGN KEY (idPsProduct)
            REFERENCES products (idProduct)
);
```

