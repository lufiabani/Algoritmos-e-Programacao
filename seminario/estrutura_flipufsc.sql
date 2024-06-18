-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Jun 09, 2024 at 11:32 PM
-- Server version: 8.0.30
-- PHP Version: 8.3.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `flipufsc2`
--

-- --------------------------------------------------------

--
-- Table structure for table `alternativas`
--

CREATE TABLE `alternativas` (
  `id` int NOT NULL,
  `texto` longtext NOT NULL,
  `resposta` int NOT NULL,
  `questao_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


CREATE TABLE `alunos` (
  `id` int NOT NULL,
  `nome` varchar(255) NOT NULL,
  `matricula` int NOT NULL,
  `pontuacao` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `alunos`
--

INSERT INTO `alunos` (`id`, `nome`, `matricula`, `pontuacao`) VALUES
(101, 'Alisson Rola Caldeira', 23201212, NULL),
(102, 'Arthur Bauer Cardoso', 24103788, NULL),
(103, 'Arthur Silveira Sampaio', 24103786, NULL),
(104, 'Artur Manarin de Jesus', 24105747, NULL),
(105, 'Breno Felisbino dos Anjos', 24102016, NULL),
(106, 'Bruna Letícia Matos dos Santos', 22104524, NULL),
(107, 'Carlos Eduardo Caetano de Melo', 21105788, NULL),
(108, 'Caroline Resende Zeferino', 24105322, NULL),
(109, 'Cassio Augusto Reus Guidi', 24102020, NULL),
(110, 'Christian de Vargas Silva', 202400535, NULL),
(111, 'Davi Estevao Arcaro', 24103787, NULL),
(112, 'Davi Ferreira da Silveira', 24102025, NULL),
(113, 'Develin Souza Goncalves', 24102015, NULL),
(114, 'Diego Nyland Bloemer', 24103789, NULL),
(115, 'Diva Moreira de Souza', 24102022, NULL),
(116, 'Eduardo Catani de Almeida', 24103785, NULL),
(117, 'Fabio Natan Oliveira Bittencourt', 24102012, NULL),
(118, 'Felipe Cidade Soares', 24102023, NULL),
(119, 'Felipe Rigueira Matar', 23201012, NULL),
(120, 'Gabriel Guterro Flor Bittencourt Silveira de Souza', 24102024, NULL),
(121, 'Gabriel Luis Biasio dos Santos', 23104643, NULL),
(122, 'Gustavo Becker Lodette', 24105324, NULL),
(123, 'Henrique de Souza Cavalheiro', 18104123, NULL),
(124, 'Ivy Oliveira dos Reis', 24103142, NULL),
(125, 'Jefferson Horacio Fernandes', 24100094, NULL),
(126, 'Jullya Estelita da Conceicao', 24103784, NULL),
(127, 'Kaberlyn Estelir Medeiros Dorigon', 24105746, NULL),
(128, 'Leonardo Latorre Boteon', 24102026, NULL),
(129, 'Lucas Alexandre Machado', 24103790, NULL),
(130, 'Luis Antonio Scarabelot Fiabani', 24102006, NULL),
(131, 'Luiz Angelo Tramontin Valdati', 22250755, NULL),
(132, 'Mauricio Melo Filho', 24103146, NULL),
(133, 'Pedro Konorath de Moraes', 23103315, NULL),
(134, 'Theo de Souza Gerhardt', 24104578, NULL),
(135, 'Thiago da Silva Fialho', 202400461, NULL),
(136, 'Victor Martins', 24103148, NULL),
(137, 'Fabrício Herpich', 1198799, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `questoes`
--

CREATE TABLE `questoes` (
  `id` int NOT NULL,
  `enunciado` longtext NOT NULL,
  `referencia` mediumtext,
  `comando` mediumtext NOT NULL,
  `prova` mediumtext NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `rodadas` (
  `id` int NOT NULL,
  `datahora` datetime NOT NULL,
  `aluno_id` int NOT NULL,
  `questao_id` int NOT NULL,
  `pontuacao` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `alternativas`
--
ALTER TABLE `alternativas`
  ADD PRIMARY KEY (`id`),
  ADD KEY `questao_id` (`questao_id`);

--
-- Indexes for table `alunos`
--
ALTER TABLE `alunos`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `questoes`
--
ALTER TABLE `questoes`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `rodadas`
--
ALTER TABLE `rodadas`
  ADD PRIMARY KEY (`id`),
  ADD KEY `aluno_id` (`aluno_id`),
  ADD KEY `questao_id` (`questao_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `alternativas`
--
ALTER TABLE `alternativas`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=103;

--
-- AUTO_INCREMENT for table `alunos`
--
ALTER TABLE `alunos`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=138;

--
-- AUTO_INCREMENT for table `questoes`
--
ALTER TABLE `questoes`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;

--
-- AUTO_INCREMENT for table `rodadas`
--
ALTER TABLE `rodadas`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `alternativas`
--
ALTER TABLE `alternativas`
  ADD CONSTRAINT `alternativas_ibfk_1` FOREIGN KEY (`questao_id`) REFERENCES `questoes` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `rodadas`
--
ALTER TABLE `rodadas`
  ADD CONSTRAINT `rodadas_ibfk_1` FOREIGN KEY (`aluno_id`) REFERENCES `alunos` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `rodadas_ibfk_2` FOREIGN KEY (`questao_id`) REFERENCES `questoes` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
