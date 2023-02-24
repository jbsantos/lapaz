-- MySQL dump 10.13  Distrib 5.7.41, for Linux (x86_64)
--
-- Host: 10.80.84.28    Database: livro_despachante
-- ------------------------------------------------------
-- Server version	5.5.5-10.1.44-MariaDB-0+deb9u1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `add_missao`
--

DROP TABLE IF EXISTS `add_missao`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `add_missao` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nome` varchar(25) NOT NULL,
  `descricao` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `add_missao`
--

LOCK TABLES `add_missao` WRITE;
/*!40000 ALTER TABLE `add_missao` DISABLE KEYS */;
INSERT INTO `add_missao` VALUES (1,'Efetivo para BARF','Levar o efetivo do Comar 2 para a Barf'),(2,'Rotina do Brigadeiro','Viatura a disposição do Brigadeiro.'),(6,'Rotina Seripa','Viatura disponível o dia todo para missões interna do Seripa 2'),(7,'Missão Funeral','Atendimento da equipe de funeral');
/*!40000 ALTER TABLE `add_missao` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `alembic_version`
--

DROP TABLE IF EXISTS `alembic_version`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `alembic_version` (
  `version_num` varchar(32) NOT NULL,
  PRIMARY KEY (`version_num`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `alembic_version`
--

LOCK TABLES `alembic_version` WRITE;
/*!40000 ALTER TABLE `alembic_version` DISABLE KEYS */;
INSERT INTO `alembic_version` VALUES ('c0e7f698ff99');
/*!40000 ALTER TABLE `alembic_version` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `category`
--

DROP TABLE IF EXISTS `category`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `category` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(20) NOT NULL,
  `description` text,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `category`
--

LOCK TABLES `category` WRITE;
/*!40000 ALTER TABLE `category` DISABLE KEYS */;
INSERT INTO `category` VALUES (1,'Calçados','');
/*!40000 ALTER TABLE `category` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `missao`
--

DROP TABLE IF EXISTS `missao`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `missao` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `data_saida` datetime NOT NULL,
  `data_chegada` datetime DEFAULT NULL,
  `status` int(11) DEFAULT NULL,
  `user_created` int(11) NOT NULL,
  `motorista` int(11) DEFAULT NULL,
  `ficha` int(10) NOT NULL,
  `siloms` int(15) DEFAULT NULL,
  `viatura` int(11) NOT NULL,
  `natureza_servico` text NOT NULL,
  `km_saida` decimal(10,2) DEFAULT NULL,
  `km_chegada` decimal(10,2) DEFAULT NULL,
  `observacao` varchar(600) DEFAULT NULL,
  `ultimo_motorista` int(11) DEFAULT NULL,
  `km_viatura` varchar(15) DEFAULT NULL,
  `ass_despachante_abrir` varchar(30) DEFAULT NULL,
  `ass_despachante_fechar` varchar(30) DEFAULT NULL,
  `ass_motorista_saida` varchar(30) DEFAULT NULL,
  `ass_motorista_chegada` varchar(30) DEFAULT NULL,
  `missao` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `motorista` (`motorista`),
  KEY `user_created` (`user_created`),
  KEY `missao_ibfk_3` (`viatura`),
  CONSTRAINT `missao_ibfk_1` FOREIGN KEY (`motorista`) REFERENCES `motorista` (`id`),
  CONSTRAINT `missao_ibfk_2` FOREIGN KEY (`user_created`) REFERENCES `user` (`id`),
  CONSTRAINT `missao_ibfk_3` FOREIGN KEY (`viatura`) REFERENCES `viatura` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=158 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `missao`
--

LOCK TABLES `missao` WRITE;
/*!40000 ALTER TABLE `missao` DISABLE KEYS */;
INSERT INTO `missao` VALUES (146,'2023-01-31 11:13:13','2023-01-31 11:13:00',2,9,10,55,55,10,'',111201.00,NULL,'55',138,'111201','administrador','administrador','S2 VALDEMAR ','1S ADRIANO',1),(147,'2023-02-06 10:12:20','2023-02-06 10:12:00',2,9,10,2,2,11,'',6.00,17.00,'2222',125,NULL,'administrador','administrador','S2 VALDEMAR ',NULL,2),(148,'2023-02-06 10:35:55','2023-02-06 11:00:00',2,2,10,11111,11111,88,'',1235.00,1.00,'teste',138,NULL,'Operações','Despachante','S2 VALDEMAR ',NULL,1),(149,'2023-02-06 10:35:55','2023-02-06 10:55:00',2,2,10,11111,11111,88,'',1234.00,1235.00,'teste',138,NULL,'Operações','Operações','S2 VALDEMAR ',NULL,1),(150,'2023-02-06 10:56:52',NULL,2,2,11,777777,777777,87,'',0.00,NULL,'teste',138,NULL,'Operações','Despachante','S2 MOURA ',NULL,1),(151,'2023-02-07 12:19:00','2023-02-07 12:20:00',2,9,11,99,99,10,'',0.00,55.00,'o militar vai seguir para o destino previsto.',125,NULL,'administrador','administrador','S2 MOURA ',NULL,2),(152,'2023-02-16 08:23:00',NULL,3,2,10,777777777,123,11,'',17.00,NULL,'oiê',0,NULL,'Operações',NULL,'S2 VALDEMAR ',NULL,1),(153,'2023-02-16 08:23:00','2023-02-16 08:24:00',2,2,10,777777777,123,11,'',17.00,10.00,'oiê',144,NULL,'Operações','Operações','S2 VALDEMAR ',NULL,1),(154,'2023-02-16 12:26:00','2023-02-19 14:00:00',2,9,26,3453,534,10,'',55.00,665.00,'5345',144,'665','administrador','administrador','S2 ROGÉRIO ','1T FÉLIX',1),(155,'2023-02-19 14:54:00','2023-02-19 14:57:00',2,9,132,432,121,14,'',0.00,55.00,'levar o cel',139,'55','administrador','administrador','2S ARQUIMEDES ','1S MARCELINO',1),(156,'2023-02-23 09:16:00',NULL,1,9,11,534534,3454,10,'',665.00,NULL,'teste',NULL,NULL,'administrador',NULL,'S2 MOURA ',NULL,2),(157,'2023-02-23 09:17:00',NULL,4,9,26,4543,354,14,'',NULL,NULL,'dfgsd',NULL,NULL,'administrador',NULL,NULL,NULL,1);
/*!40000 ALTER TABLE `missao` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `motorista`
--

DROP TABLE IF EXISTS `motorista`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `motorista` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(20) NOT NULL,
  `saram` int(11) NOT NULL,
  `om` varchar(20) NOT NULL,
  `validade_habilitacao` datetime(6) NOT NULL,
  `categoria_habilitacao` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=146 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `motorista`
--

LOCK TABLES `motorista` WRITE;
/*!40000 ALTER TABLE `motorista` DISABLE KEYS */;
INSERT INTO `motorista` VALUES (10,'S2 VALDEMAR ',7377398,'GAP-RF','0023-01-12 23:23:00.000000','AB'),(11,'S2 MOURA ',7377363,'GAP-RF','0023-08-05 23:00:00.000000','AB \r\n'),(12,'S2 TONNY ',7377690,'GAP','2025-09-28 12:47:00.000000','AB \r\n'),(13,'S2 WYLTON ',7377193,'GAP','2024-06-25 12:48:00.000000','AB \r\n'),(14,'S2 ALDINO ',7149778,'GAP','2021-11-12 12:49:00.000000','B \r\n'),(15,'S2 LAÉRCIO ',7149956,'GAP','2032-07-25 12:50:00.000000','AD \r\n'),(16,'S2 CRUZ ',7149891,'BARF','2023-06-25 12:51:00.000000','AB \r\n'),(17,'S2 ALLEF ',7149581,'GAP','2022-09-30 12:51:00.000000','AB \r\n'),(18,'S2 LUCIANO ',7149883,'GAP','2023-01-08 12:52:00.000000','AB \r\n'),(19,'S2 EUGENIO ',7227906,'GAP','2025-08-06 12:53:00.000000','AB \r\n'),(20,'S2 ELIELSON ',7149590,'GAP','2025-10-29 12:53:00.000000','AD \r\n'),(21,'S2 THIAGO ',7227574,'GAP','2025-03-07 12:54:00.000000','AB \r\n'),(22,'S2 FERREIRA ',7227469,'GAP','2032-02-17 12:55:00.000000','AD \r\n'),(23,'S2 EUDES MARTINS ',7227876,'GAP','2023-10-01 12:55:00.000000','AB \r\n'),(24,'S2 CLAUDIONOR ',7149697,'GAP','2023-11-14 12:56:00.000000','B \r\n'),(25,'S2 LOPES SILVA ',7197357,'GAP','2032-07-25 12:57:00.000000','AD \r\n'),(26,'S2 ROGÉRIO ',7227752,'GAP','2025-11-10 12:57:00.000000','AD \r\n'),(27,'S2 WESLEY ',7228317,'GAP','2022-01-17 12:58:00.000000','B \r\n'),(28,'S2 TAUAN ',7227795,'GAP','2023-08-21 12:59:00.000000','AB \r\n'),(29,'S2 ISSAC ',7149832,'GAP','2024-10-03 12:59:00.000000','AB \r\n'),(30,'S2 RENNE ',7325665,'GAP','2026-03-04 13:00:00.000000','B \r\n'),(31,'S2 MORAIS ',7325398,'GAP','2025-07-01 13:00:00.000000','AB \r\n'),(32,'S2 VICTOR			 ',7301995,'GAP','2024-08-15 13:01:00.000000','AB \r\n'),(33,'S2 MARTINS ',7301944,'GAP','2032-01-13 13:01:00.000000','AD \r\n'),(34,'S2 A.SILVA ',7301731,'GAP','2023-04-14 13:02:00.000000','AB \r\n'),(35,'S2 GIUEDISON ',7301898,'GAP','2023-09-05 13:02:00.000000','B \r\n'),(36,'S2 RINALDO ',7301910,'GAP','2023-01-11 13:03:00.000000','AB \r\n'),(37,'S2 CESAR ',7301782,'GAP','2023-03-03 13:03:00.000000','AB \r\n'),(38,'S2 PALIN ',7301774,'GAP','2030-07-25 13:17:00.000000','AD \r\n'),(39,'S2 HANIEL ',7301537,'GAP','2024-05-13 13:18:00.000000','AB \r\n'),(40,'S2 NASCIMENTO ',7301430,'GAP','2032-02-04 13:21:00.000000','AD \r\n'),(41,'S2 ALEXANDRE ',7301979,'GAP','2023-09-13 13:21:00.000000','AB \r\n'),(42,'S2 MASTROIANI ',7301880,'GAP','2023-06-01 13:22:00.000000','AB \r\n'),(43,'S2 ERALDO ',7302010,'GAP','2024-10-10 13:22:00.000000','AB \r\n'),(44,'S2 HALYSON ',7301650,'GAP','2024-09-19 13:23:00.000000','B \r\n'),(45,'S2 SILVA ',7301928,'GAP','2024-02-12 13:23:00.000000','AB \r\n'),(46,'S2 ANDREW OLIVEIRA ',7301758,'GAP','2023-05-03 13:24:00.000000','AB \r\n'),(47,'S2 M. NASCIMENTO ',7301545,'GAP','2032-07-25 13:25:00.000000','AD \r\n'),(48,'S2 DIAS ',7263538,'GAP','2024-05-16 13:25:00.000000','B \r\n'),(49,'S2 TACIANO ',7263864,'GAP','2023-08-01 13:29:00.000000','AB \r\n'),(50,'S2 LUCAS MOURA ',7263465,'GAP','2023-04-24 13:30:00.000000','AB \r\n'),(51,'S2 G. SANTOS ',7263643,'GAP','2031-12-20 13:31:00.000000','D \r\n'),(52,'S2 ROBERTO LUIZ ',7264143,'GAP','2031-09-06 13:31:00.000000','AD \r\n'),(53,'S2 DURVAL ',7264011,'GAP','2023-05-18 13:32:00.000000','AB \r\n'),(54,'S2 MERIK ',7264062,'GAP','2031-08-17 13:32:00.000000','AD \r\n'),(55,'S2 ANTHONY ',7263619,'GAP','2024-05-03 13:33:00.000000','B \r\n'),(56,'S2 MARCIO ',7263600,'GAP','2023-04-09 13:34:00.000000','AB \r\n'),(57,'S1 J. VICENTE ',6881920,'GAP','2024-01-23 13:40:00.000000','AB \r\n'),(58,'S1 PAZ ',6881610,'GAP','2025-08-04 13:41:00.000000','AD \r\n'),(59,'S1 MARCOS ANTONIO ',6847315,'GAP','2023-05-02 13:41:00.000000','AB \r\n'),(60,'S1 DIEGO SILVA ',6848834,'GAP','2023-12-12 13:42:00.000000','AD \r\n'),(61,'S1 V. GUEDES ',6847293,'GAP','2024-05-29 13:42:00.000000','AD \r\n'),(62,'S1 LADILSON ',6847072,'GAP','2029-07-25 13:43:00.000000','AD \r\n'),(63,'S1 ESTEVES ',6847137,'GAP','2024-07-03 13:48:00.000000','AB \r\n'),(64,'S1 SILVA ALVES ',6848850,'GAP','2023-09-11 13:49:00.000000','AB \r\n'),(65,'S1 FELIPE LIMA ',6846378,'GAP','2024-04-15 13:49:00.000000','AB \r\n'),(66,'S1 SEBASTIÃO ',6846351,'GAP','2023-05-07 13:50:00.000000','AB \r\n'),(67,'S1 RUAN LIMA ',6847188,'GAP','2023-09-13 13:51:00.000000','AB \r\n'),(68,'S1 EUDES ',6847579,'GAP','2029-09-25 13:52:00.000000','AB \r\n'),(69,'S1 F.TAVARES ',6848583,'GAP','2023-04-30 13:52:00.000000','AB \r\n'),(70,'S1 BOMFIM ',6846882,'GAP','2024-05-28 13:53:00.000000','AD'),(71,'S1 ALEIXO ',6847722,'GAP','2024-04-20 14:00:00.000000','AB \r\n'),(72,'S1 JUSTINO ',6847412,'GAP','2031-05-17 14:02:00.000000','B \r\n'),(73,'S1 W FERNANDO ',7227671,'GAP','2022-12-04 14:03:00.000000','AB \r\n'),(74,'S1 JOSEMAR ',7149727,'GAP','2024-04-06 14:08:00.000000','AB \r\n'),(75,'S1 VILAR ',7228279,'GAP','2025-12-10 14:09:00.000000','AD \r\n'),(76,'S1 W. CABRAL ',6991076,'GAP','2024-10-18 14:10:00.000000','AB \r\n'),(77,'S1 THASSIO ',6930026,'GAP','2025-11-09 14:10:00.000000','AD \r\n'),(78,'S1 SIDERLEI ',6928587,'GAP','2025-12-03 14:11:00.000000','E \r\n'),(79,'S1 ROBSON ',6928773,'GAP','2023-05-26 14:15:00.000000','AB \r\n'),(80,'S1 V.SERAFIM ',6930441,'GAP','2024-11-08 14:16:00.000000','AB \r\n'),(81,'S1 LUIZ LIMA ',6928595,'GAP','2024-03-22 14:20:00.000000','AB \r\n'),(82,'S1 AVELINO ',6929940,'GAP','2023-01-10 14:21:00.000000','AB \r\n'),(83,'S1 ALEXANDRE ',6929818,'GAP','2031-08-24 14:21:00.000000','AB \r\n'),(84,'S1 MANÇO',6929443,'GAP','2025-11-10 14:22:00.000000','AD \r\n'),(85,'S1 MARQUES ',6930018,'GAP-RF','2024-05-07 14:23:00.000000','AB \r\n'),(86,'S1 LUIZ ALBERTO ',6930085,'GAP','2023-08-31 14:24:00.000000','AB \r\n'),(87,'S1 DANIEL ',6928374,'GAP','2023-12-05 14:25:00.000000','AD \r\n'),(88,'S1 CHAVES ',6928200,'GAP','2025-10-28 14:25:00.000000','AB \r\n'),(89,'S1 MANIÇOBA ',6930140,'GAP','2024-05-20 14:26:00.000000','B \r\n'),(90,'S1 JAILTON ',6929354,'GAP','2027-10-13 14:27:00.000000','AB \r\n'),(91,'S1 JAILSON SILVA ',6929672,'GAP','2031-11-03 14:27:00.000000','AB \r\n'),(92,'S1 JACKSON ',6928714,'GAP','2023-08-04 14:28:00.000000','AB \r\n'),(93,'S1 KAYO LEITE ',6928684,'GAP','2023-07-27 14:29:00.000000','AB \r\n'),(94,'S1 GEAN SILVA ',6928498,'GAP','2024-08-20 14:29:00.000000','AB \r\n'),(95,'S1 M. SILVA  ',7263562,'GAP','2024-03-09 14:30:00.000000','B \r\n'),(96,'CB CONCEIÇÃO ',6881645,'GAP','2025-11-03 14:52:00.000000','AD \r\n'),(97,'CB M. OLIVEIRA ',6848532,'GAP','2030-01-17 14:53:00.000000','AB \r\n'),(98,'CB WESLEY SILVA ',6849032,'GAP','2031-11-08 14:54:00.000000','AD'),(99,'CB BONNER ',6846564,'GAP','2026-08-26 14:56:00.000000','AB \r\n'),(100,'CB V. SILVA ',6848605,'GAP','2024-02-11 14:56:00.000000','AB \r\n'),(101,'CB R. SANTOS ',6848842,'GAP','2024-06-07 14:57:00.000000','AB \r\n'),(102,'CB FREIRE ',6847536,'GAP','2023-02-15 14:58:00.000000','AB \r\n'),(103,'CB SEVERINO ',6763910,'GAP','2025-02-07 14:58:00.000000','AB \r\n'),(104,'CB MUNIZ ',6764207,'GAP','2024-01-14 14:59:00.000000','AD \r\n'),(105,'CB GONÇALVES ',6765319,'GAP','2030-07-25 15:00:00.000000','AD \r\n'),(106,'CB DENILSON ',6764754,'GAP','2023-03-27 15:00:00.000000','AB \r\n'),(107,'CB HENRIQUE SILVA ',6765530,'GAP','2025-08-03 15:01:00.000000','AD \r\n'),(108,'CB SIMÃO ',6764177,'GAP','2032-07-25 15:02:00.000000','D \r\n'),(109,'CB MORAES ',6764029,'GAP','2024-02-09 15:03:00.000000','AB \r\n'),(110,'CB CARLOS LIMA ',6765211,'GAP','2031-07-29 15:03:00.000000','AD \r\n'),(111,'CB ABSALÃO ',6694403,'GAP','2031-07-14 15:04:00.000000','AD \r\n'),(112,'CB PAULO VICTOR ',6694179,'GAP','2024-10-25 15:04:00.000000','D \r\n'),(113,'CB LÁZARO  ',6694080,'GAP','2031-07-20 15:05:00.000000','AD \r\n'),(114,'CB WAGNER ',6700993,'GAP','2024-10-21 15:06:00.000000','AD \r\n'),(115,'CB MABSON ',6695167,'GAP','2031-10-04 15:07:00.000000','AE \r\n'),(116,'CB TONIVALDO ',4101340,'GAP','2024-06-07 15:08:00.000000','AD \r\n'),(117,'CB J. SILVA ',4101987,'GAP','2023-11-28 15:09:00.000000','AB \r\n'),(118,'3S JEFFERSON ',7496176,'GAP ','2031-08-18 13:02:00.000000','AB \r\n'),(119,'3S EFESON ',7496508,'GAP ','2024-08-01 13:03:00.000000','AB \r\n'),(120,'3S WILDE ',7496400,'GAP ','2031-12-06 13:03:00.000000','AB \r\n'),(121,'3S ÍKARO ',6957897,'GAP ','2031-12-16 13:04:00.000000','AE \r\n'),(122,'3S ANTONIO ',6847102,'GAP ','2031-08-04 13:06:00.000000','AB \r\n'),(123,'3S EDMAR ',6772714,'GAP ','2024-11-08 13:09:00.000000','AB \r\n'),(124,'3S ALFREDO ',6772641,'GAP ','2024-01-16 13:10:00.000000','AD \r\n'),(125,'3S HERMOGENES ',6772838,'GAP ','2031-06-15 13:11:00.000000','AD \r\n'),(126,'3S MARCELO ',6772633,'GAP ','2024-01-17 13:12:00.000000','AB \r\n'),(127,'2S ALAN ',6190669,'GAP','2031-09-11 13:23:00.000000','AD \r\n'),(128,'2S SALES ',6000010,'GAP ','2025-11-05 13:24:00.000000','AD \r\n'),(129,'2S RAUL CESAR ',4336267,'GAP ','2025-01-03 13:24:00.000000','AB \r\n'),(130,'2S VICTOR LUIZ ',6164820,'GAP ','2024-11-14 13:25:00.000000','B \r\n'),(131,'2S LUZITANO ',6379656,'GAP ','2032-07-20 13:25:00.000000','AD \r\n'),(132,'2S ARQUIMEDES ',6318380,'GAP-RF','2025-05-28 13:26:00.000000','D \r\n'),(133,'2S DIEGO LEMOS ',6157041,'GAP ','2023-08-11 13:27:00.000000','D \r\n'),(134,'2S CLENIO ',4359046,'GAP ','2024-01-18 13:28:00.000000','AB \r\n'),(135,'2S JAILSON ',3806642,'GAP ','2031-07-20 13:28:00.000000','AD \r\n'),(136,'2S DENYS ',4027558,'GAP ','2024-10-30 13:29:00.000000','AB \r\n'),(137,'2S PAULO NUNES ',3330729,'GAP ','2024-07-09 13:29:00.000000','AD \r\n'),(138,'1S ADRIANO',3823270,'GAP','2024-09-25 13:34:00.000000','E'),(139,'1S MARCELINO',3083390,'GAP','2023-10-10 13:36:00.000000','AB'),(140,'SO RADEVAL',3172015,'GAP','2026-02-04 13:37:00.000000','B'),(141,'SO DE ARAÚJO',2880156,'GAP','2025-11-07 13:37:00.000000','AB'),(142,'SO RENATO',3083497,'GAP','2032-09-02 13:39:00.000000','B'),(143,'SO MACEDO',3083497,'GAP','2031-10-29 13:40:00.000000','AB'),(144,'1T FÉLIX',1686186,'GAP','2024-10-21 13:41:00.000000','B'),(145,'CP AUGUSTO',1686186,'GAP','2023-04-10 13:42:00.000000','D');
/*!40000 ALTER TABLE `motorista` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `product`
--

DROP TABLE IF EXISTS `product`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `product` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(20) NOT NULL,
  `description` text NOT NULL,
  `qtd` int(11) DEFAULT NULL,
  `image` text,
  `price` decimal(10,2) NOT NULL,
  `date_created` datetime NOT NULL,
  `last_update` datetime DEFAULT NULL,
  `status` int(11) DEFAULT NULL,
  `user_created` int(11) NOT NULL,
  `category` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  KEY `category` (`category`),
  KEY `user_created` (`user_created`),
  CONSTRAINT `product_ibfk_1` FOREIGN KEY (`category`) REFERENCES `category` (`id`),
  CONSTRAINT `product_ibfk_2` FOREIGN KEY (`user_created`) REFERENCES `user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `product`
--

LOCK TABLES `product` WRITE;
/*!40000 ALTER TABLE `product` DISABLE KEYS */;
INSERT INTO `product` VALUES (1,'Tênis','Calçado',20,'',149.90,'2019-03-02 19:32:00','2019-03-02 19:32:00',1,2,1),(2,'Sapato Social','Calçado',40,'',249.90,'2019-03-02 21:17:00','2019-03-02 21:20:26',1,2,1),(3,'Sapatênis','Calçado',200,NULL,350.00,'2019-03-04 12:09:42','2019-03-02 21:20:26',1,2,1),(4,'Sandália','Calçado',30,'',300.00,'2019-03-04 22:53:00','2019-03-04 22:53:00',1,2,1),(5,'Chinelo','Calçado',40,'',1900.00,'2019-03-04 22:54:00','2019-03-04 22:54:00',1,2,1);
/*!40000 ALTER TABLE `product` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `role`
--

DROP TABLE IF EXISTS `role`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `role` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(40) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `role`
--

LOCK TABLES `role` WRITE;
/*!40000 ALTER TABLE `role` DISABLE KEYS */;
INSERT INTO `role` VALUES (2,'Despachante'),(5,'Informática'),(1,'Operações'),(3,'Secretaria'),(4,'Usuário');
/*!40000 ALTER TABLE `role` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `status`
--

DROP TABLE IF EXISTS `status`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `status` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(20) NOT NULL,
  `description` text,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `status`
--

LOCK TABLES `status` WRITE;
/*!40000 ALTER TABLE `status` DISABLE KEYS */;
INSERT INTO `status` VALUES (1,'Em andamento','Missão ativa, viatura em rota.'),(2,'Concluída','Viatura entregue ao despachante e feita a vistoria.'),(3,'Cancelada','Missão cancelada'),(4,'Prevista','Missão prevista ');
/*!40000 ALTER TABLE `status` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(40) NOT NULL,
  `email` varchar(120) NOT NULL,
  `password` varchar(200) NOT NULL,
  `date_created` datetime NOT NULL,
  `last_update` datetime DEFAULT NULL,
  `role` int(11) NOT NULL,
  `active` tinyint(1) DEFAULT NULL,
  `recovery_code` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`),
  UNIQUE KEY `username` (`username`),
  KEY `role` (`role`),
  CONSTRAINT `user_ibfk_1` FOREIGN KEY (`role`) REFERENCES `role` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (2,'Operações','operacoes@email.com','$pbkdf2-sha256$29000$YMzZG2MshTAmJITwfi/F.A$5DPjGiqbfJK2MiNZoX.tU0n5B2FCECa1Dqj0FKgZHvY','2019-03-02 13:33:00','2022-11-22 12:05:01',1,1,'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MiwidXNlcm5hbWUiOiJ0aWFnb2x1aXpycyIsImV4cCI6MTU1MjI0NDQ5Mn0.S0L7LiRIWgNRT3Mf16-g1ZU6azeSF0QINyw8zVzlJyY'),(4,'Despachante','despachante@email','$pbkdf2-sha256$29000$bK1Vas0Zg5AyxjjHGENobQ$MoBCvR3TJEJJ5mT4ZbuJb1M3v3.BSfd2mIRggneuhvE','2019-03-07 17:53:00','2022-06-14 12:38:43',2,1,NULL),(5,'Secretaria','secretaria@email','$pbkdf2-sha256$29000$zJkTgvCekzIGAMD4fy9lbA$ZwiBUIMfZifDceqohQ0fn3/6LqAnYviT3Yfiz9WEW6s','2019-03-07 17:53:00','2022-06-29 14:50:14',3,1,NULL),(6,'usuario','usuario@email','$pbkdf2-sha256$29000$QejdG6OUcg7hXIuRUmoN4Q$kUGKRveiVgXJUV03DaIRwQWPOnlrAcI3sD8nmFAgsa4','2019-03-07 17:53:00','2019-04-15 16:22:28',4,1,'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6NiwidXNlcm5hbWUiOiJ1c3VhcmlvIiwiZXhwIjoxNTU1MzU2NDI3fQ.Huf6P-pr4qsfLsiVowvm3ZRSsRmNszJmxG_ezD_m2U8'),(7,'Jorge Batista Alves dos Santos','jorge0302@gmail.com','$pbkdf2-sha256$29000$4vwf41zL.V/rvTcmxLj33g$KiPwlnxJFJUK5EB1qD3cotArGsl8oYaVv3qN1ZQJjr0','2022-06-14 12:45:00',NULL,2,1,NULL),(8,'Rivelino','rivelino@email.com','$pbkdf2-sha256$29000$WasVAsD4/5.zttZ6jxEi5A$Qs76XJXIgfUaRx1.exQGInu49IkwGQQId0rFCa9d19E','2022-06-15 12:50:00','2022-11-22 12:08:23',2,1,NULL),(9,'administrador','astic@fab.mil.br','$pbkdf2-sha256$29000$//.fU4qxFuL8n7P2/t8bIw$lBFhalcAA1HbrQL/CoIxP76wDYeSR4kTO84yo6xtjII','2022-06-27 08:29:00','2022-08-24 08:58:14',5,1,NULL),(10,'teste222','email@email','$pbkdf2-sha256$29000$tRYCwBhjjDFmzBmD8D6HkA$SagVSjctGQbcMBrRCKbPZvXqfYZzLjfMDwQizgNt/Kw','2022-07-05 13:52:00',NULL,2,1,NULL),(13,'teste','teste@gmail.com','$pbkdf2-sha256$29000$6D1n7B1jDMG4917r3ds7pw$ApbZkqbLtbFjamtt4OkAVGusd7zETaWVZkvzelHdm18','2022-11-23 11:09:00',NULL,5,1,NULL),(14,'teeste','testes@gmail.com','$pbkdf2-sha256$29000$NKYUAgAAQGjNmVPqHYOwlg$ZvrQhHXV48ByndOUhy5Q8B3rW1oPdl4ITWjNgfP58YU','2022-11-23 11:15:00',NULL,1,1,NULL),(15,'jorgejbas','teste13@gmail.com','$pbkdf2-sha256$29000$JcR4j5GyVopxLiVEyBlDyA$XgulyAMXQV/QHxal6PWu91GE9hW33rVurQEOjtwir44','2022-11-23 11:55:00',NULL,4,1,NULL),(16,'arquimedes','arquimedes@fab.mil.br','$pbkdf2-sha256$29000$szZmbI0RQiiF8H4v5XwvZQ$e.RpLBVbj/ZsrRwh9c4nF7AHdwCYhW/qBdODwojW10U','2022-11-24 09:33:00',NULL,1,1,NULL);
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `viatura`
--

DROP TABLE IF EXISTS `viatura`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `viatura` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(20) NOT NULL,
  `description` text,
  `active` tinyint(1) DEFAULT NULL,
  `km_viatura` decimal(10,0) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=89 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `viatura`
--

LOCK TABLES `viatura` WRITE;
/*!40000 ALTER TABLE `viatura` DISABLE KEYS */;
INSERT INTO `viatura` VALUES (10,'20BP150','SIENA',0,665),(11,'08DE475','AMBULÂNCIA \r\n',1,10),(12,'07DE289','AMBULÂNCIA \r\n',1,0),(13,'09DE249','AMBULÂNCIA \r\n',1,0),(14,'09DE237','AMBULÂNCIA \r\n',1,55),(15,'10DE345','AMBULÂNCIA \r\n',1,0),(16,'08DE269','AMBULÂNCIA \r\n',1,0),(17,'08DE270','AMBULÂNCIA \r\n',1,0),(18,'11DE240','AMBULÂNCIA \r\n',1,0),(19,'13DC373','CAMINHÃO BAÚ\r\n',1,0),(20,'12DE207','CAMINHÃO CESTO\r\n',1,0),(21,'12DE212','CAMINHÃO CESTO\r\n',1,0),(22,'12DE209','CAMINHÃO MUNK\r\n',1,0),(23,'12DC105','CAMINHÃO LEVE\r\n',1,0),(24,'13DC304','CAMINHÃO LEVE\r\n',1,0),(25,'13DC579','CAMINHÃO LEVE\r\n',1,0),(26,'12DC091','CAMINHÃO MÉDIO/PESADO\r\n',1,0),(27,'13DC372','CAMINHÃO MÉDIO/PESADO\r\n',0,0),(28,'13DC560','CAMINHÃO MÉDIO/PESADO\r\n',1,0),(29,'13DC561','CAMINHÃO MÉDIO/PESADO\r\n',1,0),(30,'13DC580','CAMINHÃO MÉDIO/PESADO\r\n',1,0),(31,'11DP173','CAMINHÃO MILITAR\r\n',1,0),(32,'11DP174','CAMINHÃO MILITAR\r\n',1,0),(33,'12DP208','CAMINHÃO MILITAR\r\n',1,0),(34,'13DP278','CAMINHÃO MILITAR\r\n',0,0),(35,'13DP279','CAMINHÃO MILITAR\r\n',1,0),(36,'13DP280','CAMINHÃO MILITAR\r\n',1,0),(37,'13DE499',' GUINCHO- LEVE\r\n',1,0),(38,'13DE498','GUINCHO- PESADO\r\n',1,0),(39,'12DE270','CARRO LIMPA FOSSA\r\n',1,0),(40,'12DE218','CAÇAMBA\r\n',1,0),(41,'13DE305','CAÇAMBA\r\n',1,0),(42,'13DE559','CAÇAMBA\r\n',1,0),(43,'13DE577','CAÇAMBA\r\n',1,0),(44,'13DE576','CAÇAMBA\r\n',1,0),(45,'13DE395','CARRO-TANQUE\r\n',1,0),(46,'10BC001','COURRIER\r\n',1,0),(47,'13BP122','DOBLO\r\n',1,0),(48,'14BP178','DOBLO\r\n',1,0),(49,'14BP374','DOBLO\r\n',1,0),(50,'14BP460','DOBLO\r\n',1,0),(51,'09BP102','DOBLÒ\r\n',1,0),(52,'11BP020','DOBLÔ\r\n',1,0),(53,'10DP130','DUCATO\r\n',1,0),(54,'19BP065','ETIOS\r\n',1,0),(55,'10BP319','FIESTA\r\n',1,0),(56,'10BP224','FIESTA\r\n',1,0),(57,'14BP299','FLUENCE\r\n',1,0),(58,'19BE263','FURGÃO LEVE\r\n',1,0),(59,'09DC197','FURGÃO LEVE\r\n',1,0),(60,'12BC007','FIORINO\r\n',0,0),(61,'12BC021','FIORINO\r\n',1,0),(62,'10BP014','KOMBI\r\n',1,0),(63,'14DP373','L 200\r\n',1,0),(64,'08DP288','L200\r\n',1,0),(65,'07DP017','L200\r\n',1,0),(66,'09DP155','L200\r\n',1,0),(67,'20DP062','L200\r\n',1,0),(68,'20DP063','L200\r\n',1,0),(69,'20DP064','L200\r\n',1,0),(70,'20DP065','L200\r\n',1,0),(71,'20DP180	','L200',1,0),(72,'20DP181	','L200',1,0),(73,'20DP182	','L200',1,0),(74,'20DP199	','L200',1,0),(75,'20DP200	','L200',1,0),(76,'20DP201	','L200',1,0),(77,'12BP089	','LINEA',1,0),(78,'12DP093	','MICROÔNIBUS',1,0),(79,'08DP525	','ÔNIBUS',1,0),(80,'19DP118	','ÔNIBUS',1,0),(81,'10BP426	','PALIO',1,0),(82,'12BP599	','PALIO',1,0),(83,'12BP010	','UNO ',1,0),(84,'12BP090	','UNO ',1,0),(85,'08DP222	','VAN',1,0),(86,'08DP435	','VAN',1,0),(87,'PALIO','12BP218',1,0),(88,'10DP126','MICROÔNIBUS\r\n',1,1);
/*!40000 ALTER TABLE `viatura` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-02-23  9:36:30
