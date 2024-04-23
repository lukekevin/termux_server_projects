require 'sinatra'

set :public_folder, 'public'
set :bind, '0.0.0.0'

# Store messages in an array (for simplicity, you might want to use a database in a real-world scenario)
 messages = []
#
get '/' do
  erb :index, locals: { messages: messages }
end
post '/message' do
  message = params[:message]
  messages << message
  redirect '/'
end
