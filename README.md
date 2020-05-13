<h1 align="center">Planenews</h1>

A platform where users can create their own articles about any topic that involves planes and a short description of the type of plane that they have experience with. These articles can 
include your own opinion. That's what makes this platform so great!
A common place where people can just share there opinions on the type of planes that they have ever experienced


<br>
<p align="center">
<a href=#>
  <img src="https://github.com/tylerholland12/planenews/blob/master/docs/media/this.png">
  </a>
</p>
<br>

https://github.com/tylerholland12/planenews/blob/master/proposal.md

#Deployment URL


https://planenews.herokuapp.com/
<br>

## Installation using Docker
<br>
Run these commands to install using Docker


### Build Image

```bash
docker build -t image-name .
```

### Run Container

```bash
    docker run --rm --name container-name image-name
```

### Docker-Compose

- Run container of this application running the web image as well as the database image

``` bash
    docker-compose up --build