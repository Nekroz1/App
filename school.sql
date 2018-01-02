-- phpMyAdmin SQL Dump
-- version 4.5.1
-- http://www.phpmyadmin.net
--
-- Φιλοξενητής: 127.0.0.1
-- Χρόνος δημιουργίας: 29 Δεκ 2017 στις 13:05:33
-- Έκδοση διακομιστή: 10.1.19-MariaDB
-- Έκδοση PHP: 5.6.28

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Βάση δεδομένων: `school`
--

DELIMITER $$
--
-- Διαδικασίες
--
CREATE DEFINER=`root`@`localhost` PROCEDURE `addProject` (IN `title` VARCHAR(45), IN `submission` DATE, IN `description` VARCHAR(70), IN `scode` VARCHAR(45))  BEGIN
	if (select exists (select 1 from project where prtitle=title)) then
		select "Title Exists";
	ELSE 
		insert into project
        (
			prtitle,
            prsubdate,
            prdesc,
            subcode
		)
        values
        (
			title,
            submission,
            description,
            scode
		);
	End If;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `addStudent` (IN `username` VARCHAR(45), IN `passwords` VARCHAR(45), IN `fname` VARCHAR(30), IN `sname` VARCHAR(30), IN `role` VARCHAR(50), IN `bday` VARCHAR(30))  BEGIN
	if (select exists (select 1 from student where stusername=username)) then
		select "Username Exists";
	ELSE 
		insert into student
        (
			stusername,
            stpassword,
            stname,
            stsurname,
            strole,
            stbday
		)
        values
        (
			username,
            passwords,
            fname,
            sname,
            role,
            bday
		);
	End If;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `addSubject` (IN `scode` VARCHAR(45), IN `sname` VARCHAR(45), IN `description` VARCHAR(70))  BEGIN
	if (select exists (select 1 from lessons where subcode=scode)) then
		select "Subject Exists";
	ELSE 
		insert into lessons
        (
			subcode,
            subname,
            subdescription
		)
        values
        (
			scode,
            sname,
            description
		);
	End If;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `addTeacher` (IN `username` VARCHAR(45), IN `passwords` VARCHAR(45), IN `fname` VARCHAR(30), IN `sname` VARCHAR(30), IN `role` VARCHAR(50))  BEGIN
	if (select exists (select 1 from teacher where teusername=username)) then
		select "Username Exists";
	ELSE 
		insert into teacher
        (
			teusername,
            tepassword,
            tname,
            tsurname,
            trole
		)
        values
        (
			username,
            passwords,
            fname,
            sname,
            role
		);
	End If;
END$$

DELIMITER ;

-- --------------------------------------------------------

--
-- Δομή πίνακα για τον πίνακα `lessons`
--

CREATE TABLE `lessons` (
  `subid` int(11) NOT NULL,
  `subcode` varchar(45) NOT NULL,
  `subname` varchar(45) DEFAULT NULL,
  `subdescription` varchar(70) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Άδειασμα δεδομένων του πίνακα `lessons`
--

INSERT INTO `lessons` (`subid`, `subcode`, `subname`, `subdescription`) VALUES
(1, 'ZRX23', 'Computer Science1', 'Science and Computer and......stuff');

-- --------------------------------------------------------

--
-- Δομή πίνακα για τον πίνακα `project`
--

CREATE TABLE `project` (
  `prcode` int(45) NOT NULL,
  `prtitle` varchar(45) DEFAULT NULL,
  `prsubdate` date DEFAULT NULL,
  `prdesc` varchar(70) DEFAULT NULL,
  `subcode` varchar(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Άδειασμα δεδομένων του πίνακα `project`
--

INSERT INTO `project` (`prcode`, `prtitle`, `prsubdate`, `prdesc`, `subcode`) VALUES
(2, 'Create A Forum', '2017-12-05', 'The students have to make a forum using MongoDB and Php', 'ZRX23');

-- --------------------------------------------------------

--
-- Δομή πίνακα για τον πίνακα `student`
--

CREATE TABLE `student` (
  `stid` int(11) NOT NULL,
  `stusername` varchar(45) NOT NULL,
  `stpassword` varchar(45) DEFAULT NULL,
  `stname` varchar(30) DEFAULT NULL,
  `stsurname` varchar(30) DEFAULT NULL,
  `strole` varchar(50) DEFAULT NULL,
  `stbday` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Άδειασμα δεδομένων του πίνακα `student`
--

INSERT INTO `student` (`stid`, `stusername`, `stpassword`, `stname`, `stsurname`, `strole`, `stbday`) VALUES
(1, 'Jam', '10', 'Jin', 'Kazama', 'fighter', '13/7/97'),
(2, 'Jemowell', '1234', 'John', 'Dowelli', 'Medic', '3/5/97'),
(3, 'Vais', '758', 'Vasilis', 'Kazakos', 'Developer', '28/2/97');

-- --------------------------------------------------------

--
-- Δομή πίνακα για τον πίνακα `teacher`
--

CREATE TABLE `teacher` (
  `tid` int(11) NOT NULL,
  `teusername` varchar(45) NOT NULL,
  `tepassword` varchar(45) DEFAULT NULL,
  `tname` varchar(30) DEFAULT NULL,
  `tsurname` varchar(30) DEFAULT NULL,
  `trole` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Άδειασμα δεδομένων του πίνακα `teacher`
--

INSERT INTO `teacher` (`tid`, `teusername`, `tepassword`, `tname`, `tsurname`, `trole`) VALUES
(1, 'Rei Ryghts', '231', 'Rei', 'Ryghts', 'HDD'),
(2, 'Iris Heart', '123', 'Iris', 'Heart', 'HDD'),
(3, 'Red', '111', 'Roy ', 'Reed', 'PE'),
(4, 'T Hawk', '9s', 'T', 'Hawk', 'PE');

--
-- Ευρετήρια για άχρηστους πίνακες
--

--
-- Ευρετήρια για πίνακα `lessons`
--
ALTER TABLE `lessons`
  ADD PRIMARY KEY (`subid`);

--
-- Ευρετήρια για πίνακα `project`
--
ALTER TABLE `project`
  ADD PRIMARY KEY (`prcode`);

--
-- Ευρετήρια για πίνακα `student`
--
ALTER TABLE `student`
  ADD PRIMARY KEY (`stid`);

--
-- Ευρετήρια για πίνακα `teacher`
--
ALTER TABLE `teacher`
  ADD PRIMARY KEY (`tid`);

--
-- AUTO_INCREMENT για άχρηστους πίνακες
--

--
-- AUTO_INCREMENT για πίνακα `lessons`
--
ALTER TABLE `lessons`
  MODIFY `subid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
--
-- AUTO_INCREMENT για πίνακα `project`
--
ALTER TABLE `project`
  MODIFY `prcode` int(45) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
--
-- AUTO_INCREMENT για πίνακα `student`
--
ALTER TABLE `student`
  MODIFY `stid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
--
-- AUTO_INCREMENT για πίνακα `teacher`
--
ALTER TABLE `teacher`
  MODIFY `tid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
