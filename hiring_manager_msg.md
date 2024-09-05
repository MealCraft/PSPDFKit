# Hello World

Dear Hiring Manager,

I wanted to express my gratitude for the enjoyable exercise that allowed me to showcase my skill set.

Regardless of the outcome, I know that this experience, along with any feedback you provide, will make me a better developer, for which I am thankful.

Hoping for us to have a conversation at the very least,

Best wishes

Jun-te Kim

# File structure (tree .)

```sh
.
├── .devcontainer
│   ├── # in the off chance you are experience with devcontainers
│   ├── # here are these files so it excuses me from the 'but it works on my computer'
│   ├── devcontainer.json
│   ├── docker-compose.yml
│   ├── Dockerfile
│   └── post-install.sh
    # My webapp Deployment file
├── Dockerfile-Production 

├── flask_backend
|   ├── # Contains my python-flask webapp
│   ├── app.py
│   ├── __init__.py

    # Some live configuration for gunicorn
    # That I have used in the past to have juntekim.com deployed
├── gunicorn.conf.py

    # This message
├── hiring_manager_msg.md

├── k8s
    ├── # My kubernetes deployment file in RAW goodness
    ├── # Limited experience in Kustomize and Helm but excited to learn
    ├── # and next logical step
│   ├── deployment.yaml
│   ├── ingressroute.yaml
│   └── services.yaml
    # Dubious poetry file to ensure python
├── poetry.lock
├── pyproject.toml

    # My to do list to stay on spec
├── README.md

    # Provided you are running from the devcontainer. Some helper scripts
├── run_tests.sh # runs pytest locally
├── startProduction.sh # runs production server locally
├── startWebServerLocally.sh # runs flask server locally
└── tests
    ├── # Basic tests file for pytest to test flask server
    ├── conftest.py
    ├── __init__.py
    └── test_main.py
```
# Phase 2.5 K8s deployment

I have a small spare laptop that I've converted into a ubunutu server. 

I have microk8s and the github runner installed for my 'mealcraft' organisation and is currently hosting www.juntekim.com and www.mealcraft.com, which are both reachable via the web.

I was hoping I could just use my self-hosted microk8s to deploy the k8s files for live production to show you the pspdfkit flask web app **LIVE** but regretfully I have to do that with a *private* repository.

I'll be happy to get everything running **LIVE** as a seperate task but I think givien the time constraint I should make a start on PHASE 3.

I am also more diversed in gitlab pipeline but I seem to be lacking on how github does things. I'll be excited to know how you *should* or how PSPDFKit structure their pipeline yaml files to for tag released, features branches and pull requests. Pointing me to further reading materials/docs is also fine.

# Other branches
I have numbered and left the other branches intact within this repoistory so you can *git diff*.

I hope this will be useful to you but not sure in reality. Nevertheless, it is there for your own amusement/time-sink.


# Phase 3
On my microk8s set up. I have a [traefik pod](https://doc.traefik.io/traefik/) running.

This is used to proxy all my k8s deployment and services.

Fortunately, Traefik offers some way to start on metrics.

### Dashboard
Traefik offers a dashboard for developers avaliable at https://traefik.mealcraft.com/dashboard/#/

You'll need a username and password to enter this dashboard which I will forward via email, incase you are curious.

The dashboard is crucial to see an overview of the pods, services and other traefik services such as [*middlesware*](https://doc.traefik.io/traefik/middlewares/overview/).

[Imgur](https://imgur.com/FxDk5HU)


It also displays how each pod is entered by a certain entry point:

[Imgur](https://imgur.com/VL0bUgC)

I have used this to help me debug routing on kubernetes and all pods/services are up before *ssh*-ing to the server.

### Logging
It is very useful to go into a pod and

```console
kimjunte@gpd:~$ k get pods
NAME                                   READY   STATUS    RESTARTS      AGE
juntekim-deployment-7db744cb78-tgh6v   1/1     Running   0             4d11h
portfolio-page-5fcdc45f55-7rw2v        1/1     Running   0             2d13h
traefik-deployment-58f44d6dc8-kmhlb    1/1     Running   1 (16d ago)   17d
whoami-57b48994d9-2wk26                1/1     Running   3 (16d ago)   17d
whoami-57b48994d9-7wbcm                1/1     Running   3 (16d ago)   17d
kimjunte@gpd:~$ k logs juntekim-deployment-7db744cb78-tgh6v | tail -n 10
[2024-08-31 22:36:22 +0000] [18] [INFO] Booting worker with pid: 18
[2024-08-31 22:36:22 +0000] [19] [INFO] Booting worker with pid: 19
[2024-08-31 22:36:22 +0000] [20] [INFO] Booting worker with pid: 20
[2024-08-31 22:36:22 +0000] [21] [INFO] Booting worker with pid: 21
[2024-08-31 22:36:22 +0000] [1] [DEBUG] 9 workers
[2024-08-31 22:37:06 +0000] [14] [DEBUG] GET /newsletter
[2024-08-31 22:43:33 +0000] [19] [DEBUG] GET /newsletter
[2024-08-31 22:44:40 +0000] [18] [DEBUG] GET /newsletter
[2024-09-01 17:38:09 +0000] [18] [DEBUG] GET /newsletter
[2024-09-02 20:10:14 +0000] [18] [DEBUG] GET /newsletter
```


