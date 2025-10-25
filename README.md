# 🚗 Uber Python OOP Practice Proj

## Overview
We'll be build a mini Uber simulation in Python using **object-oriented programming (OOP)**.  
Our goal is to model how Uber works at a small scale — drivers, riders, and rides using classes and methods.

I have written tests to guide you through the project. Please do not put your files inside the tests folder.


---

## Learning Objectives
By the end of this project, you should be able to:
- Create and use **classes** and **objects** in Python.  
- Define **attributes** and **methods** cleanly.  
- Model relationships between objects (composition).  
- Write and pass **unit tests** that validate program behavior.  

---

## Core Classes
| Class | Purpose |
|--------|----------|
| `Driver` | Represents a driver with a name, car model, and ride history. |
| `Rider` | Represents a user who can request rides and rate drivers. |
| `Ride` | Represents a single trip connecting a driver and rider. |
| `Uber` | Manages drivers, riders, and rides (like a dispatcher). |

---

## Stages

### **Stage 1 - Drivers and Riders**
- Implement `Driver` and `Rider` classes.  
- Each should have a few attributes (e.g. name, car model, ride history).  
- Implement `__str__()` or `__repr__()` for readable output.  
- ✅ Tests will check creation and default values.

---

### **Stage 2 - Rides**
- Implement a `Ride` class with attributes:
  - `driver`
  - `rider`
  - `distance` (float, km)
  - `cost` (calculated via `RATE_PER_KM`)
  - `status` (`"requested"`, `"in_progress"`, `"completed"`)
- Implement methods:
  - `start_ride()`
  - `complete_ride()`
- ✅ Tests will check status transitions and cost correctness.

---

### **Stage 3 - Uber App (Dispatcher)**
- Create an `Uber` class that:
  - Keeps a list of available drivers.
  - Assigns drivers to rides.
  - Manages active and completed rides.
- Prevent busy drivers from being reassigned.
- ✅ Tests will check correct assignment and driver availability reset.

---

### **Stage 4 - Ratings (Optional Extension)**
- Riders can rate drivers (1–5 stars) after a ride completes.
- Drivers keep a record of ratings and an average score.
- ✅ Tests will verify correct average calculation.

---

## Testing
All tests are written using **unittest**.

To run them:
```bash
python -m unittest tests/test_blah.py