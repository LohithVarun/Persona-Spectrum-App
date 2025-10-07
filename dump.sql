BEGIN TRANSACTION;
CREATE TABLE personality_results (
	id INTEGER NOT NULL, 
	user_id INTEGER NOT NULL, 
	name VARCHAR, 
	summary_statement TEXT, 
	timestamp DATETIME NOT NULL, 
	scores JSON NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(user_id) REFERENCES users (id)
);
INSERT INTO "personality_results" VALUES(1,1,'Initial Assessment','Your results show strong tendencies as a Intuition. Here are some areas for potential growth.','2025-09-09 18:19:48.615191','{"Introvert_Extrovert": -14.285714285714285, "Sensing_Intuition": 50.0, "Thinking_Feeling": -7.142857142857142, "Judging_Perceiving": -22.22222222222222}');
INSERT INTO "personality_results" VALUES(2,1,'Initial Assessment','Your results show strong tendencies as a Intuition. Here are some areas for potential growth.','2025-09-09 18:19:52.125456','{"Introvert_Extrovert": -14.285714285714285, "Sensing_Intuition": 50.0, "Thinking_Feeling": -7.142857142857142, "Judging_Perceiving": -22.22222222222222}');
INSERT INTO "personality_results" VALUES(3,1,'Initial Assessment','Your results show strong tendencies as a Intuition. Here are some areas for potential growth.','2025-09-09 18:19:57.405353','{"Introvert_Extrovert": -14.285714285714285, "Sensing_Intuition": 50.0, "Thinking_Feeling": -7.142857142857142, "Judging_Perceiving": -22.22222222222222}');
INSERT INTO "personality_results" VALUES(4,1,'Initial Assessment','Your results show strong tendencies as a Intuition. Here are some areas for potential growth.','2025-09-09 18:20:37.952987','{"Introvert_Extrovert": -14.285714285714285, "Sensing_Intuition": 50.0, "Thinking_Feeling": -7.142857142857142, "Judging_Perceiving": -22.22222222222222}');
INSERT INTO "personality_results" VALUES(5,1,'Initial Assessment','Your results show strong tendencies as a Intuition. Here are some areas for potential growth.','2025-09-09 18:20:44.325612','{"Introvert_Extrovert": -14.285714285714285, "Sensing_Intuition": 50.0, "Thinking_Feeling": -7.142857142857142, "Judging_Perceiving": -22.22222222222222}');
INSERT INTO "personality_results" VALUES(6,1,'Initial Assessment','Your results show strong tendencies as a Intuition. Here are some areas for potential growth.','2025-09-09 18:21:12.815041','{"Introvert_Extrovert": -14.285714285714285, "Sensing_Intuition": 50.0, "Thinking_Feeling": -7.142857142857142, "Judging_Perceiving": -22.22222222222222}');
INSERT INTO "personality_results" VALUES(7,1,'Initial Assessment','Your results show strong tendencies as a Intuition. Here are some areas for potential growth.','2025-09-09 18:21:26.585221','{"Introvert_Extrovert": -14.285714285714285, "Sensing_Intuition": 50.0, "Thinking_Feeling": -7.142857142857142, "Judging_Perceiving": -22.22222222222222}');
INSERT INTO "personality_results" VALUES(8,1,'Initial Assessment','Your results show strong tendencies as a Intuition. Here are some areas for potential growth.','2025-09-09 18:21:30.771075','{"Introvert_Extrovert": -14.285714285714285, "Sensing_Intuition": 50.0, "Thinking_Feeling": -7.142857142857142, "Judging_Perceiving": -22.22222222222222}');
INSERT INTO "personality_results" VALUES(9,1,'Initial Assessment','Your results show strong tendencies as a Intuition. Here are some areas for potential growth.','2025-09-09 18:21:32.976727','{"Introvert_Extrovert": -14.285714285714285, "Sensing_Intuition": 50.0, "Thinking_Feeling": -7.142857142857142, "Judging_Perceiving": -22.22222222222222}');
INSERT INTO "personality_results" VALUES(10,1,'Initial Assessment','Your results show strong tendencies as a Intuition. Here are some areas for potential growth.','2025-09-09 18:21:33.965040','{"Introvert_Extrovert": -14.285714285714285, "Sensing_Intuition": 50.0, "Thinking_Feeling": -7.142857142857142, "Judging_Perceiving": -22.22222222222222}');
INSERT INTO "personality_results" VALUES(11,1,'Initial Assessment','Your results show strong tendencies as a Intuition. Here are some areas for potential growth.','2025-09-09 18:21:40.473366','{"Introvert_Extrovert": -14.285714285714285, "Sensing_Intuition": 50.0, "Thinking_Feeling": -7.142857142857142, "Judging_Perceiving": -22.22222222222222}');
INSERT INTO "personality_results" VALUES(12,1,'Initial Assessment','Your results show strong tendencies as a Intuition. Here are some areas for potential growth.','2025-09-09 18:23:05.670943','{"Introvert_Extrovert": -14.285714285714285, "Sensing_Intuition": 50.0, "Thinking_Feeling": -7.142857142857142, "Judging_Perceiving": -22.22222222222222}');
INSERT INTO "personality_results" VALUES(13,1,'Initial Assessment','Your results show strong tendencies as a Intuition. Here are some areas for potential growth.','2025-09-09 18:33:00.143989','{"Introvert_Extrovert": -21.428571428571427, "Sensing_Intuition": 42.857142857142854, "Thinking_Feeling": -7.142857142857142, "Judging_Perceiving": -22.22222222222222}');
INSERT INTO "personality_results" VALUES(14,2,'Initial Assessment','Your results indicate a well-balanced personality profile.','2025-09-11 04:44:37.263605','{"Introvert_Extrovert": 14.285714285714285, "Sensing_Intuition": 14.285714285714285, "Thinking_Feeling": 7.142857142857142, "Judging_Perceiving": 27.77777777777778}');
INSERT INTO "personality_results" VALUES(15,3,'Initial Assessment','Your results show strong tendencies as a Introvert, Thinking. Here are some areas for potential growth.','2025-09-29 16:58:39.578316','{"Introvert_Extrovert": -100.0, "Sensing_Intuition": -14.285714285714285, "Thinking_Feeling": -100.0, "Judging_Perceiving": -22.22222222222222}');
INSERT INTO "personality_results" VALUES(16,3,'Initial Assessment','Your results show strong tendencies as a Introvert, Thinking. Here are some areas for potential growth.','2025-09-29 17:06:18.934238','{"Introvert_Extrovert": -100.0, "Sensing_Intuition": 14.285714285714285, "Thinking_Feeling": -85.71428571428571, "Judging_Perceiving": -11.11111111111111}');
INSERT INTO "personality_results" VALUES(17,3,'Initial Assessment','Your results show strong tendencies as a Introvert, Thinking, Judging. Here are some areas for potential growth.','2025-09-29 17:08:32.528724','{"Introvert_Extrovert": -114.28571428571428, "Sensing_Intuition": 0.0, "Thinking_Feeling": -42.857142857142854, "Judging_Perceiving": -66.66666666666666}');
CREATE TABLE questions (
	id INTEGER NOT NULL, 
	question_number INTEGER NOT NULL, 
	text TEXT NOT NULL, 
	category VARCHAR, 
	options_data JSON NOT NULL, 
	PRIMARY KEY (id)
);
INSERT INTO "questions" VALUES(1,1,'You find it draining to be in large social gatherings for extended periods.','Energy','[{"value": 1, "text": "Strongly Disagree"}, {"value": 2, "text": "Disagree"}, {"value": 3, "text": "Neutral"}, {"value": 4, "text": "Agree"}, {"value": 5, "text": "Strongly Agree"}]');
INSERT INTO "questions" VALUES(2,2,'You often take the initiative to start conversations with new people.','Energy','[{"value": 1, "text": "Strongly Disagree"}, {"value": 2, "text": "Disagree"}, {"value": 3, "text": "Neutral"}, {"value": 4, "text": "Agree"}, {"value": 5, "text": "Strongly Agree"}]');
INSERT INTO "questions" VALUES(3,3,'You prefer a quiet evening with a book or a movie over a large, loud party.','Energy','[{"value": 1, "text": "Strongly Disagree"}, {"value": 2, "text": "Disagree"}, {"value": 3, "text": "Neutral"}, {"value": 4, "text": "Agree"}, {"value": 5, "text": "Strongly Agree"}]');
INSERT INTO "questions" VALUES(4,4,'You feel energized and excited after spending time with a large group of friends.','Energy','[{"value": 1, "text": "Strongly Disagree"}, {"value": 2, "text": "Disagree"}, {"value": 3, "text": "Neutral"}, {"value": 4, "text": "Agree"}, {"value": 5, "text": "Strongly Agree"}]');
INSERT INTO "questions" VALUES(5,5,'You are often described as talkative and outgoing.','Energy','[{"value": 1, "text": "Strongly Disagree"}, {"value": 2, "text": "Disagree"}, {"value": 3, "text": "Neutral"}, {"value": 4, "text": "Agree"}, {"value": 5, "text": "Strongly Agree"}]');
INSERT INTO "questions" VALUES(6,6,'You tend to think things through carefully before you speak.','Energy','[{"value": 1, "text": "Strongly Disagree"}, {"value": 2, "text": "Disagree"}, {"value": 3, "text": "Neutral"}, {"value": 4, "text": "Agree"}, {"value": 5, "text": "Strongly Agree"}]');
INSERT INTO "questions" VALUES(7,7,'Being the center of attention is something you enjoy.','Energy','[{"value": 1, "text": "Strongly Disagree"}, {"value": 2, "text": "Disagree"}, {"value": 3, "text": "Neutral"}, {"value": 4, "text": "Agree"}, {"value": 5, "text": "Strongly Agree"}]');
INSERT INTO "questions" VALUES(8,8,'You are more interested in abstract ideas and future possibilities than concrete, immediate realities.','Information','[{"value": 1, "text": "Strongly Disagree"}, {"value": 2, "text": "Disagree"}, {"value": 3, "text": "Neutral"}, {"value": 4, "text": "Agree"}, {"value": 5, "text": "Strongly Agree"}]');
INSERT INTO "questions" VALUES(9,9,'You trust practical experience and proven facts more than theories and concepts.','Information','[{"value": 1, "text": "Strongly Disagree"}, {"value": 2, "text": "Disagree"}, {"value": 3, "text": "Neutral"}, {"value": 4, "text": "Agree"}, {"value": 5, "text": "Strongly Agree"}]');
INSERT INTO "questions" VALUES(10,10,'You often find yourself lost in thought, exploring hypothetical scenarios.','Information','[{"value": 1, "text": "Strongly Disagree"}, {"value": 2, "text": "Disagree"}, {"value": 3, "text": "Neutral"}, {"value": 4, "text": "Agree"}, {"value": 5, "text": "Strongly Agree"}]');
INSERT INTO "questions" VALUES(11,11,'You prefer to focus on the details and specifics of a situation rather than the big picture.','Information','[{"value": 1, "text": "Strongly Disagree"}, {"value": 2, "text": "Disagree"}, {"value": 3, "text": "Neutral"}, {"value": 4, "text": "Agree"}, {"value": 5, "text": "Strongly Agree"}]');
INSERT INTO "questions" VALUES(12,12,'You enjoy discussing symbolic or metaphorical meanings in art and literature.','Information','[{"value": 1, "text": "Strongly Disagree"}, {"value": 2, "text": "Disagree"}, {"value": 3, "text": "Neutral"}, {"value": 4, "text": "Agree"}, {"value": 5, "text": "Strongly Agree"}]');
INSERT INTO "questions" VALUES(13,13,'You would rather work with tangible things you can see and touch.','Information','[{"value": 1, "text": "Strongly Disagree"}, {"value": 2, "text": "Disagree"}, {"value": 3, "text": "Neutral"}, {"value": 4, "text": "Agree"}, {"value": 5, "text": "Strongly Agree"}]');
INSERT INTO "questions" VALUES(14,14,'You rely on your gut feelings and hunches to make connections.','Information','[{"value": 1, "text": "Strongly Disagree"}, {"value": 2, "text": "Disagree"}, {"value": 3, "text": "Neutral"}, {"value": 4, "text": "Agree"}, {"value": 5, "text": "Strongly Agree"}]');
INSERT INTO "questions" VALUES(15,15,'When making decisions, you prioritize logic, objectivity, and impartial principles.','Decisions','[{"value": 1, "text": "Strongly Disagree"}, {"value": 2, "text": "Disagree"}, {"value": 3, "text": "Neutral"}, {"value": 4, "text": "Agree"}, {"value": 5, "text": "Strongly Agree"}]');
INSERT INTO "questions" VALUES(16,16,'You consider how your decisions will affect others'' feelings and well-being.','Decisions','[{"value": 1, "text": "Strongly Disagree"}, {"value": 2, "text": "Disagree"}, {"value": 3, "text": "Neutral"}, {"value": 4, "text": "Agree"}, {"value": 5, "text": "Strongly Agree"}]');
INSERT INTO "questions" VALUES(17,17,'You believe being truthful and direct is more important than being diplomatic to protect someone''s feelings.','Decisions','[{"value": 1, "text": "Strongly Disagree"}, {"value": 2, "text": "Disagree"}, {"value": 3, "text": "Neutral"}, {"value": 4, "text": "Agree"}, {"value": 5, "text": "Strongly Agree"}]');
INSERT INTO "questions" VALUES(18,18,'You often make decisions based on your personal values and what feels right to you.','Decisions','[{"value": 1, "text": "Strongly Disagree"}, {"value": 2, "text": "Disagree"}, {"value": 3, "text": "Neutral"}, {"value": 4, "text": "Agree"}, {"value": 5, "text": "Strongly Agree"}]');
INSERT INTO "questions" VALUES(19,19,'You can stay emotionally detached and objective in tense situations.','Decisions','[{"value": 1, "text": "Strongly Disagree"}, {"value": 2, "text": "Disagree"}, {"value": 3, "text": "Neutral"}, {"value": 4, "text": "Agree"}, {"value": 5, "text": "Strongly Agree"}]');
INSERT INTO "questions" VALUES(20,20,'You are more motivated by appreciation and harmony than by achieving a goal.','Decisions','[{"value": 1, "text": "Strongly Disagree"}, {"value": 2, "text": "Disagree"}, {"value": 3, "text": "Neutral"}, {"value": 4, "text": "Agree"}, {"value": 5, "text": "Strongly Agree"}]');
INSERT INTO "questions" VALUES(21,21,'You find it easy to identify flaws in an argument or plan.','Decisions','[{"value": 1, "text": "Strongly Disagree"}, {"value": 2, "text": "Disagree"}, {"value": 3, "text": "Neutral"}, {"value": 4, "text": "Agree"}, {"value": 5, "text": "Strongly Agree"}]');
INSERT INTO "questions" VALUES(22,22,'You prefer to have a flexible, adaptable approach to life rather than a structured, organized plan.','Lifestyle','[{"value": 1, "text": "Strongly Disagree"}, {"value": 2, "text": "Disagree"}, {"value": 3, "text": "Neutral"}, {"value": 4, "text": "Agree"}, {"value": 5, "text": "Strongly Agree"}]');
INSERT INTO "questions" VALUES(23,23,'You feel a sense of satisfaction from completing tasks on a to-do list.','Lifestyle','[{"value": 1, "text": "Strongly Disagree"}, {"value": 2, "text": "Disagree"}, {"value": 3, "text": "Neutral"}, {"value": 4, "text": "Agree"}, {"value": 5, "text": "Strongly Agree"}]');
INSERT INTO "questions" VALUES(24,24,'You like to keep your options open and enjoy spontaneity.','Lifestyle','[{"value": 1, "text": "Strongly Disagree"}, {"value": 2, "text": "Disagree"}, {"value": 3, "text": "Neutral"}, {"value": 4, "text": "Agree"}, {"value": 5, "text": "Strongly Agree"}]');
INSERT INTO "questions" VALUES(25,25,'You prefer to have matters decided and settled, and dislike uncertainty.','Lifestyle','[{"value": 1, "text": "Strongly Disagree"}, {"value": 2, "text": "Disagree"}, {"value": 3, "text": "Neutral"}, {"value": 4, "text": "Agree"}, {"value": 5, "text": "Strongly Agree"}]');
INSERT INTO "questions" VALUES(26,26,'Your workspace tends to be cluttered and disorganized, but you know where everything is.','Lifestyle','[{"value": 1, "text": "Strongly Disagree"}, {"value": 2, "text": "Disagree"}, {"value": 3, "text": "Neutral"}, {"value": 4, "text": "Agree"}, {"value": 5, "text": "Strongly Agree"}]');
INSERT INTO "questions" VALUES(27,27,'You work best when you have a clear set of rules and deadlines.','Lifestyle','[{"value": 1, "text": "Strongly Disagree"}, {"value": 2, "text": "Disagree"}, {"value": 3, "text": "Neutral"}, {"value": 4, "text": "Agree"}, {"value": 5, "text": "Strongly Agree"}]');
INSERT INTO "questions" VALUES(28,28,'You enjoy starting new projects more than finishing existing ones.','Lifestyle','[{"value": 1, "text": "Strongly Disagree"}, {"value": 2, "text": "Disagree"}, {"value": 3, "text": "Neutral"}, {"value": 4, "text": "Agree"}, {"value": 5, "text": "Strongly Agree"}]');
INSERT INTO "questions" VALUES(29,29,'You see deadlines as important goals to be met on time.','Lifestyle','[{"value": 1, "text": "Strongly Disagree"}, {"value": 2, "text": "Disagree"}, {"value": 3, "text": "Neutral"}, {"value": 4, "text": "Agree"}, {"value": 5, "text": "Strongly Agree"}]');
INSERT INTO "questions" VALUES(30,30,'You are comfortable changing plans at the last minute.','Lifestyle','[{"value": 1, "text": "Strongly Disagree"}, {"value": 2, "text": "Disagree"}, {"value": 3, "text": "Neutral"}, {"value": 4, "text": "Agree"}, {"value": 5, "text": "Strongly Agree"}]');
CREATE TABLE user_responses (
	id INTEGER NOT NULL, 
	user_id INTEGER NOT NULL, 
	question_id INTEGER NOT NULL, 
	selected_value INTEGER NOT NULL, 
	timestamp DATETIME NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(user_id) REFERENCES users (id), 
	FOREIGN KEY(question_id) REFERENCES questions (id)
);
CREATE TABLE users (
	id INTEGER NOT NULL, 
	email VARCHAR NOT NULL, 
	username VARCHAR NOT NULL, 
	hashed_password VARCHAR NOT NULL, 
	PRIMARY KEY (id)
);
INSERT INTO "users" VALUES(1,'vlohith@gmail.com','vlohith@gmail.com','$2b$12$ELdoatRbhAheuhzZ5yfv0u8Bt6Vs5D6EyXEUR5CNTOx4XapC/4Yi6');
INSERT INTO "users" VALUES(2,'sakthi@gmail.com','sakthi@gmail.com','$2b$12$szfF6yNhbM8s2hhl0ljL.OIaNrsyDpML0mUQKgNwVxysUPYZ4/6T.');
INSERT INTO "users" VALUES(3,'varun123@gmail.com','varun123@gmail.com','$2b$12$KqoqCEaRRON87UyBe3WHT.QyH4qqomT1Z4UzVsyc7q5VmPKwKN0gu');
CREATE UNIQUE INDEX ix_users_username ON users (username);
CREATE UNIQUE INDEX ix_users_email ON users (email);
CREATE INDEX ix_users_id ON users (id);
CREATE UNIQUE INDEX ix_questions_question_number ON questions (question_number);
CREATE INDEX ix_questions_id ON questions (id);
CREATE INDEX ix_user_responses_id ON user_responses (id);
CREATE INDEX ix_personality_results_id ON personality_results (id);
COMMIT;
