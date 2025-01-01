# Use the official MySQL image as the base
FROM mysql:5.7

# Copy the initialization SQL script into the MySQL init directory
COPY init.sql /docker-entrypoint-initdb.d/

# Expose the MySQL port
EXPOSE 3306
