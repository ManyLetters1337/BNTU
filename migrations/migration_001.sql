use bntu;

CREATE TABLE categories(
    id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    uuid varchar(36) NOT NULL UNIQUE,
    name varchar(100) NOT NULL UNIQUE
) CHARACTER SET utf8;

CREATE TABLE products(
    id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    uuid varchar(36) NOT NULL UNIQUE,
    name varchar(100) NOT NULL,
    image varchar(300) NOT NULL default 'https://res.cloudinary.com/manyletters/image/upload/v1589568700/015e96e6a653950ded808f5704c0727f.jpg',
    category_id INT UNSIGNED NOT NULL,
    price DECIMAL UNSIGNED NOT NULL,
    description varchar(100) NOT NULL,
    create_date datetime NOT NULL,
    update_date datetime NOT NULL,
    CONSTRAINT `fk_product_category` FOREIGN KEY (category_id) REFERENCES categories (id)
) CHARACTER SET utf8;

CREATE TABLE groups(
    id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    uuid varchar(36) NOT NULL UNIQUE,
    number varchar(50) NOT NULL UNIQUE
) CHARACTER SET utf8;

CREATE TABLE users(
    id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    uuid varchar(36) NOT NULL UNIQUE,
    first_name varchar(100) NOT NULL,
    last_name varchar(100) NOT NULL,
    email varchar (100) NOT NULL UNIQUE,
    group_id INT UNSIGNED NOT NULL,
    student_number varchar(50) NOT NULL,
    password_hash varchar(100) NOT NULL,
    birthday_date date,
    about varchar(500),
    role varchar(30) NOT NULL DEFAULT 'user',
    CONSTRAINT `fk_user_group` FOREIGN KEY (group_id) REFERENCES groups (id)
) CHARACTER SET utf8;

CREATE TABLE orders(
    id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    uuid varchar(36) NOT NULL UNIQUE,
    user_id INT UNSIGNED NOT NULL,
    country varchar(50),
    city varchar(50),
    address varchar(100),
    post_index varchar(50),
    created_date date NOT NULL,
    status varchar(50) NOT NULL DEFAULT 'Active',
    CONSTRAINT `fk_order_user` FOREIGN KEY (user_id) REFERENCES users (id)
) CHARACTER SET utf8;

CREATE TABLE tags(
    id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    uuid varchar(36) NOT NULL UNIQUE,
    name varchar(50) NOT NULL UNIQUE
) CHARACTER SET utf8;

CREATE TABLE comments(
    id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    uuid varchar(36) NOT NULL UNIQUE,
    user_id INT UNSIGNED NOT NULL,
    product_id INT UNSIGNED NOT NULL,
    text varchar(500) NOT NULL,
    rate INT NOT NULL DEFAULT 0,
    create_date date NOT NULL,
    CONSTRAINT `fk_comment_user` FOREIGN KEY (user_id) REFERENCES users (id),
    CONSTRAINT `fk_comment_product` FOREIGN KEY (product_id) REFERENCES products (id)
) CHARACTER SET utf8;

CREATE TABLE rates(
    id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    product_id INT UNSIGNED NOT NULL,
    rate INT UNSIGNED NOT NULL DEFAULT 0,
    CONSTRAINT `fk_rate_product_id` FOREIGN KEY (product_id) REFERENCES products (id) ON DELETE CASCADE
) CHARACTER SET utf8;

CREATE TABLE orders_products(
    order_id INT UNSIGNED,
    product_id INT UNSIGNED,
    CONSTRAINT `fk_order_products_id` FOREIGN KEY (order_id) REFERENCES orders (id) ON DELETE CASCADE,
    CONSTRAINT `fk_product_orders` FOREIGN KEY (product_id) REFERENCES products (id) ON DELETE CASCADE
)
CHARACTER SET utf8;

CREATE TABLE products_tags(
    product_id INT UNSIGNED,
    tag_id INT UNSIGNED,
    CONSTRAINT `fk_product_tags_id` FOREIGN KEY (product_id) REFERENCES products (id) ON DELETE CASCADE,
    CONSTRAINT `fk_tag_products` FOREIGN KEY (tag_id) REFERENCES tags (id) ON DELETE CASCADE
)
CHARACTER SET utf8;

CREATE TABLE products_users(
    product_id INT UNSIGNED,
    user_id INT UNSIGNED,
    CONSTRAINT `fk_product_users_id` FOREIGN KEY (product_id) REFERENCES products (id) ON DELETE CASCADE,
    CONSTRAINT `fk_user_products` FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE
)
CHARACTER SET utf8;

CREATE TABLE rates_users(
    rate_id INT UNSIGNED,
    user_id INT UNSIGNED,
    CONSTRAINT `fk_rate_users_id` FOREIGN KEY (rate_id) REFERENCES rates (id) ON DELETE CASCADE,
    CONSTRAINT `fk_user_rates` FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE
)
CHARACTER SET utf8;
