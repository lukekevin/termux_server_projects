require 'sinatra'

set :bind, '0.0.0.0'
set :port, 4567
# Define the directory where your photos are stored on your Android device
PHOTOS_DIRECTORY = '/data/data/com.termux/files/home/pictures'

# Serve the index page
get '/' do
  erb :index
end

# Serve the photos
get '/photos/:photo_name' do |photo_name|
  send_file File.join(PHOTOS_DIRECTORY, photo_name)
end
