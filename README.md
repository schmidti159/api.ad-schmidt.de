
API for other things on ad-schmidt.de - Implemented by a small flask app

# Endpoints
Currently the following endpoints are available
* `GET /` return a string response to test if the service is available
* `POST /github-webhook` can be used pull new changes from [blog.ad-schmidt.de](https://github.com/schmidti159/blog.ad-schmidt.de) and update https://blog.ad-schmidt.de
It will be called for every push to the blog-repo.

# Setup
## Secrets
Copy `secrets.py.template` to `secrets.py` and enter the secret entered in the GitHub configuration for the webhook.
