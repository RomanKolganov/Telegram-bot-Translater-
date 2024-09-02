FROM python:3.10-slim
ENV TOKEN='7064653520:AAG1bTDk3hs4Jnp3vriBcrx3DjHZ8WN6Tu4'
COPY . .
RUN pip install -r requirements.txt
ENTRYPOINT [ "python", "bot91.py" ]