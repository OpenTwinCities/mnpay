npm install -g webpack@1.13.2 webpack-cli@1.5.3
npm install;
if [ "$SERVER_ENV" = "production" ]
  then
    echo "Building for production"
    webpack;
else
  echo "Building for development and watching"
  webpack -w;
fi
