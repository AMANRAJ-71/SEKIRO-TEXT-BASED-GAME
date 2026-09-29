# Problem & Concept Statement

## 1. Project Motivation
The objective of this project is to model the combat mechanics of FromSoftware's *Sekiro: Shadows Die Twice* in a simplified, turn-based/reaction CLI environment. Unlike standard RPGs focused on attrition damage, combat in Sekiro emphasizes deflecting and posture management.

## 2. Core Design Goals
1. **Divergent Defensive Counters:** Distinct choices for distinct attack telegraphs (e.g., Mikiri Counter for Thrusts, Jump Kick for Sweeps).
2. **Posture Primacy:** Create a dual-resource health system where Posture is as critical as Health points (HP).
3. **Modular Code Structure:** Separate game components into `Entity`, `Player`, and `Boss` abstractions for modular extensibility and clean unit testing.

## 3. Scope & Extensibility
The initial implementation models a single boss encounter (Genichiro Ashina), with room to scale to custom boss profiles, multi-phase encounters, and prosthetic tool extensions.
