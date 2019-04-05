From node:10
# Set work directory.
RUN mkdir /app
WORKDIR /app

# Install dependencies.
COPY package.json  /app/
RUN npm install
# Copy project code.
COPY . /app/
EXPOSE 4200
CMD ["npm", "start"]
