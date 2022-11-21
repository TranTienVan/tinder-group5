create database if not exists tinder_database;
use tinder_database;

create table `school` (
	id int auto_increment,
    `name` varchar(1024),
    
    primary key (id)
);

create table `account`(
	id int auto_increment,
    email VARCHAR(330),
    `phone` varchar(12),
    `first_name` varchar(1024),
    `last_name` varchar(1024),
    `password` VARCHAR(1024),
    `is_premium` bool, /* 0 1 */
    `is_admin` bool, /* 0 1 */
    `is_active` bool,
    `is_reported` bool,
    `is_blocked` bool,
    `created_at` datetime,
    `updated_at` datetime,
    `gender` bool,
    `about_me` text,
    `birthday` datetime,
    `big_picture_url` varchar(1024),
    `small_picture_url` varchar(1024),
    `country` varchar(1024),
    `city` varchar(1024),
    `district` varchar(1024),
    `street` varchar(1024),
    `address` varchar(1024),
    `school_id` int,
    
    primary key (id),
    foreign key (`school_id`) references `school`(id)
);

create table `notification` (
	id int auto_increment,
    `account_id` int,
    `message` text,
    `redirect_url` varchar(1024),
    
    primary key (id),
    foreign key (`account_id`) references `account`(id)
);


create table `reaction` (
	id int auto_increment,
    `icon` varchar(1024),
    
    primary key (id)
);

create table `account_reaction` (
	id int auto_increment,
    `reactor_id` int,
    `receiver_id` int,
    `created_at` datetime,
    `deleted_at` datetime,
    `is_superlike` bool,
    `icon_id` int,
    
    primary key (id),
    foreign key (`receiver_id`) references `account`(`id`),
    foreign key (`reactor_id`) references `account`(`id`),
    foreign key (`icon_id`) references `reaction`(id)
);

create table `account_connection` (
	id int auto_increment,
    `account_id1` int,
    `account_id2` int,
    `created_at` datetime,
    `deleted_at` datetime,
    
    primary key (id),
    foreign key (`account_id1`) references `account`(`id`),
    foreign key (`account_id2`) references `account`(`id`)
);

create table `favorite` (
	id int auto_increment,
    account_id int,
    favorite_name varchar(1024),
    
    primary key (id),
    foreign key (account_id) references `account`(id)
);


create table `message` (
	id int auto_increment,
    `sender_id` int,
    `receiver_id` int,
    `reply_from_message` int,
    `content` text,
    `created_at` datetime,
    `deleted_at` datetime,
    
    primary key (id),
    foreign key (`reply_from_message`) references `message`(id),
    foreign key (`sender_id`) references `account`(id),
    foreign key (`receiver_id`) references `account`(id)
);



create table `message_reaction` (
	id int auto_increment,
    `reactor_id` int,
    `message_id` int,
    `created_at` datetime,
    `deleted_at` datetime,
    `icon_id` int,
    
    primary key (id),
    foreign key (`reactor_id`) references `account`(id),
    foreign key (`message_id`) references `message`(id),
    foreign key (`icon_id`) references `reaction`(id)
);


create table `message_attachment` (
	id int auto_increment,
    `message_id` int,
    `file_url` varchar(1024),
    
    primary key (id),
    foreign key (`message_id`) references `message`(id)
);


