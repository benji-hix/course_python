-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema schema_surveys
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `schema_surveys` ;

-- -----------------------------------------------------
-- Schema schema_surveys
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `schema_surveys` DEFAULT CHARACTER SET utf8 ;
USE `schema_surveys` ;

-- -----------------------------------------------------
-- Table `schema_surveys`.`surveys`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `schema_surveys`.`surveys` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NULL,
  `location` VARCHAR(45) NULL,
  `language` VARCHAR(45) NULL,
  `comment` VARCHAR(150) NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
