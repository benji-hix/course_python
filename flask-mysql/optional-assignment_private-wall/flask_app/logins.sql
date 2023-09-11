-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema schema_logins
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `schema_logins` ;

-- -----------------------------------------------------
-- Schema schema_logins
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `schema_logins` DEFAULT CHARACTER SET utf8 ;
USE `schema_logins` ;

-- -----------------------------------------------------
-- Table `schema_logins`.`logins`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `schema_logins`.`logins` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(45) NULL,
  `last_name` VARCHAR(45) NULL,
  `email` VARCHAR(60) NULL,
  `password` VARCHAR(100) NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `schema_logins`.`messages`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `schema_logins`.`messages` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `content` VARCHAR(200) NULL,
  `created_at` DATETIME NULL,
  `sender_id` INT NOT NULL,
  `receiver_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_messages_logins_idx` (`sender_id` ASC) VISIBLE,
  INDEX `fk_messages_logins1_idx` (`receiver_id` ASC) VISIBLE,
  CONSTRAINT `fk_messages_logins`
    FOREIGN KEY (`sender_id`)
    REFERENCES `schema_logins`.`logins` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_messages_logins1`
    FOREIGN KEY (`receiver_id`)
    REFERENCES `schema_logins`.`logins` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
