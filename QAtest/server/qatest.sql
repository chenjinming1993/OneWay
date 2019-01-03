/*
Navicat MySQL Data Transfer

Source Server         : localhost_3306
Source Server Version : 50719
Source Host           : localhost:3306
Source Database       : qatest

Target Server Type    : MYSQL
Target Server Version : 50719
File Encoding         : 65001

Date: 2019-01-03 15:49:27
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for architecture
-- ----------------------------
DROP TABLE IF EXISTS `architecture`;
CREATE TABLE `architecture` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` text NOT NULL,
  `area` text,
  `level` int(11) DEFAULT NULL,
  `cost_stone` int(11) DEFAULT NULL,
  `cost_metal` int(11) DEFAULT NULL,
  `cost_water` int(11) DEFAULT NULL,
  `cost_plastic` int(11) DEFAULT NULL,
  `cost_nuclear` int(11) DEFAULT NULL,
  `cost_tech` int(11) DEFAULT NULL,
  `cost_time` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of architecture
-- ----------------------------
INSERT INTO `architecture` VALUES ('0', '基地', '5*5', '1', '100', '200', '50', '110', '0', '0', '180');
INSERT INTO `architecture` VALUES ('1', '道路', '1*1', '1', '100', '200', '50', '120', '0', '0', '0');
INSERT INTO `architecture` VALUES ('2', '住宅', '2*2', '1', '100', '200', '50', '130', '0', '0', '60');
INSERT INTO `architecture` VALUES ('3', '冶炼厂', '3*3', '1', '100', '200', '50', '140', '0', '0', '120');
INSERT INTO `architecture` VALUES ('4', '氧气工厂', '2*2', '1', '100', '200', '50', '150', '60', '0', '60');
INSERT INTO `architecture` VALUES ('5', '兵营', '3*3', '1', '100', '200', '50', '160', '0', '70', '360');

-- ----------------------------
-- Table structure for test
-- ----------------------------
DROP TABLE IF EXISTS `test`;
CREATE TABLE `test` (
  `id` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of test
-- ----------------------------
