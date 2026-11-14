# Evals

Each `<skill>.json` holds at least 3 test prompts and the behaviours a good answer must show.

## How to run (manual, for now)

1. Open a fresh agent session **without** the skill and send each prompt. Save the answer as the baseline.
2. Install the skill, start a fresh session, send the same prompts.
3. For each `expect` item, mark pass/fail. A skill is ready when it passes clearly more items than the baseline and never violates a safety rule (posting on the user's behalf, hiding AI use).
4. Record results in your PR.

Also check **triggering**: phrase requests casually ("where do I put my game?", "đăng game ở đâu") and confirm the agent loads the right skill.
