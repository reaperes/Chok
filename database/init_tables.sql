USE chok;

CREATE TABLE chok.tweet (
  tweet_id int(11) comment "Tweet id",
  created_time timestamp comment "Tweet created time",
  geo point comment "Tweet's geo coordinates",
  primary key (tweet_id)
)ENGINE=INNODB;

CREATE TABLE chok.food (
  food_id int(11) comment "Food id",
  name_ko VARCHAR(20) comment "Food name in Korean",
  primary key (food_id)
)ENGINE=INNODB;

CREATE TABLE chok.tweet_food (
  tweet_id int(11),
  food_id int(11),
  FOREIGN KEY (tweet_id) REFERENCES tweet(tweet_id) ON DELETE CASCADE,
  FOREIGN KEY (food_id) REFERENCES food(food_id) ON DELETE NO ACTION
)ENGINE=INNODB;