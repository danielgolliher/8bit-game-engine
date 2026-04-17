# 8-Bit Game Engine — Plan

## 1. The vision

A browser-based "game maker" where a player picks a handful of options from menus, and those picks combine into a unique, playable 8-bit-style mini-game. Once they like their creation, they hit **Publish** and get a shareable link that anyone can open and play in their browser — no install, no account.

The charm comes from **combinatorics**: even with ~5 choices of 6 options each, you get 6^5 = 7,776 distinct games. Each one feels like a tiny, hand-crafted NES cartridge.

---

## 2. What kind of game?

This is the single biggest decision and I want your input before I build. Here are the candidates, from simplest to most ambitious:

### Option A — Top-down arena survival *(my recommendation)*
- Hero stands in a square arena. Enemies spawn in waves from the edges. You move (arrow keys) and attack (space). Survive N waves to win.
- **Why I like it**: easy to implement, every customization option has obvious visual impact, matches 8-bit classics like *Smash TV* or *Gauntlet*.

### Option B — Side-scrolling platformer
- Hero runs right, jumps over pits, stomps enemies, reaches a flag. One or two screens long.
- **Why**: iconic 8-bit feel (Mario-like). **Why not**: level design is hard to generate from simple "picks" — you'd need pre-built level templates per environment.

### Option C — Dungeon crawler (Zelda-style rooms)
- Top-down, move between rooms, fight enemies, find a key, open a door.
- **Why**: most replayability. **Why not**: bigger scope; room layout adds complexity.

### Option D — Endless runner
- Hero auto-runs, player taps to jump. Enemies and obstacles scroll past.
- **Why**: dead simple. **Why not**: less customization payoff — environment barely matters.

**My pick: A (arena survival)** unless you have a strong preference. It's the best ratio of "customization options actually matter" to "I can ship this."

---

## 3. What the player customizes

For each slot, the player picks one of ~6 options. (We can expand later.)

| Slot | Examples | Gameplay effect |
|---|---|---|
| **Hero sprite** | Knight, Ninja, Wizard, Robot, Alien, Astronaut | Visual only, but each has a subtle stat tweak (speed, attack range) |
| **Environment** | Forest, Dungeon, Space station, Desert, Underwater, Lava cave | Tileset + background color + ambient particle (e.g., snow, embers) |
| **Enemy type** | Slimes, Skeletons, Drones, Goblins, Ghosts, Bats | Different movement AI per type |
| **Music track** | Heroic, Eerie, Upbeat chase, Mysterious, Boss battle, Chill | Loops during play |
| **Win condition** | Survive 5 waves / Kill 50 / Collect 10 coins / Reach 60 seconds | Changes objective + HUD |
| **Difficulty** | Easy / Normal / Hard | Enemy speed, spawn rate, HP |

**Bonus ideas I'd like your take on:**
- Weapon pick (sword / bow / magic blast / boomerang) — more code but big gameplay variety
- Color palette swap (NES, Game Boy green, monochrome, neon) — easy, very stylish
- Hero name / game title the player types — makes it feel personal when shared

---

## 4. Tech stack

- **HTML5 Canvas + vanilla JavaScript** — no build step, runs anywhere, easy to share as a single file if needed.
- **No framework** for the game loop — 8-bit games are simple enough that a 200-line game loop is cleaner than pulling in Phaser.
- **Web Audio API** for music — I'll either ship short looping chiptune MP3/OGG files (simpler) or synthesize tones procedurally (cooler but more work). **Question for you below.**
- **Sprites**: I'll use simple programmatically-drawn pixel art (colored rectangles in recognizable shapes) or CC0 sprite sheets from sites like Kenney.nl. **Question for you below.**

---

## 5. Publishing & sharing

Three options, in order of simplicity:

### Option 1 — URL encoding *(my recommendation for MVP)*
The player's picks are encoded into the URL itself (`?hero=ninja&env=dungeon&enemy=slime&music=eerie&...`). Sharing = copy the URL. No backend, no database, works forever.
- ✅ Zero infrastructure
- ✅ Infinitely scalable (it's just a URL)
- ❌ URLs are ugly unless we shorten them

### Option 2 — Local file export
Player downloads a `.game.json` file, sends it to friends, friends drop it onto the engine.
- ✅ Still no backend
- ❌ Higher friction to share

### Option 3 — Hosted with short codes
Tiny backend (e.g., Cloudflare Workers + KV) stores each game as a 6-char code like `PLY-42X`.
- ✅ Shareable codes are clean and memorable
- ❌ Needs hosting, has running cost, needs moderation eventually

**My pick: start with Option 1 (URLs), and if you love the project we can upgrade to Option 3 later.**

---

## 6. MVP scope

What I'll build on the first pass:

1. A **title screen** with the game's title (or "Untitled")
2. A **builder screen** with dropdowns/buttons for the 6 customization slots + a live preview sprite
3. A **play screen** — the actual arena game using the chosen settings
4. A **share screen** — "copy this link" after you publish
5. Direct-link mode — if the URL already has params, skip the builder and go straight to play

**Out of scope for v1** (can add later): leaderboards, saving high scores, upvoting other people's games, mobile/touch controls, level editor beyond the preset slots.

---

## 7. File layout (proposed)

```
8bit-game-engine/
├── index.html          # builder + publish UI
├── play.html           # game runner (reads URL params)
├── engine/
│   ├── game.js         # main game loop
│   ├── sprites.js      # pixel art definitions
│   ├── enemies.js      # enemy AI
│   ├── audio.js        # music + SFX
│   └── config.js       # the lookup tables for every slot option
├── assets/
│   ├── music/          # chiptune loops
│   └── sfx/            # blips, hits, deaths
└── PLAN.md             # this file
```

---

## 8. Questions for you before I start

Please answer these so I can build the right thing:

1. **Game type** — Arena survival (A), or a different one from §2?
2. **Music approach** — ship short chiptune MP3 loops I find under CC0, or synthesize chiptune procedurally in the browser (more authentic 8-bit, but takes longer)?
3. **Sprites approach** — simple programmatic pixel art I draw in code (consistent style, no dependencies), or real pixel-art sprite sheets from Kenney.nl / OpenGameArt (prettier, adds asset files)?
4. **Publishing** — start with URL-encoded sharing (Option 1), or skip straight to a hosted short-code system?
5. **Bonus slots** — want me to include any of: weapon picker, color-palette swap, custom game title/hero name?
6. **Hosting** — where do you want the final thing to live? (local file you open in the browser, GitHub Pages, somewhere else you already use?)

Once you answer these, I'll build the MVP.
