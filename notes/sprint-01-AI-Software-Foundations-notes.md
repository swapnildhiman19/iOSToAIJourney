'''
Absolutely. I actually think **this is one of the most important exercises in the entire roadmap**. If you understand this deeply, everything else (FastAPI, SQLAlchemy, LangGraph, CrewAI, MCP, RAG...) becomes much easier because they are all just **adapters around the same core**.

Also, I remember how we've been learning previously:

* We don't jump directly to code.
* We build intuition first.
* Then we derive the architecture.
* Then you implement.
* I only give hints when you get stuck.
* After each section I become the interviewer and ask "why?" questions.

We'll continue exactly in that style.

I also read the Sprint document you uploaded. The assignment for today is specifically the **Python Domain Boundaries** section and intentionally says **do NOT add FastAPI or Postgres** today.

---

# Today's Learning Goal

Instead of thinking

> "I have to build an in-memory repository."

Think

> "I am learning how to build software that can survive changing databases for the next 10 years."

That is the real lesson.

---

# Before touching code...

Let's answer a question.

Imagine Walmart asks you to build a Task Service.

Version 1:

```
TaskService
        |
   PostgreSQL
```

Looks fine.

Six months later...

Management says

> "We are migrating to DynamoDB."

Now what?

If your service directly imports PostgreSQL...

```
TaskService
      |
 psycopg
      |
 PostgreSQL
```

You now modify every service.

Nightmare.

Instead...

```
TaskService
      |
 TaskRepository
     / \
Memory  Postgres
```

Now only one thing changes.

This idea is called

> **Dependency Inversion**

Notice that this is not about Python.

It is software engineering.

---

# Think like an iOS Engineer

Since you're already strong in Swift, let's translate.

Suppose you have

```swift
protocol UserRepository {
    func save(_ user: User)
}
```

Then

```swift
class UserService {

    let repository: UserRepository

}
```

Later

```
CoreDataRepository
```

or

```
FirebaseRepository
```

or

```
RealmRepository
```

can all be swapped.

Python's

```python
Protocol
```

is almost the same idea.

Not identical...

But conceptually the same.

---

# What are we actually building?

Forget Python.

We're building layers.

```
          User
            |
            |
      Application Service
            |
            |
      Repository Protocol
        /            \
 Memory Adapter   Postgres Adapter
```

Notice something.

The service knows

NOTHING

about memory.

NOTHING

about Postgres.

That's today's lesson.

---

# Today's Components

There are exactly **five pieces**.

```
1. Domain Record
2. Domain Exception
3. Repository Protocol
4. Memory Adapter
5. Application Service
```

Let's understand each.

---

# 1. Domain Record

The roadmap says

> immutable domain record

What does that mean?

Imagine a bank transaction.

```
Transaction

id
amount
createdAt
```

Should someone accidentally do

```
transaction.amount = 1000000
```

?

Absolutely not.

So we make it immutable.

In Swift:

```swift
struct User
```

with

```
let
```

properties.

Python equivalent

```python
@dataclass(frozen=True)
```

Question:

What happens if someone writes

```python
record.title = "abc"
```

after frozen=True?

Think before looking it up.

---

# 2. Domain Exception

Most beginners write

```python
raise Exception("Duplicate")
```

Don't.

Why?

Imagine later you have

```
DuplicateTitle

DuplicateEmail

DuplicateUsername

DuplicateOrder

PaymentFailed

UserBlocked
```

Now your application can react differently.

Instead

```python
class DuplicateTask(Exception):
    pass
```

is much better.

Notice.

Still no FastAPI.

Still no HTTP.

The domain knows nothing about HTTP.

---

# Why?

Because tomorrow

instead of

```
REST API
```

maybe this service is used by

```
CLI

Cron Job

Background Worker

Kafka Consumer
```

If your domain throws

```
HTTPException(409)
```

that's terrible.

The domain should say

> DuplicateTask

The API layer decides

> return 409.

Huge difference.

---

# 3. Repository Protocol

This is probably today's biggest concept.

Instead of

```python
class TaskService:

    repository = InMemoryRepository()
```

we do

```
TaskService
      |
TaskRepository
```

Notice the direction.

Service depends on abstraction.

Not implementation.

This is the same thing as Swift protocols.

---

Imagine tomorrow

```
TaskRepository

      / \
     /   \
Memory   Postgres
```

Service changes?

No.

Exactly the assignment's last question.

> Explain how Postgres replaces Memory without changing the service.

---

# 4. Memory Adapter

Today

we are NOT building persistence.

We're only pretending.

Instead of

```
database
```

we'll keep

```
dict
```

inside memory.

```
{
    "Buy Milk": Task(...)
}
```

Tomorrow

this whole class disappears.

Service remains untouched.

---

# 5. Application Service

This is where business rules live.

Not here

```
FastAPI
```

Not here

```
Postgres
```

Not here

```
Pydantic
```

Only business.

For example

```
create task

generate UUID

generate timestamp

save repository
```

Business logic.

---

# The Most Important Diagram

Keep this forever.

```
                HTTP
                  |
           FastAPI Route
                  |
                  |
         Application Service
                  |
                  |
        Repository Protocol
          /             \
         /               \
 InMemory Adapter   Postgres Adapter
```

Notice arrows.

Everything depends inward.

Never outward.

---

# How to Organize the Project

I would actually recommend **not** writing everything in one file like the sprint example.

Since your assignment says

> "In the existing AI Solutions Platform"

I'd structure it like this:

```
src/

    domain/

        task.py
        exceptions.py

    application/

        service.py
        protocols.py

    persistence/

        memory_repository.py

tests/

    test_service.py
```

This is much closer to production software.

---

# Your Mission (Don't Read the Sprint Code Yet)

I want you to implement it yourself.

Implement these **in order**:

### Step 1

Create an immutable `TaskRecord`.

---

### Step 2

Create `DuplicateTaskTitle`.

---

### Step 3

Create a `TaskRepository` protocol.

Ask yourself:

> What is the minimum API the service needs?

Not what Postgres needs.

---

### Step 4

Implement the memory repository.

Store tasks in a dictionary.

Think carefully:

**What should be the key?**

---

### Step 5

Implement the application service.

Its constructor should receive

```
TaskRepository
```

—not the memory repository.

---

### Step 6

Write **two tests only**, because that's exactly what today's assignment asks for:

* **Create behavior**: creating a new task succeeds and returns the expected record.
* **Duplicate behavior**: creating a second task with the same title raises your domain-specific duplicate exception.

---

# After That

Once you've written your own implementation, we'll do what we've done in earlier sessions:

1. **Code review** (I'll review it like a senior engineer at Walmart).
2. **Architecture review** (we'll verify dependency direction and imports).
3. **Interviewer round** (I'll ask questions like "Why Protocol instead of ABC?" and "Why shouldn't the domain import FastAPI?").
4. **Production evolution** (we'll replace the in-memory adapter with a hypothetical Postgres adapter without changing the service, proving why this design matters).

Finally, we'll add the tooling evidence your assignment requires:

* `uv run pytest -q`
* `uv run ruff check .`
* `uv run mypy .` (or `pyright`)

and interpret any errors rather than just fixing them.

That evidence is explicitly part of today's deliverables.

These are excellent questions. In fact, **your confusion about Domain Exceptions is exactly where most developers first encounter Domain-Driven Design (DDD)**. Let's slow down and build the intuition.

---

# Question 1: Did you understand `frozen=True` correctly?

Yes. Your understanding is **95% correct**.

Let's refine it.

When you write:

```python
from dataclasses import dataclass

@dataclass(frozen=True)
class Record:
    title: str

record = Record("Initial Title")

record.title = "New Title"
```

Python raises something similar to:

```text
dataclasses.FrozenInstanceError:
cannot assign to field 'title'
```

because **the object itself is immutable**.

Think of it exactly like Swift.

Swift:

```swift
struct User {
    let name: String
}

let user = User(name: "Swapnil")

user.name = "John"
```

Compiler:

```
Cannot assign to property:
'name' is a 'let' constant
```

Python simply performs this check at **runtime** instead of compile time.

---

## Does `replace()` modify the object?

No.

This is the important part.

Many beginners think

```python
replace(record)
```

changes the object.

It doesn't.

Imagine memory.

Initially

```text
record
   |
   v
+----------------------+
| title = Initial      |
+----------------------+
```

After

```python
new_record = replace(record, title="New")
```

memory becomes

```text
record                     new_record
   |                            |
   |                            |
   v                            v
+----------------+      +----------------+
| Initial Title  |      | A new val      |
+----------------+      +----------------+
```

Nothing changed.

A **new immutable object** was created.

Exactly like this in Swift:

```swift
struct User {
    let name: String
}

let oldUser = User(name: "Swapnil")

let newUser = User(name: "John")
```

Notice we never modify `oldUser`.

---

# Why do we even want immutability?

Imagine 15 engineers working on Walmart's backend.

Someone writes

```python
task.title = ""
```

Oops.

Now every other object holding this task sees the changed value.

Bugs become impossible to debug.

Instead

```python
new_task = replace(task, title="New Title")
```

Now everyone using the old task still has the original.

This dramatically reduces bugs.

This is why immutable objects are so popular in:

* Swift
* Kotlin
* Functional Programming
* AI pipelines
* Concurrent systems

---

# Now the really important question...

> I didn't understand Domain Exception.

Perfect.

Let's start from scratch.

Forget Python.

Forget FastAPI.

Forget exceptions.

Imagine you're running a library.

Someone asks

> Can I borrow Harry Potter?

You look.

Oops.

Already borrowed.

How do you tell them?

Possibility 1

You shout

```
ERROR!!
```

Possibility 2

You say

```
BookAlreadyBorrowed
```

Which one is more useful?

Obviously

```
BookAlreadyBorrowed
```

because everyone now knows **what happened**.

Exceptions work exactly like that.

---

# Beginner way

Most beginners write

```python
raise Exception("Duplicate")
```

Looks okay.

Now imagine later.

```python
raise Exception("Duplicate")

raise Exception("Network")

raise Exception("Database")

raise Exception("Timeout")

raise Exception("Invalid")
```

Now suppose you're catching them.

```python
try:
    ...
except Exception as e:
    print(e)
```

How do you know

Was it

* timeout?
* duplicate?
* validation?
* database?

You don't.

You only have strings.

---

# Better way

Instead

we create

```python
class DuplicateTask(Exception):
    pass
```

Notice something.

This class doesn't need any code.

Its **name** already carries the meaning.

Think of it as creating a new type.

Exactly like

```python
class Dog:
    pass

class Cat:
    pass
```

Neither class has methods.

But they represent different things.

Same idea.

---

# So what does `pass` mean?

It means

> "Nothing extra here."

Python requires something inside the class.

We don't need anything.

So we say

```python
pass
```

That's all.

---

# Now let's actually use it.

Suppose we have

```python
tasks = {
    "Buy Milk": "Task Object"
}
```

Someone tries

```python
create("Buy Milk")
```

Repository checks

```python
if title in tasks:
```

What should happen?

Instead of

```python
raise Exception("Duplicate")
```

we do

```python
raise DuplicateTask()
```

Notice.

We're not returning anything.

We're **throwing** an exception.

---

# What happens next?

Imagine

```python
TaskService
```

calls

```python
Repository
```

Repository

↓

finds duplicate

↓

raises

```python
DuplicateTask()
```

Now Python starts walking back.

Think of it like someone shouting

```
STOP!!
```

Everything immediately unwinds until somebody catches it.

---

Let's see.

```python
def repository():

    raise DuplicateTask()
```

Service

```python
def service():

    repository()
```

Main

```python
service()
```

When repository raises,

Python automatically jumps back.

---

# Someone has to catch it

```python
try:

    service()

except DuplicateTask:

    print("Task already exists.")
```

Output

```
Task already exists.
```

Now things become interesting.

---

# Where does FastAPI come in?

Notice.

Repository never imports FastAPI.

Service never imports FastAPI.

Repository only says

```
DuplicateTask
```

Then

FastAPI Route

```python
try:

    service.create(...)

except DuplicateTask:

    return HTTP 409
```

See what happened?

The repository has **no idea** HTTP exists.

This is incredibly important.

---

# Why is this separation important?

Imagine tomorrow.

Instead of REST API,

your service runs inside

```text
Kafka Consumer
```

Would returning

```python
HTTPException(409)
```

make sense?

No.

There is no HTTP.

Or imagine

```text
Command Line Tool
```

Still no HTTP.

Or imagine

```text
Cron Job
```

Still no HTTP.

The domain only knows

```
DuplicateTask
```

The outside world decides

how to present that error.

---

# Here's the complete flow

Imagine the user sends

```
Create Task

Buy Milk
```

Flow

```text
User
 |
 |
FastAPI
 |
 |
TaskService
 |
 |
Repository
 |
 |
Duplicate found
 |
 |
raise DuplicateTask
 |
 |
TaskService
 |
 |
FastAPI catches it
 |
 |
Return HTTP 409
```

Notice who converts it.

Not the repository.

Not the service.

The API.

---

# Let's write a tiny runnable example

## Repository

```python
class DuplicateTask(Exception):
    pass


class Repository:

    def __init__(self):
        self.tasks = {}

    def add(self, title):

        if title in self.tasks:
            raise DuplicateTask()

        self.tasks[title] = title
```

---

## Service

```python
class Service:

    def __init__(self, repository):
        self.repository = repository

    def create(self, title):

        self.repository.add(title)
```

Notice.

The service doesn't catch anything.

It simply lets the exception bubble up.

---

## Main

```python
repo = Repository()

service = Service(repo)

try:

    service.create("Buy Milk")
    service.create("Buy Milk")

except DuplicateTask:

    print("Duplicate Task!")
```

Output

```
Duplicate Task!
```

---

# Later, with FastAPI

Exactly the same service.

Nothing changes.

Only the outer layer changes.

```python
@app.post("/tasks")
async def create_task(request: CreateTaskRequest):

    try:

        task = service.create(request.title)

        return task

    except DuplicateTask:

        raise HTTPException(
            status_code=409,
            detail="Task already exists."
        )
```

Notice something beautiful.

The **service** is identical.

The **repository** is identical.

Only the **API** translates the domain error into an HTTP response.

This is the "domain boundary" your sprint is trying to teach. The domain speaks in **business concepts** ("DuplicateTask"), while the API speaks in **HTTP concepts** ("409 Conflict"). They intentionally don't know about each other.

---

## I think we should slightly change our learning strategy

Up until now, I've been explaining individual concepts in isolation.

For the rest of Sprint 1, I think a better approach is to **build the entire mini-project together**, one file at a time, exactly as you would in a production codebase:

1. **`domain/`** — dataclasses, immutability, exceptions.
2. **`application/`** — protocols, services, dependency inversion.
3. **`persistence/`** — in-memory adapter.
4. **`tests/`** — write tests first and prove the behavior.
5. **Only after all of that**, add FastAPI and show how nothing in the domain changes.

That way, every new concept has context, and by the end of the sprint you'll have built a small but realistic application instead of seeing disconnected code snippets. I think it will match the way you've preferred learning in our previous sessions.

This is **the** question that unlocks Clean Architecture.

The confusion comes because it looks like FastAPI is replacing something.

**It isn't replacing anything.**

It is **wrapping** your existing code.

Let's visualize it.

---

# Step 1 — Your current program

Right now you have one Python program.

```python
repo = Repository()
service = Service(repo)

try:
    service.create("Buy Milk")
    service.create("Buy Milk")

except DuplicateTask:
    print("Duplicate Task!")
```

Imagine this as:

```text
          main.py

      create("Buy Milk")
               |
               |
          Service.create()
               |
               |
        Repository.add()
               |
               |
        DuplicateTask()
               |
               |
      except DuplicateTask
               |
               |
 print("Duplicate Task!")
```

Notice something.

Who is calling the service?

**Your own Python code.**

There is no HTTP.

No network.

No FastAPI.

No browser.

---

# Step 2 — What is `main.py` actually doing?

Let's isolate it.

```python
repo = Repository()
service = Service(repo)

try:
    service.create("Buy Milk")

except DuplicateTask:
    print("Duplicate")
```

This file is just

> "Someone calling the service."

That's all.

Today that someone is Python itself.

Tomorrow that someone could be FastAPI.

---

# Step 3 — Replace the caller

We don't replace the service.

We don't replace the repository.

We only replace **who calls them**.

Instead of this:

```python
repo = Repository()
service = Service(repo)

try:
    service.create("Buy Milk")

except DuplicateTask:
    print("Duplicate")
```

FastAPI becomes the caller.

---

Think of FastAPI as another person.

Previously

```text
You
 |
 |
Service
 |
Repository
```

Now

```text
Browser
   |
HTTP Request
   |
FastAPI
   |
Service
   |
Repository
```

Notice.

The bottom half didn't move.

---

# Let's compare line-by-line

## Before

```python
repo = Repository()
service = Service(repo)

try:
    service.create("Buy Milk")

except DuplicateTask:
    print("Duplicate")
```

Who provides `"Buy Milk"`?

You.

---

## After

```python
@app.post("/tasks")
async def create_task(request):
```

Who provides `"Buy Milk"` now?

The browser.

Suppose the browser sends

```json
{
    "title": "Buy Milk"
}
```

FastAPI converts that JSON into

```python
request.title
```

Then calls

```python
service.create(request.title)
```

Exactly like you did manually.

---

# Nothing changes below the service

Before

```text
main.py

↓

Service

↓

Repository
```

After

```text
FastAPI

↓

Service

↓

Repository
```

Same service.

Same repository.

---

# Let's draw the entire stack

## Before

```text
                main.py

        service.create("Buy Milk")
                  |
                  |
           Service.create()
                  |
                  |
          Repository.add()
                  |
                  |
          raise DuplicateTask
                  |
                  |
             main.py catches
```

---

## After

```text
Browser
    |
HTTP POST /tasks
    |
FastAPI Route
    |
service.create("Buy Milk")
    |
Service.create()
    |
Repository.add()
    |
raise DuplicateTask
    |
FastAPI catches
    |
HTTP 409
```

Notice.

The service never changed.

---

# So what happened to this code?

You asked

> where will this code go?

```python
try:
    service.create(...)

except DuplicateTask:
```

Excellent question.

It simply **moves upward**.

Previously

```python
repo = Repository()
service = Service(repo)

try:
    service.create("Buy Milk")

except DuplicateTask:
    print("Duplicate")
```

Now

```python
@app.post("/tasks")
async def create_task(...):

    try:
        service.create(...)

    except DuplicateTask:
        ...
```

Same try.

Different place.

---

# Why move it?

Because before

your output was

```text
Duplicate Task!
```

Now your output needs to be

```http
HTTP 409

{
    "detail": "Task already exists."
}
```

FastAPI knows how to send HTTP.

Repository doesn't.

---

# Imagine if Repository returned HTTP

Suppose Repository did this

```python
raise HTTPException(
    status_code=409
)
```

Looks okay...

until tomorrow.

---

Tomorrow someone writes

```python
service.create(...)
```

inside

```text
Background Worker
```

There is no HTTP.

Boom.

Your repository now depends on FastAPI.

Bad architecture.

---

# Think about your iOS experience

Suppose your business logic looked like this.

```swift
class PaymentService {

    func pay() {

        let alert = UIAlertController(...)

        present(alert)
    }
}
```

Would you do this?

No.

Why?

Because

`PaymentService`

shouldn't know UIKit exists.

Instead

```swift
throw PaymentFailed()
```

Then

```swift
UIViewController
```

decides

```swift
showAlert()
```

Exactly the same thing.

---

# Here's an analogy

Imagine a restaurant.

### Kitchen

Makes food.

### Waiter

Talks to customers.

If customer says

> No onions.

Waiter tells kitchen.

Kitchen says

> Sorry, we're out of onions.

Kitchen does NOT walk to the customer.

The waiter translates.

```
Customer
    |
Waiter
    |
Kitchen
```

Now replace them.

```
Customer = Browser

Waiter = FastAPI

Kitchen = Service

Cook = Repository
```

Repository says

```text
DuplicateTask
```

FastAPI translates

```text
HTTP 409
```

Exactly like the waiter translates kitchen language into customer language.

---

# One more subtle point

Notice this line:

```python
task = service.create(request.title)
```

The service has **no idea** where `request.title` came from.

It could have come from:

```text
FastAPI
```

or

```text
Command Line
```

or

```text
Kafka
```

or

```text
RabbitMQ
```

or

```text
Unit Test
```

The service doesn't care.

It only needs

```python
title: str
```

That is the whole point of today's assignment: **the business logic should not know who is talking to it.**

---

## Now let me ask you the interview question I would ask if I were the interviewer

Suppose tomorrow Walmart removes FastAPI completely and says:

> "We now receive tasks from Kafka messages instead of HTTP requests."

If your architecture is

```
Kafka Consumer
      |
   Service
      |
 Repository
```

**Which files would change?**

Think carefully before answering.

* Would `Repository` change?
* Would `Service` change?
* Or would only the outer "caller" (previously FastAPI, now Kafka consumer) change?

If you can answer that confidently, you've understood the core idea of dependency boundaries.
'''

'''
I’ll review your actual staged domain file and notes first, then give you a simpler end-to-end lesson, corrections, remaining file-by-file implementation, and exact verification commands.Your checkpoint is staged, and Git also shows an unstaged `application/` directory that wasn’t mentioned; I’ll include it in the review so we do not overwrite or duplicate your work.The domain idea is correct; I’m running only the two non-mutating checks for that file now so the review distinguishes conceptual correctness from formatting/type-check evidence.# Checkpoint 1 review

**Result: passed.** Your `TaskRecord` and `DuplicateTaskTitle` are technically correct.

I verified:

```text
uv run --extra dev ruff check src/ai_solutions_platform/domain/tasks.py
All checks passed!

uv run --extra dev mypy src/ai_solutions_platform/domain/tasks.py
Success: no issues found in 1 source file
```

You correctly used:

- `@dataclass(frozen=True)`;
- `UUID`, `str`, and `datetime` field types;
- a domain-specific `DuplicateTaskTitle`;
- only Python standard-library imports;
- no FastAPI, Postgres, Pydantic, or model SDK imports.

Your notes also show the correct central idea: the domain reports a duplicate task, while a future API layer decides whether that becomes HTTP 409.

## Small cleanup

Your file still contains the commented starter scaffold, the type annotations need conventional spacing, and `pass` is unnecessary after a class docstring. These are readability improvements, not correctness failures.

Use this clean version:

**`AI Solutions Platform/src/ai_solutions_platform/domain/tasks.py`**

```python
"""Domain concepts for tasks."""

from dataclasses import dataclass
from datetime import datetime
from uuid import UUID


@dataclass(frozen=True)
class TaskRecord:
    """An immutable record of a task created by the application."""

    task_id: UUID
    title: str
    created_at: datetime


class DuplicateTaskTitle(Exception):
    """Raised when a task title violates the uniqueness invariant."""
```

Because this file is already staged, editing it creates a newer working-tree version than the staged version. Stage it again only after finishing:

```bash
git add "AI Solutions Platform/src/ai_solutions_platform/domain/tasks.py"
```

Do not commit yet.

Git also shows this untracked directory:

```text
AI Solutions Platform/src/ai_solutions_platform/application/
```

It already contains empty `__init__.py` and `tasks.py` files. Use those files rather than recreating them.

---

# Part 1: The whole exercise in simple language

We are building a tiny system that creates tasks.

The system has five pieces.

## 1. Domain record: “What is a task?”

A task contains:

- an ID;
- a title;
- its creation time.

This is `TaskRecord`.

It is immutable so that after we say, “This task was created with these facts,” another part of the program cannot accidentally rewrite those facts.

## 2. Domain exception: “Why was the operation rejected?”

If the same title already exists, the system raises:

```text
DuplicateTaskTitle
```

It does not raise an HTTP error or database error because “duplicate task title” is the actual business problem.

Different callers may communicate that problem differently:

- a web API may return HTTP 409;
- a CLI may print a message;
- a background worker may log it;
- a Kafka consumer may reject or acknowledge an event.

The domain error remains the same.

## 3. Repository protocol: “What storage ability does the service require?”

The service needs something that can add a task.

It does not need to know whether tasks are stored in:

- a dictionary;
- Postgres;
- a file;
- a remote service.

`TaskRepository` describes only the required ability:

```text
add a TaskRecord
```

Think of the protocol as a socket. Different storage adapters can plug into the same socket.

## 4. In-memory adapter: “Where are tasks stored today?”

Today, tasks are stored in a Python dictionary.

This is useful because it:

- requires no database;
- is fast;
- is easy to test;
- lets us learn the architecture first.

The data disappears when the Python process stops. That is acceptable for this exercise.

## 5. Application service: “What are the steps for creating a task?”

`TaskService.create(title)`:

1. generates a UUID;
2. records the current UTC time;
3. creates a `TaskRecord`;
4. asks the repository to save it;
5. returns the new record.

The service knows the creation process. It does not know how storage works.

## 6. Tests: “Can we prove the behavior?”

We need two tests:

1. a new title creates a task;
2. creating the same title again raises `DuplicateTaskTitle`.

No HTTP requests and no database are involved.

---

# Part 2: How the pieces connect

```text
Caller
  |
  v
TaskService
  |
  v
TaskRepository Protocol
  |
  +-----------------------------+
  |                             |
  v                             v
InMemoryTaskRepository     Future PostgresTaskRepository
```

The source-code dependency direction is:

```text
domain <- application <- outer adapters
```

More precisely:

```text
application --> domain
persistence --> domain
tests --> application + persistence + domain
```

What must **not** happen:

```text
domain --> FastAPI
domain --> Postgres
domain --> model SDK
application --> InMemoryTaskRepository
application --> PostgresTaskRepository
```

The application service must not select its own repository. The caller supplies one through the constructor.

This is called **dependency injection**:

```python
repository = InMemoryTaskRepository()
service = TaskService(repository)
```

“Injection” simply means that an object receives its dependency from outside instead of constructing it internally.

---

# Part 3: Python-to-Swift comparison

| Python | Similar Swift idea |
|---|---|
| `@dataclass(frozen=True)` | A `struct` whose properties are `let` |
| `typing.Protocol` | Swift `protocol` |
| Constructor dependency injection | Passing a protocol implementation through `init` |
| `DuplicateTaskTitle` | A domain-specific Swift `Error` |
| `InMemoryTaskRepository` | A concrete type conforming to a repository protocol |

One important difference: a frozen Python dataclass is not the same as Swift value semantics. Python still uses object references.

---

# Part 4: Final file structure

From `AI Solutions Platform/`, the completed exercise should contain:

```text
src/
└── ai_solutions_platform/
    ├── domain/
    │   ├── __init__.py
    │   └── tasks.py
    ├── application/
    │   ├── __init__.py
    │   └── tasks.py
    └── persistence/
        ├── __init__.py
        └── in_memory_tasks.py

tests/
└── unit/
    ├── .gitkeep
    └── test_task_service.py
```

You already have:

```text
domain/__init__.py
domain/tasks.py
application/__init__.py
application/tasks.py
tests/unit/.gitkeep
```

Create only the missing persistence files and test file:

```bash
cd "/Users/swapnildhiman/Desktop/AI/iOSToAIJourney/AI Solutions Platform"

mkdir -p src/ai_solutions_platform/persistence
touch src/ai_solutions_platform/persistence/__init__.py
touch src/ai_solutions_platform/persistence/in_memory_tasks.py
touch tests/unit/test_task_service.py
```

Do not create an API package, route, migration, Postgres repository, or model integration for this exercise.

---

# Part 5: Application layer

## File

```text
AI Solutions Platform/src/ai_solutions_platform/application/tasks.py
```

## Complete code

```python
"""Task application use cases and required persistence contract."""

from datetime import UTC, datetime
from typing import Protocol
from uuid import uuid4

from ai_solutions_platform.domain.tasks import TaskRecord


class TaskRepository(Protocol):
    """Persistence behavior required by the task application service."""

    async def add(self, record: TaskRecord) -> None:
        """Store a task record or raise a domain-specific exception."""
        ...


class TaskService:
    """Coordinates task-related application use cases."""

    def __init__(self, repository: TaskRepository) -> None:
        self._repository = repository

    async def create(self, title: str) -> TaskRecord:
        """Create, persist, and return a new task record."""

        record = TaskRecord(
            task_id=uuid4(),
            title=title,
            created_at=datetime.now(UTC),
        )

        await self._repository.add(record)

        return record
```

## Simple explanation

The protocol says:

> Any object that has the correct asynchronous `add` method can be used as a task repository.

The service receives that repository:

```python
def __init__(self, repository: TaskRepository) -> None:
```

The service does **not** do this:

```python
self._repository = InMemoryTaskRepository()
```

That would permanently connect the service to one storage implementation.

## Technical explanation

### Why use `Protocol`?

`Protocol` enables structural typing.

The in-memory repository does not need to inherit from `TaskRepository`. It only needs to have a compatible method:

```python
async def add(self, record: TaskRecord) -> None:
```

Mypy checks compatibility when an `InMemoryTaskRepository` is passed into `TaskService`.

This is similar to implicit protocol conformance by shape, although Swift normally requires explicit conformance in the type declaration.

### Why is `add` asynchronous?

The future Postgres adapter will perform network/database I/O. That operation will need `await`.

By making the port asynchronous now, both adapters have the same contract:

```python
await repository.add(record)
```

The service will not need to change when Postgres arrives.

### Why use `datetime.now(UTC)`?

It creates a timezone-aware UTC timestamp.

Avoid:

```python
datetime.now()
```

That produces a naive datetime with no timezone information.

### Why generate the UUID and time in the service?

Creating an identity and creation timestamp is part of coordinating the use case. The record should receive completed values rather than secretly creating them itself.

For a larger system, we might inject an ID generator and clock for fully deterministic tests. That would be unnecessary complexity for today’s small exercise.

### Why doesn’t the service catch `DuplicateTaskTitle`?

It has nothing useful to add. The repository raises the domain error, and the service naturally passes it to its caller.

Avoid pointless code such as:

```python
try:
    await self._repository.add(record)
except DuplicateTaskTitle:
    raise
```

---

# Part 6: In-memory persistence adapter

## Package initializer

**`src/ai_solutions_platform/persistence/__init__.py`**

```python
"""Persistence adapters for the AI Solutions Platform."""
```

## Adapter file

**`src/ai_solutions_platform/persistence/in_memory_tasks.py`**

```python
"""In-memory persistence adapter for tasks."""

import asyncio

from ai_solutions_platform.domain.tasks import (
    DuplicateTaskTitle,
    TaskRecord,
)


class InMemoryTaskRepository:
    """Store task records in memory for tests and local exercises."""

    def __init__(self) -> None:
        self._records_by_title: dict[str, TaskRecord] = {}
        self._lock = asyncio.Lock()

    async def add(self, record: TaskRecord) -> None:
        """Store a record unless its title already exists."""

        async with self._lock:
            if record.title in self._records_by_title:
                raise DuplicateTaskTitle(record.title)

            self._records_by_title[record.title] = record
```

## Simple explanation

The dictionary looks approximately like this:

```python
{
    "Prepare architecture": TaskRecord(...),
    "Write tests": TaskRecord(...),
}
```

The title is the key because today the rule is:

> Two tasks cannot have exactly the same title.

When adding a task:

1. check whether its title is already a key;
2. raise `DuplicateTaskTitle` if it is;
3. otherwise store the record.

## Why not use `task_id` as the dictionary key?

A newly generated UUID will almost always be unique. If the dictionary were keyed only by ID, checking duplicate titles would require scanning every stored task.

Keying by title directly represents today’s uniqueness requirement.

In a larger repository, you might maintain records by ID plus a separate title index. That is unnecessary today.

## What does the lock protect?

The operation is conceptually one unit:

```text
check title
then insert record
```

We do not want two concurrent calls to make conflicting decisions.

An important technical nuance: in this exact implementation, there is no `await` between the dictionary check and insertion, so normal asyncio task switching cannot occur between those two statements. The lock still makes the intended critical section explicit and keeps it safe if the adapter later gains awaited work.

The lock does **not** protect:

- another Python process;
- another application instance;
- another server;
- another repository object.

That is why production Postgres must use a unique constraint.

## Today’s title behavior

Comparison is currently:

- exact;
- case-sensitive;
- whitespace-sensitive.

Therefore:

```text
"Write Tests"
"write tests"
"Write Tests "
```

are three different titles.

Case-insensitive normalization is listed as an extension in the sprint, but it is outside today’s required minimal exercise.

---

# Part 7: Minimal tests

## File

```text
AI Solutions Platform/tests/unit/test_task_service.py
```

## Complete code

```python
"""Unit tests for the task application service."""

from datetime import UTC
from uuid import UUID

import pytest

from ai_solutions_platform.application.tasks import TaskService
from ai_solutions_platform.domain.tasks import DuplicateTaskTitle
from ai_solutions_platform.persistence.in_memory_tasks import (
    InMemoryTaskRepository,
)


async def test_create_returns_persisted_task_record() -> None:
    repository = InMemoryTaskRepository()
    service = TaskService(repository)
    title = "Prepare architecture"

    record = await service.create(title)

    assert record.title == title
    assert isinstance(record.task_id, UUID)
    assert record.task_id.version == 4
    assert record.created_at.tzinfo is UTC


async def test_create_rejects_duplicate_title() -> None:
    repository = InMemoryTaskRepository()
    service = TaskService(repository)
    title = "Prepare architecture"

    await service.create(title)

    with pytest.raises(DuplicateTaskTitle):
        await service.create(title)
```

## Why no `@pytest.mark.asyncio`?

Your `pyproject.toml` already contains:

```toml
[tool.pytest.ini_options]
asyncio_mode = "auto"
```

You also already have `pytest-asyncio` in the development dependencies. Therefore pytest automatically handles these asynchronous tests.

Adding `@pytest.mark.asyncio` would also work, but it would be redundant with the current configuration.

## What the first test proves

It proves that the service:

- accepts a title;
- returns the same title;
- generates a UUID version 4 identifier;
- generates a UTC-aware timestamp;
- accepts the in-memory adapter as its repository dependency.

It deliberately does not check the exact UUID or exact timestamp because both values are generated at runtime.

## What the duplicate test proves

It proves that:

1. the first creation succeeds;
2. the second creation with the same title fails;
3. the failure uses the domain-specific exception.

We do not inspect this private dictionary:

```python
repository._records_by_title
```

Tests should normally verify public behavior rather than internal implementation details.

---

# Part 8: Why `frozen=True` is useful—and its limit

This fails at runtime:

```python
record.title = "Changed"
```

Python raises `FrozenInstanceError`.

It may also be rejected by a static type checker before execution.

However, `frozen=True` does not create perfect or deep immutability.

For example:

```python
@dataclass(frozen=True)
class Example:
    values: list[str]
```

This assignment is blocked:

```python
example.values = []
```

But the list itself can still be mutated:

```python
example.values.append("new value")
```

Our `TaskRecord` fields—`UUID`, `str`, and `datetime`—are appropriate immutable-style value objects, so this problem does not arise in the current record.

Also, advanced Python code can deliberately bypass the frozen protection using mechanisms such as `object.__setattr__`. `frozen=True` is a strong normal-use guard, not a security boundary.

---

# Part 9: Why `datetime`, not a formatted string?

Store:

```python
created_at: datetime
```

rather than:

```python
created_at: str
```

A `datetime` preserves time meaning. The program can:

- compare two times;
- sort by time;
- calculate durations;
- convert timezones;
- validate timezone awareness;
- serialize it in different formats later.

A string such as:

```text
"July 21 at 11:30 PM"
```

is ambiguous and difficult to calculate with.

Formatting belongs at an outer boundary:

- an API can serialize it as ISO 8601;
- a UI can show a human-friendly date;
- a database adapter can convert it to the database representation.

The domain retains the meaningful typed value.

---

# Part 10: Why the exception must not inherit from `HTTPException`

This would be wrong in the domain:

```python
from fastapi import HTTPException


class DuplicateTaskTitle(HTTPException):
    ...
```

It would make the domain dependent on FastAPI.

Then the same domain could not be reused cleanly from:

- a command-line application;
- a background worker;
- a scheduled job;
- a message consumer;
- a unit test without web concerns.

Correct separation:

```text
Domain:
DuplicateTaskTitle

Future FastAPI edge:
DuplicateTaskTitle -> HTTP 409

Future CLI:
DuplicateTaskTitle -> terminal message

Future event consumer:
DuplicateTaskTitle -> duplicate-event handling
```

The domain states what happened. The outer caller decides how to communicate it.

---

# Part 11: How Postgres replaces the in-memory adapter

Today, the composition code would be:

```python
repository = InMemoryTaskRepository()
service = TaskService(repository)
```

Later, it can become:

```python
repository = PostgresTaskRepository(database_pool)
service = TaskService(repository)
```

`TaskService` still receives a `TaskRepository`.

The future Postgres class must provide:

```python
async def add(self, record: TaskRecord) -> None:
    ...
```

Therefore the service does not change.

## Future Postgres responsibilities

The Postgres adapter will:

1. receive a `TaskRecord`;
2. convert its fields into SQL parameters;
3. execute an `INSERT`;
4. rely on a database unique constraint for the title;
5. catch the database’s unique-constraint exception;
6. translate that technical exception into `DuplicateTaskTitle`.

Conceptually:

```text
Postgres unique violation
        |
        v
PostgresTaskRepository
        |
        v
DuplicateTaskTitle
        |
        v
TaskService caller
```

The database exception must not leak into the application service.

## Why a database unique constraint is still required

An application-level check like this is insufficient in production:

```text
SELECT whether title exists
INSERT if missing
```

Two application processes could both perform the check before either performs the insert.

The database must be the final authority:

```sql
UNIQUE (title)
```

We are only explaining that today. Do not create the schema or adapter yet.

---

# Part 12: Exact validation commands

Run these from:

```bash
cd "/Users/swapnildhiman/Desktop/AI/iOSToAIJourney/AI Solutions Platform"
```

## 1. Targeted tests

```bash
uv run --extra dev pytest tests/unit/test_task_service.py -q
```

Required result:

```text
2 passed
```

The duration and pytest version may vary.

## 2. Ruff

```bash
uv run --extra dev ruff check src tests
```

Required result:

```text
All checks passed!
```

## 3. Strict mypy

```bash
uv run --extra dev mypy src tests
```

Required result:

```text
Success: no issues found ...
```

The number of files may vary.

## 4. Full current test suite

```bash
uv run --extra dev pytest -q
```

Record the exact output. Do not replace a failing full-suite result with only a successful targeted command.

## 5. Optional boundary inspection

```bash
rg -n \
  '\b(fastapi|pydantic|sqlalchemy|asyncpg|psycopg|google\.genai|anthropic)\b' \
  src/ai_solutions_platform/domain \
  src/ai_solutions_platform/application
```

Expected result: no output.

The persistence adapter also should not contain those imports today, although a future Postgres adapter will legitimately import a database library.

---

# Part 13: Common mistakes to avoid

## Mistake 1: The service creates the concrete repository

Wrong:

```python
class TaskService:
    def __init__(self) -> None:
        self._repository = InMemoryTaskRepository()
```

This makes replacement difficult.

Correct:

```python
class TaskService:
    def __init__(self, repository: TaskRepository) -> None:
        self._repository = repository
```

## Mistake 2: The domain raises HTTP errors

Wrong:

```python
raise HTTPException(status_code=409)
```

Correct:

```python
raise DuplicateTaskTitle(record.title)
```

## Mistake 3: Catching every exception

Wrong:

```python
except Exception:
    raise DuplicateTaskTitle
```

That could incorrectly convert programming errors or system failures into duplicate errors.

Only known duplicate failures should become `DuplicateTaskTitle`.

## Mistake 4: Testing private storage fields

Avoid:

```python
assert title in repository._records_by_title
```

Prefer testing behavior through `TaskService`.

## Mistake 5: Using naive local time

Avoid:

```python
datetime.now()
```

Use:

```python
datetime.now(UTC)
```

## Mistake 6: Adding future scope

Do not add today:

- FastAPI;
- Pydantic request/response models;
- HTTP status codes;
- Postgres;
- SQLAlchemy;
- migrations;
- model SDKs;
- title normalization;
- read/list/update/delete operations;
- dependency-provider wiring.

---

# Part 14: Completion checklist

The exercise is complete only when every box is true:

- [x] `TaskRecord` exists.
- [x] It uses precise UUID, string, and datetime fields.
- [x] It is frozen.
- [x] `DuplicateTaskTitle` exists.
- [x] Domain checkpoint passes targeted Ruff.
- [x] Domain checkpoint passes strict mypy.
- [ ] `TaskRepository` protocol exists.
- [ ] `TaskService` depends on the protocol.
- [ ] `InMemoryTaskRepository` exists.
- [ ] Duplicate creation raises `DuplicateTaskTitle`.
- [ ] Two minimal tests pass.
- [ ] Ruff passes for `src` and `tests`.
- [ ] Mypy passes for `src` and `tests`.
- [ ] The full current test suite result is recorded.
- [ ] Domain/application code has no FastAPI, database, or model SDK imports.
- [ ] You can explain the Postgres replacement without changing the service.
- [ ] No FastAPI route or Postgres implementation was added.

The **domain checkpoint has passed**, but the whole exercise has not yet passed.

---

# Part 15: Questions you must be able to answer

## 1. Why `Protocol` instead of `InMemoryTaskRepository` in the service constructor?

Because the service needs storage behavior, not one particular storage technology. The protocol allows memory and Postgres implementations to satisfy the same contract.

## 2. Why can `InMemoryTaskRepository` satisfy the protocol without inheriting from it?

Python protocols support structural typing. Compatibility is based on having the correctly typed methods, not explicit inheritance.

## 3. Why is the duplicate exception a domain exception?

“Duplicate task title” describes the business failure. HTTP 409 and database uniqueness errors are technology-specific representations of that failure.

## 4. Why is the in-memory lock insufficient for production?

It protects only one lock object in one Python process. Multiple processes or servers do not share it. Postgres must enforce uniqueness with a database constraint.

## 5. Why does the service not change when Postgres is introduced?

Both adapters satisfy the same `TaskRepository` contract. Only the application composition code selects a different adapter.

## 6. Where does a Postgres unique violation get translated?

Inside `PostgresTaskRepository`, because that adapter understands both the database error and the application-facing domain exception.

## 7. Does `frozen=True` guarantee deep immutability?

No. It blocks normal field reassignment but does not recursively freeze mutable objects stored in fields.

---

## Your next action

Implement the application, persistence, and test files. Type the code while explaining each line to yourself rather than pasting it blindly.

Then reply with:

1. **“Implementation ready.”**
2. Your exact output from:
   - `uv run --extra dev pytest tests/unit/test_task_service.py -q`
   - `uv run --extra dev ruff check src tests`
   - `uv run --extra dev mypy src tests`
   - `uv run --extra dev pytest -q`
3. Your own four- or five-sentence explanation of how Postgres replaces the in-memory adapter without changing `TaskService`.

I will then inspect the actual files, verify the commands independently, conduct the architecture review, and assess only this exercise—not the entire sprint.
'''

## July 22, 2026 — independent verification of July 21 recovery work

This section supersedes the historical completion checklist and “next action” inside the quoted coaching transcript above. Verification was performed against the actual staged Python files and the separate Swift artifact; submitted implementation files were not rewritten.

### Decision

- **Python domain-boundary implementation: implementation evidence passes.** The frozen domain record, domain-specific duplicate exception, repository `Protocol`, injected application service, in-memory adapter, and create/duplicate behavior are present and correctly separated.
- **Architecture defense: reviewed and accepted with corrections (3/4).** Swapnil correctly identified the injected `TaskRepository` contract and why `TaskService` remains unchanged. Corrections recorded: add `PostgresTaskRepository` rather than replacing the in-memory file, switch the composition/provider to inject it, and translate the specific database unique-constraint violation inside that adapter to the exact `DuplicateTaskTitle` domain exception before the HTTP edge maps it to 409. This closes the local domain exercise checkpoint, not the full Sprint 1 gate.
- **Repository/CI recovery block: partial.** The `src/` layout and `uv.lock` exist, and local format/lint/type/test commands pass. The required architecture decision and `.github/workflows/ci.yml` do not exist. `README.md` now identifies Sprint 1 and uses the verified locked commands; ADR/CI remain scheduled for July 25.
- **July 21 DSA requirement: selected but not complete.** **Repeating and Missing Number** is selected with an intended O(n)-time/O(1)-extra-space immutable-input target. No solution or runtime evidence has been reviewed, and the requested prior-mistake note was not supplied; the earlier LIS submission still does not qualify.

### Verified Python evidence

Run from `AI Solutions Platform/` on July 22:

```text
uv lock --check
Resolved 44 packages in 19ms

uv run --locked --extra dev pytest tests/unit/test_task_service.py -q
2 passed in 0.01s

uv run --locked --extra dev ruff format --check src tests
19 files already formatted

uv run --locked --extra dev ruff check src tests
All checks passed!

uv run --locked --extra dev mypy src tests
Success: no issues found in 19 source files

uv run --locked --extra dev pytest -q
2 passed in 0.01s
```

A forbidden-import regex inspection across `domain/` and `application/` found zero references to FastAPI, Pydantic, SQLAlchemy, asyncpg, psycopg, Google Gen AI, or Anthropic SDKs. No FastAPI route or Postgres implementation was added by the submitted domain exercise.

### Requirement-by-requirement status

| July 21 requirement | Status | Verified evidence or gap |
|---|---|---|
| Immutable domain record | Complete | `@dataclass(frozen=True)` with `UUID`, `str`, and timezone-aware `datetime` construction |
| Domain-specific duplicate exception | Complete | `DuplicateTaskTitle` lives in the domain module |
| Repository protocol | Complete | Async `TaskRepository.add` protocol |
| In-memory adapter | Complete | Lock-protected adapter rejects duplicate titles |
| Application service | Complete | Constructor accepts `TaskRepository`; service creates and persists a record |
| Create and duplicate tests | Complete | Targeted and full suites both pass 2 tests |
| Format, lint, and strict type-check | Complete | Ruff format/lint and strict mypy pass |
| Clean domain/application dependency direction | Complete | Forbidden-import scan returns zero matches |
| Explain Postgres replacement without changing service | Reviewed — 3/4, accepted with corrections | Correct contract/service reasoning; add a new Postgres adapter and switch composition, and translate the exact unique violation inside it to `DuplicateTaskTitle` |
| `src/` layout and `uv.lock` | Complete | Both exist; lock check succeeds |
| Architecture decision artifact | Missing | No `docs/` decision artifact exists |
| Minimal GitHub Actions CI | Missing | No `.github/workflows/` files exist |
| One due arrays/hash-map revision | Selected, not complete | Repeating and Missing Number selected for Jul 27; target O(n)/O(1), but no reviewed solution, run, prior-mistake note, or repetition evidence |

### Swift artifact review

Artifact: `../iOS-Apps/DSA/sprint-01-AI-Software-Foundations.swift`

- Git state: untracked in the separate DSA repository.
- Static validation: `xcrun swiftc -typecheck sprint-01-AI-Software-Foundations.swift` succeeds with a trailing-closure warning at line 57.
- Active algorithm: LIS tail replacement using `firstIndex`, which is **O(n²) time and O(n) space**, not binary search despite the comment.
- The commented binary-search attempt is inactive and uses inconsistent half-open bounds (`high = mid - 1`).
- Behavioral runtime execution remains unverified because the temporary harness could not run under the available shell allowlist/front-end environment; the temporary harness was removed.
- This artifact does not increment the Sprint 1 arrays/hash-map solve count.

### Recording boundaries

- No actual July 21 or July 22 hours were recorded because none were supplied.
- The Sprint 1 gate remains active and unscored until August 2.
- Safe async remains scheduled for Saturday, July 25; Swift concurrency remains merged into Sunday, July 26.

## July 22, 2026 — backlog distribution adopted

The authoritative dated plan now lives in `sprints/Sprint-01-AI-Software-Foundations.md` under **Recovery override — recorded Wednesday, July 22**. This note records the rationale and current evidence boundary; it does not mark any future block complete.

### Current closeout state

Swapnil submitted the independent Postgres adapter-swap explanation and selected
**Repeating and Missing Number** as the due arrays/hash problem. The architecture
defense was reviewed at 3/4 and accepted for the local checkpoint with the
adapter/composition and exact-exception corrections recorded above. The DSA
selection is recorded, but the problem remains unsolved and its requested prior
mistake was not supplied; therefore it is not counted in the DSA ledger.

### One-to-one backlog map

| Origin | Remaining outcome | One replacement or integration point |
|---|---|---|
| Mon Jul 20 domain boundaries | Independent adapter-swap defense | Reviewed Jul 22 at 3/4; local checkpoint accepted with corrections |
| Mon Jul 20 repository/CI | Architecture decision and minimal CI | Sat Jul 25, 4:30–6:00 |
| Mon Jul 20 DSA | Repeating and Missing Number; prior-mistake note, solve, and evidence still required | Mon Jul 27, 9:30–10:30 |
| Tue Jul 21 safe async | Full safe-async evidence | Sat Jul 25, 2:15–4:15 |
| Tue Jul 21 Swift concurrency | Actor/service, cancellation, `MainActor`, Swift test | First 90 minutes of Sun Jul 26 Apple block |
| Tue Jul 21 unseen arrays/hash | One unseen arrays/hash outcome | Jul 29 mixed timed set |
| Wed Jul 22 FastAPI | Health/readiness placeholder, create/read, DI, error mapping, OpenAPI | Thu Jul 23, 2:15–4:15 |
| Thu Jul 23 API contracts displaced by that substitution | Exit-critical contract/failure tests only | Jul 23 success/validation/duplicate; Jul 25 timeout/cancellation; Jul 27 integration; Jul 28 rollback/conflict; Jul 30 lifecycle/concurrency; Jul 31 CI |
| Wed Jul 22 DSA | Two-pointer pattern, timed solve, and repetition | Jul 26 review, Jul 28 timed solve, Jul 29 repetition |
| Wed Jul 22 IIT | Attendance unreported | Separate IIT record/catch-up; never counted as Sprint-1 roadmap backlog |

### Capacity decision

- Week 1 uses exactly two optional replacement blocks: both Saturday blocks.
- Thursday's FastAPI work is a substitution, not an extra block.
- The standalone API-contract block is decomposed into implementation-adjacent evidence; duplicate test-framework breadth and middleware-only polish are removed if they do not serve the exit gate.
- DSA recovery uses existing Sprint-1 DSA slots; it does not add late-night or weekend solves.
- No sleep, meditation, IIT, Thursday/Friday fixed block, Week-2 platform block, or August 2 gate is borrowed.
- If a replacement is missed again, record it as missed at review and cut scope; never stack it into another deep block.

### Immediate stop condition

The late-night architecture closeout is complete. Record the missing prior
mistake for Repeating and Missing Number when recalled, but do not invent one
and do not begin the solve tonight. Stop roadmap work; FastAPI begins in the
Thursday July 23 replacement block.

## July 22, 2026 — architecture defense review and DSA selection

### Architecture defense: 3/4, accepted with corrections

| Prompt | Result | Review |
|---|---:|---|
| What contract does `TaskService` depend on? | 1/1 | Correctly identified the injected `TaskRepository` protocol. FastAPI is a caller/edge and composition selects the adapter; it is not the service's contract. |
| What concrete object changes with Postgres? | 0.5/1 | Correctly identified that a repository adapter satisfying the protocol is injected. Correction: add `PostgresTaskRepository`; do not replace or rewrite `InMemoryTaskRepository`. Change the composition/provider to select the Postgres adapter. |
| Where is database uniqueness translated? | 0.5/1 | Correctly rejected raising an HTTP exception from persistence/domain code. Correction: the Postgres adapter catches only the driver's unique-constraint violation and raises the exact domain exception `DuplicateTaskTitle`; the HTTP edge later maps that domain error to 409. The exception is not arbitrary. |
| Why does `TaskService` remain unchanged? | 1/1 | Correctly explained that the service orchestrates the use case against the stable protocol and remains independent of storage and transport technologies. |

This is a foundational checkpoint pass, not a Sprint 1 gate score. The implementation must follow the two corrections during the July 27 Postgres adapter block.

### Selected DSA recovery problem

**Repeating and Missing Number**

- Input: immutable integer array of length n containing values from 1 through n, with one duplicated value A and one missing value B.
- Output: `[A, B]`.
- Intended target: O(n) time and O(1) extra space without modifying the input.
- Scheduled solve: Monday, July 27, 9:30–10:30 PM.
- Current evidence: problem and target selected only.
- Still required: the prior mistake (if genuinely remembered), independently derived implementation, runnable/accepted cases, complexity proof, current mistake tag, and next repetition date.
- Guardrail: do not reveal or copy a solution before the independent attempt; do not count the target complexity as achieved until the code and reasoning are reviewed.
