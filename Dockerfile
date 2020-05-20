FROM python:3
ADD azuremsi_readblob.py /
CMD [ "python", "azuremsi_readblob.py" ]
