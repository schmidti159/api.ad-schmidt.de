#!/usr/bin/env python3.6
import os
from flask import Flask
from flask import render_template
from flask import request
import json
import subprocess
import sys
import hmac
import hashlib
from secrets import API_SECRET

app = Flask(__name__)

VALID_BRANCH_NAMES=['pre-prod','master']
VALID_REPO_NAMES=['schmidti159/blog.ad-schmidt.de']

@app.route("/")
def index():
    return "nothing to be seen here, but thank you for dropping by"

@app.route("/github-webhook", methods=['POST'])
def githubWebhook():
    if not verifySignature():
        return 'signature verification failed'

    content = request.json
    branch = content['ref'].partition('refs/heads/')[2]
    if not branch in VALID_BRANCH_NAMES:
        print(branch+' does not match any of the branches in '+str(VALID_BRANCH_NAMES)+'. Skipping this event.')
        return 'skipped'
    if not content['repository']['full_name'] in VALID_REPO_NAMES:
        print(content['repository']['full_name']+' does not match any of the repos in '+str(VALID_REPO_NAMES)+'. Skipping this event.')
        return 'skipped'
    # check out and compile content
    subprocess.run(['git','pull','origin',branch], stdout=sys.stdout, stdin=sys.stdin, cwd='blog.ad-schmidt.de')
    subprocess.run(['bash','deploy.sh'], stdout=sys.stdout, stdin=sys.stdin, cwd='blog.ad-schmidt.de')
    return "ok"

def verifySignature():
    signature = "sha256="+hmac.new(bytes(API_SECRET , 'utf-8'), msg = request.data, digestmod = hashlib.sha256).hexdigest().lower()
    return hmac.compare_digest(signature, request.headers['X-Hub-Signature-256'])

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=9003, debug=True)
