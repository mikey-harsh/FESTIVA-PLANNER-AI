# Build stage
FROM node:18-alpine AS build

WORKDIR /app

# Copy package files and install dependencies
COPY package*.json ./
RUN npm install

# Copy source code and build
COPY . .
# Setting this arg allows you to pass API URL at build time if needed
ARG VITE_API_URL
ENV VITE_API_URL=$VITE_API_URL
RUN npm run build

# Production serving stage
FROM nginx:alpine

# Copy the build output to Nginx's web folder
COPY --from=build /app/dist /usr/share/nginx/html

# Expose port 80
EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
