# Image Node
FROM node:20

WORKDIR /app

# Copie les dépendances
COPY package*.json ./

RUN npm rebuild better-sqlite3

# Installe
RUN npm install

# Copie le reste du code
COPY . .

# Expose le port du serveur Nuxt
EXPOSE 3000

# Lance Nuxt
CMD ["npm", "run", "dev"]

