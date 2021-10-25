-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Tempo de geração: 01-Out-2021 às 16:19
-- Versão do servidor: 10.4.21-MariaDB
-- versão do PHP: 8.0.11

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `ficha1`
--
CREATE DATABASE IF NOT EXISTS `ficha1` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
USE `ficha1`;

-- --------------------------------------------------------

--
-- Estrutura da tabela `alunos`
--

CREATE TABLE `alunos` (
  `numero` int(5) NOT NULL,
  `nome` varchar(255) NOT NULL,
  `morada` varchar(255) NOT NULL,
  `idade` int(3) NOT NULL,
  `email` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Extraindo dados da tabela `alunos`
--

INSERT INTO `alunos` (`numero`, `nome`, `morada`, `idade`, `email`) VALUES
(1, 'André Oliveira Gomes', 'Lever', 17, 'al4707.andregomes@aediogomacedo.com'),
(2, 'Carlos Alexandre Barbosa Ribeiro', 'Olival', 17, 'al5244.carlosribeiro@aediogomacedo.com'),
(3, 'Daniela Alexandra Pereira Pinto', 'Mozelos', 17, 'al6405.danielapinto@aediogomacedo.com');

--
-- Índices para tabelas despejadas
--

--
-- Índices para tabela `alunos`
--
ALTER TABLE `alunos`
  ADD PRIMARY KEY (`numero`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
