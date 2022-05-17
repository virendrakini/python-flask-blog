-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 17, 2022 at 09:25 AM
-- Server version: 10.4.21-MariaDB
-- PHP Version: 7.3.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `rkcomputer`
--

-- --------------------------------------------------------

--
-- Table structure for table `contacts`
--

CREATE TABLE `contacts` (
  `contacts_id` int(11) NOT NULL,
  `contacts_name` varchar(255) NOT NULL,
  `contacts_email` varchar(255) NOT NULL,
  `contacts_phone` varchar(255) NOT NULL,
  `contacts_mesg` longtext NOT NULL,
  `contacts_date` varchar(255) NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `contacts`
--

INSERT INTO `contacts` (`contacts_id`, `contacts_name`, `contacts_email`, `contacts_phone`, `contacts_mesg`, `contacts_date`) VALUES
(1, 'first', 'first@first.com', '2737737373', 'first post', 'current_timestamp()'),
(2, 'first', 'first@first.com', '3627373848', '4', '2022-05-13 12:14:41'),
(3, 'first', 'first@first.com', '3627373848', '5', '2022-05-13 12:15:18'),
(4, 'test ', 'test@teting.com', '5355463728', 'tester', '2022-05-14 10:39:27'),
(5, 'first', 'first@first.com', '3627373848', 'dtrhr', '2022-05-14 10:44:26'),
(6, 'testing', 'test@teting.com', '5355463728', 'test', '2022-05-14 10:46:39'),
(7, 'testing', 'first@first.com', '3627373848', 'test', '2022-05-14 15:38:32'),
(8, 'testing', 'first@first.com', '3627373848', 'test', '2022-05-14 15:39:10'),
(9, 'testing', 'test@teting.com', '3627373848', 'test', '2022-05-17 11:05:41');

-- --------------------------------------------------------

--
-- Table structure for table `posts`
--

CREATE TABLE `posts` (
  `post_id` int(11) NOT NULL,
  `post_title` varchar(255) NOT NULL,
  `post_description` varchar(255) NOT NULL,
  `post_slug` varchar(255) NOT NULL,
  `post_img` varchar(255) NOT NULL,
  `post_date` varchar(255) NOT NULL DEFAULT current_timestamp(),
  `post_author` varchar(255) NOT NULL,
  `post_status` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `posts`
--

INSERT INTO `posts` (`post_id`, `post_title`, `post_description`, `post_slug`, `post_img`, `post_date`, `post_author`, `post_status`) VALUES
(1, 'Man must explore, and this is exploration at its greatest', 'Big Problems look mighty small from 150 miles up', 'exploration', 'post-bg.jpg', '2022-05-14 10:39:27', 'Admin', 'active'),
(2, 'No POST, No Power, No Video', 'This article takes you through how to troubleshoot start up issues with your desktop personal computer.', 'postpower', 'post-bg.jpg', '2022-05-14 10:39:27', 'Admin', 'active'),
(3, 'SUGGESTED RESOLUTION', 'he term POST refers to Power-On Self-Test, which is a series of checks the computer goes through whenever it starts. If the computer fails any of these tests, it stops the start-up process and report a fault. This informative YouTube video (English only, ', 'resolution', 'post-bg.jpg', '2022-05-14 10:39:27', 'Admin', 'active'),
(4, 'BIOS may be corrupt ', 'The computer hardware is operating normally, but the BIOS may be corrupt or missing.\r\nDownload the current BIOS version from our Support site.', 'bios', 'post-bg.jpg', '2022-05-14 10:39:27', 'Admin', 'active'),
(5, 'A possible coin cell battery failure has occurred.', 'Remove the coin cell battery for one minute, reinstall the battery, and restart.\r\nIf the computer still does not POST after this, replace the coin cell battery.', 'battery', 'post-bg.jpg', '2022-05-14 10:39:37', 'Admin', 'active');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `contacts`
--
ALTER TABLE `contacts`
  ADD PRIMARY KEY (`contacts_id`);

--
-- Indexes for table `posts`
--
ALTER TABLE `posts`
  ADD PRIMARY KEY (`post_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `contacts`
--
ALTER TABLE `contacts`
  MODIFY `contacts_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `posts`
--
ALTER TABLE `posts`
  MODIFY `post_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
