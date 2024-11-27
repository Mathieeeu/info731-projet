#!/bin/sh

# Créer la base de données 'firewall_logs'
mysql -u root -p -e "CREATE DATABASE IF NOT EXISTS firewall_logs;"

# Créer la table 'http_requests' dans la base de données 'firewall_logs'
mysql -u root -p -D firewall_logs -e "
CREATE TABLE IF NOT EXISTS http_requests (
    id INT AUTO_INCREMENT PRIMARY KEY,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    source_ip VARCHAR(45),
    host TEXT,
    allowed BOOLEAN
);"

# Accorder tous les privilèges à l'utilisateur 'root' avec le mot de passe 'password'
mysql -u root -p -e "GRANT ALL PRIVILEGES ON firewall_logs.* TO 'root' IDENTIFIED BY 'password';"

# Test de la connexion avec le nouveau mot de passe
mysql -u root -ppassword -e "SELECT 1;"


# # Insersion de données dans la table 'http_requests'
# # Variables pour l'insertion
# SOURCE_IP="192.168.1.1"
# HOST="http://example.com"
# ALLOWED=true

# # Insérer une nouvelle requête HTTP dans la table
# mysql -u root -ppassword -D firewall_logs -e "
# INSERT INTO http_requests (source_ip, host, allowed)
# VALUES ('$SOURCE_IP', '$HOST', $ALLOWED);"
