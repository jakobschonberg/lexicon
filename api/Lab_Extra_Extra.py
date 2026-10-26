import os
from dotenv import load_dotenv
from api_client import get_json, get_request
from pathlib import Path
from re import sub
from time import sleep

dotenv_path = Path('../.venv/.env')
load_dotenv(dotenv_path=dotenv_path)
token = os.getenv("GITHUB_TOKEN")
if len(token) == 40:
  headers = {'Authorization': f"Bearer {token}", 'X-GitHub-Api-Version': '2026-03-10'}
  user = "jakobschonberg"
  user = sub(r'[^a-zA-Z0-9\-\_]', '', user)
  print(user)

  response = get_request("https://api.github.com/user/repos?type=private", headers= headers)
  print(response)
  repos = response.json()
  print(len(repos))
  #print(repos)
  for repo in repos:
    if (repo['name'] == 'Group-7-gym-app'):
      print(repo['html_url'], repo['url'])

  sleep(0.2)

  # response = get_request("https://api.github.com/repos/jakobschonberg/Group-7-gym-app/issues", headers= headers)
  # print(response)
  # issues = response.json()
  # print(len(issues))
  # for issue in issues:
  #   if issue["number"] == 8:
  #     print(issue)

  response = get_request("https://api.github.com/repos/jakobschonberg/Group-7-gym-app/issues/8/issue-field-values", headers= headers)
  print(response)
  # 404
  # It would seem issue-field-values is for organizations only as of 2026 api :(
  # So... as a non-org maybe you can do it through the MCP server? but not via normal api