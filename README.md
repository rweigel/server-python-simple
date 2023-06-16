Simple Python HAPI server using FastAPI and asyncio

# Running

```
pip install git+https://github.com/rweigel/server-python-simple.git@main
python hapi/hapi.py &
curl http://0.0.0.0/hapi
```

# Testing

```
git clone https://github.com/rweigel/server-python-simple
pip install -e '.[dev]'
pytest hapi/test_hapi.py
```