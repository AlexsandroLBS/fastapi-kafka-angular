-- Creating users table
CREATE TABLE if not exists users (
                    id SERIAL NOT NULL PRIMARY KEY,
                    user_name TEXT,
                    user_password TEXT,
                    created_at timestamp NOT NULL
                    );

-- Creating status table
CREATE TABLE if not exists status_table (
                    id INT NOT NULL PRIMARY KEY,
                    status_name TEXT NOT NULL
                    );

-- Creating subscription table
CREATE TABLE if not exists subscription (
                    id SERIAL NOT NULL  PRIMARY KEY,
                    user_id int NOT NULL,
                    status_id int NOT NULL,
                    created_at timestamp NOT NULL,
                    updated_at timestamp NOT NULL,
                    FOREIGN KEY (user_id) REFERENCES users (id),
                    FOREIGN KEY (status_id) REFERENCES status_table(id)
                    );
                    
-- Creating event_history table
CREATE TABLE if not exists event_history (
                    id SERIAL NOT NULL,
                    subscription_id INT NOT NULL,
                    type VARCHAR NOT NULL,
                    created_at timestamp NOT NULL,
                    FOREIGN KEY (subscription_id) REFERENCES subscription (id)
                    );
