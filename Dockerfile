FROM python:3.13-slim

WORKDIR /lab

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt \
    && useradd --create-home simulator

COPY --chown=simulator:simulator simulace/encrypt.py simulace/decrypt.py ./simulace/
COPY --chown=simulator:simulator simulace/ransom_note.html ./simulace/
COPY --chown=simulator:simulator testovaci_data/ ./testovaci_data/

USER simulator

CMD ["/bin/sh"]
