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
│   ├── # In case you are experience with devcontainers
│   ├── # the files to ensure environment consistency between developement
│   ├── devcontainer.json
│   ├── docker-compose.yml
│   ├── Dockerfile
│   └── post-install.sh
    # My webapp Deployment file
├── Dockerfile-Production 

├── flask_backend
│   ├── # Contains my python-flask webapp
│   ├── app.py
│   ├── __init__.py

    # Some live configuration for gunicorn
    # That I have used in the past to have juntekim.com deployed
├── gunicorn.conf.py

    # This message
├── hiring_manager_msg.md

├── k8s
│   ├── # My kubernetes deployment file in RAW goodness
│   ├── # Limited experience in Kustomize and Helm but excited to learn
│   └── # and next logical step for more fancy k8s file deployment
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

I initially planned to use my self-hosted microk8s to deploy live production for the PSPDFKit app. However, due to constraints with the private repository, this wasn’t feasible in this challenge's time frame.

I am also more diversed in gitlab pipeline but I seem to be lacking on how github does things. I would appreciate any insights into how PSPDFKit structures their pipelines. 

# Other branches
I have numbered and left the other branches intact within this repoistory so you can *git diff*.


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

This helps ensure all pods and services are routed correctly before accessing the server.

### Logging
Logs are essential for debugging, monitoring requests, and tracking events in the application lifecycle.

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

Within traefik documentation, traefik provides a way to capture logs and output them to a file. Via their traefik yaml file:
```yaml
log:
  level: DEBUG
  filePath: "/path/to/traefik.log"
accessLog:
  filePath: "/path/to/all_pod_logs_on_k8.log"
```

Source of knowledge: https://traefik.io/blog/log-aggregation-in-kubernetes-with-traefik-proxy/

From docs: https://doc.traefik.io/traefik/observability/access-logs/

As logs grow more verbose, filtering by headers, timestamps, and identifiers becomes essential for clarity.

I have solved some of these issues by deploying an ELK stack in my previous line of work.

The ELK stack will provide central logging for all pods, maybe even for different clusters and allow powerful search and analysis tools (filter). The kibana webview will also allow you to setup custom dashboards to help you debug an erronously problem and see how it behaves realtime.

### Tracing

End-to-end tracing helps developers and operations teams identify bottlenecks and resolve performance issues within microservices

Traefik by default seems to be using OpenTelemetry (source: https://doc.traefik.io/traefik/observability/tracing/overview/). 

Installation guide on opentelmetry: https://opentelemetry.io/docs/kubernetes/getting-started/

### Metrics Collection:

Traefik docs on metrics: https://doc.traefik.io/traefik/observability/metrics/overview/
 
I have used prometheus and grafana in the past which also taefik supports.


So Prometeus will get data (metrics) from different sources and aggrigate them to one. Then grafana can be used to query the metrics from prometeus and visualise the information.

### Dashboarding 

Since Grafana can be plugged into prometeus we can extract data and visualise. Obviously the promethus data has to be inputted so grafana can query it but the data source could range from antyhing to cpu usuage, memory, pings (latency).

Can also make your own data using python-prometheus: https://github.com/prometheus/client_python

The key things here is that grafana can now be used to visualise the data that we measured.

Developers could use this visulisation to help to debug an performance issue that is happening when the microservice is overloaded, which could be loaded to pod by a test script.


If one of the metrics is disk space and we can track how full a certain disk is.

### Notifications

We can then use grafana to set up alerts/notification to when the disk space is running out. Obviously we can do it for any other metrics but this is a way to simplfy the process.

These alerts could then be plugged onto something that emails/messages/pings a developer to take manual action. ( the alert could also be diverted to a specific person/team, it could also be to trigger an automation).

This allows incident to be delt with in a more timely manner before the disk is completely full. (Provided the developer see and actions on the notification)

Which in turns gives more system reliability and avalibility.

It could also give more peace of mind to the developers as they can focus on their other high priorites until a notification is recieved. (Trade off being without a notification system, they have to watch over the system like a hawk). As a computer can do constant monitoring 24/7.

### Summary

I have chosen solution that integrate with traefik due to the familiarity and modularity of the proxy and my own k8s deployment.

Once everything is in place, here’s an example of how a typical user and developer interaction could unfold.

1) A user visits the website but is met with an unexpected issue—"Hello from PSPDFKit Engineer!" is not displaying as expected.
2) The user reports this issue to the PSPDFKit team, which had not detected the error.
The engineering team investigates the issue using available observability tools. Tracing reveals which pod the user interacted with, and logs indicate erroneous behavior that only occurs in Safari.
3) The developer reproduces the behavior in their local environment, writes a test to cover the edge case, and incorporates it into the CI/CD pipeline. The test now makes the CI/CD fail.
4) The developer resolves the issue, the pipeline passes and pushes the changes via a pull request.
5) During integration testing (maybe at a pull request), another issue is discovered, but with the visibility and logs via the stdout of the pipeline, the developer quickly resolves both the original and new issue.
6) After ensuring all test cases pass, the developer merges their changes and updates relevant documentation.
7) The PSPDFKit team informs the user that the issue has been resolved, and the user is satisfied.
8) The operations team enhances their alerting and monitoring tools to ensure this error does not occur on any browser in the future.


As a result, the problems were detected early, and the issue was resolved before a wider impact. This demonstrates how observability enables rapid identification and resolution of bugs and regressions. By integrating tracing, logging, and monitoring, the development process becomes more efficient, allowing for quicker iterations and higher user satisfaction 

Additionally, developers benefit from improved work-life balance as they can deploy with confidence, knowing that monitoring tools will alert them to any production issues, reducing stress and the need for constant manual-repitive (toil) checks.

Ultimately, these observability tools ensure that production systems are reliable, resilient, and performant, leading to faster iteration cycles and higher user satisfaction.

