FROM python:3-alpine
LABEL authors="Victoria Torres"

RUN apk update
RUN apk add git
RUN git clone https://github.com/um-computacion-tm/scrabble-2023-vickytorresburgos.git
WORKDIR scrabble-2023-vickytorresburgos 
RUN pip install -r requirements.txt
RUN git checkout develop

CMD [ "sh", "-c", "coverage run -m unittest && coverage report -m && python -m game.main" ]