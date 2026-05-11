/*
 Navicat Premium Data Transfer

 Source Server         : localhost_3306
 Source Server Type    : MySQL
 Source Server Version : 50726
 Source Host           : localhost:3306
 Source Schema         : bishe2025

 Target Server Type    : MySQL
 Target Server Version : 50726
 File Encoding         : 65001

 Date: 14/04/2025 19:11:36
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for normal_data
-- ----------------------------
DROP TABLE IF EXISTS `normal_data`;
CREATE TABLE `normal_data`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `predict_host` varchar(20) CHARACTER SET utf8 COLLATE utf8_unicode_ci NULL DEFAULT NULL,
  `prediction` varchar(45) CHARACTER SET utf8 COLLATE utf8_unicode_ci NULL DEFAULT NULL,
  `src_ip` varchar(45) CHARACTER SET utf8 COLLATE utf8_unicode_ci NULL DEFAULT NULL,
  `dst_ip` varchar(45) CHARACTER SET utf8 COLLATE utf8_unicode_ci NULL DEFAULT NULL,
  `capture_time` datetime(0) NULL DEFAULT NULL,
  `url` text CHARACTER SET utf8 COLLATE utf8_unicode_ci NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 452 CHARACTER SET = utf8 COLLATE = utf8_unicode_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of normal_data
-- ----------------------------
INSERT INTO `normal_data` VALUES (1, 'computer2', '0.00245253', '192.168.38.130', '192.168.38.1', '2025-04-14 18:42:25', '/pikachu/vul/sqli/sqli_blind_b.php?name=s&submit=%E6%9F%A5%E8%AF%A2');
INSERT INTO `normal_data` VALUES (2, 'computer3', '0.00245253', '192.168.38.130', '192.168.38.1', '2025-04-14 18:42:30', '/pikachu/vul/sqli/sqli_blind_b.php?name=s&submit=%E6%9F%A5%E8%AF%A2');
INSERT INTO `normal_data` VALUES (3, 'computer1', '0.0053131985', '192.168.38.130', '192.168.38.1', '2025-04-14 18:42:31', '/pikachu/vul/sqli/sqli_blind_b.php?name=3170&submit=%E6%9F%A5%E8%AF%A2');
INSERT INTO `normal_data` VALUES (4, 'computer2', '0.382653', '192.168.38.130', '192.168.38.1', '2025-04-14 18:42:32', '/pikachu/vul/sqli/sqli_blind_b.php?name=s%29...%2C%29%29%22%27.&submit=%E6%9F%A5%E8%AF%A2');
INSERT INTO `normal_data` VALUES (5, 'computer2', '0.470465', '192.168.38.130', '192.168.38.1', '2025-04-14 18:42:38', '/pikachu/vul/sqli/sqli_blind_b.php?name=s%20AND%202747%3D2293&submit=%E6%9F%A5%E8%AF%A2');
INSERT INTO `normal_data` VALUES (6, 'computer3', '0.38910165', '192.168.38.130', '192.168.38.1', '2025-04-14 18:42:54', '');
INSERT INTO `normal_data` VALUES (7, 'computer3', '0.0010280615', '192.168.38.130', '192.168.38.1', '2025-04-14 18:43:07', '/pikachu/vul/sqli/sqli_blind_b.php?name=s&submit=6109');
INSERT INTO `normal_data` VALUES (8, 'computer2', '0.00245253', '192.168.38.130', '192.168.38.1', '2025-04-14 18:43:18', '/pikachu/vul/sqli/sqli_blind_b.php?name=s&submit=%E6%9F%A5%E8%AF%A2');
INSERT INTO `normal_data` VALUES (9, 'computer3', '0.00245253', '192.168.38.130', '192.168.38.1', '2025-04-14 18:44:11', '/pikachu/vul/sqli/sqli_blind_b.php?name=s&submit=%E6%9F%A5%E8%AF%A2');
INSERT INTO `normal_data` VALUES (10, 'computer1', '0.00245253', '192.168.38.130', '192.168.38.1', '2025-04-14 18:45:17', '/pikachu/vul/sqli/sqli_blind_b.php?name=s&submit=%E6%9F%A5%E8%AF%A2');
INSERT INTO `normal_data` VALUES (11, 'computer3', '0.00245253', '192.168.38.130', '192.168.38.1', '2025-04-14 18:45:28', '/pikachu/vul/sqli/sqli_blind_b.php?name=s&submit=%E6%9F%A5%E8%AF%A2');
INSERT INTO `normal_data` VALUES (12, 'computer3', '0.00245253', '192.168.38.130', '192.168.38.1', '2025-04-14 18:47:06', '/pikachu/vul/sqli/sqli_blind_t.php?name=s&submit=%E6%9F%A5%E8%AF%A2');
INSERT INTO `normal_data` VALUES (13, 'computer3', '0.00245253', '192.168.38.130', '192.168.38.1', '2025-04-14 18:47:08', '/pikachu/vul/sqli/sqli_blind_t.php?name=s&submit=%E6%9F%A5%E8%AF%A2');
INSERT INTO `normal_data` VALUES (14, 'computer3', '0.0053131985', '192.168.38.130', '192.168.38.1', '2025-04-14 18:47:09', '/pikachu/vul/sqli/sqli_blind_t.php?name=7329&submit=%E6%9F%A5%E8%AF%A2');
INSERT INTO `normal_data` VALUES (15, 'computer3', '0.470465', '192.168.38.130', '192.168.38.1', '2025-04-14 18:47:17', '/pikachu/vul/sqli/sqli_blind_t.php?name=s%20AND%207397%3D2043&submit=%E6%9F%A5%E8%AF%A2');
INSERT INTO `normal_data` VALUES (16, 'computer2', '0.38910165', '192.168.38.130', '192.168.38.1', '2025-04-14 18:47:40', '');
INSERT INTO `normal_data` VALUES (17, 'computer3', '0.00245253', '192.168.38.130', '192.168.38.1', '2025-04-14 18:48:34', '/pikachu/vul/sqli/sqli_blind_t.php?name=s&submit=%E6%9F%A5%E8%AF%A2');
INSERT INTO `normal_data` VALUES (18, 'computer2', '0.00245253', '192.168.38.130', '192.168.38.1', '2025-04-14 18:48:35', '/pikachu/vul/sqli/sqli_blind_t.php?name=s&submit=%E6%9F%A5%E8%AF%A2');
INSERT INTO `normal_data` VALUES (19, 'computer2', '0.00245253', '192.168.38.130', '192.168.38.1', '2025-04-14 18:48:37', '/pikachu/vul/sqli/sqli_blind_t.php?name=s&submit=%E6%9F%A5%E8%AF%A2');
INSERT INTO `normal_data` VALUES (20, 'computer3', '0.00245253', '192.168.38.130', '192.168.38.1', '2025-04-14 18:48:38', '/pikachu/vul/sqli/sqli_blind_t.php?name=s&submit=%E6%9F%A5%E8%AF%A2');
INSERT INTO `normal_data` VALUES (21, 'computer2', '0.00245253', '192.168.38.130', '192.168.38.1', '2025-04-14 18:48:39', '/pikachu/vul/sqli/sqli_blind_t.php?name=s&submit=%E6%9F%A5%E8%AF%A2');
INSERT INTO `normal_data` VALUES (22, 'computer1', '0.00245253', '192.168.38.130', '192.168.38.1', '2025-04-14 18:48:40', '/pikachu/vul/sqli/sqli_blind_t.php?name=s&submit=%E6%9F%A5%E8%AF%A2');
INSERT INTO `normal_data` VALUES (23, 'computer2', '0.00245253', '192.168.38.130', '192.168.38.1', '2025-04-14 18:48:41', '/pikachu/vul/sqli/sqli_blind_t.php?name=s&submit=%E6%9F%A5%E8%AF%A2');
INSERT INTO `normal_data` VALUES (24, 'computer3', '0.00245253', '192.168.38.130', '192.168.38.1', '2025-04-14 18:48:42', '/pikachu/vul/sqli/sqli_blind_t.php?name=s&submit=%E6%9F%A5%E8%AF%A2');
INSERT INTO `normal_data` VALUES (25, 'computer3', '0.00245253', '192.168.38.130', '192.168.38.1', '2025-04-14 18:48:43', '/pikachu/vul/sqli/sqli_blind_t.php?name=s&submit=%E6%9F%A5%E8%AF%A2');
INSERT INTO `normal_data` VALUES (26, 'computer3', '0.00245253', '192.168.38.130', '192.168.38.1', '2025-04-14 18:48:44', '/pikachu/vul/sqli/sqli_blind_t.php?name=s&submit=%E6%9F%A5%E8%AF%A2');
INSERT INTO `normal_data` VALUES (27, 'computer2', '0.00245253', '192.168.38.130', '192.168.38.1', '2025-04-14 18:48:44', '/pikachu/vul/sqli/sqli_blind_t.php?name=s&submit=%E6%9F%A5%E8%AF%A2');
INSERT INTO `normal_data` VALUES (28, 'computer1', '0.00245253', '192.168.38.130', '192.168.38.1', '2025-04-14 18:48:44', '/pikachu/vul/sqli/sqli_blind_t.php?name=s&submit=%E6%9F%A5%E8%AF%A2');
INSERT INTO `normal_data` VALUES (29, 'computer3', '0.00245253', '192.168.38.130', '192.168.38.1', '2025-04-14 18:48:44', '/pikachu/vul/sqli/sqli_blind_t.php?name=s&submit=%E6%9F%A5%E8%AF%A2');
INSERT INTO `normal_data` VALUES (30, 'computer2', '0.00245253', '192.168.38.130', '192.168.38.1', '2025-04-14 18:48:45', '/pikachu/vul/sqli/sqli_blind_t.php?name=s&submit=%E6%9F%A5%E8%AF%A2');
INSERT INTO `normal_data` VALUES (31, 'computer1', '0.00245253', '192.168.38.130', '192.168.38.1', '2025-04-14 18:48:45', '/pikachu/vul/sqli/sqli_blind_t.php?name=s&submit=%E6%9F%A5%E8%AF%A2');
INSERT INTO `normal_data` VALUES (32, 'computer3', '0.00245253', '192.168.38.130', '192.168.38.1', '2025-04-14 18:48:44', '/pikachu/vul/sqli/sqli_blind_t.php?name=s&submit=%E6%9F%A5%E8%AF%A2');
INSERT INTO `normal_data` VALUES (33, 'computer1', '0.00245253', '192.168.38.130', '192.168.38.1', '2025-04-14 18:48:45', '/pikachu/vul/sqli/sqli_blind_t.php?name=s&submit=%E6%9F%A5%E8%AF%A2');
INSERT INTO `normal_data` VALUES (34, 'computer3', '0.00245253', '192.168.38.130', '192.168.38.1', '2025-04-14 18:48:44', '/pikachu/vul/sqli/sqli_blind_t.php?name=s&submit=%E6%9F%A5%E8%AF%A2');
INSERT INTO `normal_data` VALUES (35, 'computer1', '0.00245253', '192.168.38.130', '192.168.38.1', '2025-04-14 18:48:45', '/pikachu/vul/sqli/sqli_blind_t.php?name=s&submit=%E6%9F%A5%E8%AF%A2');
INSERT INTO `normal_data` VALUES (36, 'computer3', '0.00245253', '192.168.38.130', '192.168.38.1', '2025-04-14 18:48:45', '/pikachu/vul/sqli/sqli_blind_t.php?name=s&submit=%E6%9F%A5%E8%AF%A2');
INSERT INTO `normal_data` VALUES (37, 'computer1', '0.00245253', '192.168.38.130', '192.168.38.1', '2025-04-14 18:48:45', '/pikachu/vul/sqli/sqli_blind_t.php?name=s&submit=%E6%9F%A5%E8%AF%A2');
INSERT INTO `normal_data` VALUES (38, 'computer3', '0.00245253', '192.168.38.130', '192.168.38.1', '2025-04-14 18:48:45', '/pikachu/vul/sqli/sqli_blind_t.php?name=s&submit=%E6%9F%A5%E8%AF%A2');
INSERT INTO `normal_data` VALUES (39, 'computer1', '0.00245253', '192.168.38.130', '192.168.38.1', '2025-04-14 18:48:45', '/pikachu/vul/sqli/sqli_blind_t.php?name=s&submit=%E6%9F%A5%E8%AF%A2');
INSERT INTO `normal_data` VALUES (40, 'computer3', '0.00245253', '192.168.38.130', '192.168.38.1', '2025-04-14 18:48:45', '/pikachu/vul/sqli/sqli_blind_t.php?name=s&submit=%E6%9F%A5%E8%AF%A2');
INSERT INTO `normal_data` VALUES (41, 'computer1', '0.00245253', '192.168.38.130', '192.168.38.1', '2025-04-14 18:48:45', '/pikachu/vul/sqli/sqli_blind_t.php?name=s&submit=%E6%9F%A5%E8%AF%A2');
INSERT INTO `normal_data` VALUES (42, 'computer3', '0.00245253', '192.168.38.130', '192.168.38.1', '2025-04-14 18:48:45', '/pikachu/vul/sqli/sqli_blind_t.php?name=s&submit=%E6%9F%A5%E8%AF%A2');
INSERT INTO `normal_data` VALUES (43, 'computer1', '0.00245253', '192.168.38.130', '192.168.38.1', '2025-04-14 18:48:45', '/pikachu/vul/sqli/sqli_blind_t.php?name=s&submit=%E6%9F%A5%E8%AF%A2');
INSERT INTO `normal_data` VALUES (44, 'computer3', '0.00245253', '192.168.38.130', '192.168.38.1', '2025-04-14 18:48:45', '/pikachu/vul/sqli/sqli_blind_t.php?name=s&submit=%E6%9F%A5%E8%AF%A2');
INSERT INTO `normal_data` VALUES (45, 'computer1', '0.00245253', '192.168.38.130', '192.168.38.1', '2025-04-14 18:48:45', '/pikachu/vul/sqli/sqli_blind_t.php?name=s&submit=%E6%9F%A5%E8%AF%A2');
INSERT INTO `normal_data` VALUES (46, 'computer3', '0.00245253', '192.168.38.130', '192.168.38.1', '2025-04-14 18:48:45', '/pikachu/vul/sqli/sqli_blind_t.php?name=s&submit=%E6%9F%A5%E8%AF%A2');
INSERT INTO `normal_data` VALUES (47, 'computer1', '0.00245253', '192.168.38.130', '192.168.38.1', '2025-04-14 18:48:45', '/pikachu/vul/sqli/sqli_blind_t.php?name=s&submit=%E6%9F%A5%E8%AF%A2');
INSERT INTO `normal_data` VALUES (48, 'computer2', '0.00245253', '192.168.38.130', '192.168.38.1', '2025-04-14 18:51:48', '/pikachu/vul/sqli/sqli_str.php?name=s&submit=%E6%9F%A5%E8%AF%A2');
INSERT INTO `normal_data` VALUES (49, 'computer1', '0.00245253', '192.168.38.130', '192.168.38.1', '2025-04-14 18:51:50', '/pikachu/vul/sqli/sqli_str.php?name=s&submit=%E6%9F%A5%E8%AF%A2');
INSERT INTO `normal_data` VALUES (50, 'computer1', '0.0053131985', '192.168.38.130', '192.168.38.1', '2025-04-14 18:51:51', '/pikachu/vul/sqli/sqli_str.php?name=6477&submit=%E6%9F%A5%E8%AF%A2');
INSERT INTO `normal_data` VALUES (51, 'computer2', '0.470465', '192.168.38.130', '192.168.38.1', '2025-04-14 18:51:58', '/pikachu/vul/sqli/sqli_str.php?name=s%20AND%206238%3D6238&submit=%E6%9F%A5%E8%AF%A2');
INSERT INTO `normal_data` VALUES (52, 'computer1', '0.470465', '192.168.38.130', '192.168.38.1', '2025-04-14 18:51:58', '/pikachu/vul/sqli/sqli_str.php?name=s%20AND%201322%3D5527&submit=%E6%9F%A5%E8%AF%A2');
INSERT INTO `normal_data` VALUES (53, 'computer2', '0.02301149', '192.168.38.130', '192.168.38.1', '2025-04-14 18:52:01', '/pikachu/vul/sqli/sqli_str.php?name=-8283&submit=%E6%9F%A5%E8%AF%A2');
INSERT INTO `normal_data` VALUES (54, 'computer3', '0.38910165', '192.168.38.130', '192.168.38.1', '2025-04-14 18:52:19', '');
INSERT INTO `normal_data` VALUES (55, 'computer1', '0.00245253', '192.168.38.130', '192.168.38.1', '2025-04-14 18:52:41', '/pikachu/vul/sqli/sqli_search.php?name=s&submit=%E6%9F%A5%E8%AF%A2');
INSERT INTO `normal_data` VALUES (56, 'computer1', '0.00245253', '192.168.38.130', '192.168.38.1', '2025-04-14 18:52:43', '/pikachu/vul/sqli/sqli_search.php?name=s&submit=%E6%9F%A5%E8%AF%A2');
INSERT INTO `normal_data` VALUES (57, 'computer3', '0.0053131985', '192.168.38.130', '192.168.38.1', '2025-04-14 18:52:45', '/pikachu/vul/sqli/sqli_search.php?name=8757&submit=%E6%9F%A5%E8%AF%A2');
INSERT INTO `normal_data` VALUES (58, 'computer3', '0.470465', '192.168.38.130', '192.168.38.1', '2025-04-14 18:52:51', '/pikachu/vul/sqli/sqli_search.php?name=s%20AND%205481%3D4558&submit=%E6%9F%A5%E8%AF%A2');
INSERT INTO `normal_data` VALUES (59, 'computer2', '0.470465', '192.168.38.130', '192.168.38.1', '2025-04-14 18:52:51', '/pikachu/vul/sqli/sqli_search.php?name=s%20AND%202035%3D2035&submit=%E6%9F%A5%E8%AF%A2');
INSERT INTO `normal_data` VALUES (60, 'computer3', '0.02301149', '192.168.38.130', '192.168.38.1', '2025-04-14 18:52:55', '/pikachu/vul/sqli/sqli_search.php?name=-1740&submit=%E6%9F%A5%E8%AF%A2');
INSERT INTO `normal_data` VALUES (61, 'computer2', '0.30613232', '192.168.38.130', '192.168.38.1', '2025-04-14 18:53:11', '/pikachu/vul/sqli/sqli_search.php?name=-2023%27%20HOiAVEeJwT--%20EhjD&submit=%E6%9F%A5%E8%AF%A2');
INSERT INTO `normal_data` VALUES (62, 'computer3', '0.26124394', '192.168.38.130', '192.168.38.1', '2025-04-14 18:53:22', '/pikachu/vul/sqli/sqli_search.php?name=-1336%27%20HOiAVEeJwT--%20vcPA&submit=%E6%9F%A5%E8%AF%A2');
INSERT INTO `normal_data` VALUES (63, 'computer1', '0.38910165', '192.168.38.130', '192.168.38.1', '2025-04-14 18:53:39', '');
INSERT INTO `normal_data` VALUES (64, 'computer1', '0.00245253', '192.168.38.130', '192.168.38.1', '2025-04-14 18:53:58', '/pikachu/vul/sqli/sqli_x.php?name=s&submit=%E6%9F%A5%E8%AF%A2');
INSERT INTO `normal_data` VALUES (65, 'computer2', '0.00245253', '192.168.38.130', '192.168.38.1', '2025-04-14 18:54:01', '/pikachu/vul/sqli/sqli_x.php?name=s&submit=%E6%9F%A5%E8%AF%A2');
INSERT INTO `normal_data` VALUES (66, 'computer2', '0.0053131985', '192.168.38.130', '192.168.38.1', '2025-04-14 18:54:02', '/pikachu/vul/sqli/sqli_x.php?name=3529&submit=%E6%9F%A5%E8%AF%A2');
INSERT INTO `normal_data` VALUES (67, 'computer2', '0.470465', '192.168.38.130', '192.168.38.1', '2025-04-14 18:54:10', '/pikachu/vul/sqli/sqli_x.php?name=s%20AND%203806%3D9390&submit=%E6%9F%A5%E8%AF%A2');
INSERT INTO `normal_data` VALUES (68, 'computer2', '0.470465', '192.168.38.130', '192.168.38.1', '2025-04-14 18:54:10', '/pikachu/vul/sqli/sqli_x.php?name=s%20AND%207346%3D7346&submit=%E6%9F%A5%E8%AF%A2');
INSERT INTO `normal_data` VALUES (69, 'computer3', '0.02301149', '192.168.38.130', '192.168.38.1', '2025-04-14 18:54:13', '/pikachu/vul/sqli/sqli_x.php?name=-3859&submit=%E6%9F%A5%E8%AF%A2');
INSERT INTO `normal_data` VALUES (70, 'computer2', '0.38910165', '192.168.38.130', '192.168.38.1', '2025-04-14 18:54:30', '');
INSERT INTO `normal_data` VALUES (71, 'computer2', '0.013786135', '192.168.38.130', '192.168.38.1', '2025-04-14 18:55:09', '/pikachu/vul/sqli/sqli_iu/sqli_login.php?username=s&password=s&submit=Login');
INSERT INTO `normal_data` VALUES (72, 'computer2', '0.013786135', '192.168.38.130', '192.168.38.1', '2025-04-14 18:55:12', '/pikachu/vul/sqli/sqli_iu/sqli_login.php?username=s&password=s&submit=Login');
INSERT INTO `normal_data` VALUES (73, 'computer2', '0.026520219', '192.168.38.130', '192.168.38.1', '2025-04-14 18:55:13', '/pikachu/vul/sqli/sqli_iu/sqli_login.php?username=1937&password=s&submit=Login');
INSERT INTO `normal_data` VALUES (74, 'computer3', '0.0102041755', '192.168.38.130', '192.168.38.1', '2025-04-14 18:55:23', '/pikachu/vul/sqli/sqli_iu/sqli_login.php?username=s&password=1854&submit=Login');
INSERT INTO `normal_data` VALUES (75, 'computer1', '0.24834925', '192.168.38.130', '192.168.38.1', '2025-04-14 18:55:23', '/pikachu/vul/sqli/sqli_iu/sqli_login.php?username=s&password=s%20AND%206967%3D2592&submit=Login');
INSERT INTO `normal_data` VALUES (76, 'computer3', '0.0024553488', '192.168.38.130', '192.168.38.1', '2025-04-14 18:55:26', '/pikachu/vul/sqli/sqli_iu/sqli_login.php?username=s&password=s&submit=2707');
INSERT INTO `normal_data` VALUES (77, 'computer3', '0.36249682', '192.168.38.130', '192.168.38.1', '2025-04-14 18:55:27', '/pikachu/vul/sqli/sqli_iu/sqli_login.php?username=s&password=s&submit=Login%20AND%201832%3D2409');

SET FOREIGN_KEY_CHECKS = 1;
