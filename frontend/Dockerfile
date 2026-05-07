# Build stage
FROM node:20-slim AS build

WORKDIR /app

# Copy package files and install dependencies
COPY package*.json ./
RUN npm install

# Copy all source code
COPY . .

# Pass the Backend URL during the build process
ARG VITE_API_URL
ENV VITE_API_URL=$VITE_API_URL

# Build the React app
RUN npm run build

# Production serving stage (using Nginx)
FROM nginx:stable-alpine

# Copy the built files to Nginx
COPY --from=build /app/dist /usr/share/nginx/html

# Expose the port Nginx uses
EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]

