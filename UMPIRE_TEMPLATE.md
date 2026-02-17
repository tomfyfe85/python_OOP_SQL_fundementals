PART 3: Office class that works with interfaces (MEDIUM DIFFICULTY)

Class: Office

Attributes:

- devices: list - stores all devices

Methods:

- **init**(): Initialize empty devices list

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
