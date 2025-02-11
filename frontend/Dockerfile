FROM node:16

WORKDIR /app

# Copy package.json and package-lock.json first
COPY package.json package-lock.json ./

# Install dependencies
RUN npm install

# Copy the rest of the frontend files
COPY . .

# Expose React's default port
EXPOSE 3000

# Start the React app
CMD ["npm", "start"]
