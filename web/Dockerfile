# Build environment
FROM node:18.6 as build
WORKDIR /usr/src/app

# Install dependencies
COPY ["package.json", "yarn.lock", "./"]
RUN yarn install

COPY . .

RUN yarn build

# Nginx stage for serving react app
FROM nginx:1.23

COPY --from=build /usr/src/app/build /usr/share/nginx/html
COPY --from=build /usr/src/app/nginx/nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
