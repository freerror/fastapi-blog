# Get all users
Invoke-RestMethod -Method Get -Uri http://127.0.0.1:8000/users/

# Get a specific user
$user_id = 1
Invoke-RestMethod -Method Get -Uri http://127.0.0.1:8000/users/$user_id

# Get all posts
Invoke-RestMethod -Method Get -Uri http://127.0.0.1:8000/posts/

# Get a specific post
$post_id = 1
Invoke-RestMethod -Method Get -Uri http://127.0.0.1:8000/posts/$post_id

# Create a new user
$user = @{
  name = "Alistair"
  email = "Alistair@example.com"
} | ConvertTo-Json
Invoke-RestMethod -Method Post -Uri http://127.0.0.1:8000/users/ -Body $user -ContentType "application/json"

# Create a new post
$post = @{
  title = "My first blog post"
  content = "This is the content of my first blog post."
  user_id = 1
} | ConvertTo-Json
Invoke-RestMethod -Method Post -Uri http://127.0.0.1:8000/posts/ -Body $post -ContentType "application/json"