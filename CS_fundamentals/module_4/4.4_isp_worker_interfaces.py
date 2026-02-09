"""
Exercise 4.4: Interface Segregation Principle (ISP)

INTERFACE SEGREGATION PRINCIPLE

Definition: Clients should not be forced to depend on interfaces they don't use.

In other words:
- Don't create FAT interfaces with many methods
- Split large interfaces into smaller, focused ones
- Classes should only implement what they actually need

===================================
ISP vs LSP (What's the difference?)
===================================

LSP: "Can a subclass BEHAVE correctly when substituted?"
      - About behavioral compatibility
      - Penguin inheriting fly() that raises exception = LSP violation

ISP: "Should a class be FORCED to implement methods it doesn't need?"
      - About interface design
      - Penguin being forced to implement fly() at all = ISP violation

They're related! ISP helps PREVENT LSP violations by design.

===================================
BAD APPROACH (violates ISP)
===================================

    from abc import ABC, abstractmethod

    class Worker(ABC):
        @abstractmethod
        def work(self) -> str:
            pass

        @abstractmethod
        def eat(self) -> str:
            pass

        @abstractmethod
        def sleep(self) -> str:
            pass

        @abstractmethod
        def take_break(self) -> str:
            pass

    class HumanWorker(Worker):
        def work(self) -> str:
            return "Human working"
        def eat(self) -> str:
            return "Human eating"
        def sleep(self) -> str:
            return "Human sleeping"
        def take_break(self) -> str:
            return "Human on break"

    class RobotWorker(Worker):
        def work(self) -> str:
            return "Robot working"
        def eat(self) -> str:
            raise NotImplementedError("Robots don't eat!")  # ISP violation!
        def sleep(self) -> str:
            raise NotImplementedError("Robots don't sleep!")  # ISP violation!
        def take_break(self) -> str:
            return "Robot in standby"

Problems:
1. RobotWorker is FORCED to implement eat() and sleep()
2. These methods make no sense for robots
3. Raises exceptions = breaks LSP too!
4. The Worker interface is too "fat"

===================================
GOOD APPROACH (follows ISP)
===================================

    from abc import ABC, abstractmethod

    # Split into focused interfaces
    class Workable(ABC):
        @abstractmethod
        def work(self) -> str:
            pass

    class Eatable(ABC):
        @abstractmethod
        def eat(self) -> str:
            pass

    class Sleepable(ABC):
        @abstractmethod
        def sleep(self) -> str:
            pass

    class HumanWorker(Workable, Eatable, Sleepable):
        def work(self) -> str:
            return "Human working"
        def eat(self) -> str:
            return "Human eating"
        def sleep(self) -> str:
            return "Human sleeping"

    class RobotWorker(Workable):  # Only implements what it needs!
        def work(self) -> str:
            return "Robot working"

Benefits:
1. Each interface has ONE purpose
2. Classes only implement what makes sense for them
3. No forced implementations of irrelevant methods
4. Easier to understand and maintain

===================================
EXERCISE: Device Management System
===================================

You're building a system to manage different types of devices.
Some devices can print, some can scan, some can fax, some can do all three.

THE ISP CHALLENGE:
- Don't create one fat "Device" interface with print, scan, and fax
- Instead, create small focused interfaces
- Let devices implement only what they can actually do

---

PART 1: Define the Interfaces (ABC classes)

Create THREE separate abstract base classes:

1. Printable (ABC)
    - @abstractmethod print_document(document: str) -> str

2. Scannable (ABC)
    - @abstractmethod scan_document() -> str

3. Faxable (ABC)
    - @abstractmethod fax_document(document: str, number: str) -> str

---

PART 2: Implement the Devices

1. SimplePrinter (implements Printable only)
    - print_document(document) -> f"Printing: {document}"

2. SimpleScanner (implements Scannable only)
    - scan_document() -> "Scanned document content"

3. AllInOnePrinter (implements Printable, Scannable, Faxable)
    - print_document(document) -> f"[All-in-One] Printing: {document}"
    - scan_document() -> "[All-in-One] Scanned document content"
    - fax_document(document, number) -> f"[All-in-One] Faxing '{document}' to {number}"

4. ModernPrinter (implements Printable, Scannable but NOT Faxable)
    - print_document(document) -> f"[Modern] Printing: {document}"
    - scan_document() -> "[Modern] Scanned document content"
    - No fax capability (fax is outdated!)

---

PART 3: Office class that works with interfaces (MEDIUM DIFFICULTY)

Class: Office

Attributes:
- devices: list - stores all devices

Methods:
- __init__(): Initialize empty devices list

- add_device(device) -> None:
  Add any device to the office

- print_to_all(document: str) -> list[str]:
  Print document to ALL devices that can print
  Use isinstance(device, Printable) to check
  Return list of results from each printer

- scan_from_any() -> str | None:
  Find FIRST device that can scan and use it
  Use isinstance(device, Scannable) to check
  Return scanned content, or None if no scanner available

- get_fax_machines() -> list:
  Return list of all devices that can fax
  Use isinstance(device, Faxable) to check

- get_device_capabilities(device) -> list[str]:
  Return list of capability names for a device
  Check isinstance for each interface
  Return something like ["print", "scan"] or ["print", "scan", "fax"]

---

PART 4: PrintJobManager (HARD - Beyond Office)

Create a print job manager that queues and processes jobs based on device capabilities.

Class: PrintJobManager

Attributes:
- devices: list - available devices
- job_queue: list - pending jobs (each job is a dict)

Methods:
- __init__(): Initialize empty devices list and job_queue

- add_device(device) -> None:
  Add a device to the manager

- submit_job(job_type: str, content: str, **kwargs) -> int:
  Add a job to the queue
  job_type is one of: "print", "scan", "fax"
  For fax jobs, kwargs will include "number" (the fax number)
  Return the job_id (position in queue, starting at 0)
  Store job as dict: {"id": int, "type": str, "content": str, "status": "pending", ...}
  Include any kwargs in the job dict (e.g., "number" for fax)

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

---

LEARNING OBJECTIVES:

1. Understand why fat interfaces are problematic
2. Learn to split interfaces by capability
3. Practice multiple inheritance with ABCs
4. Use isinstance() to check for specific capabilities
5. See how ISP leads to more flexible, maintainable code

ESTIMATED TIME: 30-45 minutes
"""

from abc import ABC, abstractmethod

# ==========================================
# YOUR CODE GOES BELOW
# ==========================================

# PART 1: Define the interfaces (ABCs)
class Printable (ABC):
    @abstractmethod
    def print_document(self, document: str) -> str:
        """Accepts a document and prints it"""
        pass

class Scannable(ABC):
    @abstractmethod
    def scan_document(self) -> str:
        """scans documents returns scanning message"""
        pass
    
class Faxable(ABC):
    @abstractmethod
    def fax_document(self, document:str, number:str) -> str:
        """Accepts a document and a fax no. Returns confirmation message"""
        pass


# PART 3: Office class




# ==========================================
# TEST CASES
# ==========================================

if __name__ == "__main__":
    print("\n=== Test 1: SimplePrinter (Printable only) ===")
    printer = SimplePrinter()
    result = printer.print_document("Hello World")
    assert result == "Printing: Hello World"
    assert isinstance(printer, Printable)
    assert not isinstance(printer, Scannable)
    assert not isinstance(printer, Faxable)
    print(f"✓ SimplePrinter works: {result}")

    print("\n=== Test 2: SimpleScanner (Scannable only) ===")
    scanner = SimpleScanner()
    result = scanner.scan_document()
    assert result == "Scanned document content"
    assert isinstance(scanner, Scannable)
    assert not isinstance(scanner, Printable)
    assert not isinstance(scanner, Faxable)
    print(f"✓ SimpleScanner works: {result}")

    print("\n=== Test 3: AllInOnePrinter (all capabilities) ===")
    allinone = AllInOnePrinter()

    print_result = allinone.print_document("Report")
    assert print_result == "[All-in-One] Printing: Report"
    print(f"✓ Print: {print_result}")

    scan_result = allinone.scan_document()
    assert scan_result == "[All-in-One] Scanned document content"
    print(f"✓ Scan: {scan_result}")

    fax_result = allinone.fax_document("Contract", "555-1234")
    assert fax_result == "[All-in-One] Faxing 'Contract' to 555-1234"
    print(f"✓ Fax: {fax_result}")

    assert isinstance(allinone, Printable)
    assert isinstance(allinone, Scannable)
    assert isinstance(allinone, Faxable)
    print("✓ AllInOnePrinter implements all interfaces")

    print("\n=== Test 4: ModernPrinter (no fax - ISP in action!) ===")
    modern = ModernPrinter()

    print_result = modern.print_document("Photo")
    assert print_result == "[Modern] Printing: Photo"
    print(f"✓ Print: {print_result}")

    scan_result = modern.scan_document()
    assert scan_result == "[Modern] Scanned document content"
    print(f"✓ Scan: {scan_result}")

    assert isinstance(modern, Printable)
    assert isinstance(modern, Scannable)
    assert not isinstance(modern, Faxable), "ModernPrinter should NOT be Faxable!"
    print("✓ ModernPrinter correctly does NOT implement Faxable")

    print("\n=== Test 5: Office - Adding Devices ===")
    office = Office()
    office.add_device(SimplePrinter())
    office.add_device(SimpleScanner())
    office.add_device(AllInOnePrinter())
    office.add_device(ModernPrinter())
    print("✓ Added 4 devices to office")

    print("\n=== Test 6: Office - Print to All ===")
    results = office.print_to_all("Memo")
    assert len(results) == 3, f"Should have 3 printers, got {len(results)}"
    assert "Printing: Memo" in results[0]
    print(f"✓ Printed to {len(results)} devices:")
    for r in results:
        print(f"  - {r}")

    print("\n=== Test 7: Office - Scan from Any ===")
    scan_result = office.scan_from_any()
    assert scan_result is not None
    assert "Scanned" in scan_result
    print(f"✓ Scanned: {scan_result}")

    print("\n=== Test 8: Office - Get Fax Machines ===")
    fax_machines = office.get_fax_machines()
    assert len(fax_machines) == 1, f"Should have 1 fax machine, got {len(fax_machines)}"
    assert isinstance(fax_machines[0], AllInOnePrinter)
    print(f"✓ Found {len(fax_machines)} fax machine(s)")

    print("\n=== Test 9: Office - Device Capabilities ===")
    simple_printer = SimplePrinter()
    caps = office.get_device_capabilities(simple_printer)
    assert caps == ["print"], f"SimplePrinter caps should be ['print'], got {caps}"
    print(f"✓ SimplePrinter capabilities: {caps}")

    allinone = AllInOnePrinter()
    caps = office.get_device_capabilities(allinone)
    assert "print" in caps
    assert "scan" in caps
    assert "fax" in caps
    assert len(caps) == 3
    print(f"✓ AllInOnePrinter capabilities: {caps}")

    modern = ModernPrinter()
    caps = office.get_device_capabilities(modern)
    assert "print" in caps
    assert "scan" in caps
    assert "fax" not in caps
    assert len(caps) == 2
    print(f"✓ ModernPrinter capabilities: {caps}")

    print("\n=== Test 10: ISP Demonstration ===")
    # This is the key insight!
    # Each device only implements what it can actually do
    # No forced implementations of irrelevant methods

    devices = [SimplePrinter(), SimpleScanner(), AllInOnePrinter(), ModernPrinter()]

    print("Device capabilities:")
    for device in devices:
        caps = office.get_device_capabilities(device)
        print(f"  {device.__class__.__name__}: {caps}")

    print("\n✓ ISP allows each device to implement only what it needs!")

    print("\n=== Test 11: No Forced Implementations ===")
    # Verify that devices don't have methods they shouldn't have
    simple_printer = SimplePrinter()
    assert not hasattr(simple_printer, 'scan_document') or not callable(getattr(simple_printer, 'scan_document', None)), \
        "SimplePrinter should not have scan_document"
    assert not hasattr(simple_printer, 'fax_document') or not callable(getattr(simple_printer, 'fax_document', None)), \
        "SimplePrinter should not have fax_document"
    print("✓ SimplePrinter doesn't have scan or fax methods")

    simple_scanner = SimpleScanner()
    assert not hasattr(simple_scanner, 'print_document') or not callable(getattr(simple_scanner, 'print_document', None)), \
        "SimpleScanner should not have print_document"
    print("✓ SimpleScanner doesn't have print or fax methods")

    print("\n✓✓✓ Parts 1-3 passed! ✓✓✓")

    # ==========================================
    # PART 4 TESTS (HARD) - Uncomment when ready
    # ==========================================

    # print("\n" + "="*60)
    # print("PART 4: PrintJobManager (HARD)")
    # print("="*60)

    # print("\n=== Test 12: PrintJobManager - Setup ===")
    # manager = PrintJobManager()
    # manager.add_device(SimplePrinter())
    # manager.add_device(AllInOnePrinter())
    # print("✓ Added SimplePrinter and AllInOnePrinter to manager")

    # print("\n=== Test 13: PrintJobManager - Submit Jobs ===")
    # job_id1 = manager.submit_job("print", "Document 1")
    # job_id2 = manager.submit_job("scan", "")
    # job_id3 = manager.submit_job("fax", "Contract", number="555-1234")
    # assert job_id1 == 0
    # assert job_id2 == 1
    # assert job_id3 == 2
    # print(f"✓ Submitted 3 jobs with IDs: {job_id1}, {job_id2}, {job_id3}")

    # print("\n=== Test 14: PrintJobManager - Get Pending Jobs ===")
    # pending = manager.get_pending_jobs()
    # assert len(pending) == 3
    # assert all(job["status"] == "pending" for job in pending)
    # print(f"✓ Found {len(pending)} pending jobs")

    # print("\n=== Test 15: PrintJobManager - Process Next Job ===")
    # result = manager.process_next_job()
    # assert result["status"] == "completed"
    # assert result["type"] == "print"
    # assert "result" in result
    # assert "device" in result
    # print(f"✓ Processed job: {result}")

    # print("\n=== Test 16: PrintJobManager - Process All Jobs ===")
    # results = manager.process_all_jobs()
    # assert len(results) == 2  # 2 remaining jobs
    # print("✓ Processed remaining jobs:")
    # for r in results:
    #     print(f"  - {r['type']}: {r['status']}")

    # print("\n=== Test 17: PrintJobManager - Job Status ===")
    # job = manager.get_job_status(0)
    # assert job is not None
    # assert job["status"] == "completed"
    # print(f"✓ Job 0 status: {job['status']}")

    # assert manager.get_job_status(999) is None
    # print("✓ Returns None for non-existent job")

    # print("\n=== Test 18: PrintJobManager - Failed Jobs (No Capable Device) ===")
    # manager2 = PrintJobManager()
    # manager2.add_device(SimpleScanner())  # Can only scan!
    # manager2.submit_job("print", "Document")  # No printer available!
    # result = manager2.process_next_job()
    # assert result["status"] == "failed"
    # assert "error" in result
    # assert "No capable device" in result["error"]
    # print(f"✓ Job failed correctly: {result['error']}")

    # print("\n=== Test 19: PrintJobManager - Get Completed/Failed Jobs ===")
    # completed = manager.get_completed_jobs()
    # failed = manager.get_failed_jobs()
    # assert len(completed) == 3
    # assert len(failed) == 0
    # print(f"✓ Completed: {len(completed)}, Failed: {len(failed)}")

    # failed2 = manager2.get_failed_jobs()
    # assert len(failed2) == 1
    # print(f"✓ Manager2 has {len(failed2)} failed job(s)")

    # print("\n=== Test 20: PrintJobManager - Statistics ===")
    # manager3 = PrintJobManager()
    # manager3.add_device(AllInOnePrinter())
    # manager3.submit_job("print", "Doc1")
    # manager3.submit_job("print", "Doc2")
    # manager3.submit_job("scan", "")
    # manager3.submit_job("fax", "Contract", number="555-0000")
    # manager3.process_all_jobs()

    # stats = manager3.get_statistics()
    # assert stats["total_jobs"] == 4
    # assert stats["completed"] == 4
    # assert stats["pending"] == 0
    # assert stats["failed"] == 0
    # assert stats["jobs_by_type"]["print"] == 2
    # assert stats["jobs_by_type"]["scan"] == 1
    # assert stats["jobs_by_type"]["fax"] == 1
    # print(f"✓ Statistics: {stats}")

    # print("\n=== Test 21: PrintJobManager - Mixed Success/Failure ===")
    # manager4 = PrintJobManager()
    # manager4.add_device(SimplePrinter())  # Can only print!
    # manager4.submit_job("print", "Doc1")
    # manager4.submit_job("scan", "")  # Will fail - no scanner
    # manager4.submit_job("print", "Doc2")
    # manager4.submit_job("fax", "Contract", number="555-0000")  # Will fail - no fax
    # manager4.process_all_jobs()

    # stats = manager4.get_statistics()
    # assert stats["completed"] == 2
    # assert stats["failed"] == 2
    # print(f"✓ Mixed results: {stats['completed']} completed, {stats['failed']} failed")

    # print("\n✓✓✓ All Part 4 tests passed! ✓✓✓")

    print("\n" + "="*60)
    print("ISP KEY LESSONS")
    print("="*60)
    print("\n1. FAT INTERFACES are problematic:")
    print("   - Force classes to implement methods they don't need")
    print("   - Lead to NotImplementedError or pass statements")
    print("   - Violate LSP (broken substitution)")

    print("\n2. SEGREGATED INTERFACES are better:")
    print("   - Printable, Scannable, Faxable are separate")
    print("   - Devices implement only what they can do")
    print("   - No dummy implementations needed")

    print("\n3. Multiple inheritance with ABCs:")
    print("   - Python allows inheriting from multiple ABCs")
    print("   - AllInOnePrinter(Printable, Scannable, Faxable)")
    print("   - ModernPrinter(Printable, Scannable) - no Faxable!")

    print("\n4. isinstance() checks for capabilities:")
    print("   - isinstance(device, Printable) -> can it print?")
    print("   - Allows polymorphic handling of different devices")
    print("   - Office can work with any combination of capabilities")

    print("="*60)