
# replicate-protobuf-issue

Helping out in [issue](https://github.com/protocolbuffers/protobuf/issues/5272#issuecomment-433510476)

## how to

```bash
PY_VERSION="3.7"
docker run -it --rm -v $(pwd):/data -w /data python:$PY_VERSION bash
pip3 install -r requirements.txt
python3 debug.py
```

