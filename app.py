from flask import Flask, request
from simpletransformers.classification import ClassificationModel
import requests

app = Flask(__name__)


@app.route('/')
def entrypoint():
  owner = request.args.get("owner")
  repo = request.args.get("repo")
  issue = request.args.get("issue")
  token = request.args.get("token")

  r = requests.get(f"https://api.github.com/repos/{owner}/{repo}/issues/{issue}", headers={
    "Authorization": f"baerer {token}"
  })

  data = r.json()
  cor_tab = {0: 'Not a Bug', 1: 'Bug!'}
  model_input = f"{data['title']}\n{data['body']}"
  model = ClassificationModel(
    "roberta", "outputs/checkpoint-938-epoch-1",
    use_cuda=False
  )

  predictions, raw_outputs = model.predict([model_input])
  return {"result": cor_tab[predictions[0]]}


if __name__ == '__main__':
  app.run()
