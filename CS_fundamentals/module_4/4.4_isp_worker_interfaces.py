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

LEARNING OBJECTIVES:

1. Understand why fat interfaces are problematic
2. Learn to split interfaces by capability
3. Practice multiple inheritance with ABCs
4. Use isinstance() to check for specific capabilities
5. See how ISP leads to more flexible, maintainable code

ESTIMATED TIME: 30-45 minutes
"""

from abc import ABC, abstractmethod

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

class SimplePrinter(Printable):
    def print_document(self, document):
        return f"Printing: {document}"

class SimpleScanner(Scannable):
    def scan_document(self):
        return "Scanned document content"

class AllInOnePrinter(Printable, Scannable, Faxable):
    def print_document(self, document):
        return f"[All-in-One] Printing: {document}"

    def scan_document(self):
        return "[All-in-One] Scanned document content"
    
    def fax_document(self, document, number):
        return f"[All-in-One] Faxing '{document}' to {number}"

class ModernPrinter(Printable, Scannable):
    def print_document(self, document):
      return f"[Modern] Printing: {document}"
    
    def scan_document(self):
      return f"[Modern] Scanned document content"
    

# Part 3
class Office():
    def __init__(self):
        self.devices_list = []

    def add_device(self, device) -> None:
        self.devices_list.append(device)

    def print_to_all(self, document: str) -> list[str]:
        document_list = []
        for device in self.devices_list:
            if isinstance(device, Printable):
                document_list.append(device.print_document(document))
        return document_list
    
    def scan_from_any(self) -> str | None:
        for device in self.devices_list:
            if isinstance(device, Scannable):
                return device.scan_document()
        return None

    def get_fax_machines(self) -> list:
        devices_that_fax = []
        for device in self.devices_list:
            if isinstance(device, Faxable):
                devices_that_fax.append(device)
        return devices_that_fax

    def get_device_capabilities(self, device) -> list[str]:
        device_capabilities = []
        if isinstance(device, Faxable):
            device_capabilities.append("fax")
        if isinstance(device, Scannable):
            device_capabilities.append("scan")
        if isinstance(device, Printable):
            device_capabilities.append("print")
        return device_capabilities

class PrintJobManager():
    def __init__(self):
        self.devices_list = []
        self.job_queue_list = []

    def add_device(self, device):
        self.device_list = []

    def submit_job(self, job_type: str, content:str, **kwargs) -> int:
        job = {"id": len(self.job_queue_list - 1),
                'type': job_type, "content": content,
              "status": "pending"}
        if kwargs:
            for key ,value in kwargs.items():
                job[key] = value
              
        self.job_queue_list.append(job)

        return job['id']


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