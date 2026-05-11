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

 Date: 14/04/2025 19:18:58
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
) ENGINE = InnoDB AUTO_INCREMENT = 90 CHARACTER SET = utf8 COLLATE = utf8_unicode_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of normal_data
-- ----------------------------
INSERT INTO `normal_data` VALUES (1, 'computer1', '0.38910165', '192.168.38.130', '192.168.38.1', '2025-04-14 19:15:05', '/pikachu/vul/sqli/sqli_id.php');
INSERT INTO `normal_data` VALUES (2, 'computer3', '0.38910165', '192.168.38.130', '192.168.38.1', '2025-04-14 19:15:05', '/favicon.ico');
INSERT INTO `normal_data` VALUES (3, 'computer2', '0.38910165', '192.168.38.130', '192.168.38.1', '2025-04-14 19:15:07', '/pikachu/vul/burteforce/bf_form.php');
INSERT INTO `normal_data` VALUES (4, 'computer1', '0.38910165', '192.168.38.130', '192.168.38.1', '2025-04-14 19:15:08', '/pikachu/vul/burteforce/burteforce.php');
INSERT INTO `normal_data` VALUES (5, 'computer3', '0.38910165', '192.168.38.130', '192.168.38.1', '2025-04-14 19:15:09', '/pikachu/vul/burteforce/bf_server.php');
INSERT INTO `normal_data` VALUES (6, 'computer3', '0.38910165', '192.168.38.130', '192.168.38.1', '2025-04-14 19:15:09', '/pikachu/inc/showvcode.php');
INSERT INTO `normal_data` VALUES (7, 'computer3', '0.38910165', '192.168.38.130', '192.168.38.1', '2025-04-14 19:15:09', '/pikachu/vul/burteforce/bf_client.php');
INSERT INTO `normal_data` VALUES (8, 'computer3', '0.38910165', '192.168.38.130', '192.168.38.1', '2025-04-14 19:15:10', '/pikachu/vul/burteforce/bf_token.php');
INSERT INTO `normal_data` VALUES (9, 'computer3', '0.38910165', '192.168.38.130', '192.168.38.1', '2025-04-14 19:15:22', '/pikachu/vul/burteforce/bf_form.php');
INSERT INTO `normal_data` VALUES (10, 'computer1', '0.38910165', '192.168.38.130', '192.168.38.1', '2025-04-14 19:15:22', '/pikachu/vul/burteforce/burteforce.php');
INSERT INTO `normal_data` VALUES (11, 'computer3', '0.38910165', '192.168.38.130', '192.168.38.1', '2025-04-14 19:15:23', '/pikachu/vul/burteforce/bf_client.php');
INSERT INTO `normal_data` VALUES (12, 'computer2', '0.38910165', '192.168.38.130', '192.168.38.1', '2025-04-14 19:15:23', '/pikachu/vul/burteforce/bf_server.php');
INSERT INTO `normal_data` VALUES (13, 'computer2', '0.38910165', '192.168.38.130', '192.168.38.1', '2025-04-14 19:15:23', '/pikachu/inc/showvcode.php');
INSERT INTO `normal_data` VALUES (14, 'computer2', '0.38910165', '192.168.38.130', '192.168.38.1', '2025-04-14 19:15:24', '/pikachu/vul/burteforce/bf_token.php');
INSERT INTO `normal_data` VALUES (15, 'computer1', '0.38910165', '192.168.38.130', '192.168.38.1', '2025-04-14 19:15:25', '/pikachu/vul/xss/xss.php');
INSERT INTO `normal_data` VALUES (16, 'computer1', '0.38910165', '192.168.38.130', '192.168.38.1', '2025-04-14 19:15:25', '/pikachu/vul/xss/xssblind/xss_blind.php');
INSERT INTO `normal_data` VALUES (17, 'computer1', '0.38910165', '192.168.38.130', '192.168.38.1', '2025-04-14 19:15:26', '/pikachu/vul/xss/xss_reflected_get.php');
INSERT INTO `normal_data` VALUES (18, 'computer1', '0.38910165', '192.168.38.130', '192.168.38.1', '2025-04-14 19:15:27', '/pikachu/vul/xss/xsspost/post_login.php');
INSERT INTO `normal_data` VALUES (19, 'computer2', '0.38910165', '192.168.38.130', '192.168.38.1', '2025-04-14 19:15:27', '/pikachu/vul/xss/xss_stored.php');
INSERT INTO `normal_data` VALUES (20, 'computer1', '0.38910165', '192.168.38.130', '192.168.38.1', '2025-04-14 19:15:27', '/pikachu/vul/xss/xss_dom.php');
INSERT INTO `normal_data` VALUES (21, 'computer3', '0.38910165', '192.168.38.130', '192.168.38.1', '2025-04-14 19:15:28', '/pikachu/vul/xss/xss_dom_x.php');
INSERT INTO `normal_data` VALUES (22, 'computer3', '0.38910165', '192.168.38.130', '192.168.38.1', '2025-04-14 19:15:28', '/pikachu/vul/xss/xss_01.php');
INSERT INTO `normal_data` VALUES (23, 'computer3', '0.38910165', '192.168.38.130', '192.168.38.1', '2025-04-14 19:15:29', '/pikachu/vul/xss/xssblind/xss_blind.php');
INSERT INTO `normal_data` VALUES (24, 'computer3', '0.38910165', '192.168.38.130', '192.168.38.1', '2025-04-14 19:15:29', '/pikachu/vul/xss/xss_02.php');
INSERT INTO `normal_data` VALUES (25, 'computer2', '0.38910165', '192.168.38.130', '192.168.38.1', '2025-04-14 19:15:29', '/pikachu/vul/xss/xss_03.php');
INSERT INTO `normal_data` VALUES (26, 'computer2', '0.38910165', '192.168.38.130', '192.168.38.1', '2025-04-14 19:15:30', '/pikachu/vul/xss/xss_04.php');
INSERT INTO `normal_data` VALUES (27, 'computer3', '0.38910165', '192.168.38.130', '192.168.38.1', '2025-04-14 19:15:36', '/pikachu/vul/csrf/csrf.php');
INSERT INTO `normal_data` VALUES (28, 'computer1', '0.38910165', '192.168.38.130', '192.168.38.1', '2025-04-14 19:15:38', '/pikachu/vul/csrf/csrfget/csrf_get_login.php');
INSERT INTO `normal_data` VALUES (29, 'computer1', '0.38910165', '192.168.38.130', '192.168.38.1', '2025-04-14 19:15:38', '/pikachu/vul/csrf/csrfpost/csrf_post_login.php');
INSERT INTO `normal_data` VALUES (30, 'computer2', '0.38910165', '192.168.38.130', '192.168.38.1', '2025-04-14 19:15:39', '/pikachu/vul/csrf/csrftoken/token_get_login.php');
INSERT INTO `normal_data` VALUES (31, 'computer3', '0.38910165', '192.168.38.130', '192.168.38.1', '2025-04-14 19:15:41', '/pikachu/vul/sqli/sqli.php');
INSERT INTO `normal_data` VALUES (32, 'computer2', '0.38910165', '192.168.38.130', '192.168.38.1', '2025-04-14 19:15:41', '/pikachu/vul/sqli/sqli_iu/sqli_login.php');
INSERT INTO `normal_data` VALUES (33, 'computer2', '0.38910165', '192.168.38.130', '192.168.38.1', '2025-04-14 19:15:42', '/pikachu/vul/sqli/sqli_id.php');
INSERT INTO `normal_data` VALUES (34, 'computer3', '0.38910165', '192.168.38.130', '192.168.38.1', '2025-04-14 19:15:42', '/pikachu/vul/sqli/sqli.php');
INSERT INTO `normal_data` VALUES (35, 'computer2', '0.38910165', '192.168.38.130', '192.168.38.1', '2025-04-14 19:15:43', '/pikachu/vul/sqli/sqli_str.php');
INSERT INTO `normal_data` VALUES (36, 'computer3', '0.38910165', '192.168.38.130', '192.168.38.1', '2025-04-14 19:15:43', '/pikachu/vul/sqli/sqli_search.php');
INSERT INTO `normal_data` VALUES (37, 'computer1', '0.38910165', '192.168.38.130', '192.168.38.1', '2025-04-14 19:15:43', '/pikachu/vul/sqli/sqli_x.php');
INSERT INTO `normal_data` VALUES (38, 'computer2', '0.38910165', '192.168.38.130', '192.168.38.1', '2025-04-14 19:15:44', '/pikachu/vul/sqli/sqli_iu/sqli_login.php');
INSERT INTO `normal_data` VALUES (39, 'computer3', '0.38910165', '192.168.38.130', '192.168.38.1', '2025-04-14 19:15:44', '/pikachu/vul/sqli/sqli_del.php');
INSERT INTO `normal_data` VALUES (40, 'computer2', '0.38910165', '192.168.38.130', '192.168.38.1', '2025-04-14 19:15:44', '/pikachu/vul/sqli/sqli_header/sqli_header_login.php');
INSERT INTO `normal_data` VALUES (41, 'computer1', '0.38910165', '192.168.38.130', '192.168.38.1', '2025-04-14 19:15:45', '/pikachu/vul/sqli/sqli_blind_b.php');
INSERT INTO `normal_data` VALUES (42, 'computer1', '0.38910165', '192.168.38.130', '192.168.38.1', '2025-04-14 19:15:45', '/pikachu/vul/sqli/sqli_blind_b.php');
INSERT INTO `normal_data` VALUES (43, 'computer2', '0.38910165', '192.168.38.130', '192.168.38.1', '2025-04-14 19:15:45', '/pikachu/vul/sqli/sqli_blind_t.php');
INSERT INTO `normal_data` VALUES (44, 'computer1', '0.014176864', '192.168.38.130', '192.168.38.1', '2025-04-14 19:15:46', '/pikachu/vul/sqli/sqli_blind_t.php?name=&submit=%E6%9F%A5%E8%AF%A2');
INSERT INTO `normal_data` VALUES (45, 'computer1', '0.014176864', '192.168.38.130', '192.168.38.1', '2025-04-14 19:15:48', '/pikachu/vul/sqli/sqli_blind_b.php?name=&submit=%E6%9F%A5%E8%AF%A2');
INSERT INTO `normal_data` VALUES (46, 'computer2', '0.38910165', '192.168.38.130', '192.168.38.1', '2025-04-14 19:15:48', '/pikachu/vul/sqli/sqli_blind_b.php');
INSERT INTO `normal_data` VALUES (47, 'computer3', '0.38910165', '192.168.38.130', '192.168.38.1', '2025-04-14 19:15:50', '/pikachu/vul/sqli/sqli_blind_t.php');
INSERT INTO `normal_data` VALUES (48, 'computer2', '0.014176864', '192.168.38.130', '192.168.38.1', '2025-04-14 19:15:51', '/pikachu/vul/sqli/sqli_blind_t.php?name=&submit=%E6%9F%A5%E8%AF%A2');
INSERT INTO `normal_data` VALUES (49, 'computer1', '0.38910165', '192.168.38.130', '192.168.38.1', '2025-04-14 19:15:52', '/pikachu/vul/sqli/sqli_widebyte.php');
INSERT INTO `normal_data` VALUES (50, 'computer2', '0.014176864', '192.168.38.130', '192.168.38.1', '2025-04-14 19:15:53', '/pikachu/vul/sqli/sqli_widebyte.php?name=&submit=%E6%9F%A5%E8%AF%A2');
INSERT INTO `normal_data` VALUES (51, 'computer1', '0.38910165', '192.168.38.130', '192.168.38.1', '2025-04-14 19:15:55', '/pikachu/vul/rce/rce.php');
INSERT INTO `normal_data` VALUES (52, 'computer2', '0.06329394', '192.168.38.130', '192.168.38.1', '2025-04-14 19:15:57', '/pikachu/vul/rce/rce_ping.php?ipaddress=&submit=ping');
INSERT INTO `normal_data` VALUES (53, 'computer3', '0.38910165', '192.168.38.130', '192.168.38.1', '2025-04-14 19:15:56', '/pikachu/vul/rce/rce_ping.php');
INSERT INTO `normal_data` VALUES (54, 'computer3', '0.38910165', '192.168.38.130', '192.168.38.1', '2025-04-14 19:15:58', '/pikachu/vul/rce/rce_eval.php');
INSERT INTO `normal_data` VALUES (55, 'computer1', '0.12157649', '192.168.38.130', '192.168.38.1', '2025-04-14 19:15:59', '/pikachu/vul/rce/rce_eval.php?txt=&submit=%E6%8F%90%E4%BA%A4');
INSERT INTO `normal_data` VALUES (56, 'computer1', '0.38910165', '192.168.38.130', '192.168.38.1', '2025-04-14 19:16:00', '/pikachu/vul/fileinclude/fileinclude.php');
INSERT INTO `normal_data` VALUES (57, 'computer3', '0.38910165', '192.168.38.130', '192.168.38.1', '2025-04-14 19:16:01', '/pikachu/vul/fileinclude/fi_local.php');
INSERT INTO `normal_data` VALUES (58, 'computer2', '0.22668758', '192.168.38.130', '192.168.38.1', '2025-04-14 19:16:02', '/pikachu/vul/fileinclude/fi_local.php?filename=&submit=Submit+Query');
INSERT INTO `normal_data` VALUES (59, 'computer2', '0.0410178', '192.168.38.130', '192.168.38.1', '2025-04-14 19:16:04', '/pikachu/vul/fileinclude/fi_local.php?filename=file1.php&submit=Submit+Query');
INSERT INTO `normal_data` VALUES (60, 'computer3', '0.38910165', '192.168.38.130', '192.168.38.1', '2025-04-14 19:16:04', '/pikachu/vul/fileinclude/include/kobe.png');
INSERT INTO `normal_data` VALUES (61, 'computer3', '0.38910165', '192.168.38.130', '192.168.38.1', '2025-04-14 19:16:06', '/pikachu/vul/fileinclude/fi_remote.php');
INSERT INTO `normal_data` VALUES (62, 'computer1', '0.38910165', '192.168.38.130', '192.168.38.1', '2025-04-14 19:16:08', '/pikachu/vul/unsafedownload/unsafedownload.php');
INSERT INTO `normal_data` VALUES (63, 'computer2', '0.38910165', '192.168.38.130', '192.168.38.1', '2025-04-14 19:16:10', '/pikachu/vul/unsafedownload/down_nba.php');
INSERT INTO `normal_data` VALUES (64, 'computer1', '0.38910165', '192.168.38.130', '192.168.38.1', '2025-04-14 19:16:10', '/pikachu/vul/unsafedownload/download/kb.png');
INSERT INTO `normal_data` VALUES (65, 'computer3', '0.38910165', '192.168.38.130', '192.168.38.1', '2025-04-14 19:16:10', '/pikachu/vul/unsafedownload/download/rayal.png');
INSERT INTO `normal_data` VALUES (66, 'computer2', '0.38910165', '192.168.38.130', '192.168.38.1', '2025-04-14 19:16:10', '/pikachu/vul/unsafedownload/download/ai.png');
INSERT INTO `normal_data` VALUES (67, 'computer1', '0.38910165', '192.168.38.130', '192.168.38.1', '2025-04-14 19:16:10', '/pikachu/vul/unsafedownload/download/mbl.png');
INSERT INTO `normal_data` VALUES (68, 'computer3', '0.38910165', '192.168.38.130', '192.168.38.1', '2025-04-14 19:16:10', '/pikachu/vul/unsafedownload/download/camby.png');
INSERT INTO `normal_data` VALUES (69, 'computer2', '0.38910165', '192.168.38.130', '192.168.38.1', '2025-04-14 19:16:10', '/pikachu/vul/unsafedownload/download/ns.png');
INSERT INTO `normal_data` VALUES (70, 'computer1', '0.38910165', '192.168.38.130', '192.168.38.1', '2025-04-14 19:16:10', '/pikachu/vul/unsafedownload/download/oldfish.png');
INSERT INTO `normal_data` VALUES (71, 'computer3', '0.38910165', '192.168.38.130', '192.168.38.1', '2025-04-14 19:16:10', '/pikachu/vul/unsafedownload/download/bigben.png');
INSERT INTO `normal_data` VALUES (72, 'computer2', '0.38910165', '192.168.38.130', '192.168.38.1', '2025-04-14 19:16:10', '/pikachu/vul/unsafedownload/download/pj.png');
INSERT INTO `normal_data` VALUES (73, 'computer3', '0.38910165', '192.168.38.130', '192.168.38.1', '2025-04-14 19:16:10', '/pikachu/vul/unsafedownload/download/sks.png');
INSERT INTO `normal_data` VALUES (74, 'computer2', '0.38910165', '192.168.38.130', '192.168.38.1', '2025-04-14 19:16:10', '/pikachu/vul/unsafedownload/download/lmx.png');
INSERT INTO `normal_data` VALUES (75, 'computer3', '0.38910165', '192.168.38.130', '192.168.38.1', '2025-04-14 19:16:10', '/pikachu/vul/unsafedownload/download/smallane.png');
INSERT INTO `normal_data` VALUES (76, 'computer2', '0.38910165', '192.168.38.130', '192.168.38.1', '2025-04-14 19:16:12', '/pikachu/vul/unsafeupload/clientcheck.php');
INSERT INTO `normal_data` VALUES (77, 'computer1', '0.38910165', '192.168.38.130', '192.168.38.1', '2025-04-14 19:16:13', '/pikachu/vul/unsafeupload/clientcheck.php');
INSERT INTO `normal_data` VALUES (78, 'computer1', '0.38910165', '192.168.38.130', '192.168.38.1', '2025-04-14 19:16:14', '/pikachu/vul/unsafeupload/getimagesize.php');
INSERT INTO `normal_data` VALUES (79, 'computer1', '0.38910165', '192.168.38.130', '192.168.38.1', '2025-04-14 19:16:14', '/pikachu/vul/unsafeupload/servercheck.php');
INSERT INTO `normal_data` VALUES (80, 'computer2', '0.38910165', '192.168.38.130', '192.168.38.1', '2025-04-14 19:16:16', '/pikachu/vul/overpermission/op.php');
INSERT INTO `normal_data` VALUES (81, 'computer3', '0.38910165', '192.168.38.130', '192.168.38.1', '2025-04-14 19:16:17', '/pikachu/vul/overpermission/op1/op1_login.php');
INSERT INTO `normal_data` VALUES (82, 'computer1', '0.38910165', '192.168.38.130', '192.168.38.1', '2025-04-14 19:16:18', '/pikachu/vul/overpermission/op2/op2_login.php');
INSERT INTO `normal_data` VALUES (83, 'computer3', '0.38910165', '192.168.38.130', '192.168.38.1', '2025-04-14 19:16:20', '/pikachu/vul/infoleak/infoleak.php');
INSERT INTO `normal_data` VALUES (84, 'computer3', '0.38910165', '192.168.38.130', '192.168.38.1', '2025-04-14 19:16:21', '/pikachu/vul/infoleak/findabc.php');
INSERT INTO `normal_data` VALUES (85, 'computer3', '0.38910165', '192.168.38.130', '192.168.38.1', '2025-04-14 19:16:23', '/pikachu/vul/unserilization/unser.php');
INSERT INTO `normal_data` VALUES (86, 'computer1', '0.38910165', '192.168.38.130', '192.168.38.1', '2025-04-14 19:16:25', '/pikachu/vul/xxe/xxe_1.php');
INSERT INTO `normal_data` VALUES (87, 'computer1', '0.38910165', '192.168.38.130', '192.168.38.1', '2025-04-14 19:16:28', '/pikachu/vul/urlredirect/unsafere.php');
INSERT INTO `normal_data` VALUES (88, 'computer3', '0.38910165', '192.168.38.130', '192.168.38.1', '2025-04-14 19:16:29', '/pikachu/vul/urlredirect/urlredirect.php');
INSERT INTO `normal_data` VALUES (89, 'computer3', '0.38910165', '192.168.38.130', '192.168.38.1', '2025-04-14 19:16:31', '/pikachu/vul/ssrf/ssrf_curl.php');

SET FOREIGN_KEY_CHECKS = 1;
