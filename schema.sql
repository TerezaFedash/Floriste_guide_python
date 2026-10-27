CREATE DATABASE IF NOT EXISTS florist_catalog;
USE florist_catalog;

-- 1. Користувачі
CREATE TABLE IF NOT EXISTS auth_user (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(150) NOT NULL UNIQUE,
    first_name VARCHAR(150) DEFAULT '',
    last_name VARCHAR(150) DEFAULT '',
    email VARCHAR(254) DEFAULT '',
    password VARCHAR(128) NOT NULL,
    is_staff BOOLEAN DEFAULT 0,
    is_superuser BOOLEAN DEFAULT 0,
    is_active BOOLEAN DEFAULT 1,
    date_joined DATETIME NOT NULL,
    last_login DATETIME
);

-- 2. Групи користувачів
CREATE TABLE IF NOT EXISTS auth_group (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(150) NOT NULL UNIQUE
);

-- 3. Зв'язок користувачів з групами
CREATE TABLE IF NOT EXISTS auth_user_groups (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    group_id INT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES auth_user(id) ON DELETE CASCADE,
    FOREIGN KEY (group_id) REFERENCES auth_group(id) ON DELETE CASCADE
);

-- 4. Сесії відвідувачів
CREATE TABLE IF NOT EXISTS django_session (
    session_key VARCHAR(40) PRIMARY KEY,
    session_data LONGTEXT NOT NULL,
    expire_date DATETIME NOT NULL
);

-- 5. Категорії квітів
CREATE TABLE IF NOT EXISTS catalog_category (
    category_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL UNIQUE,
    slug VARCHAR(100) NOT NULL UNIQUE,
    description TEXT,
    icon_emoji VARCHAR(10) DEFAULT '🌸'
);

-- 6. Нагоди та події
CREATE TABLE IF NOT EXISTS catalog_occasion (
    occasion_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL UNIQUE,
    slug VARCHAR(100) NOT NULL UNIQUE,
    description TEXT,
    season VARCHAR(20) DEFAULT 'all_year',
    badge_color VARCHAR(30) DEFAULT 'danger'
);

-- 7. Квіти
CREATE TABLE IF NOT EXISTS catalog_flower (
    flower_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(150) NOT NULL,
    latin_name VARCHAR(150) DEFAULT '',
    category_id INT NOT NULL,
    owner_id INT NOT NULL,
    description TEXT NOT NULL,
    fun_fact TEXT,
    difficulty_level VARCHAR(20) DEFAULT 'easy',
    image_url VARCHAR(2000) DEFAULT '',
    created_at DATETIME NOT NULL,
    FOREIGN KEY (category_id) REFERENCES catalog_category(category_id),
    FOREIGN KEY (owner_id) REFERENCES auth_user(id) ON DELETE CASCADE
);

-- 8. Зв'язок квітів і нагод
CREATE TABLE IF NOT EXISTS catalog_flower_occasions (
    flower_occasion_id INT AUTO_INCREMENT PRIMARY KEY,
    flower_id INT NOT NULL,
    occasion_id INT NOT NULL,
    FOREIGN KEY (flower_id) REFERENCES catalog_flower(flower_id) ON DELETE CASCADE,
    FOREIGN KEY (occasion_id) REFERENCES catalog_occasion(occasion_id) ON DELETE CASCADE
);

-- 9. Довідник з догляду
CREATE TABLE IF NOT EXISTS catalog_careguide (
    careguide_id INT AUTO_INCREMENT PRIMARY KEY,
    flower_id INT NOT NULL UNIQUE,
    expert_id INT,
    watering_frequency_days INT DEFAULT 2,
    temperature_range VARCHAR(50) DEFAULT '18-22°C',
    light_requirement VARCHAR(30) DEFAULT 'bright_indirect',
    humidity_level VARCHAR(20) DEFAULT 'medium',
    soil_type VARCHAR(200) DEFAULT '',
    stem_cutting_tips TEXT NOT NULL,
    florist_secret TEXT,
    fun_fact TEXT,
    updated_at DATE NOT NULL,
    FOREIGN KEY (flower_id) REFERENCES catalog_flower(flower_id) ON DELETE CASCADE,
    FOREIGN KEY (expert_id) REFERENCES auth_user(id) ON DELETE SET NULL
);

-- 10. Обране
CREATE TABLE IF NOT EXISTS catalog_favorite (
    favorite_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    flower_id INT NOT NULL,
    created_at DATETIME NOT NULL,
    FOREIGN KEY (user_id) REFERENCES auth_user(id) ON DELETE CASCADE,
    FOREIGN KEY (flower_id) REFERENCES catalog_flower(flower_id) ON DELETE CASCADE
);

-- 11. Заявки на консультацію
CREATE TABLE IF NOT EXISTS catalog_consultationrequest (
    consultation_id INT AUTO_INCREMENT PRIMARY KEY,
    client_name VARCHAR(100) NOT NULL,
    phone VARCHAR(20) NOT NULL,
    email VARCHAR(254) NOT NULL,
    occasion_description VARCHAR(200) NOT NULL,
    preferences TEXT,
    status VARCHAR(20) DEFAULT 'new',
    created_at DATETIME NOT NULL
);
