FROM node:15-alpine
WORKDIR /app
COPY package.json package-lock.json ./
RUN npm install --legacy-peer-deps
COPY . .
# Build React app into /app/build directory
# RUN npm run prod
# Expose port
EXPOSE 3000
# Run app
CMD ["npm", "run", "start"]
###