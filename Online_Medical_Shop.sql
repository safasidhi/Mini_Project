-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Nov 17, 2023 at 11:41 AM
-- Server version: 10.4.21-MariaDB
-- PHP Version: 8.1.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `Online_Medical_Shop`
--

-- --------------------------------------------------------

--
-- Table structure for table `complaints`
--

CREATE TABLE `complaints` (
  `complaint_id` int(11) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  `title` varchar(255) DEFAULT NULL,
  `description` varchar(255) DEFAULT NULL,
  `reply` varchar(255) DEFAULT NULL,
  `date` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `complaints`
--

INSERT INTO `complaints` (`complaint_id`, `user_id`, `title`, `description`, `reply`, `date`) VALUES
(1, 1, 'sorry', 'testing', 'Pending', '2023-11-10'),
(2, 1, 'testing', 'sdfghj', 'Pending', '2023-11-09'),
(3, 1, 'sample', 'dvfsfbdhkhjsd', 'Pending', '2023-11-17'),
(4, 1, 'sample\'s', 'testing vvhgh\'gvg', 'Pending', '2023-11-17');

-- --------------------------------------------------------

--
-- Table structure for table `login`
--

CREATE TABLE `login` (
  `login_id` int(11) NOT NULL,
  `username` varchar(255) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `usertype` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `login`
--

INSERT INTO `login` (`login_id`, `username`, `password`, `usertype`) VALUES
(1, 'admin@gmail.com', 'admin', 'admin'),
(2, 'sam@gmail.com', 'sam', 'User');

-- --------------------------------------------------------

--
-- Table structure for table `medicine`
--

CREATE TABLE `medicine` (
  `medicine_id` int(11) NOT NULL,
  `name` varchar(255) DEFAULT NULL,
  `description` varchar(255) DEFAULT NULL,
  `price` varchar(255) DEFAULT NULL,
  `exp_date` varchar(255) DEFAULT NULL,
  `stock` varchar(255) DEFAULT NULL,
  `image` varchar(500) NOT NULL,
  `status` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `medicine`
--

INSERT INTO `medicine` (`medicine_id`, `name`, `description`, `price`, `exp_date`, `stock`, `image`, `status`) VALUES
(1, 'qwerty', 'testing', '100', '2023-11-01', '883', 'static/uploads/qwerty_kk.png', 'Not-Available'),
(2, 'abc', 'hte', '777', '2023-11-15', '443', 'static/uploads/abc_md1.png', 'Not-Available');

-- --------------------------------------------------------

--
-- Table structure for table `payment`
--

CREATE TABLE `payment` (
  `payment_id` int(11) NOT NULL,
  `prescription_id` int(11) DEFAULT NULL,
  `amount` varchar(255) DEFAULT NULL,
  `date` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `payment`
--

INSERT INTO `payment` (`payment_id`, `prescription_id`, `amount`, `date`) VALUES
(1, 2, '877.0', '2023-11-17');

-- --------------------------------------------------------

--
-- Table structure for table `review`
--

CREATE TABLE `review` (
  `review_id` int(11) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  `review_des` varchar(255) DEFAULT NULL,
  `date` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `review`
--

INSERT INTO `review` (`review_id`, `user_id`, `review_des`, `date`) VALUES
(1, 1, ' hdd', '2023-11-17');

-- --------------------------------------------------------

--
-- Table structure for table `upload_prescription`
--

CREATE TABLE `upload_prescription` (
  `prescription_id` int(11) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  `title` varchar(255) DEFAULT NULL,
  `file` varchar(255) DEFAULT NULL,
  `date` varchar(255) DEFAULT NULL,
  `status` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `upload_prescription`
--

INSERT INTO `upload_prescription` (`prescription_id`, `user_id`, `title`, `file`, `date`, `status`) VALUES
(1, 1, 'sample', 'static/uploads/abc_md1.png', '2023-11-14', 'Accepted'),
(2, 1, 'sample 2', 'static/uploads/qwerty_kk.png', '2023-11-12', 'Paid'),
(3, 1, 'sample 2', 'static/upload_prescription/Pre_Green Illustrative Children\'s Day Instagram Post.png', '2023-11-16', 'Accepted'),
(4, 1, 'ass', 'static/upload_prescription/Pre_Green Illustrative Children\'s Day Instagram Post.png', '2023-11-16', 'Pending');

-- --------------------------------------------------------

--
-- Table structure for table `upload_pres_medicine`
--

CREATE TABLE `upload_pres_medicine` (
  `up_pres_medicine_id` int(11) NOT NULL,
  `prescription_id` int(11) DEFAULT NULL,
  `medcine_id` int(11) DEFAULT NULL,
  `quantity` varchar(255) DEFAULT NULL,
  `amount` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `upload_pres_medicine`
--

INSERT INTO `upload_pres_medicine` (`up_pres_medicine_id`, `prescription_id`, `medcine_id`, `quantity`, `amount`) VALUES
(3, 2, 2, '1', '777.00'),
(4, 2, 1, '1', '100.00'),
(8, 1, 1, '4', '400.00');

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `user_id` int(11) NOT NULL,
  `login_id` int(11) DEFAULT NULL,
  `fname` varchar(255) DEFAULT NULL,
  `lname` varchar(255) DEFAULT NULL,
  `phone` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`user_id`, `login_id`, `fname`, `lname`, `phone`, `email`) VALUES
(1, 2, 'sam', 'john', '0987456321', 'sam@gmail.com');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `complaints`
--
ALTER TABLE `complaints`
  ADD PRIMARY KEY (`complaint_id`);

--
-- Indexes for table `login`
--
ALTER TABLE `login`
  ADD PRIMARY KEY (`login_id`);

--
-- Indexes for table `medicine`
--
ALTER TABLE `medicine`
  ADD PRIMARY KEY (`medicine_id`);

--
-- Indexes for table `payment`
--
ALTER TABLE `payment`
  ADD PRIMARY KEY (`payment_id`);

--
-- Indexes for table `review`
--
ALTER TABLE `review`
  ADD PRIMARY KEY (`review_id`);

--
-- Indexes for table `upload_prescription`
--
ALTER TABLE `upload_prescription`
  ADD PRIMARY KEY (`prescription_id`);

--
-- Indexes for table `upload_pres_medicine`
--
ALTER TABLE `upload_pres_medicine`
  ADD PRIMARY KEY (`up_pres_medicine_id`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`user_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `complaints`
--
ALTER TABLE `complaints`
  MODIFY `complaint_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `login`
--
ALTER TABLE `login`
  MODIFY `login_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `medicine`
--
ALTER TABLE `medicine`
  MODIFY `medicine_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `payment`
--
ALTER TABLE `payment`
  MODIFY `payment_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `review`
--
ALTER TABLE `review`
  MODIFY `review_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `upload_prescription`
--
ALTER TABLE `upload_prescription`
  MODIFY `prescription_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `upload_pres_medicine`
--
ALTER TABLE `upload_pres_medicine`
  MODIFY `up_pres_medicine_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `user_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
