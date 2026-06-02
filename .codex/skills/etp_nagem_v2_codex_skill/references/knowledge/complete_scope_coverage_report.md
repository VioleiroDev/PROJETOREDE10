# Complete Scope Coverage

{
  "scope_start": "2023-05-16",
  "scope_end": "2026-05-15",
  "total_days": 1096,
  "completed_days": 1075,
  "failed_days": 4,
  "pending_days": 17,
  "running_days": 0,
  "coverage_percent": 98.08,
  "chunks_total": 1096,
  "chunks_completed": 1075,
  "chunks_failed": 4,
  "chunks_pending": 17,
  "current_period_covered": "",
  "next_pending_chunk": {
    "chunk_id": "chunk_00000",
    "start": "2023-05-16",
    "end": "2023-05-16",
    "status": "failed_timeout",
    "attempts": 1,
    "last_started_at": "2026-05-16T15:01:08.022164",
    "last_finished_at": "2026-05-16T15:21:22.797270",
    "last_error": "Recovered stale running microbatch after local timeout",
    "command": "python -m pncp_kb.main build-complete-scope-microbatch --start 2023-05-16 --end 2023-05-16 --days 1 --max-days-per-run 1 --http-timeout 25 --real-only --skip-archives --resume --no-package"
  },
  "next_command": "python -m pncp_kb.main run-next-microbatch --plan data/state/microbatch_plan.jsonl --http-timeout 25 --real-only --skip-archives --no-package --max-chunks 1 --continue-on-error",
  "readiness_partial_real_package": "APTO COM RESSALVAS — COBERTURA AMPLIADA REAL",
  "readiness_complete_scope": "APTO COM RESSALVAS — BASE COMPLETA INICIAL",
  "last_successful_package": "",
  "last_validated_package": "",
  "gaps_by_month": {},
  "failed_chunks": [
    {
      "chunk_id": "chunk_00000",
      "start": "2023-05-16",
      "end": "2023-05-16",
      "status": "failed_timeout",
      "attempts": 1,
      "last_started_at": "2026-05-16T15:01:08.022164",
      "last_finished_at": "2026-05-16T15:21:22.797270",
      "last_error": "Recovered stale running microbatch after local timeout",
      "command": "python -m pncp_kb.main build-complete-scope-microbatch --start 2023-05-16 --end 2023-05-16 --days 1 --max-days-per-run 1 --http-timeout 25 --real-only --skip-archives --resume --no-package"
    },
    {
      "chunk_id": "chunk_00001",
      "start": "2023-05-17",
      "end": "2023-05-17",
      "status": "failed_timeout",
      "attempts": 1,
      "last_started_at": "2026-05-16T15:21:22.829207",
      "last_finished_at": "2026-05-16T15:22:52.869326",
      "last_error": "microbatch subprocess timeout after 90s",
      "command": "python -m pncp_kb.main build-complete-scope-microbatch --start 2023-05-17 --end 2023-05-17 --days 1 --max-days-per-run 1 --http-timeout 25 --real-only --skip-archives --resume --no-package"
    },
    {
      "chunk_id": "chunk_00002",
      "start": "2023-05-18",
      "end": "2023-05-18",
      "status": "failed_timeout",
      "attempts": 1,
      "last_started_at": "2026-05-16T15:22:54.368431",
      "last_finished_at": "2026-05-16T15:24:24.419583",
      "last_error": "microbatch subprocess timeout after 90s",
      "command": "python -m pncp_kb.main build-complete-scope-microbatch --start 2023-05-18 --end 2023-05-18 --days 1 --max-days-per-run 1 --http-timeout 25 --real-only --skip-archives --resume --no-package"
    },
    {
      "chunk_id": "chunk_00003",
      "start": "2023-05-19",
      "end": "2023-05-19",
      "status": "failed_timeout",
      "attempts": 1,
      "last_started_at": "2026-05-16T15:24:31.429640",
      "last_finished_at": "2026-05-16T15:26:01.567723",
      "last_error": "microbatch subprocess timeout after 90s",
      "command": "python -m pncp_kb.main build-complete-scope-microbatch --start 2023-05-19 --end 2023-05-19 --days 1 --max-days-per-run 1 --http-timeout 25 --real-only --skip-archives --resume --no-package"
    }
  ],
  "recommended_resume_command": "python -m pncp_kb.main run-next-microbatch --plan data/state/microbatch_plan.jsonl --http-timeout 25 --real-only --skip-archives --no-package --max-chunks 1 --continue-on-error"
}