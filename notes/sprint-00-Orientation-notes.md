To put it simply: **SQL is a language, while PostgreSQL is the actual software that speaks it.**

Think of it like cooking: SQL is the recipe format and cooking terminology, while PostgreSQL (often just called Postgres) is the high-end kitchen where you actually make the meal.

---

## 1. Postgres vs. SQL: The Core Difference

### What is SQL?

SQL stands for **Structured Query Language**. It isn't a program you download; it's a standardized programming language used to talk to databases. It gives you a universal way to say, *"Hey, show me all users who signed up in the last 24 hours."*

### What is PostgreSQL?

Postgres is a **Relational Database Management System (RDBMS)**. It is an open-source database engine that stores your data on a disk, handles security, and runs the SQL queries you write.

While Postgres uses standard SQL, it also adds its own advanced features. It's famous for being incredibly robust, handling complex data types (like JSON or geographic data), and being highly extensible.

---

## 2. Where Does Docker Fit Into This?

If you want to use Postgres on your laptop, you traditionally have to download an installer, run it, configure user permissions, and ensure it boots up correctly with your operating system. If you want to share your project with a coworker, they have to do the exact same setup—and if their laptop is running a different OS, things might break.

**Docker solves this by turning the database into a portable, isolated package.**

Instead of installing Postgres directly onto your computer's operating system, Docker lets you run Postgres inside a **container**. A container is a lightweight, isolated environment that has everything Postgres needs to run, pre-configured and ready to go.

### The Developer Workflow: Then vs. Now

Without Docker, setting up a project takes multiple manual installation steps. With Docker, you run a single command in your terminal:

```bash
docker run --name my-postgres -e POSTGRES_PASSWORD=mysecretpassword -d -p 5432:5432 postgres

```

This command instantly downloads the official Postgres image and fires up a running database on port `5432`, completely isolated from the rest of your system.

### Why Developers Love Using Postgres with Docker

* **No "It Works on My Machine" Syndrome:** The container runs exactly the same way on a Mac, Windows PC, or a Linux cloud server.
* **Zero Mess:** If you decide you don't need Postgres anymore, you just delete the container. It leaves no leftover config files or background processes rotting on your main operating system.
* **Version Switching:** Need to test your app on Postgres 14, 15, and 16? With Docker, you can spin up different versions in seconds without them interfering with one another.
In standard SQL (and specifically in PostgreSQL), **yes, unique constraints can absolutely have NULL values.** In fact, they can have *multiple* NULL values.

The rule of thumb to remember is: **Unique constraints treat every `NULL` as completely distinct from every other `NULL`.**

Because `NULL` represents the absence of a value (an unknown state), SQL logic dictates that one unknown value cannot be equal to another unknown value.

---

## How It Works in Practice

Imagine you have a `users` table with a unique constraint on the `phone_number` column.

* **User A** registers with `555-1234`.
* **User B** tries to register with `555-1234`. **(Blocked by the unique constraint)**
* **User C** registers but skips the phone number field (`NULL`). **(Allowed)**
* **User D** registers and also skips the phone number field (`NULL`). **(Allowed)**

Even though there are now two `NULL` rows, Postgres will not throw an error.

---

## How to Change This Behavior

Depending on what you actually want your database to do, you have a couple of options to modify how empty fields are handled.

### 1. The Strict Approach: No Empties Allowed

If you want a column to be both unique and mandatory, you must pair the `UNIQUE` constraint with a `NOT NULL` constraint.

```sql
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL
);

```

### 2. The Postgres Special: `UNIQUE NULLS NOT DISTINCT`

If you are using PostgreSQL 15 or newer, there is a feature that changes the default SQL rules. If you want to allow `NULL` values but **only exactly one** (treating all `NULL`s as identical), you can define the constraint like this:

```sql
CREATE TABLE coupons (
    id SERIAL PRIMARY KEY,
    code VARCHAR(50) UNIQUE NULLS NOT DISTINCT
);

```

With this setting, the first row with a `NULL` code will be allowed, but a second row with a `NULL` code will be rejected as a duplicate.


Postgres Index is a B-tree - a balanced sorted tree . Search in O(log N)

-------------

-- ============ TABLE 1: customers ============
CREATE TABLE customers (
    customer_id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY, -- PK (unique + not null, auto-indexed)
    email       TEXT        NOT NULL UNIQUE,   -- UNIQUE constraint: no duplicate emails
    full_name   TEXT        NOT NULL,          -- NOT NULL: must be provided
    created_at  TIMESTAMPTZ NOT NULL DEFAULT now()
);
-- ============ TABLE 2: orders ============
CREATE TABLE orders (
    order_id     BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    customer_id  BIGINT  NOT NULL
                 REFERENCES customers(customer_id),  -- FOREIGN KEY -> referential integrity
    amount_cents INTEGER NOT NULL
                 CHECK (amount_cents >= 0),           -- CHECK constraint: no negative money
    status       TEXT    NOT NULL DEFAULT 'pending',
    created_at   TIMESTAMPTZ NOT NULL DEFAULT now()
);
-- 
============ INDEX on the FK column (Postgres won't do this for us)============
CREATE INDEX idx_orders_customer_id ON orders(customer_id);
------------------


Absolutely. This topic is actually one of the most important foundations before you start building AI systems.

The reason is simple:

> **Every production AI application is two systems combined:**
>
> * an AI system (LLMs, agents, embeddings, tools...)
> * a traditional backend (users, billing, auth, conversations, permissions, transactions...)

Many people spend months learning LangChain or MCP and then get stuck because they don't understand databases.

---

# Before SQL, let's answer your AI architecture question

Because this will make the SQL part make much more sense.

You asked:

> Should production AI systems use SQL or Firebase/NoSQL?

The answer is:

> **Almost every serious AI company uses BOTH.**

Not either-or.

Imagine OpenAI.

---

## If you login to ChatGPT

What information exists?

```
User
-------
id
email
name
subscription
plan
created_at
```

That's structured.

Then

```
Conversation
--------------
conversation_id
owner_id
created_at
title
visibility
```

Structured.

Then

```
Messages
-------------
message_id
conversation_id
role
content
timestamp
```

Still structured.

Billing

```
Payments
Invoices
Subscriptions
Organizations
Members
API Keys
Usage
```

All structured.

These are relational.

---

## What SQL databases are likely storing

Think of tables like

```
Users

id
email
name
plan
created_at
```

```
Conversations

id
owner_id
title
created_at
```

```
Messages

id
conversation_id
role
text
created_at
```

```
Projects

id
owner_id
visibility
```

```
Organizations

id
name
```

Everything has relationships.

This is exactly what SQL excels at.

---

# What isn't stored in SQL?

Embeddings.

Example

```
1536 floating point numbers

[
0.183,
-0.294,
...
]
```

That's usually inside

* Vector DB
* pgvector
* Pinecone
* Weaviate
* Milvus
* Qdrant

---

# Does ChatGPT use SQL?

Nobody outside OpenAI knows their exact architecture.

But if I were designing ChatGPT today...

I'd absolutely use SQL.

Something like

```
Postgres

Users
Organizations
Billing
Projects
API Keys
Conversations
Messages metadata
Permissions
OAuth
Audit Logs
```

Vector search

```
pgvector

or

Pinecone
```

Redis

```
Caching
Rate limiting
Sessions
```

Blob storage

```
Images
Voice
Files
```

Search engine

```
Elastic/OpenSearch
```

This is extremely common.

---

# What about Firebase?

Firebase is fantastic for

* MVP
* startup
* hackathon
* realtime apps
* mobile apps

Example document

```json
{
  "name":"Swapnil",
  "email":"abc@gmail.com",
  "history":[...]
}
```

Looks easy.

---

Until six months later.

Now you need

* organizations

* shared conversations

* billing

* permissions

* admin panel

* analytics

* joins

* reports

Suddenly...

NoSQL becomes painful.

---

# Example

Suppose you ask

> Show me

* Premium users
* who created >50 chats
* last week
* but never used GPT-5
* sorted by payment amount

SQL

```sql
SELECT ...
JOIN ...
GROUP BY ...
HAVING ...
```

One query.

Firebase

Many reads.

Many collections.

Manual joins.

Higher cost.

---

# What do AI startups usually do?

A common stack today

```
FastAPI

↓

Postgres

↓

Redis

↓

Vector DB

↓

S3

↓

LLMs
```

Very common.

---

# Can Pydantic + Firebase replace SQL?

Technically yes.

Architecturally?

Usually no.

Pydantic only validates Python objects.

Example

```python
class User(BaseModel):
    name: str
    age: int
```

It has nothing to do with database relationships.

You still need somewhere to store data.

Pydantic doesn't solve

* joins

* transactions

* foreign keys

* indexes

* constraints

---

# My recommendation for your AI journey

Since your goal is

> Production-grade AI Engineer

I'd learn

```
FastAPI

↓

SQLAlchemy

↓

Postgres

↓

Alembic

↓

Redis

↓

pgvector
```

That stack is everywhere.

---

# Today's lesson

Now let's start SQL from absolute zero.

---

# Imagine you're Walmart

You have employees.

```
Employee

ID
Name
Salary
Department
```

Should two employees have the same ID?

Obviously no.

That's why databases need a

# Primary Key

Think of Aadhaar Number.

```
Employee

ID   Name

1    Alice
2    Bob
3    Charlie
```

ID is unique.

It identifies exactly one row.

```
PRIMARY KEY
```

means

* unique

* never NULL

* identity of the row

Example

```sql
CREATE TABLE employees (
    id INTEGER PRIMARY KEY,
    name TEXT
);
```

---

# Unique Constraint

Suppose

```
Email
```

Two users shouldn't share

```
swapnil@gmail.com
```

But email isn't the primary identity.

So

```
PRIMARY KEY

id
```

```
UNIQUE

email
```

Example

```sql
email TEXT UNIQUE
```

Difference

```
Primary Key

identity
```

```
Unique

also unique

but not the row identity
```

---

# Foreign Key

Now another table.

Orders

```
Order

id

user_id
```

How do we know

```
user_id = 5
```

actually exists?

Foreign key.

```
Users

1 Alice

2 Bob
```

Orders

```
101

user_id = 2
```

Database checks

```
Does User 2 exist?

Yes.

Allowed.
```

If

```
user_id = 999
```

No user.

Database rejects it.

This maintains **referential integrity**.

---

# Let's create it

```sql
CREATE TABLE users (

    id INTEGER PRIMARY KEY,

    email TEXT UNIQUE
);
```

```sql
CREATE TABLE orders(

    id INTEGER PRIMARY KEY,

    user_id INTEGER,

    FOREIGN KEY(user_id)
        REFERENCES users(id)
);
```

---

Think of it visually:

```
Users
+----+-------------------+
| id | email             |
+----+-------------------+
| 1  | alice@email.com   |
| 2  | bob@email.com     |
+----+-------------------+
        ▲
        │
        │ Foreign Key
        │
Orders
+-----+---------+
| id  | user_id |
+-----+---------+
|101  |    2    |
+-----+---------+
```

The arrow means every `orders.user_id` must point to an existing `users.id`.

---

# Index

Imagine this table.

```
10 million users.
```

You search

```
email
```

Without an index

Database does

```
Row1

No

Row2

No

Row3

No
...
```

Linear scan.

O(n)

---

With an index

Think of a book.

Need page

```
Transformer
```

Do you read every page?

No.

You open

```
Index

Transformer → Page 325
```

Database works similarly.

---

Create one

```sql
CREATE INDEX idx_users_email
ON users(email);
```

Now searching email becomes much faster.

---

# But why can indexes slow writes?

Every index is another data structure the database must keep in sync.

Suppose you have:

```
Users table
```

and an index on `email`.

Insert:

```sql
INSERT INTO users (id, email)
VALUES (3, 'charlie@example.com');
```

The database must:

1. Write the new row into the table.
2. Update the email index so it points to the new row.

If you have five indexes, every insert/update/delete may require updating all five.

Think of a library:

* Without a catalog, adding a new book means putting it on a shelf.
* With five catalogs (author, title, genre, ISBN, publisher), every new book also requires updating five catalog systems.

So:

* **Reads become faster** because the catalog exists.
* **Writes become slower** because the catalog must be maintained.

This is the classic read/write trade-off.

---

# Transaction

Suppose transferring money.

```
Swapnil

1000
```

```
Alice

500
```

Transfer

200

What if the system crashes after

```
Swapnil

800
```

before

```
Alice

700
```

Money vanished.

Transactions solve this.

---

```sql
BEGIN;
```

Deduct

```
UPDATE ...
```

Add

```
UPDATE ...
```

Everything succeeded?

```
COMMIT;
```

Crash?

```
ROLLBACK;
```

Database restores previous state.

---

Think of it as:

```
BEGIN
   ↓
Make several changes
   ↓
All OK?
   ↓
COMMIT  ✅

OR

ROLLBACK ❌
```

---

# Parameterized Query

Never do this:

```python
query = f"""
SELECT *
FROM users
WHERE email='{email}'
"""
```

If `email` is:

```text
' OR 1=1 --
```

The SQL becomes:

```sql
SELECT *
FROM users
WHERE email='' OR 1=1 --'
```

`1=1` is always true, so the query returns every user. This is a classic SQL injection attack.

Instead:

```python
cursor.execute(
    "SELECT * FROM users WHERE email = %s",
    (email,)
)
```

The database receives:

* SQL template
* data value

separately, so the value is treated as data, not executable SQL.

---

# EXPLAIN

Suppose

```sql
SELECT *
FROM users
WHERE email='abc';
```

Database can tell us

```
How I plan to execute this.
```

```sql
EXPLAIN
SELECT *
FROM users
WHERE email='abc';
```

Possible outputs:

Without an index:

```text
Seq Scan on users
```

Meaning: "I'll read the table row by row."

With an index:

```text
Index Scan using idx_users_email
```

Meaning: "I'll use the index to jump directly to matching rows."

This doesn't run the query—it shows the execution plan.

---

# Minimal reproducible SQL script

Below is a small PostgreSQL script that demonstrates every required concept:

```sql
-- 1. Schema
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    email TEXT UNIQUE,
    name TEXT
);

CREATE TABLE orders (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id),
    amount NUMERIC
);

-- 2. Index
CREATE INDEX idx_users_email ON users(email);

-- 3. Commit demonstration
BEGIN;

INSERT INTO users(email, name)
VALUES ('swapnil@example.com', 'Swapnil');

COMMIT;

SELECT * FROM users;

-- 4. Rollback demonstration
BEGIN;

INSERT INTO users(email, name)
VALUES ('rollback@example.com', 'Temporary User');

ROLLBACK;

SELECT * FROM users;

-- 5. EXPLAIN
EXPLAIN
SELECT *
FROM users
WHERE email = 'swapnil@example.com';
```

---

# Python parameterized query (psycopg)

```python
cur.execute(
    """
    SELECT id, name
    FROM users
    WHERE email = %s
    """,
    ("swapnil@example.com",)
)
```

---

# What you would submit for the diagnostic

**Required evidence:**

* ✅ SQL script (shown above)
* ✅ Successful `COMMIT` (the `swapnil@example.com` row remains after `COMMIT`)
* ✅ `ROLLBACK` demonstration (the `rollback@example.com` row does **not** exist after `ROLLBACK`)
* ✅ Parameterized query (Python example above)
* ✅ `EXPLAIN` output showing either `Seq Scan` or `Index Scan`
* ✅ Short explanation of why indexes speed reads but can slow writes

If PostgreSQL isn't available, you can honestly record that the concepts were understood but the execution couldn't be demonstrated because of the environment.

---

# Diagnostic ledger (honest assessment)

| Topic                         | Confidence |
| ----------------------------- | ---------: |
| Primary Key                   |      10/10 |
| Foreign Key                   |      10/10 |
| Unique Constraint             |      10/10 |
| Index                         |       9/10 |
| Transaction (Commit/Rollback) |       9/10 |
| Parameterized Query           |      10/10 |
| EXPLAIN                       |       8/10 |
| Index read/write trade-offs   |       9/10 |

Overall, I'd score this diagnostic at **9/10** conceptually. The remaining 1 point comes from actually running these commands in PostgreSQL and observing the outputs yourself.

---

## Where this fits in your AI Engineer roadmap

This lesson is much more than "learning SQL." It's the foundation for everything you'll build next.

Soon, you'll see this exact stack:

```
FastAPI
    ↓
Pydantic (validate incoming requests)
    ↓
SQLAlchemy (convert Python objects ↔ SQL)
    ↓
PostgreSQL (persistent relational data)
    ↓
Redis (cache/session/rate limiting)
    ↓
pgvector (embeddings & semantic search)
    ↓
LLMs (OpenAI, Gemini, Claude, local models)
```

Notice that **Pydantic is not a database**, and **PostgreSQL is not a validator**. Each layer has a distinct responsibility, and understanding those boundaries is what separates production-grade backend systems from demos.

In the next chapter, we'll build exactly that pipeline from scratch: **FastAPI → Pydantic → SQLAlchemy → PostgreSQL**, showing how a user registration request travels through every layer before it reaches the database. That will connect your Python knowledge with real production AI architecture.

----------------------------------------------------------

Excellent. This is one of the most important Swift Concurrency topics because it teaches **how Swift replaced "manually managing threads" with "protecting data."**

Let's study it exactly the way we studied Docker, FastAPI and ADK—from first principles.

---

# Part 1 — The Big Problem

Imagine this code without an actor.

```swift
class ResultStore {
    var values: [String] = []

    func append(_ value: String) {
        values.append(value)
    }
}
```

Now three tasks execute simultaneously.

```
Task A                Task B                Task C

append("1")
                      append("2")
                                             append("3")
```

All three are trying to modify

```
values
```

at the same time.

Remember:

```
Array is NOT thread-safe.
```

Internally `append()` is much more than one instruction.

Very roughly:

```
1. Read current count
2. Check capacity
3. Possibly allocate larger buffer
4. Copy elements
5. Write new element
6. Increase count
```

Imagine this timeline.

```
Task A

Count = 2

------------switch------------

Task B

Count = 2

append()

Count = 3

------------switch------------

Task A

Still thinks Count = 2

append()

Count = 3
```

Now one append is lost.

This is called

```
Data Race
```

---

# Traditional Solution

Before Swift Concurrency we wrote

```swift
class ResultStore {

    private let queue = DispatchQueue(label: "store")

    private var values = [String]()

    func append(_ value: String) {
        queue.sync {
            values.append(value)
        }
    }
}
```

Notice what happened.

Multiple threads exist.

But only ONE thread may enter

```
values.append(...)
```

at a time.

The queue serializes access.

---

# Swift Actor

Now compare.

```swift
actor ResultStore {

    private var values = [String]()

    func append(_ value: String) {
        values.append(value)
    }
}
```

Looks magical.

Question:

> Did Swift secretly create a DispatchQueue?

Answer:

**Conceptually yes, implementation-wise not exactly.**

Swift runtime maintains something called an

```
Actor Executor
```

Every actor owns one executor.

Think of it as

```
                Actor

          +----------------+
          |                |
          |   Mailbox      |
          |                |
          +-------+--------+
                  |
                  |
           Actor Executor
```

Tasks don't immediately execute actor methods.

Instead they send messages.

```
Task A

await store.append()

↓

Mailbox

append("1")
```

Another task

```
await store.append("2")
```

becomes

```
Mailbox

append("1")
append("2")
```

Another

```
append("3")
```

becomes

```
Mailbox

append("1")
append("2")
append("3")
```

The executor removes

exactly one message at a time.

```
Mailbox

↓

append("1")

↓

append("2")

↓

append("3")
```

So there is **never simultaneous execution of actor-isolated code**.

---

# Does that mean one thread?

No.

This is the biggest misconception.

People imagine

```
Actor
↓

One Thread
```

Wrong.

The executor may resume on different threads.

Example:

```
append()

Thread 8

↓

suspend

↓

resume

Thread 2

↓

finish
```

Perfectly legal.

The guarantee is NOT

```
same thread
```

The guarantee is

```
only one execution inside the actor at once
```

Huge difference.

---

# Does this oppose multithreading?

No.

Think of a restaurant.

There are

```
100 chefs
```

(multiple threads)

But there is

```
one cashier
```

(actor)

Customers

```
Task A

Task B

Task C
```

all submit orders simultaneously.

```
Cashier Queue

Burger

Pizza

Coffee
```

Cashier processes

```
one order

↓

next order

↓

next order
```

Meanwhile

the chefs are cooking in parallel.

So actors serialize access to shared mutable state.

They do NOT eliminate parallelism.

---

# Why is store an actor?

Because

```
values
```

is mutable shared state.

Multiple tasks

```
Task1

Task2

Task3
```

all need to modify it.

Without protection

```
Race Condition
```

With actor

```
Actor owns

values
```

Nobody else may touch it directly.

Instead

```
await store.append()
```

asks the actor politely.

---

# Why await?

Notice

```swift
await store.append(...)
```

People ask:

> append doesn't look asynchronous.

Correct.

The function itself isn't asynchronous.

The wait is because

```
You might have to wait your turn.
```

Imagine

```
Mailbox

append()

append()

append()

append()
```

Your message is number five.

So

```
await
```

means

```
Wait until actor is ready.
```

Not

```
Wait because append() downloads data.
```

Very different reason.

---

# Actor Isolation

The compiler enforces this.

Inside actor

```swift
actor ResultStore {

    var values = [String]()
}
```

Outside

```swift
store.values.append("hello")
```

Compiler says

```
No.
```

Why?

Because that would bypass the mailbox.

Instead

```
await store.append(...)
```

goes through the executor.

---

# What Isolation Guarantees

Actor isolation guarantees

✅ Only one task executes actor-isolated code at once.

```
Task A

append()

Task B

append()

Task C

append()
```

becomes

```
A

↓

B

↓

C
```

---

It also guarantees

No data races on actor state.

```
values
```

is always consistent.

---

# What It DOES NOT Guarantee

This is extremely important.

Suppose

```swift
actor Bank {

    var balance = 100
}
```

You write

```swift
let money = await bank.balance

if money > 50 {
    await bank.withdraw(50)
}
```

Looks okay?

No.

Between these two awaits

```
Task A

Read balance

100

-------------------

Task B

Withdraw 90

Balance = 10

-------------------

Task A

Withdraw 50
```

Oops.

The value changed.

Actor isolation prevents races.

It does NOT make multiple operations atomic.

Instead write

```swift
actor Bank {

    func withdrawIfPossible(_ amount: Int) {
    }
}
```

One actor method.

One mailbox entry.

One atomic operation.

---

# Child Tasks

Look here

```swift
await withTaskGroup(of: Void.self) { group in
```

This creates

```
Parent Task
```

```
          Parent
             |
    ------------------
    |       |        |
 Child1 Child2 Child3
```

Every

```swift
group.addTask
```

creates a child.

Children inherit

* priority
* cancellation
* task-local values

from the parent.

They are structured.

Meaning

The parent cannot finish until children finish.

```
Parent

wait

↓

Child1

↓

Child2

↓

Child3

↓

Parent returns
```

Unlike detached tasks.

---

# Cancellation

Notice

```swift
guard !Task.isCancelled else { return }
```

Why here?

Imagine

```
Download 4 GB

↓

Resize Images

↓

ML Processing

↓

Upload
```

Suppose user leaves.

Parent gets cancelled.

Children also become cancelled.

Swift does NOT stop them automatically.

Instead

```
Task.isCancelled == true
```

Now you decide

```
Stop immediately.
```

Cancellation is cooperative.

---

Where should cancellation checks happen?

Good places:

Before expensive work.

```swift
guard !Task.isCancelled else { return }
```

Before network requests.

After long loops.

```swift
for image in images {

    if Task.isCancelled {
        return
    }

    ...
}
```

Between processing stages.

```swift
download()

check cancellation

process()

check cancellation

upload()
```

---

# MainActor

Now the most important SwiftUI concept.

Imagine

```
Actor

ResultStore
```

protects

```
values
```

Similarly

```
MainActor
```

protects

```
UI
```

SwiftUI expects UI state to change only on the main actor.

For example

```swift
@MainActor
class ViewModel: ObservableObject {

    @Published var name = ""
}
```

Now

```swift
name = "Swapnil"
```

always happens on the main actor.

Network work should NOT be on MainActor.

Bad

```swift
@MainActor

func fetchData() async {

    let data = try await api.download()
}
```

This keeps the entire method isolated to the main actor, though the runtime can suspend during the network wait. A cleaner pattern is often to keep only UI state isolated and let the networking happen in a nonisolated service.

Better architecture:

```
               MainActor

           ViewModel

                │
                │ await
                ▼

        Network Service

        (not MainActor)

                │
                ▼

          URLSession
```

The flow is:

```
User taps button

↓

MainActor ViewModel

↓

await Network Service

↓

background execution while waiting for I/O

↓

response arrives

↓

resume on MainActor

↓

update @Published state
```

This keeps UI updates safe while allowing non-UI work to execute independently.

---

# Putting It All Together

Here's how your program executes:

```
                Parent Task
                     │
      withTaskGroup creates children
                     │
     ┌──────────┬──────────┬──────────┐
     ▼          ▼          ▼
   Child1     Child2     Child3
     │          │          │
     │ await    │ await    │ await
     └──────┬───┴──────┬───┘
            ▼
     ResultStore Actor
      (Mailbox + Executor)
            │
    append("item-1")
            │
    append("item-2")
            │
    append("item-3")
            │
            ▼
        values = [
          "item-1",
          "item-2",
          "item-3"
        ]
            │
     await snapshot()
            │
            ▼
         print(sorted)
```

## Interview takeaway

If an interviewer asks, *"How do actors provide thread safety?"*, a strong answer is:

> An actor protects its mutable state through actor isolation. Calls from outside the actor become asynchronous messages that are scheduled on the actor's executor. The executor ensures only one actor-isolated operation runs at a time, preventing data races. This is different from dedicating a thread to the actor—execution may move between different threads, but access to the actor's state is still serialized. Actors therefore provide safe concurrent access without removing parallelism from the rest of the program.

I'm glad you said that. I actually think we jumped one abstraction too high.

You're asking exactly the right question:

> **"Why do I even need Child Tasks? Why Cancellation? Why MainActor? I don't yet see the problem they're solving."**

That's exactly how we should learn it.

Let's rebuild everything from **zero**, using concepts you already know as an iOS developer.

---

# Chapter 1 : Imagine this is an iOS App

Suppose you have a screen with a button.

```text
-------------------
|                 |
|  Download       |
|                 |
-------------------
```

When the user taps it,

```swift
downloadButtonTapped()
```

is called.

Now imagine inside it you write

```swift
func downloadButtonTapped() {

    let data = downloadFromServer()

    imageView.image = UIImage(data: data)
}
```

Question:

**What happens while downloading?**

Nothing else.

The UI freezes.

Why?

Because everything is happening on

```
Main Thread
```

This is why since UIKit days we've written

```swift
DispatchQueue.global().async {

    let data = download()

    DispatchQueue.main.async {

        imageView.image = ...
    }
}
```

You already know this.

Let's draw it.

```
Main Thread

Button Tap

↓

Download

↓

Wait 5 seconds

↓

Update UI
```

The user can't scroll.

Can't tap.

Everything freezes.

So we move downloading to another thread.

```
Main Thread

Button Tap

↓

Continue responding


Background Thread

↓

Download

↓

Finished

↓

Main Thread

↓

Update UI
```

You've probably written this hundreds of times.

---

# Swift Concurrency replaces THIS

Instead of writing

```swift
DispatchQueue.global().async
```

you now write

```swift
Task {

    let data = await download()

    image = data
}
```

Notice...

You never mentioned threads.

Swift decides.

This is the first mindset change.

Old thinking:

```
I choose threads.
```

New thinking:

```
I describe work.
Swift chooses threads.
```

This is a HUGE philosophical difference.

---

# Then why do Tasks exist?

Imagine your app.

```
User opens Home Screen
```

Now simultaneously,

the app wants to

```
Download Profile

Download Notifications

Download Friends

Download Stories
```

Should these happen one after another?

```
Profile

↓

Notifications

↓

Friends

↓

Stories
```

No.

Independent work should happen together.

So Swift creates multiple tasks.

```
Task A

↓

Profile


Task B

↓

Notifications


Task C

↓

Friends


Task D

↓

Stories
```

Notice

These are NOT necessarily threads.

They're units of work.

Think

```
Task = Job
```

not

```
Task = Thread
```

---

# Now comes Child Tasks

Imagine this.

Your Home Screen loads.

It needs

```
Profile

Friends

Messages
```

The Home Screen is responsible for all three.

So conceptually,

```
Home Screen

│

├── Download Profile

├── Download Friends

└── Download Messages
```

That's exactly what child tasks are.

One parent owns many children.

```
Parent Task

│

├── Child

├── Child

└── Child
```

The parent says

> "Go do these three jobs."

It waits until all finish.

That's literally

```swift
withTaskGroup
```

Let's compare.

Without task group

```swift
await downloadProfile()

await downloadFriends()

await downloadMessages()
```

Timeline

```
Profile

↓

Friends

↓

Messages

Total = 9 seconds
```

With task group

```swift
await withTaskGroup {

    downloadProfile()

    downloadFriends()

    downloadMessages()
}
```

Timeline

```
Profile      3 sec

Friends      2 sec

Messages     4 sec


Total = 4 sec
```

Huge improvement.

This is why child tasks exist.

---

# Why not just create three Tasks?

Good question.

Imagine

```swift
Task {

    downloadProfile()
}

Task {

    downloadFriends()
}

Task {

    downloadMessages()
}
```

Who owns them?

Nobody.

They're floating around.

What if your Home Screen disappears?

Should downloads continue?

Maybe.

Maybe not.

Swift doesn't know.

Task Groups solve this.

```
Home Screen

↓

Task Group

↓

Children
```

Now the parent owns them.

When parent finishes

children must finish too.

This is called

```
Structured Concurrency
```

Think of a family tree.

```
Parent

↓

Children

↓

Grandchildren
```

Everything has an owner.

---

# Now Cancellation

Suppose user opens

```
Instagram Profile
```

The app starts downloading

```
Posts

Followers

Following

Highlights
```

Suddenly

the user presses Back.

Should downloads continue?

No.

Waste of battery.

Waste of bandwidth.

Waste of CPU.

So parent says

```
I'm cancelled.
```

All children become cancelled.

```
Parent

Cancelled

↓

Child A

Cancelled

↓

Child B

Cancelled

↓

Child C

Cancelled
```

Notice

Swift DOES NOT kill them.

Instead it politely says

```
You're cancelled.
```

Then child checks

```swift
Task.isCancelled
```

If true

```
Stop.
```

Imagine cooking.

Mom shouts

```
Dinner cancelled!
```

She doesn't grab food from your hand.

You stop cooking yourself.

Cancellation is cooperative.

---

# Why check cancellation?

Suppose

```swift
download()

resize()

compress()

upload()
```

If cancellation happened after download

Should you still resize?

No.

So

```swift
download()

guard !Task.isCancelled else { return }

resize()

guard !Task.isCancelled else { return }

compress()

guard !Task.isCancelled else { return }

upload()
```

You're saving CPU.

---

# Now MainActor

This one is MUCH easier because you already know GCD.

Old UIKit

```swift
DispatchQueue.main.async {

    label.text = "Hello"
}
```

Swift Concurrency

```swift
await MainActor.run {

    label.text = "Hello"
}
```

or

```swift
@MainActor
class ViewModel {

}
```

Both mean

```
Run on Main Thread.
```

So yes,

your understanding is correct.

MainActor exists because

UIKit

SwiftUI

AppKit

all require UI updates from the main thread.

---

# Is MainActor literally Main Thread?

Almost.

Think

```
MainActor

↓

uses

↓

Main Thread
```

So whenever someone says

```
MainActor
```

You can mentally translate it as

```
UI Thread
```

for now.

That's accurate enough until advanced Swift Concurrency.

---

# Where should network calls happen?

Not on MainActor.

Correct architecture

```
Button Tap

↓

MainActor ViewModel

↓

await API

↓

Background

↓

Network waits

↓

Response

↓

Back to MainActor

↓

Update UI
```

Notice

UI stays responsive.

---

# Finally let's break YOUR code line by line.

---

## Import Foundation

```swift
import Foundation
```

Imports Foundation framework.

Nothing related to concurrency here.

---

## Create Actor

```swift
actor ResultStore {
```

Instead of

```swift
class ResultStore
```

we're saying

```
This object owns mutable state.

Nobody should modify it simultaneously.
```

---

## Mutable Array

```swift
private var values: [String] = []
```

Initially

```
[]
```

Only the actor may touch it.

Outside code cannot.

---

## append()

```swift
func append(_ value: String) {
    values.append(value)
}
```

Adds one value.

Initially

```
[]
```

After

```
append("item-1")
```

becomes

```
["item-1"]
```

---

## snapshot()

```swift
func snapshot() -> [String] {
    values
}
```

Returns a copy of current values.

Suppose

```
["item-1","item-2"]
```

Returns

```
["item-1","item-2"]
```

---

## Entry Point

```swift
@main
struct ConcurrencyDiagnostic
```

Equivalent to

```swift
main()
```

in C.

Program starts here.

---

## Async Main

```swift
static func main() async
```

Because we're going to use

```
await
```

main itself must be async.

---

## Create Actor

```swift
let store = ResultStore()
```

Memory

```
store

↓

ResultStore

↓

values=[]
```

---

## Task Group

```swift
await withTaskGroup(of: Void.self)
```

Create one parent task.

```
Parent

↓

Task Group
```

The parent waits until every child finishes.

---

## Loop

```swift
for id in 1...3
```

Runs

```
1

2

3
```

---

## Add Child

```swift
group.addTask
```

Iteration 1

creates

```
Child 1
```

Iteration 2

creates

```
Child 2
```

Iteration 3

creates

```
Child 3
```

Tree becomes

```
Parent

│

├── Child1

├── Child2

└── Child3
```

These can all run concurrently.

---

## Cancellation Check

```swift
guard !Task.isCancelled else {
    return
}
```

If parent was cancelled,

child exits immediately.

Otherwise continue.

---

## Append

```swift
await store.append("item-\(id)")
```

For each child:

Child 1 requests

```
append("item-1")
```

Child 2 requests

```
append("item-2")
```

Child 3 requests

```
append("item-3")
```

The actor executes these one at a time, even though the children themselves are running concurrently.

The order might be:

```
item-2

↓

item-1

↓

item-3
```

or

```
item-3

↓

item-2

↓

item-1
```

Any order is valid.

---

## Read Final Values

```swift
let values = await store.snapshot()
```

After all children have completed, ask the actor for its array.

Maybe it's

```
["item-2","item-1","item-3"]
```

---

## Verify

```swift
precondition(...)
```

Checks that all three items exist, regardless of order.

If not,

the program crashes.

It's acting like an assertion.

---

## Print

```swift
print(values.sorted())
```

Sorts them for deterministic output:

```
item-1
item-2
item-3
```

even if the actor stored them in a different order.

---

## One final mental model

If you remember just one diagram from today's lesson, make it this one:

```text
                    Program Starts
                          │
                          ▼
                 ResultStore Actor Created
                          │
                          ▼
                Parent Task (main function)
                          │
                          ▼
              withTaskGroup creates 3 children
                 ┌────────┼────────┐
                 ▼        ▼        ▼
              Child1   Child2   Child3
                 │        │        │
                 │        │        │
                 └─────── await store.append(...) ───────┐
                                                         ▼
                                            ResultStore Actor Mailbox
                                                         │
                                   (one append executes at a time)
                                                         │
                                                         ▼
                                 values = ["item-2","item-1","item-3"]
                                                         │
                                                         ▼
                                           await store.snapshot()
                                                         │
                                                         ▼
                                          sort and print the result
```

Notice the key idea: **the child tasks run concurrently, but the actor serializes access to the shared array.** That's the combination that gives you both performance (parallel work) and safety (no data races).

-----------------------------------

60 mins FDE Diagnostic 

Okay so right now we will be discussing an interview format way of thinking, like the FD diagnostic and question is from the sprint00orientation.md. It will be the operation teams. The bottom statement is we are having operation teams and they get some incident alerts then they search for documents plus to look for the dashboards and then finally post the recommendation. Now we have to see how exactly we can solve this and make the process seamless and easier using the AI. So first of all let me qualify the opportunity to see what exactly is the qualification time here in the dhc2 that I am dealing with. Yes the problem seems to be frequent and yes it seems to be really slow if the humans are only involved since they have to search for all the documents and the majority of the new databases as well as dashboards. Given that if a new human has entered then he has to start from scratch itself and learn that, that is also one thing.

Another one is that it seems strategically important so that as soon as the error gets resolved it will be helpful for them. AI handles ambiguity that the normal software cannot. Yes sort of a way I can say that AI will handle that ambiguity because we have an intelligence layer sort of a thing. If we have to think about it, given that its data and its brain are already updated and the required data is available, I would like to have the required data here. How much is possible?

The couple of constraints that I am looking for are:

- The data needs to be clean as well as accountable and should be correct. That is one thing since our data and the source of truth have to be correct for our AI to work and to give the solutions correctly.

- Output quality will automatically be measured using the mean time to response, how much time we have taken to respond and solve this error as soon as possible.

- There would be an owner and the group of the real users will be using this. Probably the engineering department would be the owner of this and we will be taking accountability for this. That would be the best solution that I will be thinking of.

- This solution should be able to integrate with the current workflows in use. I can see that your logs, each and everything, get logged into the open house as well as just from the dashboard so that can be used as well for the dashboard purposes. We have the confluences and the GJARs that must also be attached to the given link epic that you are working on so that could also be helpful.

- What would make the project unsafe or uneconomic will only be, I think, as long as I can think of, probably about how clean the data is, how pure the data is, and how secure the data is. That would be the scenario I'm thinking of.

Now coming to the technical discovery of this thing. See first let me think of the solution that I am thinking here. I was thinking if it could be possible to build a production-grade quality RAC solution, sort of a thing, and RAC plus I was also thinking of introducing the graph. Maybe a new concept that I am proposing here will be the graph RAC I would be saying.

Basically an EI system and whole intelligence layer system that is grounded to your database, your documents that you have been giving, all your confluences docs that are present as well as the data documents. I was thinking if we could have a possible production-quality-grade RAC that can actually be triggered as soon as an alert has been there. It understands the alert and then it searches in the graph RAC what exactly could be the possible cause and then probably tries to create the chain of the events also.

There could be a possibility that the business is facing some sort of a bug and that bug was introduced by maybe an engineering team that was being presented wrongly by the program team. Sort of a graph, right, that introduces a causal chain. Now if this causal chain can give us a really good answer to find out the root cause of the problem, we could have a system where we can actually create the jira tickets as well as a proposed solution in the comments based on the scenarios that have been given to us. This is a brief broad overview of the solution that I am proposing here. Now seeing who performs this task, we'll be taking ownership to create this system and we'll try to integrate in your system how exactly you can do that. The event starts when you must have some sort of an X matters or some way in which the events are getting triggered for you. The alerts are getting triggered. We can have an attachment there itself and it can trigger. How fresh must it be as soon as your data gets resolved? Our document histories as well as the source of truth, the brain that we have here for the graphic, should get updated.

Another thing is permissions. We can have a rule-based authentication here, RBAC here, so your engineering team can have access to whatever data has been present in the engineering site as well as for the others also. PI data, I would say, we won't be requiring that. We are talking about the causal chains as well as the impact and implementation side here. We would try to hash mask PI data as soon as possible and it would be better if it's getting ingested there. We can have some sort of a validation check there itself. What can leave the customer boundary? See if the documents that are not present but have been introduced for the first time. That would be a sort of a learning curve for us. Also it can give you that, "Okay this needs to be tested." As soon as a manual intervention has been done and the solution has been updated, our graph track would also be a bit so that in future if a similar sort of issue comes then our AI would be prepared. It would be learning from itself in a sort of way how correction, retention, deletion, and the audit are handled. All these would be the RAG implementation. We are thinking about the cosine similarities here so that we are not having duplications in our database for the documents that we want and can represent it in historical examples. Definitely it can become an evil set. Definitely it can become any was or how we have Solver work. We will be having that and we can train and see the scenarios that would be there, right, set of the documents in the right method metadata that is required. Now coming to the integration, let's talk about the integration thing. Definitely it will be an AI system that I believe could work directly with the pub/sub as soon as XMeter publishes an event and AI would be the subscription-based. It would be triggering that and I don't think a webhook would be required or an HTTP protocol. On a quick basis that would be better here.

We can have connectors in Slack as well as the GitHub connector so that we need the information on what exactly are the code changes that are required if we are talking about the engineering side and causal. As I explained above for the graph, we could have end-user-delegated authority of the service. I don't even know. That could be. We can think of it as: let's see who's only required. The network would also be: we can have a new proxy-based firewall so that your organization people only would be able to access that data as well as access the platform that we will be building for you guys. A few years after the launch, it could definitely be there and we'll be having the logs for that. We will be monitoring that if some sort of issues come. We are there for you to give you that service there itself.

Now let's think of a pilot. I will be proposing that if we can have a graph-based solution for you. We would be requiring the clean metadata of the documents that have been there for you and we will be providing you the architecture for that, the causal chains and everything that would be there. It would be able to help given that we'll be having it and then we can test on the hypothesis as well as the evils for how the past has been working there. That evil would be able to help us with what exactly is the quality of the data that we would be requiring them.

For the scope say let's stick to a pilot where we can have it for the specific department itself rather than going and making it launch available to the whole public. Let's try to test it out within the internal teams and let's try to have it specific for a certain group. I think for that we would be requiring some sort of metrics, like meantime-to-resolve metrics, which could be one that we can think of: how exactly our AI helps in solving the bugs as soon as possible. That would be there.

Architecture-wise I told you that we will be requiring the VPN Firefox proxy wall that would be there and definitely will be giving you a dashboard where you can have the responsiveness of the AI, what exactly it has, and how exactly it is clear and what would be the recommended solution for that. For the pilot let's stick to the recommendation itself rather than having the agent itself do the code changes and raise the PRs for that. That would be there for the scope of the pilot that we are thinking of. We can have a provider fallback that we need to think of. I really don't have the idea right now and telemetry audits are there, okay, in degradations, reuse rules.