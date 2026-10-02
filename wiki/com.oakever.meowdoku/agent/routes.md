---
game: com.oakever.meowdoku
title: "Routes"
type: agent
version_seen: 1.18.0
verified_at: 2026-10-02
sources: [20260930-233055-chrono-2FYKPJ, 20261001-013526-chrono-2FYKPJ, 20261001-022624-chrono-2FYKPJ, 20261001-060942-chrono-2FYKPJ, 20261001-093348-chrono-2FYKPJ, 20261001-115413-chrono-2FYKPJ, 20261001-181422-chrono-2FYKPJ, 20261001-182015-chrono-2FYKPJ, 20261001-183504-chrono-2FYKPJ, 20261001-185238-chrono-2FYKPJ]
---

# Routes

Positions in the 730x1583 frame.

- Next level from Home: "Level N" (365,1185) [s:20261001-185238-chrono-2FYKPJ#10] [s:20261001-183504-chrono-2FYKPJ#2].

  > ⚠️ Previously (v1.18.0, 2026-10-01): the routes and the playbook gave (365,1245) for "Level N". That
  > is the next-level button on the win screen; on Home it does nothing [s:20261001-183504-chrono-2FYKPJ#1].
- Home: back arrow in a level (57,110) [s:20260930-233055-chrono-2FYKPJ#34]. Never Android Back on Home:
  it opens the Quit popup; X (621,535) closes it [s:20261001-185238-chrono-2FYKPJ#7] [s:20261001-185238-chrono-2FYKPJ#9].
- Daily Challenge: Home → button (365,1330) → interstitial → `launch` [s:20261001-013526-chrono-2FYKPJ#99] [s:20261001-013526-chrono-2FYKPJ#100].
- Profile: avatar (80,125) → Frame tab (500,690) → Confirm (365,1100) [s:20261001-013526-chrono-2FYKPJ#96] [s:20261001-013526-chrono-2FYKPJ#98].
- Streak page (skill `open-streak-page`): yarn counter (365,112) on Home; back (57,102) [s:20261001-013526-chrono-2FYKPJ#94] [s:20261001-022624-chrono-2FYKPJ#5].
- Leaderboard: podium (100,790) on Home → (i) (671,112); Go to Collect (365,1420) starts the next level [s:20261001-022624-chrono-2FYKPJ#8] [s:20261001-022624-chrono-2FYKPJ#11].
- Settings (skill `open-home-settings` from Home): gear (670,110); in a level Pattern Mode (575,758), Restart (365,1057), close (622,462) [s:20261001-013526-chrono-2FYKPJ#82] [s:20261001-013526-chrono-2FYKPJ#86] [s:20261001-115413-chrono-2FYKPJ#75].
- Support: Settings → Feedback; leave with `launch` [s:20261001-022624-chrono-2FYKPJ#23] [s:20261001-022624-chrono-2FYKPJ#30].
- Home settings: Language (365,870) (skill `open-language-list` from Home) → swipe up twice to reach the end of the list (Turkish) [s:20261001-060942-chrono-2FYKPJ#2] [s:20261001-060942-chrono-2FYKPJ#4]; Save progress (365,707) [s:20261001-022624-chrono-2FYKPJ#70].
- Home settings: Terms of Service (222,1120), Privacy Policy (507,1120) → Chrome; `launch` returns to Settings [s:20261001-115413-chrono-2FYKPJ#2] [s:20261001-115413-chrono-2FYKPJ#4] [s:20261001-115413-chrono-2FYKPJ#5].
- After a win (from level 11): Tap to Continue (365,1413) → look at the frame → next-level button (365,1245) [s:20260930-233055-chrono-2FYKPJ#72] [s:20260930-233055-chrono-2FYKPJ#73].
- Golden offer on the win screen (every 4th level from 54): Golden Fish sits where the next-level button
  is (about y 1217–1245); "Skip to Level N" (365,1475) goes on without it [s:20261001-093348-chrono-2FYKPJ#64] [s:20261001-182015-chrono-2FYKPJ#20] [s:20261001-181422-chrono-2FYKPJ#11].
- Out of Fishes: Restart (365,1398) — the same level on a new board, free [s:20261001-115413-chrono-2FYKPJ#43].
- An interstitial with a close button: Close (190,1472) worked once; `launch` always works [s:20261001-182015-chrono-2FYKPJ#14].
