# Flask Issues

## Run locally

```Bash
pip install -r requirements.txt
gunicorn app:app
```

Server listening at http://127.0.0.1:8000

## Outputs

For `outputs` folder, you must run this [Jupyter Notebook](https://colab.research.google.com/drive/1xFxOXfDYlMbUCPrxSaOzvHKmxx2cihAE?usp=sharing) and download it

## How use

```Bash
curl 'http://127.0.0.1:8000?owner={owner}&repo={repo}&issue={issue}'
```

### Example

```Bash
curl 'http://127.0.0.1:8000?owner=nestjs&repo=nest&issue=100'
```
