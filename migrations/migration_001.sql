use bntu;

CREATE TABLE Categories(
    id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    uuid varchar(36) NOT NULL UNIQUE,
    name varchar(100) NOT NULL UNIQUE
) CHARACTER SET utf8;

CREATE TABLE Products(
    id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    uuid varchar(36) NOT NULL UNIQUE,
    name varchar(100) NOT NULL,
    category_id INT UNSIGNED NOT NULL,
    price DECIMAL UNSIGNED NOT NULL,
    description varchar(100) NOT NULL,
    create_date date NOT NULL,
    update_date date NOT NULL,
    CONSTRAINT `fk_product_category` FOREIGN KEY (category_id) REFERENCES Categories (id)
) CHARACTER SET utf8;

CREATE TABLE Groups(
    id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    uuid varchar(36) NOT NULL UNIQUE,
    number varchar(50) NOT NULL UNIQUE
) CHARACTER SET utf8;

CREATE TABLE Users(
    id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    uuid varchar(36) NOT NULL UNIQUE,
    first_name varchar(100) NOT NULL,
    last_name varchar(100) NOT NULL,
    group_id INT UNSIGNED NOT NULL,
    student_number varchar(50) NOT NULL,
    password_hash varchar(100) NOT NULL,
    birthday_date date,
    about varchar(500),
    role varchar(30) NOT NULL DEFAULT 'user',
    CONSTRAINT `fk_user_group` FOREIGN KEY (group_id) REFERENCES Groups (id)
) CHARACTER SET utf8;

CREATE TABLE Orders(
    id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    uuid varchar(36) NOT NULL UNIQUE,
    user_id INT UNSIGNED NOT NULL,
    country varchar(50),
    city varchar(50),
    address varchar(100),
    post_index varchar(50),
    created_date date NOT NULL,
    status varchar(50) NOT NULL DEFAULT 'Created',
    CONSTRAINT `fk_order_user` FOREIGN KEY (user_id) REFERENCES Users (id)
) CHARACTER SET utf8;

CREATE TABLE Tags(
    id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    uuid varchar(36) NOT NULL UNIQUE,
    name varchar(50) NOT NULL UNIQUE
) CHARACTER SET utf8;

CREATE TABLE Comments(
    id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    uuid varchar(36) NOT NULL UNIQUE,
    user_id INT UNSIGNED NOT NULL,
    product_id INT UNSIGNED NOT NULL,
    text varchar(500) NOT NULL,
    rate INT NOT NULL DEFAULT 0,
    create_date date NOT NULL,
    CONSTRAINT `fk_comment_user` FOREIGN KEY (user_id) REFERENCES Users (id),
    CONSTRAINT `fk_comment_product` FOREIGN KEY (product_id) REFERENCES Products (id)
) CHARACTER SET utf8;

CREATE TABLE Rates(
    product_id INT UNSIGNED NOT NULL,
    rate INT UNSIGNED NOT NULL DEFAULT 0
) CHARACTER SET utf8;

