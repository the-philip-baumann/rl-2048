# 2048 RL-Projekt

Implementierung einer [2048](https://play2048.co/)-Spielumgebung mit dem [Gymnasium](https://gymnasium.farama.org/)-Interface als Grundlage für Reinforcement-Learning-Experimente.

## Lernziele

- Eine eigene Gymnasium-Umgebung von Grund auf implementieren
- Verschiedene RL-Algorithmen (Q-Learning, DQN, PPO) verstehen und vergleichen
- Den gesamten RL-Loop selbst umsetzen: Umgebung → Agent → Training → Auswertung

## Tech Stack

| Bibliothek | Zweck |
|---|---|
| Python 3.x | Sprache |
| [Gymnasium](https://gymnasium.farama.org/) | RL-Umgebungsinterface |
| [Stable-Baselines3](https://stable-baselines3.readthedocs.io/) | DQN & PPO Implementierungen |
| NumPy | Grid-Operationen |

## Projektstatus

- [ ] Spiellogik (Grid, Züge, Merge)
- [ ] Gymnasium-Interface
- [ ] Random Agent als Baseline
- [ ] DQN implementieren
- [ ] PPO implementieren
- [ ] Auswertung & Plots

## Über das Projekt

Dieses Projekt entsteht im Rahmen meines AIML-Studiums. Der Fokus liegt darauf, die Konzepte hinter Reinforcement Learning praktisch zu verstehen — deshalb wird jede Komponente selbst implementiert, anstatt auf fertige Lösungen zurückzugreifen.

Als Programming Buddy wird [Claude Code](https://claude.ai/code) eingesetzt. Claude erklärt Konzepte, gibt Hinweise und zeigt Fehler auf — schreibt aber bewusst keine einzige Zeile Code. Das Ziel ist es, durch eigenes Schreiben und Verstehen zu lernen, nicht durch Abschreiben.
