# frontend/Dockerfile
FROM node:20-alpine

# Set working directory
WORKDIR /app

# Copy package files
COPY package*.json ./

# Install dependencies
RUN npm install

# Rebuild native modules for the container architecture
RUN npm rebuild better-sqlite3

# Copy project files
COPY . .

# Expose port
EXPOSE 3100

# Start development server
CMD ["npm", "run", "dev", "--", "--host", "0.0.0.0", "--port", "3100"]