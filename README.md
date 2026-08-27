# 🏴‍☠️ The Lost Treasure Hunt

> **A modular, riddle-based Python CLI scavenger hunt built from scratch
> to practice real Python software design.**

The Lost Treasure Hunt is a terminal-based adventure game where the
player explores a connected world, solves timed puzzles, collects
progression items, manages health and score, survives random threats,
and follows a chain of clues toward a final Treasure Room.

This project was intentionally kept **Python-only and CLI-based** rather
than turning it into a GUI, database application, or networked game. The
goal was to build a complete, understandable Python application using
classes, modules, state management, validation, timers, random events,
and structured terminal UI.

## Why this project exists

This started as a small Python scavenger-hunt assignment and evolved
into a modular application with:

-   Object-oriented game entities
-   Multiple puzzle types
-   Timed challenges
-   Inventory-based progression
-   Locked locations
-   Health and scoring systems
-   Random environmental threats
-   ASCII map visualization
-   A torch/battery gameplay mechanic
-   Multi-stage Treasure Map assembly
-   A structured Colorama CLI
-   A complete win/game-over flow

The project is deliberately designed to be **small enough to understand
but complex enough to demonstrate software engineering decisions**.

------------------------------------------------------------------------

## 🎯 Objective

Build a complete Python command-line game that demonstrates practical
Python programming beyond isolated exercises.

The project objectives were to:

1.  Apply Python OOP concepts in a real application.
2.  Separate responsibilities across modules.
3.  Build a connected game world using objects and relationships.
4.  Implement puzzle validation and timed interaction.
5.  Use inventory items as progression gates.
6.  Manage mutable game state such as health, score, location, and
    completion.
7.  Introduce random events and consequences.
8.  Build a readable CLI without relying on a heavy UI framework.
9.  Debug and stabilize the application through iterative versions.
10. Produce a portfolio-quality Python project that can be explained in
    a viva/interview.

------------------------------------------------------------------------

## 🧰 Tech Stack

  Technology                   Purpose
  ---------------------------- ---------------------------------
  Python 3                     Core programming language
  Colorama                     Cross-platform terminal colors
  `time`                       Timing and small UI transitions
  `random`                     Random threat activation
  `os`                         Terminal screen clearing
  `shutil`                     Detecting terminal width
  Standard `input()`           Player interaction
  ASCII / Unicode characters   Terminal UI and map

### External dependency

``` bash
pip install colorama
```

No GUI framework, database, web framework, game engine, or heavy CLI
framework is required.

------------------------------------------------------------------------

## 📦 Project Structure

``` text
The_Lost_Treasure_Hunt/
│
├── main.py
├── game.py
├── player.py
├── location.py
├── puzzle.py
├── timer.py
├── threat.py
├── inventory.py
│
├── test_player.py
├── test_location.py
│
└── README.md
```

### File responsibilities

#### `main.py`

Application entry point.

It creates the `Game` object and starts the game.

#### `game.py`

The central controller/orchestrator.

It handles:

-   CLI rendering
-   world creation
-   dashboard
-   map
-   game loop
-   exploration
-   travel
-   puzzle execution
-   item rewards
-   threats
-   Dark Cave torch mechanic
-   Library progression
-   Treasure Room
-   Game Over

This is intentionally the largest module because it coordinates the game
state and interactions.

#### `player.py`

Defines the `Player` class.

Player state includes:

``` text
name
health
max_health
score
inventory
current_location
```

Important methods include:

``` text
move_to()
add_item()
show_inventory()
take_damage()
heal()
show_health()
is_alive()
add_score()
remove_score()
show_status()
```

#### `location.py`

Defines the `Location` class.

It stores:

-   name
-   description
-   puzzle
-   connected locations
-   required item

This allows the world to be represented as connected objects rather than
hard-coded menu jumps.

#### `puzzle.py`

Defines the `Puzzle` class.

Each puzzle stores:

``` text
puzzle_type
question
answer
reward
difficulty
time_limit
completed
```

The same class supports:

-   Riddles
-   Logic puzzles
-   Cipher puzzles
-   Pattern puzzles

Answer checking is normalized using lowercase/whitespace stripping.

#### `timer.py`

Contains the `GameTimer` utility used by timed puzzles.

The selected implementation measures elapsed time around standard
terminal input.

#### `threat.py`

Defines environmental threats/traps.

The current game uses a random Hidden Spike Trap that damages the
player.

#### `inventory.py`

A standalone inventory implementation retained from an earlier
architecture.

The active game architecture intentionally uses:

``` python
player.inventory
player.add_item()
```

instead of maintaining two competing inventory controllers.

#### `test_player.py`

Player-related testing.

#### `test_location.py`

Location-related testing.

------------------------------------------------------------------------

# 🧠 Python Concepts Demonstrated

## 1. Classes and Objects

The project uses classes for:

-   `Game`
-   `Player`
-   `Location`
-   `Puzzle`
-   `GameTimer`
-   `Threat`
-   `Inventory`

This demonstrates modeling game entities as objects with state and
behavior.

## 2. Encapsulation

Player data and behavior live inside `Player`.

Location behavior lives inside `Location`.

Puzzle behavior lives inside `Puzzle`.

The controller coordinates these objects rather than putting every
responsibility into one giant function.

## 3. Lists

Lists are used for:

-   player inventory
-   location connections
-   puzzle collections
-   dashboard rows
-   map rows

## 4. Conditional Logic

Examples include:

-   checking whether a location requires an item
-   checking puzzle completion
-   checking health
-   determining whether the cave is lit
-   validating menu choices
-   deciding which Library puzzle comes next

## 5. Loops

Loops drive:

-   the main game loop
-   puzzle sequences
-   location lists
-   inventory display
-   map generation
-   terminal animation frames

## 6. Exception Handling

Travel input is protected against invalid numeric input and invalid
destination indexes.

## 7. Modules

The project is intentionally divided into multiple `.py` files so that
responsibilities are separated.

## 8. State Management

The game maintains state such as:

``` text
current location
health
score
inventory
completed puzzles
cave_lit
game_running
```

## 9. Randomness

Threat activation uses random selection.

## 10. Time-Based Logic

Puzzle difficulty includes time limits and timeout consequences.

------------------------------------------------------------------------

# 🎮 Features

## Core Gameplay

-   Explorer name input
-   Connected world
-   Explore action
-   Travel action
-   Inventory action
-   Exit action
-   Player dashboard
-   Health system
-   Score system
-   Game Over state
-   Treasure Room victory state

## Puzzle System

### Ancient Forest

Hard riddle:

> I am a two-digit number.\
> My digits add up to 9.\
> My tens digit is twice my ones digit.\
> What number am I?

Answer:

``` text
63
```

Reward:

``` text
+20
```

This puzzle also awards:

``` text
Ancient Key
Torch Batteries
```

### Dark Cave

Logic puzzle:

``` text
If 5 cats catch 5 mice in 5 minutes,
how long for 1 cat to catch 1 mouse?
```

Answer:

``` text
5 minutes
```

### Ancient Library

Three sequential stages:

1.  Cipher → Treasure Map Piece 1
2.  Medium Riddle → Treasure Map Piece 2
3.  Hard Pattern → Treasure Map Piece 3

Cipher:

``` text
UFTU
```

Answer:

``` text
TEST
```

Riddle:

``` text
I am always in front of you but can never be seen.
What am I?
```

Answer:

``` text
FUTURE
```

Pattern:

``` text
2, 6, 12, 20, 30, ?
```

Answer:

``` text
42
```

------------------------------------------------------------------------

# 🔐 Progression System

The game is not just a collection of unrelated puzzles.

Progression is dependency-driven:

``` text
Ancient Forest
      │
      ├── Solve Riddle
      │
      ├── Ancient Key
      └── Torch Batteries
              │
              ▼
       Abandoned Cabin
              │
              └── Torch
                    │
                    ▼
                Dark Cave
                    │
                    ├── Light Torch
                    │
                    ├── Logic Puzzle
                    │
                    └── Cave Clue
                            │
                            ▼
                     Ancient Library
                            │
                 ┌──────────┼──────────┐
                 ▼          ▼          ▼
              Cipher     Riddle     Pattern
                 │          │          │
              Piece 1     Piece 2    Piece 3
                 └──────────┼──────────┘
                            ▼
                    Complete Map
                            │
                            ▼
                     Treasure Room
                            │
                            ▼
                         Victory
```

------------------------------------------------------------------------

# 🗺️ ASCII Map

The dashboard maintains a permanent map panel.

Before the torch is activated:

``` text
Treasure Room
      │
Ancient Library
      │
????????????????????
      │
Abandoned Cabin
      │
Ancient Forest
```

After the torch is activated:

``` text
Treasure Room
      │
Ancient Library
      │
Dark Cave
      │
Abandoned Cabin
      │
Ancient Forest
```

The map is intentionally simple. It is a visual representation of the
fixed game route rather than a procedural world generator.

------------------------------------------------------------------------

# 🔦 Torch Mechanic

The Dark Cave is deliberately hidden until the player has the required
equipment.

The Forest provides:

``` text
Ancient Key
Torch Batteries
```

The Cabin provides:

``` text
Torch
```

Entering/exploring the Dark Cave triggers the mandatory lighting
sequence.

The game verifies:

``` text
Torch exists
AND
Torch Batteries exist
```

Only then does:

``` python
self.cave_lit = True
```

and the map changes from:

``` text
????????????????????
```

to:

``` text
Dark Cave
```

A lightweight terminal reveal animation is used instead of adding
another UI dependency.

------------------------------------------------------------------------

# ⚔️ Health, Score and Threats

### Starting state

``` text
Health: 100/100
Score: 0
```

### Score

Puzzle rewards are defined by puzzle.

Current puzzle rewards:

``` text
Forest Riddle   +20
Dark Cave       +30
Library Cipher  +40
Library Riddle  +30
Library Pattern +40
```

Timeout:

``` text
-10 Score
```

Wrong puzzle answer:

``` text
-10 Health
```

Random Hidden Spike Trap:

``` text
-15 Health
```

Health cannot fall below zero and score cannot fall below zero.

------------------------------------------------------------------------

# ⏱️ Timer Design Decision

One important technical limitation appeared during development:

Standard Python `input()` blocks the normal execution flow.

A continuously updating countdown beside a blocking `input()` therefore
requires additional concurrency/threading or terminal-control
complexity.

Instead, the project uses a stable approach:

1.  Display the time limit.
2.  Start `GameTimer`.
3.  Accept the answer.
4.  Stop the timer.
5.  Check elapsed time.
6.  Apply `-10` score if expired.

This was intentionally chosen because the project goal was **reliable
Python architecture rather than unnecessary concurrency complexity**.

------------------------------------------------------------------------

# 🧩 Algorithms

## 1. Puzzle Answer Validation

``` text
Input answer
     ↓
strip whitespace
     ↓
convert to lowercase
     ↓
compare with stored answer
     ↓
Correct / Incorrect
```

Implemented conceptually as:

``` python
player_answer.lower().strip() == answer.lower().strip()
```

## 2. Sequential Library Puzzle Algorithm

``` text
For each Library puzzle:
    if puzzle is incomplete:
        solve it
        stop
```

This guarantees the intended order:

``` text
Cipher → Riddle → Pattern
```

## 3. Location Requirement Algorithm

``` text
Player chooses destination
        ↓
Does destination require item?
        ↓
      Yes
        ↓
Is item in inventory?
    /          \
  Yes           No
  ↓             ↓
Travel       Block travel
```

## 4. Random Threat Algorithm

``` text
Generate random number 1–5
        ↓
If number == 3
        ↓
Trigger Hidden Spike Trap
        ↓
15 health damage
```

This gives a 1-in-5 activation chance per threat check.

## 5. Map Generation

The map is generated from an ordered list of locations and connector
rows.

It is not a random/procedural map.

------------------------------------------------------------------------

# 🏗️ Architecture

The project follows a lightweight modular object-oriented architecture.

``` text
                    ┌─────────────┐
                    │   main.py   │
                    │ Entry Point │
                    └──────┬──────┘
                           │
                           ▼
                    ┌─────────────┐
                    │   Game      │
                    │ Controller  │
                    └──────┬──────┘
                           │
          ┌────────────────┼────────────────┐
          ▼                ▼                ▼
      Player           Location          Puzzle
          │                │                │
          │                │                └── GameTimer
          │                │
          │                └── Connections
          │
          └── Inventory / Health / Score

                    Game
                     │
                     └── Threat
```

### Responsibility principle

The architecture intentionally avoids making every class responsible for
everything.

For example:

-   `Player` owns player state.
-   `Location` owns location data/connections.
-   `Puzzle` owns puzzle data/validation.
-   `Threat` owns threat behavior.
-   `Game` coordinates the interactions.

------------------------------------------------------------------------

# 📈 Version History

> **Versioning note:** The project was developed iteratively and some
> later version labels were used as development milestones rather than
> formal releases. The original progress tracker documents the early
> versions, while later iterations were tracked during development
> conversations. The source `game.py` header was not updated on every
> milestone, so this history should be treated as an engineering
> timeline rather than a strict Git release history.

  -----------------------------------------------------------------------------------------
  Version           Milestone                 Main Change          Problem / Lesson
  ----------------- ------------------------- -------------------- ------------------------
  v0.1              Initial Working Version   Basic CLI scavenger  Established the initial
                                              hunt structure       game concept

  v0.3              Inventory                 Added item           Needed items to become
                                              collection           meaningful progression
                                                                   objects

  v0.4              Location Integration      Connected locations  World objects needed to
                                              and gameplay         interact correctly

  v0.5              Player Expansion          Added health, score, Player became a real
                                              inventory, movement, stateful entity
                                              status               

  v0.5.2            Player Refinement         Refined Player       Evolving architecture
                                              methods              required compatibility
                                                                   work

  v0.5.3            Game Integration          Integrated Player    Reduced mismatch between
                                              changes into Game    controller and player
                                                                   state

  v0.7              Gameplay Expansion        Threats and time     Gameplay needed
                                              pressure introduced  consequences beyond
                                                                   solving puzzles

  v0.7.1            Location Refinement       Improved location    Improved world
                                              handling             integration

  v0.7.2            Game Refinement           Improved overall     Reduced integration
                                              game flow            problems

  v0.7.3            Travel Feedback           Improved movement    Travel needed clearer
                                              messages             user feedback

  v0.7.4            Inventory Usage           Improved item        Inventory became part of
                                              collection/usage     progression

  v0.75             Compatibility/Stability   Standardized on      Fixed
                                              `Player.inventory`   `inventory.add_item()`
                                                                   vs `player.add_item()`
                                                                   mismatch

  v0.8              Feature Upgrade           Riddle, Logic,       Established the first
                                              Cipher, threats,     stable gameplay
                                              timers, HUD          architecture

  v0.8 Stable       Stable Baseline           Timed challenges,    Provided a reliable base
                                              score penalties,     for later UI/gameplay
                                              item requirements    work

  v0.81             Colorama/UI milestone     Introduced colorized Improved presentation
                                              CLI direction        without a heavy UI
                                                                   framework

  v0.82             Clean CLI milestone       Structured boxes,    UI became
                                              terminal width       presentation-oriented
                                              handling, Colorama   
                                              UI                   

  v0.83             ASCII Map                 Added persistent     Map had to stay aligned
                                              world/map            with terminal layout
                                              visualization        

  v0.84             Save/Load experiment      Considered save/load Rejected because the
                                                                   game is designed to be
                                                                   completed in one sitting

  v0.85             Progression expansion     Harder Forest        Puzzle rewards became
                                              riddle, additional   more meaningful
                                              progression items    

  v0.86             Dark Cave mechanic        Torch + batteries +  Added environmental
                                              hidden cave + reveal dependency to
                                                                   progression

  v0.90             Integrated feature        Library map pieces,  Feature-complete
                    milestone                 final progression,   direction established
                                              treasure opening,    
                                              consolidated         
                                              gameplay             
  -----------------------------------------------------------------------------------------

### Important engineering decisions

#### Save/Load was deliberately rejected

Save/load was considered but removed from scope.

Reason:

The game is designed as an on-the-spot scavenger hunt. Saving would
weaken the intended one-session challenge and add file persistence
complexity without improving the core experience.

#### Database was rejected

The game has no persistent business data that needs a database.

Player state exists only for the current session.

#### Multiplayer was rejected

Multiplayer would require networking, synchronization, conflict
handling, and a completely different architecture.

That would distract from the project's Python-learning objective.

#### Procedural map generation was rejected

The world is intentionally fixed and puzzle-driven.

A deterministic map makes the puzzle sequence easier to design, test,
explain, and demonstrate.

#### Heavy CLI frameworks were rejected

Rich was considered but Colorama was selected because:

-   Smaller dependency footprint
-   Lower abstraction overhead
-   Easier to understand as a Python student
-   Enough functionality for the desired UI

------------------------------------------------------------------------

# 🧪 Testing

The project was tested through iterative execution and debugging.

Important test scenarios include:

-   Game startup
-   Player name input
-   Initial location
-   Player dashboard
-   Exploration
-   Travel
-   Locked location handling
-   Correct puzzle answers
-   Incorrect puzzle answers
-   Timeout
-   Score updates
-   Health damage
-   Random threats
-   Inventory updates
-   Ancient Key progression
-   Torch discovery
-   Torch Batteries
-   Dark Cave visibility
-   Torch activation
-   Library puzzle sequence
-   Map Piece 1
-   Map Piece 2
-   Map Piece 3
-   Complete Treasure Map
-   Treasure Room access
-   Treasure opening
-   Game Over
-   Invalid menu input
-   Invalid travel input

------------------------------------------------------------------------

# 🐛 Problems Solved During Development

## Inventory architecture mismatch

Earlier versions had both:

``` text
inventory.add_item()
```

and:

``` text
player.add_item()
```

This created compatibility problems.

The architecture was standardized around:

``` python
player.inventory
player.add_item()
```

The standalone `inventory.py` remains as a retained module/reference.

## CLI line wrapping

Side-by-side panels initially broke when terminal width was
insufficient.

The UI was redesigned around terminal width detection and fixed panel
widths.

## Map connector alignment

Hard-coded spaces caused connectors to escape their panel.

The map was changed to center locations/connectors based on the panel
width.

## Indentation errors

During UI iteration, inserting map code at the wrong indentation level
caused:

``` text
IndentationError
```

and later:

``` text
AttributeError: 'Game' object has no attribute 'map_lines'
```

The lesson was that UI helpers must remain inside the `Game` class and
should be modified as complete methods rather than pasted fragments.

## Treasure screen nesting

The final treasure display initially placed a manually drawn ASCII box
inside the existing `box()` renderer.

That produced a nested, visually broken layout.

The solution was to let the existing `box()` renderer handle the entire
final screen.

------------------------------------------------------------------------

# ⚠️ Limitations

The project is intentionally scoped.

### 1. CLI only

There is no GUI.

### 2. No persistence

Game progress exists only during the current run.

### 3. No multiplayer

The game supports one player/session.

### 4. Fixed world

The map and location sequence are predefined.

### 5. Timer/input limitation

The timer checks expiration around blocking terminal input rather than
rendering a continuously updating countdown beside the input prompt.

### 6. Basic answer validation

Answers are string-based and do not support advanced natural-language
interpretation.

### 7. Terminal-dependent layout

The CLI relies on terminal dimensions and Unicode box-drawing
characters.

------------------------------------------------------------------------

# 🚀 Future Scope

Potential future versions could include:

## Short-term

-   More puzzle types
-   More locations
-   Better automated testing
-   Cleaner test coverage
-   Configuration-driven puzzle definitions
-   Better terminal compatibility
-   Final README screenshots

## Medium-term

-   Difficulty scaling
-   Hint system with score penalties
-   Multiple game routes
-   More inventory interactions
-   Event system
-   Puzzle randomization

## Long-term

If the goal changed from a Python-learning CLI project to a larger
software product, the architecture could evolve toward:

-   Persistent storage
-   Web/GUI frontend
-   Multiplayer/network architecture
-   Database-backed player profiles
-   Procedural world generation
-   Analytics
-   Content management for puzzles

These are deliberately **future possibilities**, not requirements for
the current project.

------------------------------------------------------------------------

# 💡 What I Learned

This project taught more than Python syntax.

### Python

-   Classes and objects
-   Constructors
-   Methods
-   Lists
-   Conditionals
-   Loops
-   Exceptions
-   Imports
-   Modules
-   String normalization
-   Random numbers
-   Time measurement
-   Terminal control

### Software design

-   Separation of responsibilities
-   Object interaction
-   State management
-   Dependency-based progression
-   Reusable UI helpers
-   Compatibility management
-   Incremental development

### Debugging

The project repeatedly exposed real development problems:

``` text
IndentationError
AttributeError
UI wrapping
Alignment bugs
State synchronization
Module compatibility
```

Solving these problems was a major part of the learning outcome.

### Scope management

One of the biggest lessons was that **adding a feature is not
automatically an improvement**.

Save/load, database, multiplayer, and procedural maps were considered
and rejected when they did not strengthen the project's core objective.

------------------------------------------------------------------------
