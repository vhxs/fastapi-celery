Quickest example I could come up with where a web server's workers share a common process pool.

When `gunicorn` or `uvicorn` are started with multiple workers, it forks off multiple processes that concurrently handle HTTP requests. If one wants to use a process pool to handle these requests, either (1) each request must create an ephemeral process pool or (2) they must share a long-lived pool

(1) is easy to implement but seems undesirable.

(2) requires a shared object or synchronization of some kind among the web server's worker processes. Sharing a complex object like `multiprocessing.Pool` seems hard to do.

I opted to instead use a Celery server, which every worker process throws tasks at. This is effectively a shared process pool. The behavior we get is as follows: if Celery manages a pool of 15 processes, and two requests come in each requesting to run 10 tasks, then these are 20 tasks total, and 5 of them will block before 5 of the first 15 tasks are run to completion.