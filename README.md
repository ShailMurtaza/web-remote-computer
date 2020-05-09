# web-remote-computer
This web app is based on flask framework to remotely control pc using web<br>
This open source project has been created by Shail in python using flask web framework.
By using this you will be able to remotely control computer using web browser.
<h3>Functions</h3>
<ul>
  <li>Take and delete screenshots</li>
  <li>Send message to remote computer</li>
  <li>Shutdown remote computer using timer</li>
  <li>It include web based games</li>
  <li>Start ncat at background of Windows</li>
  <li>It contains login and logout sessions</li>
  <li>Create New user in SQL databases</li>
  <li>Keylogger (antivirus can detect it), (written in c++)</li>
  <li>Execute any shell command</li>
  <li>It contains Task Manager to kill any process running on Windows</li>
  <li>Change Windows password (It will not ask for previous password for Windows if account is administrator)</li>
  <li>Control movement of mouse</li>
  <li>Control keyboard</li>
  <li>It contains file named IP.txt which will save all logged in ip's</li>
  <li>It has file named allowed_IP.txt which contains list of ip's which not requres any user and apssword authentication</li>
  <li>Enjoy!</li>
</ul>
<h3>Usage</h3>
If you does not wants to use user and password authentication then this project has web(non_sql) version.<br>
<hr>MYSQL command to create database compatible with this web app<br>
create database test;<br>
DROP TABLE IF EXISTS `username_password`;<br>
CREATE TABLE IF NOT EXISTS `username_password` (<br>
  `Id` int(11) NOT NULL AUTO_INCREMENT,<br>
  `Username` varchar(55) DEFAULT NULL,<br>
  `Password` varchar(55) DEFAULT NULL,<br>
  `Date` datetime NOT NULL DEFAULT current_timestamp(),<br>
  PRIMARY KEY (`Id`)<br>
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;<br>
Use above command in your mysql server to create databases<br>
<hr>
You can also import my "test.sql" file using PhpMyAdmin
