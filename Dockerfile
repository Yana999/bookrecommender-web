FROM python:3.10

# Create the user that will run the app
RUN adduser --disabled-password --gecos '' ml-api-user

WORKDIR /opt/bookrecwebapp

ENV PORT=8001

# Install requirements
ADD ./ /opt/bookrecwebapp
RUN pip install --upgrade pip &\
    pip install -r /opt/bookrecwebapp/requirements.txt

RUN chmod +x /opt/bookrecwebapp/run.sh &\
    chown -R ml-api-user:ml-api-user ./

USER ml-api-user

EXPOSE 8001

CMD ["bash", "./run.sh"]