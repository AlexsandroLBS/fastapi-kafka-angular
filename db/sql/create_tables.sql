-- Creating users table
CREATE TABLE if not exists users (
                    id SERIAL NOT NULL PRIMARY KEY,
                    user_name TEXT,
                    created_at timestamp NOT NULL
                    );

-- Creating subscription table
CREATE TABLE if not exists subscription (
                    id SERIAL NOT NULL  PRIMARY KEY,
                    user_id int NOT NULL,
                    status_id int NOT NULL,
                    created_at timestamp NOT NULL,
                    updated_at timestamp NOT NULL,
                    FOREIGN KEY (user_id) REFERENCES users (id)
                    );
-- Creating status table
CREATE TABLE if not exists status_table (
                    id INT NOT NULL,
                    status_name TEXT NOT NULL
                    -- FOREIGN KEY (id) REFERENCES subscription (status_id)
                    );
                    
-- Creating event_history table
CREATE TABLE if not exists event_history (
                    id SERIAL NOT NULL PRIMARY KEY,
                    subscription_id INT NOT NULL,
                    type VARCHAR NOT NULL,
                    created_at timestamp NOT NULL,
                    FOREIGN KEY (subscription_id) REFERENCES subscription (id)
                    );
