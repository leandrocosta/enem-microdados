mysql -u root -p <<__END__
CREATE DATABASE geoenem CHARACTER SET utf8 COLLATE utf8_bin;
CREATE USER 'enem'@'localhost' IDENTIFIED BY 'enem';
GRANT ALL PRIVILEGES ON geoenem.* TO 'enem'@'localhost';
__END__
