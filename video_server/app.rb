require 'sinatra'
require 'json'
set :bind, '0.0.0.0'
set :port, 4567

# Set the public folder to the directory where your videos are stored in Nginx
set :public_folder, '/data/data/com.termux/files/home/ruby_video_server/videos/'

get '/' do
  @videos = Dir.glob('/data/data/com.termux/files/home/ruby_video_server/videos/*.{mp4,mkv}').map { |file| File.basename(file) }
  erb :index
end
