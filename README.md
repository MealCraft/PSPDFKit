# Phase 1: Development & Release Artifacts

Create and automate the building of a Go web application to be distributed as a container, using
the following process:

- [x] 1. Create a clean Github repository

- [x] Make a small devcontainer for a flask container application
    - [x] Install Python
    - [x] Start a new python flask server

- [x] 2. Write a very basic HTTP web server application that simply listens on a port and prints
         “Hello from PSPDFKit Engineer!” Nothing fancy or complicated. This doesn’t need to be
         done from memory, it’s not a test of your development technique per se but rather a
         basic level competency.
- [x] 3. Create a Github Action 
    - [x] exec a SAST, 
        - [x] lint and 
        - [x] build ( Build a docker image )
- [x] 4. Create a Github Action that, on each Github Repository Release, 
    - on git push and tag:
        - [x] tests (in pipeline)
        - [x] builds (docker image in pipline)
        - [x] stores the binary (again, depending on your language of choice) as a release asset ( Docker push to docker hub)
        - [ ] TODO: Please feel free to see the docker image here: [Docker Hub - kimjunte/pspdfkit](https://hub.docker.com/r/kimjunte/pspdfkit/tags) 

# Phase 2: Containerization & CI/CD

Frequently deployment occurs in a repo other than the one in which development occurs,
prepare deployment and automate interaction in the following way:

- [x] 1. Create a Dockerfile for the application created in Phase 1
- [x] 2. Create an action which will containerize the released application and store it in a registry
         (DockerHub, GHCR, whatever you like)
- [x] 3. Create a kubernetes definition (Helm Chart, Kustomize, Raw YAML, whatever) that would allow a simple ‘kubectl create ...’ to deploy the application
    - [FAILED] Try to deploy to my k8s cluster. It might not work due to being a public repo, but try
        - This failed due to being a public repository.

# Phase 3: Production Observability

Deployment is only the first part of an applications' lifecycle, in order to satisfy the needs of
customers it must be available and performant, which means it must be observable and
maintainable. 

**Please see hiring_manager_msg.md for answers to these questions** 

- [ ] Please write approx. 1 page to describe how you would personally go about
establishing 
    - [ ] logging 
    - [ ] tracing 
    - [ ] metrics collection
    - [ ] dashboarding 
    - [ ] notifications
    - [ ] alerting

- [ ] Emphasis on how you’d do it and why you’d choose certain solutions and how that all works to
satisfy the needs of your users and developers alike. 

Store this document as Markdown in the repository.

When you are done, provide the links to the Phase 1 & 2 repositories. 

The challenge should take between 30m to 3 hours, not more.