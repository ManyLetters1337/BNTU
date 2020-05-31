-- MySQL dump 10.13  Distrib 5.7.30, for Linux (x86_64)
--
-- Host: localhost    Database: bntu
-- ------------------------------------------------------
-- Server version	5.7.30-0ubuntu0.18.04.1

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
-- Table structure for table `categories`
--

DROP TABLE IF EXISTS `categories`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `categories` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `uuid` varchar(36) NOT NULL,
  `name` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uuid` (`uuid`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `categories`
--

LOCK TABLES `categories` WRITE;
/*!40000 ALTER TABLE `categories` DISABLE KEYS */;
INSERT INTO `categories` VALUES (1,'8e0e050c-06e2-11ea-a36e-74d435ecfdb9','Худи'),(2,'8e0e020c-06e2-11ea-a36e-74d435ecfdb9','Ручки'),(3,'120a6a60-a0eb-11ea-a61d-d0c5d3fd4421','Майка'),(4,'4918f98e-a0ed-11ea-a61d-d0c5d3fd4421','Ручка'),(5,'4f764386-a0ed-11ea-a61d-d0c5d3fd4421','Рюкзак'),(6,'51136a52-a0ed-11ea-a61d-d0c5d3fd4421','Пенал'),(7,'5dc053c8-a0ed-11ea-a61d-d0c5d3fd4421','Бомбер'),(8,'653038a8-a0ed-11ea-a61d-d0c5d3fd4421','Аксессуары '),(9,'aee7b19a-a0ef-11ea-a61d-d0c5d3fd4421','Кепки'),(10,'75a3f438-a0f0-11ea-a61d-d0c5d3fd4421','Свитшот');
/*!40000 ALTER TABLE `categories` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `comments`
--

DROP TABLE IF EXISTS `comments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `comments` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `uuid` varchar(36) NOT NULL,
  `user_id` int(10) unsigned NOT NULL,
  `product_id` int(10) unsigned NOT NULL,
  `text` varchar(500) NOT NULL,
  `rate` int(11) NOT NULL DEFAULT '0',
  `create_date` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uuid` (`uuid`),
  KEY `fk_comment_user` (`user_id`),
  KEY `fk_comment_product` (`product_id`),
  CONSTRAINT `fk_comment_product` FOREIGN KEY (`product_id`) REFERENCES `products` (`id`),
  CONSTRAINT `fk_comment_user` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `comments`
--

LOCK TABLES `comments` WRITE;
/*!40000 ALTER TABLE `comments` DISABLE KEYS */;
INSERT INTO `comments` VALUES (1,'25429f84-a0ec-11ea-a61d-d0c5d3fd4421',1,1,'Это мой комментарий на этот Батник',0,'2020-05-28 17:04:15'),(2,'a1e4a2a8-a281-11ea-ac7e-d0c5d3fd4421',1,1,'Это мой комментарий на этот Батник',0,'2020-05-30 17:15:28');
/*!40000 ALTER TABLE `comments` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `groups`
--

DROP TABLE IF EXISTS `groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `groups` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `uuid` varchar(36) NOT NULL,
  `number` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uuid` (`uuid`),
  UNIQUE KEY `number` (`number`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `groups`
--

LOCK TABLES `groups` WRITE;
/*!40000 ALTER TABLE `groups` DISABLE KEYS */;
INSERT INTO `groups` VALUES (1,'8e0e020c-06e2-11ea-a36e-74d435ecfdb9','10701216'),(2,'8e0e020c-06e2-11ea-a32e-74d435ecfdb9','10701116');
/*!40000 ALTER TABLE `groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `orders`
--

DROP TABLE IF EXISTS `orders`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `orders` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `uuid` varchar(36) NOT NULL,
  `user_id` int(10) unsigned NOT NULL,
  `country` varchar(50) DEFAULT NULL,
  `city` varchar(50) DEFAULT NULL,
  `address` varchar(100) DEFAULT NULL,
  `post_index` varchar(50) DEFAULT NULL,
  `created_date` datetime DEFAULT NULL,
  `status` varchar(50) NOT NULL DEFAULT 'Active',
  PRIMARY KEY (`id`),
  UNIQUE KEY `uuid` (`uuid`),
  KEY `fk_order_user` (`user_id`),
  CONSTRAINT `fk_order_user` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `orders`
--

LOCK TABLES `orders` WRITE;
/*!40000 ALTER TABLE `orders` DISABLE KEYS */;
INSERT INTO `orders` VALUES (1,'bc83107b-a0e9-11ea-a61d-d0c5d3fd4421',1,'Беларусь','Минск','Плеханова','1231451','2020-05-28 17:56:35','Pending'),(2,'6e00f7f0-a0f3-11ea-a61d-d0c5d3fd4421',1,'Беларусь','Минск','Плеханова','12412','2020-05-28 18:29:58','Pending'),(3,'190e00a8-a0f8-11ea-a61d-d0c5d3fd4421',1,'Беларусь','Минск','Плеханова','2314421','2020-05-28 23:59:04','Pending'),(4,'1ed2ed90-a126-11ea-890b-d0c5d3fd4421',1,NULL,NULL,NULL,NULL,NULL,'Active');
/*!40000 ALTER TABLE `orders` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `orders_products`
--

DROP TABLE IF EXISTS `orders_products`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `orders_products` (
  `order_id` int(10) unsigned DEFAULT NULL,
  `product_id` int(10) unsigned DEFAULT NULL,
  KEY `fk_order_products_id` (`order_id`),
  KEY `fk_product_orders` (`product_id`),
  CONSTRAINT `fk_order_products_id` FOREIGN KEY (`order_id`) REFERENCES `orders` (`id`) ON DELETE CASCADE,
  CONSTRAINT `fk_product_orders` FOREIGN KEY (`product_id`) REFERENCES `products` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `orders_products`
--

LOCK TABLES `orders_products` WRITE;
/*!40000 ALTER TABLE `orders_products` DISABLE KEYS */;
INSERT INTO `orders_products` VALUES (1,1),(2,3),(2,5),(3,8),(3,4),(3,9),(3,7),(3,6),(4,2),(4,5),(4,7);
/*!40000 ALTER TABLE `orders_products` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `products`
--

DROP TABLE IF EXISTS `products`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `products` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `uuid` varchar(36) NOT NULL,
  `name` varchar(100) NOT NULL,
  `image` varchar(300) NOT NULL DEFAULT 'https://res.cloudinary.com/manyletters/image/upload/v1589568700/015e96e6a653950ded808f5704c0727f.jpg',
  `category_id` int(10) unsigned NOT NULL,
  `price` decimal(10,0) unsigned NOT NULL,
  `description` varchar(100) NOT NULL,
  `create_date` datetime NOT NULL,
  `update_date` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uuid` (`uuid`),
  KEY `fk_product_category` (`category_id`),
  CONSTRAINT `fk_product_category` FOREIGN KEY (`category_id`) REFERENCES `categories` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `products`
--

LOCK TABLES `products` WRITE;
/*!40000 ALTER TABLE `products` DISABLE KEYS */;
INSERT INTO `products` VALUES (1,'c1f926d8-a0ea-11ea-a61d-d0c5d3fd4421',' Батник','http://127.0.0.1:5000/_uploads/photos/batnik_whit.jpg',1,1000,'Удобный и стильный батник с логотипом БНТУ. Цвет: Белый','2020-05-28 16:54:33','2020-05-28 16:54:33'),(2,'d92efb16-a0ea-11ea-a61d-d0c5d3fd4421','Батник','http://127.0.0.1:5000/_uploads/photos/batnik.jpg',1,1000,'Удобный и стильный батник с логотипом БНТУ. Цвет: Зелёный','2020-05-28 16:55:11','2020-05-28 16:55:11'),(3,'0b094588-a0eb-11ea-a61d-d0c5d3fd4421','Бомбер','http://127.0.0.1:5000/_uploads/photos/bomber.jpg',1,900,'Стиль Американского студента, только для тебя. Удобно и стильно. Цвет: Белый и Зелёный','2020-05-28 16:56:35','2020-05-28 16:56:35'),(4,'2f12ad98-a0eb-11ea-a61d-d0c5d3fd4421','Поло','http://127.0.0.1:5000/_uploads/photos/polo.jpg',3,700,'Белая майка поло. То что нужно жарким летом во время сессии.','2020-05-28 16:57:36','2020-05-28 16:57:36'),(5,'ce3fa9aa-a0ed-11ea-a61d-d0c5d3fd4421','Ручки','http://127.0.0.1:5000/_uploads/photos/another_pancil_2.jpg',4,70,'Ручки с символикой БНТУ. Можешь приходить в другой раз с нашей ручкой.','2020-05-28 17:16:22','2020-05-28 17:16:22'),(6,'f78d030c-a0ed-11ea-a61d-d0c5d3fd4421','Пенал','http://127.0.0.1:5000/_uploads/photos/another_penal_1.jpg',6,300,'Купи наш пинал, он всё равно будет пустым','2020-05-28 17:17:31','2020-05-28 17:17:31'),(7,'1aa01eb0-a0ee-11ea-a61d-d0c5d3fd4421','Рюкзак (Чёрный)','http://127.0.0.1:5000/_uploads/photos/backpack_black.jpg',1,1000,'Чёрный рюкзак с символикой БНТУ. Только для одной тетрадки.','2020-05-28 17:18:30','2020-05-28 17:18:30'),(8,'46aa7c4e-a0ee-11ea-a61d-d0c5d3fd4421','Рюкзак (Серый)','http://127.0.0.1:5000/_uploads/photos/backpack_gray.jpg',1,1100,'Серый рюкзак с символикой БНТУ. Такой же как чёрный, только серый','2020-05-28 17:19:44','2020-05-28 17:19:44'),(9,'7ccb8db8-a0ee-11ea-a61d-d0c5d3fd4421','Рюкзак (Зелёны)','http://127.0.0.1:5000/_uploads/photos/backpack_green.jpg',5,1000,'Зелёный рюкзак с символикой БНТУ. Купи сразу 3 на все случаи жизни','2020-05-28 17:21:14','2020-05-28 17:21:14'),(10,'98cd6220-a0ee-11ea-a61d-d0c5d3fd4421','Батник (Серый)','http://127.0.0.1:5000/_uploads/photos/batnik_gray.jpg',1,1100,'Серый батник с символикой любимого университета. Купи себе и друзьям из БГУИР','2020-05-28 17:22:01','2020-05-28 17:22:01'),(11,'ba326668-a0ee-11ea-a61d-d0c5d3fd4421','Бомбер (Белый, Коричневый)','http://127.0.0.1:5000/_uploads/photos/bobmer_brown.jpg',7,1200,'По совету Дэдпула покупай коричневый','2020-05-28 17:22:57','2020-05-28 17:22:57'),(12,'dcf99d6a-a0ee-11ea-a61d-d0c5d3fd4421','Брелки','http://127.0.0.1:5000/_uploads/photos/brelki.jpg',8,70,'Обвесь рюкзак БНТУ, брелками БНТУ. ','2020-05-28 17:23:56','2020-05-28 17:23:56'),(13,'f093b3ce-a0ee-11ea-a61d-d0c5d3fd4421','Папки','http://127.0.0.1:5000/_uploads/photos/folder.jpg',6,150,'Папки с символикой БНТУ','2020-05-28 17:24:29','2020-05-28 17:24:29'),(14,'cc0fc4ba-a0ef-11ea-a61d-d0c5d3fd4421','Кепка (Чёрная)','http://127.0.0.1:5000/_uploads/photos/head_black.jpg',9,600,'Кепка с символикой БНТУ. Носи кепку, не будь идиотом','2020-05-28 17:30:37','2020-05-28 17:30:37'),(15,'e6c13c08-a0ef-11ea-a61d-d0c5d3fd4421','Кепка (Белый, Чёрный)','http://127.0.0.1:5000/_uploads/photos/head_black_white.jpg',9,600,'Кепка как у рэпера из твоего подъезда','2020-05-28 17:31:22','2020-05-28 17:31:22'),(16,'f82b8430-a0ef-11ea-a61d-d0c5d3fd4421','Кепка (Серая)','http://127.0.0.1:5000/_uploads/photos/head_gray.jpg',9,500,'Серая кепка с символикой БНТУ','2020-05-28 17:31:51','2020-05-28 17:31:51'),(17,'0480e892-a0f0-11ea-a61d-d0c5d3fd4421','Кепка (Зелёная)','http://127.0.0.1:5000/_uploads/photos/head_green.jpg',9,500,'Зелёная кепка с символикой БНТУ','2020-05-28 17:32:12','2020-05-28 17:32:12'),(18,'2cda4dce-a0f0-11ea-a61d-d0c5d3fd4421','Лента','http://127.0.0.1:5000/_uploads/photos/lenta.jpg',8,30,'Лента для твоего б','2020-05-28 17:33:19','2020-05-28 17:33:19'),(19,'439406fe-a0f0-11ea-a61d-d0c5d3fd4421','Подарочная ручка','http://127.0.0.1:5000/_uploads/photos/pancil_great.jpg',4,700,'Подарочная ручка с символикой БНТУ. Лучший обмен на Автомат','2020-05-28 17:33:57','2020-05-28 17:33:57'),(20,'52919298-a0f0-11ea-a61d-d0c5d3fd4421','Пенал','http://127.0.0.1:5000/_uploads/photos/penal.jpg',6,300,'Пенал с символикой БНТУ','2020-05-28 17:34:23','2020-05-28 17:34:23'),(21,'647d9510-a0f0-11ea-a61d-d0c5d3fd4421','Сумка (Серая)','http://127.0.0.1:5000/_uploads/photos/sumka_gray.jpg',5,800,'Серая как Гендольф','2020-05-28 17:34:53','2020-05-28 17:34:53'),(22,'8ab2cce6-a0f0-11ea-a61d-d0c5d3fd4421','Свитшот (Серый)','http://127.0.0.1:5000/_uploads/photos/switshot_gray.jpg',10,1200,'Серый свитшот с символикой БНТУ. Может переродится в белый','2020-05-28 17:35:57','2020-05-28 17:35:57'),(23,'a15040e6-a0f0-11ea-a61d-d0c5d3fd4421','Свитшот (Зелёный)','http://127.0.0.1:5000/_uploads/photos/switshot_green.jpg',10,1100,'Зелёный свитшот с символикой БНТУ. Можно лежать на траве.','2020-05-28 17:36:35','2020-05-28 17:36:35'),(24,'d945c8d6-a0f0-11ea-a61d-d0c5d3fd4421','Свитшот (Белый)','http://127.0.0.1:5000/_uploads/photos/switshot_white.jpg',10,1200,'Белый на пару дней','2020-05-28 17:38:09','2020-05-28 17:38:09'),(25,'e8a7cc3e-a0f0-11ea-a61d-d0c5d3fd4421','Значки','http://127.0.0.1:5000/_uploads/photos/znachki.jpg',8,100,'Подари другу из БГУИР. Может он тебе подарит такой же','2020-05-28 17:38:34','2020-05-28 17:38:34');
/*!40000 ALTER TABLE `products` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `products_tags`
--

DROP TABLE IF EXISTS `products_tags`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `products_tags` (
  `product_id` int(10) unsigned DEFAULT NULL,
  `tag_id` int(10) unsigned DEFAULT NULL,
  KEY `fk_product_tags_id` (`product_id`),
  KEY `fk_tag_products` (`tag_id`),
  CONSTRAINT `fk_product_tags_id` FOREIGN KEY (`product_id`) REFERENCES `products` (`id`) ON DELETE CASCADE,
  CONSTRAINT `fk_tag_products` FOREIGN KEY (`tag_id`) REFERENCES `tags` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `products_tags`
--

LOCK TABLES `products_tags` WRITE;
/*!40000 ALTER TABLE `products_tags` DISABLE KEYS */;
/*!40000 ALTER TABLE `products_tags` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `products_users`
--

DROP TABLE IF EXISTS `products_users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `products_users` (
  `product_id` int(10) unsigned DEFAULT NULL,
  `user_id` int(10) unsigned DEFAULT NULL,
  KEY `fk_product_users_id` (`product_id`),
  KEY `fk_user_products` (`user_id`),
  CONSTRAINT `fk_product_users_id` FOREIGN KEY (`product_id`) REFERENCES `products` (`id`) ON DELETE CASCADE,
  CONSTRAINT `fk_user_products` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `products_users`
--

LOCK TABLES `products_users` WRITE;
/*!40000 ALTER TABLE `products_users` DISABLE KEYS */;
/*!40000 ALTER TABLE `products_users` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `rates`
--

DROP TABLE IF EXISTS `rates`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `rates` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `product_id` int(10) unsigned NOT NULL,
  `rate` int(10) unsigned NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`),
  KEY `fk_rate_product_id` (`product_id`),
  CONSTRAINT `fk_rate_product_id` FOREIGN KEY (`product_id`) REFERENCES `products` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rates`
--

LOCK TABLES `rates` WRITE;
/*!40000 ALTER TABLE `rates` DISABLE KEYS */;
/*!40000 ALTER TABLE `rates` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `rates_users`
--

DROP TABLE IF EXISTS `rates_users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `rates_users` (
  `rate_id` int(10) unsigned DEFAULT NULL,
  `user_id` int(10) unsigned DEFAULT NULL,
  KEY `fk_rate_users_id` (`rate_id`),
  KEY `fk_user_rates` (`user_id`),
  CONSTRAINT `fk_rate_users_id` FOREIGN KEY (`rate_id`) REFERENCES `rates` (`id`) ON DELETE CASCADE,
  CONSTRAINT `fk_user_rates` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rates_users`
--

LOCK TABLES `rates_users` WRITE;
/*!40000 ALTER TABLE `rates_users` DISABLE KEYS */;
/*!40000 ALTER TABLE `rates_users` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tags`
--

DROP TABLE IF EXISTS `tags`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tags` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `uuid` varchar(36) NOT NULL,
  `name` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uuid` (`uuid`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tags`
--

LOCK TABLES `tags` WRITE;
/*!40000 ALTER TABLE `tags` DISABLE KEYS */;
INSERT INTO `tags` VALUES (1,'8e0e020c-06e2-11ea-a36e-84d435ecfdb9','BNTU2020'),(2,'8e0e020c-06e2-11ea-a36e-72d435ecfdb9','BNTUStyle');
/*!40000 ALTER TABLE `tags` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `uuid` varchar(36) NOT NULL,
  `first_name` varchar(100) NOT NULL,
  `last_name` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `image` varchar(300) NOT NULL DEFAULT 'https://res.cloudinary.com/manyletters/image/upload/v1589568700/015e96e6a653950ded808f5704c0727f.jpg',
  `group_id` int(10) unsigned NOT NULL,
  `student_number` varchar(50) NOT NULL,
  `password_hash` varchar(100) NOT NULL,
  `birthday_date` date DEFAULT NULL,
  `about` varchar(500) DEFAULT NULL,
  `role` varchar(30) NOT NULL DEFAULT 'user',
  PRIMARY KEY (`id`),
  UNIQUE KEY `uuid` (`uuid`),
  UNIQUE KEY `email` (`email`),
  KEY `fk_user_group` (`group_id`),
  CONSTRAINT `fk_user_group` FOREIGN KEY (`group_id`) REFERENCES `groups` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'bc83107a-a0e9-11ea-a61d-d0c5d3fd4421','Виталий','Счастный','VS20132013@gmail.com','https://res.cloudinary.com/manyletters/image/upload/v1589568700/015e96e6a653950ded808f5704c0727f.jpg',1,'1070121628','pbkdf2:sha256:150000$WNtgegbj$c5ac70f7cfc99340255b0691d3f74c8038af69d8cfc00b1206e16c9bcee0ff25',NULL,NULL,'admin');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-05-31 14:51:45
