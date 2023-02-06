# Create a new Heroku app
resource "heroku_app" "default" {
  name = "webster-and-webster-test-app"
  region = "eu"
}

# Create a database, and configure the app to use it
resource "heroku_addon" "database" {
  app_id = heroku_app.default.id
  plan   = "heroku-postgresql:mini"
}
