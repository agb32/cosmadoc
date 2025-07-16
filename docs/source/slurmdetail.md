# COSMA Scheduling and Fairshare Overview

COSMA uses SLURM to manage job scheduling and access to the compute resources
(nodes, CPU cores, and memory) across its various clusters.

SLURM assigns a priority to each job to determine the order in which they are
considered for scheduling. However, a job will only start when the resources
it needs are actually available, so scheduling is not a simple first-in,
first-out queue based on priority.

A job's priority is determined using several factors, including:

    - The user's fairshare score.
    - The total computing time the user has already consumed.
    - The age of the job (how long it has been queued).
    - The size of the job (cores, nodes).

In the current configuration, all users are assigned equal fairshare, ensuring
that everyone starts with the same likelihood of scheduling their jobs.

Larger jobs are given preference. This reflects the cluster's primary goal of
supporting large-scale computations. Prioritising large jobs also improves
overall scheduling efficiency, as it helps prevent resource blocking and
fragmentation caused by pending large jobs.

To support this policy, additional scheduling mechanisms are available through
the prince queues, which run at a priority that guarantees scheduling ahead of
the other queues, and reservations that provide exclusive access to parts of
the cluster.

This approach offers several advantages:

    - It is simple, transparent, and easy to maintain.
    - It has proven effective over time.
    - Equal fairness among users supports smaller projects and development
      work, ensuring timely access to resources.

# Pauper Queues

To complement the main scheduling system, COSMA also includes pauper
queues. These are lower-priority queues with shorter maximum
runtimes. Projects that have exceeded their quarterly allocation are
automatically directed to use these queues.

The purpose of the pauper queues is to allow continued access to the system
while ensuring fair resource distribution. Jobs submitted to these queues will
only run when there are otherwise idle resources available, helping to
maintain high overall system efficiency without disrupting higher-priority
workloads.

Pauper access is also granted during the first quarter after a project has
ended -- that is, when it no longer has an active allocation. This grace
period is intended to allow the completion of any remaining work. Without
this, projects might be forced to abandon or pause their work until new
resources are awarded (which could lead to the same outcome -
abandonment). However, this access is not intended for starting new
work. Philosophically it also reflects that working to artificial deadlines
can be difficult.

# Backfilling


All COSMA queues support backfilling, a key feature for improving system
efficiency. Backfilling allows smaller or shorter jobs to be run out of order
if they can fit into gaps in the schedule without delaying higher-priority
jobs.

This is possible because longer-running jobs often hold future reservations on
resources due to their priority and requirements, leaving those resources
temporarily idle.

For backfilling to work effectively, it is essential that users provide
realistic runtime estimates when submitting jobs. If all jobs are submitted
with identical or overly conservative runtimes, the scheduler cannot make
informed decisions, and the system would behave more like a simple priority
queue, reducing overall efficiency.

Backfilling is also an excellent tool for developers, as it allows short jobs
to run quickly helping to speed up the development and testing cycle.


# Assumptions for Good Outcomes in This System


While assigning equal shares to all users may seem mismatched with the reality
that projects have differing allocations, this approach has worked effectively
for many years. Most projects have been able to use their allocations
successfully. Occasional complaints typically stem from misunderstandings
about how the system operates, rather than from systemic issues.

A key underlying assumption is that projects with large allocations also have
a large number of active users. This ensures that resources are consistently
in use -- either through many users submitting jobs or through the regular
submission of large jobs. Until recently, this assumption has generally held
true.

Another important factor is the presence of some idle capacity in the
system. A certain level of unused resources is necessary to maintain
responsiveness and flexibility, allowing the scheduler to accommodate jobs
efficiently and avoid bottlenecks.

