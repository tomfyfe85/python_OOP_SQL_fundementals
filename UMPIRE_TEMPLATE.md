
PART 4: PrintJobManager (HARD - Beyond Office)

Create a print job manager that queues and processes jobs based on device capabilities.

Class: PrintJobManager

Attributes:
- devices: list - available devices
- job_queue: list - pending jobs (each job is a dict)

Methods:
- __init__(): Initialize empty devices list and job_queue

- process_next_job() -> dict:
  Process the first pending job in the queue
  Find a device that can handle the job type (use isinstance)
  If device found:
    - Execute the job (call appropriate method on device)
    - Update job status to "completed"
    - Add "result" key with the return value from the device
    - Add "device" key with device class name
  If no capable device:
    - Update job status to "failed"
    - Add "error" key with message "No capable device available"
  Return the job dict

- process_all_jobs() -> list[dict]:
  Process all pending jobs
  Return list of all job dicts (with updated statuses)

- get_job_status(job_id: int) -> dict | None:
  Return the job dict for given job_id, or None if not found

- get_pending_jobs() -> list[dict]:
  Return list of all jobs with status "pending"

- get_completed_jobs() -> list[dict]:
  Return list of all jobs with status "completed"

- get_failed_jobs() -> list[dict]:
  Return list of all jobs with status "failed"

- get_statistics() -> dict:
  Return:
  {
    "total_jobs": int,
    "pending": int,
    "completed": int,
    "failed": int,
    "jobs_by_type": {"print": int, "scan": int, "fax": int}
  }

THE HARD CHALLENGES:
1. Matching job types to device capabilities using isinstance()
2. Managing job state transitions (pending -> completed/failed)
3. Handling jobs that can't be processed (no capable device)
4. Processing jobs in queue order
5. Tracking statistics across job types and statuses

This is harder than Office because:
- Office: Check capabilities and call methods directly
- PrintJobManager: Queue jobs, match to devices, track state, handle failures
