# Dockerfile

# FROM base image to build upon
FROM phusion/passenger-customizable:0.9.24 

#RUN install python support
RUN /pd_build/python.sh

# RUN install python and pip
RUN apt-get update
RUN apt-get install -y python python-pip python-dev 

# ENV set environment directory tree
ENV PROJECT=mysite
ENV CONTAINER_HOME=/opt
ENV CONTAINER_PROJECT=$CONTAINER_HOME/$PROJECT

# move to project WORKDIR
WORKDIR $CONTAINER_PROJECT

# COPY project to container directory
COPY . $CONTAINER_PROJECT

# RUN pip and install requirements
RUN pip install -r requirements.txt


# COPY start.sh into known container location 
COPY start.sh /start.sh

# EXPOSE port 8000 to allow communication to/from server
EXPOSE 8000

# CMD execute start.sh to start the server running.
CMD ["/start.sh"]
# done!