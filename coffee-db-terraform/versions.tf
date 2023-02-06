terraform {
  backend "s3" {
    bucket         = "terraform-backend-state-npw"
    key            = "terraform.tfstate"
    region         = "eu-west-2"
    dynamodb_table = "app-state"
  }
  required_providers {
    heroku = {
      source  = "heroku/heroku"
      version = "~>5.0"
    }
  }
}


#provider "heroku" {
#  email   = var.heroku_email
#  api_key = var.heroku_token
#}