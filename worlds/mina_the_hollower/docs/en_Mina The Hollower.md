# Mina The Hollower

If you are reading this, you have either been invited to or are interested in helping alpha test Mina the Hollower Archipelago. This randomizer is still in ALPHA, so please play with the intention of reporting bugs and providing feedback.

- If you are unsure what is causing the issue, create an issue on the [AP World Issue Tracker](https://github.com/FyreDay/Archipelago-MinaTheHollower/issues).
- If you know the problem is with the mod itself, create an issue on the [Mod Issue Tracker](https://github.com/Axertin/mth-apclient/issues)

## Current State

The randomizer is currently believed to be completable. Below is an ever-changing list of implemented features we want tested, and known bugs. Please let us know how your experience goes!


- Known issues:
  - Backer code breaks any save created in AP. Remove backer code for AP.
  - You are forced to teleport to ossex if transitions take you to ropes without you having climb
  - Goal in theory sends after a fix. Let us know how if it sends.

- Location logic has been improved, but still has bugs. Please report anything that UT says is inaccessible that you can reach, or anything UT says is accessible that you cannot reach.

### Tracker
Use [Universal Tracker](https://github.com/FarisTheAncient/Archipelago/releases?q=Tracker) to keep track of what you can access. There is also an in-progress map tracker built into UT that is actively being worked on.
The map tracker is currently complete for Train, Ossex, Loner's Landing, Southern Outskirts, and Eastern Hearth. Please limit map tracker feedback to these areas for now.

You can use ```/explain Max Jump``` To see what AP thinks your best trinket combo is at the moment

We would also appreciate feedback on how the map tracker is organized and whether you find it useful as development continues.

## Installing

If you previously had this installed, remove the version.dll or the libmthap.so from your game directory

Download the mod and the AP world. The mod will be a zip file with your OS name
- [Latest Mod Release](https://github.com/Axertin/mth-apclient/releases/latest)

- [Latest AP World release](https://github.com/FyreDay/Archipelago-MinaTheHollower/releases/latest)

### Switch to the Experimental Modding Beta
 The mod requires a Steam copy of Mina the Hollower on the **experimental-modding Beta** It also requires 
 `-mod -mod-allow-code` launch options set (this enables loading a mod's code library).

If you have never done this before, 
1. navigate to Steam->Mina The Hollower->Properties->Game Versions & Betas
2. Select `experimental-modding` in the version list

### Windows

Unzip the mod.zip (containing a `apclient` folder with a `mod.dll` and `mod.yc`) inside into:

```
%APPDATA%\Yacht Club Games\Mina the Hollower\mods
```
so that the .dll and .yc files are in
```
%APPDATA%\Yacht Club Games\Mina the Hollower\mods\apclient\
```

Set Steam launch options for Mina the Hollower:

```
-mod -mod-allow-code
```

The game's mod loader writes `%APPDATA%\Yacht Club Games\Mina the Hollower\mod.log` each run;
the mod's own runtime log is `%LOCALAPPDATA%\mth-apclient\mthap_*.log`.

### Linux

The mod is installed into Mina The Hollower's save directory (the SDL prefix path), not the install dir.

Unzip the mod.zip (containing a `apclient` folder with a `mod.so` and `mod.yc`) inside into:, 

```
~/.local/share/Yacht Club Games/Mina the Hollower/mods
```
so that the .dll and .yc files are in
```
~/.local/share/Yacht Club Games/Mina the Hollower/mods/apclient/
```
Set Steam launch options for Mina the Hollower:

```
-mod -mod-allow-code
```

The game's mod loader writes `~/.local/share/Yacht Club Games/Mina the Hollower/mod.log` each
run (whether a mod loaded, version-check or load failures) - check it first if the mod doesn't
appear. The mod's own runtime log is `~/.local/share/mth-apclient/mthap_*.log` (one file per run).

## Running
An ImGui overlay window should appear allowing connection and disconnection to an AP server. If it
doesn't appear or you want to hide it once connected, it can be toggled by pressing `F2`.

1. Connect to AP immediately on game launch
2. Create a new save or load into a save already played on with this slot

# Warnings

**NEVER CREATE A SAVE AND THEN CONNECT**

**NEVER COPY A SAVE AND PLAY THAT SAVE IN AP**

**NEVER LOAD INTO A SAVE AND THEN CONNECT**

**NEVER LOAD INTO A VANILLA SAVE YOU DONT WANT MODIFIED**

There is also a console you can access by presssing **F1**. type ```help``` to see commands

## What does randomization do to this game?

All chests, shops, trinkets, and large Bonestones are randomized.

### Goals
- Defeat Giga Lionel and repair the final generator
- Repair a target number of generators

## Options

### Start In Ossex
- Skips Loner's Landing. You can still teleport there from the pause menu.

### Kear Rando
- **Vanilla**: Universal Kears are placed in the multiworld. Any Kear Lock opened before receiving every Kear will be **OUT OF LOGIC**
- **AP Items**: Each Kear Lock is removed by a unique AP item.

### Bone Up Caps
- **Per Upgrade**: Attack, defense, and sidearm upgrades are progressively limited separately.
- **All upgrade**: A single progressive cap applies to attack, defense, and sidearm upgrades.

### Randomize Starting Items
- Takes your 15 starting items and shuffles them. This increases difficulty and can cause some funny starts.

### Ability Rando
- Allows you to select which abilities become items from the list below. Burrow is disabled by default because it significantly limits your starting options.

**Burrow** - The ability to burrow. You will still be able to enter Underlabs, go into geysers, and go into pipes.

**Swim** - The ability to swim (burrow in deep water).

**Climb** - The ability to climb ropes.

**Bounce** - The ability to bounce on bounce plants and springboards.

**Spring** - The ability to be launched by springboards.

**Carry** - The ability to carry objects.

### Deathlink
- Sends a DeathLink every time you die.

(Planned change: only sparkless deaths will trigger DeathLink in the future.)
