npm install;
if [ "$SERVER_ENV" = "production" ]
  then
    echo "Building for production"
    webpack;
else
  echo "Building for development and watching"
  webpack -w;
fi
